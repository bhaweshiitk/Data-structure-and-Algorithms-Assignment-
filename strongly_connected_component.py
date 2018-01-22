# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 11:13:37 2017

@author: Bhawesh
link to the problem on SPOJ:
http://www.spoj.com/problems/IITKESO207A_3P_1/
"""
time=0
count=0
class node(object):
    def __init__(self,data):
        self.data=data
        self.color='w'
        self.d=-1
        self.f=-1
        self.cycle=-1
#***************************************
def adj_mat():           # makes an adjecency list of the graph
    n=int(input().strip())
    d={}
    l=[]
    for i in range(n):
        d[i]=[]
        l.append(node(i))#l=[0,1,2,.....,n-1]
    for i in range(n):
        a=input().strip()
        a=a.split(" ")
        a.pop()
        a=list(map(int,a))
        s=[]
        for element in a:
            if element not in s and element !=i:
                s.append(element)
        d[i].extend(s)
    return (l,d)
#****************************************
def inv_g(d):            #inverts the directed graph
    dinv={}
    for i in range(len(d)):
        dinv[i]=[]
    for key in d:
        for value in d[key]:
            dinv[value].append(key)
    return dinv
#*****************************************
def dfs_visit(l,d,vertex,cy_id):
    #print(type(vertex))
    
    global time
    time=time+1
    vertex.d=time
    vertex.color='g'
    vertex.cycle=cy_id
    for element in d[vertex.data]:
        if(l[element].color=='w'):
            l[element].cycle=cy_id
            dfs_visit(l,d,l[element],cy_id)
    time=time+1
    vertex.f=time
    vertex.color='b'
#*****************************************
def dfs(l,d,arr):
    global count
    for i in range(len(arr)):
        nodes=l[arr[i]]
#        print(nodes.data)
        if nodes.color=='w':
            dfs_visit(l,d,nodes,nodes.data)
            count=count+1
#*****************************************
def dfs_initialize(l):
    for element in l:
        element.color='w'
        element.d=-1
        element.f=-1
        element.cycle=-1
#*****************************************
(l,d)=adj_mat()
#print(type(l[0]))
#print(d)
dinv=inv_g(d)
#print(dinv)
arr=[]
for element in range(len(l)):
    arr.append(element)
dfs(l,dinv,arr)

#for element in l:
#    print(element.d,'*',element.f," ",end='')
#******************************************64-73 gives list with nodes s.t. the element are topologically sorted
sortedlist=[]    
for element in l:
    sortedlist.append((element.f,element.data))
sortedlist.sort(reverse=True)
#sortedlist.reverse()
#print(sortedlist)
sink=[]
for element in sortedlist:
    sink.append(element[1])
#******************************************

#for element in sink:
#    print(element,' ',end='')
dfs_initialize(l)
time=0
count=0
#print(d)
dfs(l,d,sink)
#******************************************108-142 finds different cycles and their interconnection
#print('\n')
#for element in l:
#    print(element.data,'*',element.cycle," ",end='')
#sys.stdout.write(str(count))
#sys.stdout.write('\n')
print(count)
dict1={}
for element in l:
    if element.cycle not in dict1:
        dict1[element.cycle]=[]
        dict1[element.cycle].append(element.data)
    else:
        dict1[element.cycle].append(element.data)
minlist=[]
for element in dict1:
    minlist.append((element,min(dict1[element])))
dictnew={}
for element in minlist:
    if element[1] not in dictnew:
        dictnew[element[1]]=[]
    dictnew[element[1]].extend(list(dict1[element[0]]))
finallist=list(dictnew.items())
finallist.sort()
finaldict={}
for element in range(len(finallist)):
    finaldict[element]=finallist[element][1]
for element in finaldict.items():
    id=element[0]
    vertices=element[1]
    for i in vertices:
        l[i].cycle=id
#for element in l:
#    print(element.data,'*',element.cycle," ",end='')
#*********************************************143-153 renames cycles in required format  
newadj={}
for node1 in l:
    idnew=node1.cycle
    if idnew not in newadj:
        newadj[idnew]=[]
    for i in d[node1.data]:
        if(l[i].cycle==node1.cycle):
            continue
        else:
            if l[i].cycle not in newadj[idnew] and l[i].cycle != idnew:
                newadj[idnew].append(l[i].cycle)
#**********************************************154-166 prints the cycles and their interconnection in required format      
for element in range(len(newadj)): 
    newadj[element].sort()
    #newadj[element].append(-1)
newadjlist=list(newadj.items())
newadjlist.sort()
for element in range(len(newadjlist)):
    if newadjlist[element][1]==[]:
        print("-1")
    else:
        print(" ".join(str(x) for x in newadjlist[element][1]),end='')
        print(" ",end='')
        print("-1")
        
 
