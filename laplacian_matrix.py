#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 13:10:08 2020

@author: malaikakironde
"""
#This document shows how to get the adjaceny and degree matrix, as well as
#graph laplacian

import matplotlib.pyplot as plt
import networkx as nx


#Type of graph
G = nx.complete_graph(5)

#Drawing the graph
nx.draw(G)
plt.show()

#Getting the adjaceny matrix
A = nx.adjacency_matrix(G)
print(A.todense())

#Getting the graph laplacian
L = nx.laplacian_matrix(G)
print(L.todense())

#Using the laplacian formula to find the degree matrix
D = A + L
print(D.todense())




