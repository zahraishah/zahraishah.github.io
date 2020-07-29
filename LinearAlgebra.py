#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 21:20:07 2020

@author: zahrashah
"""

import numpy as np
from scipy.linalg import null_space

#creating an array
a = np.array([10,2,3,4,5])

print("array a: \n",a)
print(type(a))
print('')
#indexing elements in a numpy array

print("element at position 0: \n",a[0])

print("element 0-1: \n",a[0:2]) #0 and 1st element
print('')
#retrieving (reading) dimensions of array

print("size of a: \n",a.shape)
print("size of first row of a: \n",a.shape[0])
print('')

#create a matrix

A = np.array([[1,2,3,4],[10,20,30,40],[100,200,300,400]])
print("A: \n",A)
print('')



#indexing a matrix

print("A[2,3]: \n",A[2,3])
print('')

#creating a submatrix

B=A[1:3,1:] #the number after : is not inlcuded
print("B: \n",B)
print('')

#creating special matrices

I = np.eye(3) #identity matrix
print("Identity matrix: \n",I)

Z = np.zeros((5,5)) #zero matrix
print("Zero matrix: \n",Z)

O = np.ones ((3,4)) #ones matrix
print("Ones matrix: \n",O)

C = np.full((4,5),10) #constant matrix
print("Constant matrix: \n",C)

#creating a random matrix

A= np.random.random((2,2))
print("Random matrix: \n",A)
print('')

#matrix addition

A = np.array([[1,5,6],[1,8,9],[0,-1,6]])
B = np.array([[4,8,4],[1,0,5],[6,-8,4]])

print("A: \n",A)
print("B: \n",B)

print("A+B: \n",np.add(A,B))
print('')

#matrix subtraction

print("A-B: \n",np.subtract(A,B))
print('')

#matrix multiplication(POINTWISE)
#not the one we do in linear alg
print(A*B)
print("A*B: \n",np.multiply(A,B))
print('')

#transpose a matrix
print("A: \n",A)
print("A transpose: \n",np.transpose(A))
print('')

#MATRIX PRODUCTS

##inner product

print("Inner product of A and B: \n",np.matmul(A,B))

##dot product of vectors
a = A[:,0]
b=B[:,0]
print("a: \n",a)
print("b: \n",b)

print("a.b: \n",np.dot(a,b))
print('')

##kronecker product of matrix

print("Kron product A,B: \n",np.kron(A,B))
print('')


##matrix exponetaion

D= np.linalg.matrix_power(A,4)
print("D^4: \n",D)
print('')

#EIGENVECTORS AND EIGENVALUES 

E =np.mat("3,2; 1 0")
print("E: \n", E)
print("Eigenvalues: \n", np.linalg.eigvals(E))

eigenvalue, eigenvector = np.linalg.eig(E)
print("Eigenvector: \n", eigenvector)
print("Eigenvalues: \n", eigenvalue)
print('')

#MATRIX DECOMPOSITIONS

##QR decomposition, A=QR

Q=np.linalg.qr(A)[0]
R=np.linalg.qr(A)[1]

print("QR decom(A): \n",np.matmul(Q,R))
print('')

##Eigenvalue decomposition(EVD)
## A= PDP(inv)

(d,P) = np.linalg.eig(A)

print("diagonal value: \n",d)
print("P: \n",P)

D= np.diag(d) #convert d to a diagonal matrix

###verify this

V= np.matmul(np.matmul(P,D),np.linalg.inv(P))
print("A: \n",A)
print("A: \n",np.real(V))
print('')

#determinant of a matrix

print("detA: \n",np.linalg.det(A))
print('')

#rank of a matrix
print("rank(A): \n",np.linalg.matrix_rank(A))
print('')

#trace of a matrix
print("trace(A): \n",np.trace(A))
print('')

# solving equations Ax = b

b = np.random.random((3,1))
print("b: \n",b)

x1 = np.linalg.solve(A,b)
print("x1: \n",x1)



Z =np.mat("3,2; 1 0")
print(Z)

print(np.matmul(Z,Z))
print(np.linalg.matrix_power(Z,2))



# Calculating the kernel of a matrix
N = np.mat("3,4; 3,4")
print("N: \n", N)

k = null_space(N)

print("Ker(N): \n", k)










