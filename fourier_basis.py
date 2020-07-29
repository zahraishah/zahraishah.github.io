#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 16:36:39 2020

@author: malaikakironde
"""

#This code diagonalizes a network and finds its fourier basis 

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

#Diagonalizing the Laplacian
#Compute the Eigenvalues
#Compute the corresponding Eigenvectors

n = int(input('Enter the number of nodes: '))
m = int(input('Enter the number of edges: '))
G = nx.gnm_random_graph(n, m) #get the graph
nx.draw(G, with_labels=True, node_color=range(n),cmap=plt.cm.Reds)
plt.show() #draw the graph

#L = nx.normalized_laplacian_matrix(G).todense()
L = nx.laplacian_matrix(G).todense()
print(L)
# e = np.linalg.eigvals(L) #Use eig(L) to find both the values and vectors
# print(e)

#Creating the diagonal matrix
eig_val, eig_vec = np.linalg.eig(L)
print(eig_val)
inv_vec = np.linalg.inv(eig_vec) #inverse of eigenvectors
diagonal= inv_vec.dot(L).dot(eig_vec)

fourier_basis = diagonal.round(5)
print(fourier_basis)




