# your code goes here
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 23:11:11 2017

@author: Bhawesh

Link to the question on SPOJ:
http://www.spoj.com/problems/IITKESO207A_4P_1/
"""

import math
import sys
l=[]
class node(object):
    def __init__(self,num):
        self.num=num
        self.parent=None
        self.dist=sys.maxint
#******************************************************************************
class minheap(object):
    def __init__ (self):
        self.data=[]
        self.pos=[]
    def addelem(self,i):
        self.data.append(i)
    def parent(self,i):
        return self.data[math.floor(i/2)]
    def rchild(self,i):
        return self.data[2*i+1]
    def lchild(self,i):
        return self.data[2*i]
    def size(self):
        return len(self.data)
#******************************************************************************
def minheapify(minh,i,size):
    """
    minheapify at index i of self.data
    """
    minheaplist=minh.data
    sindx=i
   # print(i)
    n=size
    if(2*i<n)and(minheaplist[i].dist>minheaplist[2*i].dist):
        sindx=2*i
    if(2*i+1<n)and(minheaplist[sindx].dist>minheaplist[2*i+1].dist):
        sindx=2*i+1
    if(sindx!=i):
        temp=minheaplist[i]
        minh.pos[minheaplist[i].num]=sindx
        minheaplist[i]=minheaplist[sindx]
        minh.pos[minheaplist[sindx].num]=i
        minheaplist[sindx]=temp
        temp=minh.pos[i]
        minheapify(minh,sindx,size)
   # for element in minheaplist:
        #print(element.num,end=' ')
   # print('\n')
#******************************************************************************
def extractmin(mh,size):
    global l
    mhlist=mh.data
    x=mhlist[1]
    g=(mhlist[1].num)
    mh.pos[g]=-10
    mhlist[1]=mhlist[size-1]
    g=(mhlist[size-1].num)
    mh.pos[g]=1
    mhlist[size-1]=x
    p=mhlist.pop()
   # print(p.num,'*pop*',p.dist)
    l.append(p)
    size=size-1
    minheapify(mh,1,size)
   # for element in mh.data:
   #     print(element.dist,'elem.dist',end=' ')
   # print('\n')
    return p
#******************************************************************************
#def decreasekey(mh,key,index,size):
#    mh=key
#    minheapify(mh,index,size)
#******************************************************************************
#def adj_mat():           # makes an adjecency list of the graph (This part of code is same as in last assignment except some minor modificarion)
#    n=int(raw_input().strip())
#    d={}
#    mheap=minheap()
#    mheap.addelem(node(-1))
#    mheap.pos.append(0)
#    for i in range(n):
#        d[i]=[]
#        mheap.addelem(node(i))#l=[0,1,2,.....,n-1]
#        mheap.pos.append(i+1)
#    for i in range(n):
#        a=input().strip()
#        a=a.split()
#        a.pop()
#        a=list(map(int,a))
#        size=len(a)
#        w=0
#        edge=[]
#        while(w<size):
#            edge.append([a[w],a[w+1]])
#            w=w+2    
#        s=[]
#        for element in edge:
#            s.append(element)
#        d[i].extend(s)
   # return (mheap,d)
def heapify(mheap,index):
    heaplist=mheap.data
    index_p=int(index/2)
    if(heaplist[index].dist<heaplist[index_p].dist and index_p>0):
        g=heaplist[index].num
        h=heaplist[index_p].num
        mheap.pos[g]=index_p
        mheap.pos[h]=index
        temp=heaplist[index]
        heaplist[index]=heaplist[index_p]
        heaplist[index_p]=temp
        heapify(mheap,index_p)
        
        
                  
                 
#****************************************************************************** 
def relax(mh,u,v,w,size,c):
    if(v.dist>u.dist+w):
        v.dist=u.dist+w
        #print(v.dist,'haha',v.num)
        v.parent=u
        heapify(mh,c)
def Dijkstra(mheap,d,size):
    while(size!=1):
        u=extractmin(mheap,size)
        #print(u.num,'*min*',u.dist)
        size=size-1
        for element in d[u.num]:
            ind=element[0]
            w=element[1]
            if(mheap.pos[ind]!=-10):
               # print(mheap.pos)
                c=mheap.pos[ind]
               # print(c)
                relax(mheap,u,mheap.data[c],w,size,c)
#******************************************************************************
#(mheap,d)=adj_mat()
# given_data=input()
given_data=[int(i) for i in raw_input().split()]
n=given_data[0]
s=given_data[1]
d={}
mheap=minheap()
mheap.addelem(node(0))
mheap.pos.append(0)
for i in range(1,n+1):
    d[i]=[]
    mheap.addelem(node(i))
    mheap.pos.append(i)
    deg=(i*given_data[4]+i*i*given_data[6])%given_data[2]
    for j in range(1,deg+1):
        vertex=(i*given_data[3]+j*given_data[5])%n
        vertex=vertex+1
        weight=(i*given_data[7]+j*given_data[8])%given_data[9]
        d[i].append([vertex,weight])
source=mheap.data[s]
source.dist=0
sz=mheap.size()
heapify(mheap,s)
# for element in mheap.data:
#     print(element.num,element.dist)
Dijkstra(mheap,d,sz)
ans=[]
for element in l:
    ans.append((element.num,element.dist))
ans.sort()
for element in ans:
    if element[1] is not sys.maxint:
        print element[0],element[1]
    else:
        print element[0],-1
    

