# -*- coding: utf-8 -*-
"""
Created on Tue May 17 21:12:02 2016

@author: Jeffrey Chan
         Manav Sharma
"""
import sys 
import heapq
from operator import itemgetter
class Node:
    #initializing an empty new node with these values
    def __init__(self,key,value,parent=None):
        self.lChild = None
        self.rChild = None
        self.parent = parent
        self.key = key    
        self.value = value
        
class BSTree:
    def __init__(self):
        self.root = None
       
    #insert a key into a new node into the tree
    def insert(self,key,value):
       current = self.root       
       #root is none, so insert a new node with root
       if self.root == None:
            self.root = Node(key,value)
            return True
            #print (self.root.key)
       #find the insertion point to insert the new key
       while current != None:
           
           if current.key == key:
               current.value += value
               return True
           #compare the current key with the key to be inserted
           elif current.key > key:
               #if the current has a left child keep going down the tree
               if current.lChild is not None:
                   current = current.lChild
               else:
               #insert new node if current does not have a left child
                   current.lChild = Node(key,value,current)
                   return True
           else:
               if current.rChild is not None:
                   current = current.rChild
               else:
                   current.rChild = Node(key,value,current)
                   return True
    def delete(self,key):
        #find where the node is located
        current = self.findn(key)
        
        if (current == None):
            return
        #case where it has two childrens
        
        if current.lChild is not None and current.rChild is not None:
            succ = self.successor(key)
            #print(succ.key)
            current.value = succ.value
            current.key = succ.key  
            #send successor to be deleted
            self.deleteHelper(succ)
        else:
            #send the current to be deleted
            self.deleteHelper(current)
            
           
    def deleteHelper(self,node):
        current = node
        #case where there is only one child
        if current.lChild is None and current.rChild is None:
            if(current.parent.lChild == current):            
                current.parent.lChild = None
            else:
                current.parent.rChild = None
            current = None            
            return True
        #case where theres is only one child
        if current.lChild is None and current.rChild is not None:
            p = current.parent
            #delete the current and fix the pointers
            if p.lChild == current:
                p.lChild = current.rChild
                current = None
            elif p.rChild == current:
                p.rChild = current.rChild
                current = None
            return 
        #case where theres no child
        if current.rChild is None and current.lChild is not None:
            p = current.parent
            #delete the current and fix the pointers
            if p.lChild == current:
                p.lChild = current.lChild
                current = None
            elif p.rChild == current:
                p.rChild = current.lChild
                
            return
    #find key and return value
    def findn(self,key):
        if self.root is None:
            return None
        current = self.root
        #traverse and find the value
        while(current != None):
            if current.key == key:
                return current
            else:
                #check if key is in the left side
                if current.key > key:
                    if current.lChild is None:
                       # print ("Key cannot be found")
                        return None
                    else:
                #if there is a left child, keep traversing until key is found
                        current = current.lChild
                else:
                    if current.rChild is None:
                        #print ("Key cannot be found")
                        return None
                    else:
                        current = current.rChild        
    def find(self,key):
        if self.root is None:
            return None
        current = self.root
        #traverse and find the value
        while(current != None):
            if current.key == key:
                return current.value
            else:
                #check if key is in the left side
                if current.key > key:
                    if current.lChild is None:
                       # print ("Key cannot be found")
                        return None
                    else:
                #if there is a left child, keep traversing until key is found
                        current = current.lChild
                else:
                    if current.rChild is None:
                        #print ("Key cannot be found")
                        return None
                    else:
                        current = current.rChild
    def successor(self,key):
        current = self.findn(key)
        #find where the key is located in the tree
        if current is None:
            return None
        #when its not a leaf node and contains childrens.
        if current.rChild is not None:
            cur = current.rChild
            while cur.lChild is not None:
                cur = cur.lChild
            return cur
        #when it is a leaf node, traverse up to find the successor
        while current.parent is not None and current.parent.rChild is current:
            current = current.parent
        return current.parent
    #helper function for traversal
    def travhelp(self,node):
        current = node
        if current is None:
            return None
        self.travhelp(current.lChild)
        print (current.key,",",current.value)
        self.travhelp(current.rChild)
    def inOrderTraversal(self):
        if(self is None):
            return None
        self.travhelp(self.root)
        
  

