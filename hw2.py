# -*- coding: utf-8 -*-
# Manav Sharma msharma7
# Jeffrey Chan jchan40 
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import timeit 
import matplotlib.pyplot as plt
import scipy
    
def selectionsort(A):
   
    for i in range (len(A)):
        minIndex = i #set the minimum index i
        for j in range (i, len(A)): #iterate through unsorted part of array
            if A[j] < A[minIndex]: 
                minIndex = j #find the smallest element and set it to j
        if minIndex != i:
            A[i], A[minIndex] = A[minIndex], A[i] #swap the element into its sorted place
    return(A)


def insertionsort(A):
   
    for i in range(len(A)):
         j = i-1  #for looping through all items to i's left
         while A[j] > A[j+1] and j>=0: 
             A[j], A[j+1] = A[j+1], A[j] #swap the elements if the one to the right is larger
             j = j-1
    return(A)
    
def mergesort(A):
    n = len(A) #initialize n as the length of A
    if (n <= 1):
        return A
    middle = n//2
    left = A[:middle] #declare left for all elements to the left of middle
    right = A[middle:] #declare right for all elements to the right of middle
    l = mergesort(left)
    r = mergesort(right) #recursive call to mergesort 
    return merge(l, r)
    

def merge(B, C):
    B = np.append(B,float('inf')) 
    C = np.append(C,float('inf')) #adding infinity to the end of B,C
    D = []
    i = j = 0
    while B[i] < (float('inf')) or C[j] < (float('inf')): 
        if B[i] < C[j]: #if the element of B is less than the element of C
            D.append(B[i]) #Add the element of B to the end of D
            i = i+1
        else:
            D.append(C[j]) #Add the element of C to the end D
            j = j + 1
    return D
    
'''
np.random.seed(0)
array = np.random.permutation(1000000)
intime = timeit.timeit(lambda: insertionsort(array),number=1)
mergetime = timeit.timeit(lambda: mergesort(array),number=1)
seltime = timeit.timeit(lambda: selectionsort(array),number=1)

print("insertion time: ", intime)
print("merge time: ", mergetime)
print("selection time: ", seltime)
    

x = np.arange(100,10100,100) #fully sorted
y = np.arange(10100,100,-100) #inverted
result2 = []
result = []
meresult = []
meresult2 = []
selresult = []
selresult2 = []

for i in range(len(x)):     #fully sorted
    t = timeit.timeit(lambda: insertionsort(np.arange(1,x[i])),number = 1)
    ts = timeit.timeit(lambda: selectionsort(np.arange(1,x[i])),number = 1)
    tm = timeit.timeit(lambda: mergesort(np.arange(1,x[i])),number = 1)
    result.append(t)
    meresult.append(tm)
    selresult.append(ts)
    i = i +1
    print(i)
for i in range(len(y)):     #inverted
    t = timeit.timeit(lambda: insertionsort(np.arange(y[i],1,-1)),number = 1)
    ts = timeit.timeit(lambda: selectionsort(np.arange(y[i],1,-1)),number = 1)
    tm = timeit.timeit(lambda: mergesort(np.arange(y[i],1,-1)),number = 1)
    result2.append(t),
    meresult2.append(tm)
    selresult2.append(ts)
    i = i + 1
    print(i)
x = np.arange(10,1000,10)

number 4 plot
i=100
j=0
inlist = []
merlist = []
selist = []
avg = 0
merAvg = 0
selAvg = 0
while (i <= 5000):
    print(i)
    while (j <= 100):
        np.random.seed(j)
        array= np.random.permutation(i)
        #print (array)
        avg += timeit.timeit(lambda: insertionsort(array),number = 1)
        merAvg += timeit.timeit(lambda: mergesort(array),number = 1)
        selAvg += timeit.timeit(lambda: selectionsort(array),number = 1)
        j += 1
    avg = avg / 100 
    merAvg = merAvg / 100
    selAvg = selAvg / 100
    merlist.append(merAvg)
    selist.append(selAvg)     
    inlist.append(avg)
    avg = 0
    i = i + 100
    j = 0
x = np.arange(100,5100,100)
plt.plot(x,inlist,'g-',label = "insertion-sort")
plt.plot(x,merlist,'b-',label = "mergesort")
plt.plot(x,selist, 'y-',label= "selectionsort")
plt.xlabel('Input Size')
plt.ylabel('Average Time')
plt.title("Average Sorting Times on Random Arrays") 
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()  

plot 4-5
plt.plot(x,result,'g-',label = "insertion-sort")
plt.plot(x,meresult,'b-',label="mergesort")
plt.plot(x,selresult,'y-',label="selectionsort")
plt.xlabel('numElements')
plt.ylabel('times')
plt.title("Fully Sorted")
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()

plt.plot(y,result2,'g-',label = "insertion-sort")
plt.plot(y,meresult2,'b-',label="mergesort")
plt.plot(y,selresult2,'y-',label="selectionsort")
plt.xlabel('numElements')
plt.ylabel('times')
plt.title("Reverse Sorted")
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()


plot 1-3    
plt.plot(x,result,'g-',label = "sorted")
plt.plot(y,result2,'b-',label = "reverse")
plt.xlabel('numElements')
plt.ylabel('insertiontimes')
plt.title("InsertionSort")
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()
    
plt.plot(x,meresult,'g-',label = "sorted")
plt.plot(y,meresult2,'b-',label = "reverse")
plt.xlabel('numElements')
plt.ylabel('Mergetimes')
plt.title("MergeSort")
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()  

plt.plot(x,selresult,'g-',label = "sorted")
plt.plot(y,selresult2,'b-',label= "reverse")
plt.xlabel('numElements')
plt.ylabel('Selecttimes')
plt.title("SelectionSort")
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()  
'''
