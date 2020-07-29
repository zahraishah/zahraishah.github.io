5#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 12:06:16 2020

@author: malaikakironde
"""


#This code calculates the odd laplacian and uses it to find the final state of
#the heat equation.

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import scipy as sp

def heat_eq (G,k,t,e0):
    
    #Getting I and its transpose
    I = nx.incidence_matrix(G, oriented=True).todense()
    #print(I) #I is number of edges x number of vertices for the order
    I_t = I.transpose()
    #print(I_t)
    
    #Multiplying I_t by I/Find the odd laplacian
    L = np.dot(I_t, I)
    print(L)
    A= -k*t*L
    
    E=sp.linalg.expm(A) #create exponential of matrix
    et= np.matmul(E,e0) #final state
    return et

def main():

    #Getting the graph
    n = int(input('Enter the number of nodes: '))
    m = int(input('Enter the number of edges: '))
    G = nx.gnm_random_graph(n, m) #try with different graph
    nx.draw(G, with_labels = True)
    plt.show()
        
    #Finding the inputs of the graph
    t = eval(input('Enter the time: '))
    k = eval(input('What is the heat constant? '))
    
    #finding the matrix for the initial temperature
    e_vec = input("Enter the initial state as a vector, separated by';' ")
    e0 = np.mat(e_vec)

    print(heat_eq(G,k,t,e0))
    
main()