'''    #inorder traversal through the tree
    def inOrderTraversal(self, node):
        current = node        
        if current is None:
            return None
        self.inOrderTraversal(current.lChild)
        print (current.key,",",current.value)
        self.inOrderTraversal(current.rChild)
  '''   
   # def helper(self,node):
     #   return self.root
    
'''
    def inOrderTraversal2(self,node):
            current = node
            if current is None:
                return None
            
            self.inOrderTraversal2(current.lChild)
            #print (current.key,",",current.value)    
            self.h.append(current.key)
            self.l.append((current.key,current.value))
            self.inOrderTraversal2(current.rChild) 
'    
    def returnH(self):
        return self.h
    def returnl(self):
        return self.l    

def process(stopfile,finefile,lowr,highr):

    items = set()
    line = stopfile.readline()
    while line:
        w = line.split('\n')
        line = stopfile.readline()
        items.add(w[0])
    line2 = finefile.readline()
    while line2:
        word = line2.split(" ")
        line2 = finefile.readline()
        score = word[0].split(":")
        score2 = int(score[0])
        for i in range(1,len(word)):
            if(i == (len(word)-1)):
                string = word[i].split('\n')
                if string[0] not in items:
                    if (score2 <= 3):
                        lowr.insert(string[0],1)
                    else:
                        highr.insert(string[0],1)
                else:
                    continue
            else:
                if (word[i] in items):
                    continue
                else:
                    if (score2 <= 3):
                
                        lowr.insert(word[i],1)
                    else:
                        highr.insert(word[i],1)
   
def main():
    stopwords = open(sys.argv[1])
    finefoods = open(sys.argv[2])
    lowr = BSTree()
    highr = BSTree()
   
    l = ["asymptotic","binary","complexity","depth","mergesort","quicksort","structure","theta"]
   
    process(stopwords,finefoods,lowr,highr)
    lowr.inOrderTraversal2(lowr.root)
    list2 = list(lowr.returnH())
    print("length of list2 is: " , len(list2))
    #heapq.heapify(list2)
    for i in range(len(list2)):
        highr.delete(list2[i])
    highr.inOrderTraversal2(highr.root)
    list1 = list(highr.returnl())
    print("length of list1: " , len(list1))
    heapq.heapify(list1)
    top = [x[0] for x in heapq.nlargest(25,list1,key=itemgetter(1))]
    print(top)
    
    
    
    print ("length of list2", len(list2))
    heap = list(highr.returnH())
    heapq.heapify(heap)
    h = heapq.nlargest(21,heap)
    top = [x[0] for x in heapq.nlargest(2,list2,key=itemgetter(1))]
    print(top)
    for i in range(len(h)):
        for j in range(len(list2)):
            #print (h[i], list2[j][1])
            if h[i] == list2[j][1]:
                print (list2[j])
                continue
            j += 1
        i += 1 
    lowr.inOrderTraversal2(lowr.root)
    list3 = list(lowr.returnl())
    heapq.heapify(list3)
    #print ("length of list2", len(list2))
   
    top2 = [x[0] for x in heapq.nlargest(21,list3,key=itemgetter(1))]
    print("low", top2)
               

    for i in range(len(l)):
        word = lowr.find(l[i])
        if word is False:        
            lowr.insert(l[i],1) 
            succ = lowr.successor(l[i])
            print("low tree succ: ",l[i], succ.key)
            print("frequency of low: ",lowr.find(l[i]).value) 
            
        else:
            print ("low word: " , l[i])
            print ("value of word in low: ",word.value)
            
    for i in range(len(l)):
        word = highr.find(l[i])
        if word is False:
            highr.insert(l[i],1)
            succ = highr.successor(l[i])
            print("high tree succ: ",l[i], succ.key)
            print("frequency of high: ",highr.find(l[i]).value)    
           
        else:
            print ("high word: " , l[i])
            print ("value of word in high: ", word.value)
    #highr.inOrderTraversal(lowr.root)
main()
'''