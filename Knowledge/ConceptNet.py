import json
import time

import networkx as nx
import numpy as np
import torch.nn.functional as F
import torch
import torchtext
from scipy import spatial
from tqdm import tqdm


# remove conceptnet pos tags
from Knowledge.ConceptBlacklist import blacklist


def remove_pos_tag(s):
    if s.endswith("/n") or s.endswith("/a") or s.endswith("/v") or s.endswith("/r"):
        s = s[:-2]
    return s


# get networkx format conceptnet
def get_conceptnet(file_path='Knowledge/Data/conceptnet_en.txt', embeddings=None, numberbatch=True):
    print('[ConceptNet Constructing] Load ConceptNet from file')
    english_conceptnet = []
    conceptnet = nx.MultiGraph()

    # process raw conceptnet Data
    with open(file_path, encoding="utf-8") as f:
        for line in tqdm(f.readlines()):
            seps = line.rstrip('\n').split('\t')
            # english concepts and edges
            if seps[2].startswith('/c/en/') and seps[3].startswith('/c/en/'):
                relation = seps[1].split("/")[-1].lower()
                head = remove_pos_tag(seps[2][6:]).split("/")[0].lower()
                tail = remove_pos_tag(seps[3][6:]).split("/")[0].lower()

                if '_' in head or '_' in tail:
                    continue

                if numberbatch:
                    if head not in embeddings or tail not in embeddings:
                        continue
                else:
                    if head not in embeddings.stoi or tail not in embeddings.stoi:
                        continue

                data = json.loads(seps[4])
                weight = data["weight"]
                conceptnet.add_edge(head, tail, rel=relation, weight=1 / weight)
                english_conceptnet.append(line)

    return conceptnet


