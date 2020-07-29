#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 21:57:08 2020

@author: malaikakironde
"""

#This code plots the difference between the highest and lowest temperature in a network versus time
#for both the even and odd laplacian

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import scipy as sp

def heat_eq (G,k,e0):
    L= nx.laplacian_matrix(G).todense() #create laplacian
    
    dif =[]
    
    for t in np.arange(0,10,0.1):
        
        A= -k*t*L
        E=sp.linalg.expm(A) #create exponential of matrix
        et= np.matmul(E,e0) #final state
    
        #Find the highest temperature in the matrix et
        temp_high = np.amax(et)
        #Find the lowest temperature in the matrix et
        temp_low = np.amin(et)
        #Find the difference between the highest and lowest temperature
        temp = temp_high - temp_low
        #Append the difference to the list 'dif'
        dif.append(temp)
        
    #Plot the data
    t = np.arange(0,10,0.1)
    plt.plot(t,dif)
    plt.xlabel('Time')
    plt.ylabel('Difference in Temperature')
    plt.title('Even Laplacian')
    #print(optimize.minimize(dif, x0=0))
    return plt.show()
    
def heateq_oddL(G,k,e2,I):
    I_t = I.transpose()
    
    #Multiplying I_t by I/Find the odd laplacian
    L = np.dot(I_t, I)
    
    dif = []
    for t in np.arange(0,10,0.1):
        A= -k*t*L
        
        E=sp.linalg.expm(A) #create exponential of matrix
        et= np.matmul(E,e2) #final state
        
        #Find the highest temperature in the matrix et
        temp_high = np.amax(et)
        #Find the lowest temperature in the matrix et
        temp_low = np.amin(et)
        #Find the difference between the highest and lowest temperature
        temp = temp_high - temp_low
        #Append the difference to the list 'dif'
        dif.append(temp)
    
    #Plot the data
    t = np.arange(0,10,0.1)
    plt.plot(t,dif)
    plt.xlabel('Time')
    plt.ylabel('Difference in Temperature')
    plt.title('Odd Laplacian')
    return plt.show()
    

def main():

    graph = input('Random or SWN? ').upper()
     
    if graph == 'RANDOM':
        n = int(input('Enter the number of nodes: '))
        m = int(input('Enter the number of edges: '))
        G = nx.gnm_random_graph(n, m) 
     
    elif graph == 'SWN':
        n = int(input('Enter the number of nodes in the graph: '))
        k = int(input('Enter the number of nearest neighbors that each node is connected to in ring topology: '))
        p = float(input('Enter the probabilty of rewiring each edge: '))
        G = nx.watts_strogatz_graph(n, k, p)  
             
    nx.draw(G, with_labels=True, node_color=range(n),cmap=plt.cm.Reds)
    plt.show()
    I = nx.incidence_matrix(G, oriented=True).todense() #incidence matrix
    
    #Number of edges for odd laplacian
    edges = G.number_of_edges()
    print('#edges =', G.number_of_edges())
     
    #Finding the inputs of the graph 
    k = eval(input('What is the heat constant? '))
     
    #finding the matrix for the initial temperature #order is equal to number of nodes
    #e_vec = input("Enter the initial state as a vector, separated by';'(even laplacian) ")
    e_vec = '1'+ (n-1)*';0'
    e0 = np.mat(e_vec)
    
    #order is equal to the number of edges 
    #e2_vec = input("Enter the initial state as a vector, separated by';'(odd laplacian) ")
    e2_vec = '1'+ (edges-1)*';0'
    e2 = np.mat(e2_vec)  

    heat_eq(G,k,e0)
    heateq_oddL(G, k, e2, I)
    
main()


