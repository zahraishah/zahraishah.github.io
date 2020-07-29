#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 01:21:37 2020

@author: zahrashah
"""

import numpy as np

#calculating eigenvalues and eigengraphs for a given matrix

#the numpy.linalg.eig function returns a tuple consisting of
# a vector and an array. The vector (here w) contains the eigenvalues. 
#The array (here v) contains the corresponding eigenvectors, one eigenvector per column. 

E =np.mat("1,4; 3 2") #a matrix
print("E: \n", E)

eigvals, v = np.linalg.eig(E) #returns eigenvalues and eigenvectors

#the first eigenvalue corresponds to  the first eigenvector and so on
#if we know the eigenvalues are real (matrix is symmetric), we can use the numpy method .real to
#convert the eigenvalues into real number if they are initially not

print("Eigenvalues: \n", eigvals)

#v is an array of eigenvectors, with every column corresponding to one eigenvector.
#to extract those, we can do the following;

v1 = v[:,0].reshape(2,1)
print("Eigenvector for lambda1: \n",v1)
v2 = v[:,1].reshape(2,1)
print("Eigenvector for lambda2: \n",v2)

