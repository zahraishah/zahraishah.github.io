import re
import string
import networkx as nx
import sys
import numpy as np
import matplotlib.pyplot as plt

def sigma (G,x):
    order=G.order()
    size=G.size()
    CrList=list()
    LrList=list()
    for i in range(x):
        Gr=nx.gnm_random_graph(order,size)
        CrList.append(nx.transitivity(Gr))
        LrList.append(nx.average_shortest_path_length(Gr))

    C = nx.transitivity(G)
    L = nx.average_shortest_path_length(G)
    Cr = np.mean(CrList)
    Lr = np.mean(LrList)

    sigma = (C / Cr) / (L / Lr)

    return sigma


def Union(lst1, lst2):
    final_list = list(set(lst1) | set(lst2))
    return final_list

adjacency = dict()
file = open('test.txt')
text=file.read()
paragraphs = list()
for paragraph in text.split('\n\n'):
    wordsInP=list()
    for line in paragraph.split('\n'):
        line.strip()
        for word in re.split(r'\W+', line):
            word=word.lower()
            word=word.translate(str.maketrans('', '', string.punctuation))
            if len(word)<2:
                continue
            if not word in wordsInP:
                wordsInP.append(word)
    paragraphs.append(wordsInP)

for item in paragraphs:
    for word in item :
        adjacency[word]=Union(adjacency.get(word,[]),item)


G = nx.from_dict_of_lists(adjacency)
for x in G.nodes():
    G.remove_edge(x,x)

nx.draw(G)
plt.show()

print(sigma(G,5))
