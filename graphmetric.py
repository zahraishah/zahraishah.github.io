#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 19:05:25 2020

@author: Leo Xu
"""

#Calculating the clusting coefficient for one vertex
def clustering (G,v):
    x=list(G.neighbors(v))
    x.append(v)
    H=G.subgraph(x)
    K=nx.complete_graph(H.order())
    result=float(H.size())/float(K.size())
    return result

#Calculating the avargae clustering coefficient
def cluster_coefficient (G):
    sum=0
    for x in list(G.nodes()):
        sum=sum+clustering(G,x)
    return sum/G.order()

