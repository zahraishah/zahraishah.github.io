#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 10:11:21 2020

@author: malaikakironde
"""
#This document goes over implementing a random graph with n nodes and
#m edges

import sys

import matplotlib.pyplot as plt
import networkx as nx
import random

def random_graph():
    #G(n,m)
    n = int(input('Enter the number of nodes: '))  # eg. 10 nodes
    m = int(input('Enter the number of edges: '))  # eg. 20 edges
    
    #Key function to generate random graph
    G = nx.gnm_random_graph(n, m)
    
    nx.draw(G)
    plt.show()

random_graph()


    