class ConceptNet:
    def __init__(self, root='Knowledge/Data/', numberbatch=True, load_glove=True):
        self.root = root
        if numberbatch:
            print('[ConceptNet Constructing] Using ConceptNet Numberbatch')
            self.concept_embedding = self.get_numberbatch_mapping()
        else:
            print('[ConceptNet Constructing] Using GLoVe')
            self.concept_embedding = torchtext.vocab.GloVe(name='6B', dim=300)
        self.numberbatch = numberbatch
        self.conceptnet = get_conceptnet(root + 'conceptnet_en.txt', self.concept_embedding, numberbatch=numberbatch)
        self.nodes = list(self.conceptnet.nodes)
        self.concept_distance = {}

    def get_numberbatch_mapping(self):
        f = open(self.root + 'whole-en.txt', encoding='utf-8')
        lines = f.readlines()

        conceptnet_embedding = {}

        for line in tqdm(lines):
            word, vector = line.split(' ', 1)
            if not word.isalpha():
                continue
            vector = [float(n) for n in vector.split(' ')]
            conceptnet_embedding[word] = vector

        return conceptnet_embedding

    def get_concept(self, concept):
        return self.conceptnet[concept]

    def get_concept_embedding(self, concept):
        if concept not in self.concept_embedding:
            return None
        return self.concept_embedding[concept]

    def cached_shortest_path(self, source, target):
        source, target = [source, target] if source < target else [target, source]
        if source in self.concept_distance:
            if target in self.concept_distance[source]:
                return self.concept_distance[source][target]
        return -1

    def shortest_path(self, source, target, value=False):
        # load value if cached
        if value:
            cached_value = self.cached_shortest_path(source, target)
            if cached_value != -1:
                return None, cached_value

        try:
            path = nx.shortest_path(self.conceptnet, source=source, target=target, weight='weight')
            path_weight_sum = nx.path_weight(self.conceptnet, path, weight='weight')
        except nx.exception.NetworkXNoPath:
            path = None
            path_weight_sum = 100

        # cache the shortest path
        source, target = [source, target] if source < target else [target, source]
        if source not in self.concept_distance:
            self.concept_distance[source] = {}
        self.concept_distance[source][target] = path_weight_sum

        return path, path_weight_sum

    def shortest_paths(self, source, target):
        paths = nx.all_shortest_paths(self.conceptnet, source=source, target=target, weight='weight')
        paths = [path for path in paths]
        path_weight_sum = nx.path_weight(self.conceptnet, paths[0], weight='weight')
        result = {'paths': paths, 'weight': path_weight_sum}
        return result

    def adjacent(self, concept):
        if not self.conceptnet.has_node(concept):
            return None
        return list(self.conceptnet.neighbors(concept))

    def neighbour_concept_multi_source(self, concepts):
        result = []
        for concept in concepts:
            result.extend(self.adjacent(concept))
        result = set(result)
        return result

    def build_connection(self, concepts_a, concepts_b):
        pass

    def min_neighbours(self, concept):
        rels = self.conceptnet[concept]
        result = []
        for k in rels:
            rel = rels[k]
            min_weight = min([rel[t]['weight'] for t in rel])
            result.append({'tail': k, 'weight': min_weight})

        return result

    def min_neighbour_target(self, concept, target):
        neighbours = self.adjacent(concept)
        result = []
        for neighbour in neighbours:
            _, w = self.shortest_path(neighbour, target, value=True)
            result.append({'tail': neighbour, 'weight': w})
        result = sorted(result, key=lambda x: x['weight'])
        return result

    def indexOf(self, word):
        return self.nodes.index(word)

    def get_adjacent_graph(self, target):
        G_adjacent = nx.Graph()
        nodes = self.adjacent(target)
        G_adjacent.add_node(target, x=self.concept_embedding.stoi[target])
        for node in nodes:
            G_adjacent.add_node(node, x=self.concept_embedding.stoi[node])
            G_adjacent.add_edge(target, node)
        return G_adjacent

    def get_adjacent_subgraph(self, target):
        G_adjacent = nx.Graph()
        nodes = self.adjacent(target)
        G_adjacent.add_node(target, x=self.concept_embedding.stoi[target])
        for node in nodes:
            G_adjacent.add_node(node, x=self.concept_embedding.stoi[node])
            G_adjacent.add_edge(target, node)
        return G_adjacent

    def bidirectional_reasoning(self, source_concepts, target, K=10, hops=3, torch_calculation=True):
        G_global = nx.Graph()

        S = [concept for concept in source_concepts]
        target_encoded = self.concept_embedding[target]

        for _ in range(hops):
            temp = []
            while len(S) != 0:
                head_entity = S.pop(0)
                if head_entity in blacklist:
                    continue

                # calculate neighbouring concepts
                neighbouring_concepts = self.adjacent(head_entity)
                if neighbouring_concepts is None:
                    continue

                neighbouring_concepts = [n for n in neighbouring_concepts if n not in blacklist]
                if len(neighbouring_concepts) == 0:
                    continue

                head_encoded = self.concept_embedding[head_entity]

                # get top 10 similar to target and head entity
                if not torch_calculation:
                    head_sim = [(n, 1 - spatial.distance.cosine(self.concept_embedding[n], head_encoded))
                                for n in neighbouring_concepts]

                    target_sim = [(n, 1 - spatial.distance.cosine(self.concept_embedding[n], target_encoded))
                                  for n in neighbouring_concepts]

                    head_topK = sorted(head_sim, key=lambda x: x[1], reverse=True)[:K]
                    target_topK = sorted(target_sim, key=lambda x: x[1], reverse=True)[:K]
                    intermediates = list(set(head_topK) & set(target_topK))

                    for inter in intermediates:
                        if not G_global.has_node(inter[0]):
                            if self.numberbatch:
                                G_global.add_node(inter[0], x=self.concept_embedding[inter[0]])
                            else:
                                G_global.add_node(inter[0], x=self.concept_embedding.stoi[inter[0]])
                            temp.append(inter[0])
                        if not G_global.has_node(head_entity):
                            if self.numberbatch:
                                G_global.add_node(head_entity, x=self.concept_embedding[head_entity])
                            else:
                                G_global.add_node(head_entity, x=self.concept_embedding.stoi[head_entity])
                        G_global.add_edge(head_entity, inter[0])
                else:
                    word_embeddings = [self.concept_embedding[n] for n in neighbouring_concepts]
                    neighbouring_length = len(neighbouring_concepts)
                    if neighbouring_length == 0:
                        continue

                    stacked_embeddings = torch.stack(word_embeddings)
                    head_encoded_repeated = head_encoded.repeat(stacked_embeddings.size(0), 1)
                    target_encoded_repeated = target_encoded.repeat(stacked_embeddings.size(0), 1)

                    head_sim = F.cosine_similarity(stacked_embeddings, head_encoded_repeated, dim=1)
                    target_sim = F.cosine_similarity(stacked_embeddings, target_encoded_repeated, dim=1)

                    top_K_indices_head = torch.topk(head_sim,
                                                    k=K if neighbouring_length > K else neighbouring_length,
                                                    largest=True).indices
                    top_K_indices_target = torch.topk(target_sim,
                                                      k=K if neighbouring_length > K else neighbouring_length,
                                                      largest=True).indices

                    top_K_indices = torch.cat((top_K_indices_head, top_K_indices_target))
                    intermediates = np.array(neighbouring_concepts)[top_K_indices]

                    for inter in intermediates:
                        if not G_global.has_node(inter):
                            if self.numberbatch:
                                G_global.add_node(inter, x=self.concept_embedding[inter])
                            else:
                                G_global.add_node(inter, x=self.concept_embedding.stoi[inter])
                            temp.append(inter)
                        if not G_global.has_node(head_entity):
                            if self.numberbatch:
                                G_global.add_node(head_entity, x=self.concept_embedding[head_entity])
                            else:
                                G_global.add_node(head_entity, x=self.concept_embedding.stoi[head_entity])
                        G_global.add_edge(head_entity, inter)

            temp = list(set(temp))
            S = temp

        return G_global