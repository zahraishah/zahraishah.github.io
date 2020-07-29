#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 11:43:46 2020

@author: malaikakironde
"""


#This document goes over implementing a random graph using 
#the Erdos-Renyi Model


import sys

import matplotlib.pyplot as plt
import networkx as nx
import random

def erdos_renyi(G,p):
    #finding all possible edges in G
    for i in G.nodes():
        for j in G.nodes():
            #the edges do not count if they start and end at the same node
            if i != j:
                r = random.random()
                #if the random number is less than the probabilty, then
                #an edge will be drawn
                if r <= p:
                    G.add_edge(i,j)
                #if not, the edge will not be drawn
                else:
                    continue
                
def graph_G():
        #G(n,p)
    n = int(input('Enter the number of nodes: '))
    p = float(input('Enter a number between 0 and 1 for the probability: '))
    
    #Creating an empty graph
    G = nx.Graph()
    
    #Adding nodes and edges to the graph
    G.add_nodes_from([i for i in range(n)])
    erdos_renyi(G,p)
    
    #Drawing the graph
    nx.draw(G)
    plt.show()
    
graph_G()