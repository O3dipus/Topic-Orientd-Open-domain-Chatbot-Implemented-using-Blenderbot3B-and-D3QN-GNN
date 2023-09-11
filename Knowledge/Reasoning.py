import multiprocessing
from multiprocessing import Pool
import time

import networkx as nx
import numpy as np
import torch
from sentence_transformers import SentenceTransformer, util
from tqdm import tqdm


def bidirectional_reasoning(conceptnet, source_concepts, target, K=10, hops=3):
    G_global = nx.Graph()

    encoder = SentenceTransformer('sentence-transformers/sentence-t5-base')

    # initialize stack
    S = [concept for concept in source_concepts]
    target_encoded = encoder.encode(target, convert_to_tensor=True)

    sort_time = 0
    encode_time = 0
    sim_time = 0

    for _ in tqdm(range(hops)):
        temp = []
        print('Stack Size: {}'.format(len(S)))
        while len(S) != 0:
            head_entity = S.pop(0)
            head_encoded = encoder.encode(head_entity, convert_to_tensor=True)

            # calculate neighbouring concepts
            encode_start = time.time()
            neighbouring_concepts = np.array(conceptnet.adjacent(head_entity))
            neighbouring_encoded = encoder.encode(neighbouring_concepts, convert_to_tensor=True)
            encode_end = time.time()
            encode_time = encode_time + (encode_end - encode_start)

            neighbour_size = neighbouring_concepts.shape[0]

            # get top 10 similar to target and head entity
            sim_start = time.time()
            head_sim = torch.tensor([util.cos_sim(n, head_encoded) for n in neighbouring_encoded])
            target_sim = torch.tensor([util.cos_sim(n, target_encoded) for n in neighbouring_encoded])
            sim_end = time.time()
            sim_time = sim_time + (sim_end - sim_start)

            sort_start = time.time()
            head_indices = torch.topk(head_sim, K if neighbour_size > K else neighbour_size,
                                      sorted=False).indices.tolist()
            target_indices = torch.topk(target_sim, K if neighbour_size > K else neighbour_size,
                                        sorted=False).indices.tolist()
            head_indices.extend(target_indices)
            indices = list(set(head_indices))
            intermediates = neighbouring_concepts[indices].tolist()
            # sorted(head_sim, key=lambda x: x['sim'], reverse=True)
            # sorted(target_sim, key=lambda x: x['sim'], reverse=True)
            sort_end = time.time()

            sort_time = sort_time + (sort_end - sort_start)

            for inter in intermediates:
                if not G_global.has_node(inter):
                    G_global.add_node(inter)
                    temp.append(inter)
                G_global.add_edge(head_entity, inter)
        temp = list(set(temp))
        S = temp

    print('sort consumption: {}s'.format(sort_time))
    print('encode consumption: {}s'.format(encode_time))
    print('similarity calculation consumption: {}s'.format(sim_time))

    return G_global


def bidirectional_reasoning_batched(cpnet, source_concepts, target, K=10, hops=3):
    G_global = nx.Graph()

    encoder = SentenceTransformer('sentence-transformers/sentence-t5-base')

    # initialize stack
    S = [concept for concept in source_concepts]
    target_encoded = encoder.encode(target, convert_to_tensor=True)

    for _ in tqdm(range(hops)):
        temp = []
        neighbour_words = []
        for s in S:
            neighbouring_concepts = cpnet.adjacent(s)
            neighbour_words.extend(neighbouring_concepts)

        neighbour_words = list(set(neighbour_words))
        words_encoded = encoder.encode(neighbour_words, convert_to_tensor=True)
        target_similarities = util.cos_sim(words_encoded, target_encoded)

        neighbour_dict = {}
        for i in range(len(neighbour_words)):
            neighbour_dict[neighbour_words[i]] = {'ts': target_similarities[i].item(),
                                                  'en': words_encoded[i]}

        for s in S:
            head_encoded = encoder.encode(s, convert_to_tensor=True)

            neighbouring_concepts = np.array(cpnet.adjacent(s))
            neighbour_size = neighbouring_concepts.shape[0]

            target_sim = []
            neighbouring_encoded = []

            for tail_entity in neighbouring_concepts:
                target_sim.append(neighbour_dict[tail_entity]['ts'])
                neighbouring_encoded.append(neighbour_dict[tail_entity]['en'].tolist())
            head_sim = util.cos_sim(torch.tensor(neighbouring_encoded).cuda(), head_encoded).flatten()
            target_sim = torch.tensor(target_sim)

            head_indices = torch.topk(head_sim, K if neighbour_size > K else neighbour_size,
                                      sorted=False).indices.tolist()
            target_indices = torch.topk(target_sim, K if neighbour_size > K else neighbour_size,
                                        sorted=False).indices.tolist()
            head_indices.extend(target_indices)
            indices = list(set(head_indices))
            intermediates = neighbouring_concepts[indices].tolist()
            # sorted(head_sim, key=lambda x: x['sim'], reverse=True)
            # sorted(target_sim, key=lambda x: x['sim'], reverse=True)

            for inter in intermediates:
                if not G_global.has_node(inter):
                    G_global.add_node(inter)
                    temp.append(inter)
                G_global.add_edge(s, inter)
        temp = list(set(temp))
        S = temp

    return G_global
