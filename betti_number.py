
import sys
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def betti1(G):
    return nx.number_connected_components(G)
def betti2(G):
    return len(nx.cycle_basis(G))

G=nx.complete_graph(5)
print (betti1(G))
print (betti2(G))
