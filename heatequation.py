#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 17:54:51 2020

@author: zahrashah
"""


##solving the graph heat equation

import numpy as np
import scipy as sp
import networkx as nx

G = nx.complete_graph(4)
e0= np.mat("1;0;3;4") #initial state
k = 2 # constant
t= 5 # time elapsed



def heat_eq (G,k,t,e0):
    L= nx.laplacian_matrix(G).todense() #create laplacian
    L= -k*t*L
    
    E=sp.linalg.expm(L) #create exponential of matrix
    et= np.matmul(E,e0) #final state
    return et

print(heat_eq(G,2,0.1,e0))












