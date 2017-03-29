# -*- coding: utf-8 -*-
"""
Created on Mon May  2 21:14:12 2016
# Author:
# Manav Sharma msharma7
# Jeffrey Chan jchan40
"""

import numpy as np
import timeit 
import matplotlib.pyplot as plt

def matmult(A,x):
    B = np.empty([len(x)], dtype=np.int) #initialize an empty array of ints
    product = 0
    for i in range (len(A)):    #iterate through the array
        for j in range (len(A)):
            product += A[i][j] * x[j]   #save the product of each element in the array
            j += 1
        B[i] = product  #save the final product into array B
        product = 0
        i += 1       
    return B    
def hadmat(k):
    n = 2**k
    A = np.empty([2**k,2**k], dtype=np.int) #initialize an empty array of ints
    A[0][0] = 1
    x = 1
    while x < n:
        for i in range (x):
            for j in range (x):
                A[i+x][j] = A[i][j] #initializing elements to 1
                A[i][j+x] = A[i][j] 
                A[i+x][j+x] = -1 * A[i][j]  #make the bottom right negative
        x += x
    return A
def hadmatmult(H, x):
   if (len(x) != len (H)):  #if the two arrays are not of equal length, give error
       raise ValueError('Length of H and x are not the same')
   if (len(H) == 2):    
       return matmult(H,x)
   if (len(H)/2 == 2):  #base case
       return matmult(H,x)
   Hu = H[0:(len(H)//2),0:(len(H)//2)]  #left side of upper hafl
   Hl2 = H[(len(H)//2):len(H),(len(H)//2):len(H)] #right side of lower half
   F = np.split(x,2)    #split the vector into 2
   A = hadmatmult(Hu,F[0])  
   B = hadmatmult(Hu,F[1]) 
   D = hadmatmult(Hl2,F[1])
   b1 = A + B #add left half with right half
   b2 = A + D
   return np.concatenate((b1,b2), axis = 0) 
'''
k = 12
n = 1
mat = []
mat2 = []

while n <= k:
     x = np.random.randint(100,size=2**n)
     A = hadmat(n)
     mattime = timeit.timeit(lambda: matmult(A,x),number = 1)
     had = timeit.timeit(lambda: hadmatmult(A,x),number = 1)
     mat.append(mattime)
     mat2.append(had)
     n += 1

x = np.arange(0,12)     

plt.plot(x,mat,'g-',label="matmult")
plt.plot(x,mat2,'b-',label="hadmatmult")
plt.xlabel('n')
plt.ylabel('time')
plt.plot
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()

A = hadmat(3)
B = np.arange(0,8)
print (hadmatmult(A,B))
print (matmult(A,B))
'''
    

