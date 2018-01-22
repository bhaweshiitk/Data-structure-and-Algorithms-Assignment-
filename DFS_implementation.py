# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 15:21:13 2017

@author: Bhawesh
"""
time=0
class node(object):
    def __init__(self,data):
        self.data=data
        self.color='w'
        self.parent=None
        self.d=-1
        self.f=-1
def adj_matrix():
    j=(input().strip())
    j=j.split(" ")
    j=list(map(int,j))
    n=j[0]#no of nodes,edges
    m=j[1]
    d={}#adj matrix
    l=[]#contaons all nodes
    for element in range(n+1):
        d[element]=[]
        l.append(node(element))
    for element in range(m):
        x=input().strip()
        x=x.split(" ")
        x=list(map(int,x))#contains edge info
        d[x[0]].append(x[1])
        d[x[1]].append(x[0])
    l[0].color='b'
    return(l,d)
def dfs(l,d):
    for vertex in l:
        if(vertex.color=='w'):
            dfs_visit(l,d,vertex)
def dfs_visit(l,d,vertex):
    #print(type(vertex))
    global time
    time=time+1
    vertex.d=time
    vertex.color='g'
    for element in d[vertex.data]:
        if(l[element].color=='w'):
            l[element].parent=vertex
            dfs_visit(l,d,l[element])
    time=time+1
    vertex.f=time
    vertex.color='b'
    
(l,d)=adj_matrix()

head=int(input().strip())
dfs_visit(l,d,l[head])
c=0
for vertex in l:
    if vertex.color=='w':
        c=c+1
print(c)
for element in l:
        print(element.d, end='')
        print("*",end='')
        print(element.f)    
    