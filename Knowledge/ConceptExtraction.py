# concept extractor
import nltk
from nltk import stem
from nltk.corpus import wordnet
from Knowledge.ConceptBlacklist import blacklist


# extract nouns and verbs in sentence
def concept_extractor(sentence):
    # tokenize sentence
    tokens = nltk.word_tokenize(sentence)
    # extract nouns and verbs respectively for lemmatization
    nouns = []
    verbs = []
    tags = nltk.pos_tag(tokens)
    lemmatizer = stem.WordNetLemmatizer()
    concepts = []

    for word, tag in tags:
        word = word.lower()
        if word.isalpha():
            if tag.startswith('N'):
                word = lemmatizer.lemmatize(word, wordnet.NOUN)
                if word not in blacklist:
                    concepts.append(word)
            elif tag.startswith('V'):
                word = lemmatizer.lemmatize(word, wordnet.VERB)
                if word not in blacklist:
                    concepts.append(word)

    if len(concepts) == 0:
        for word, tag in tags:
            word = word.lower()
            if word not in blacklist and word.isalpha():
                concepts.append(word)

    return list(set(concepts))
