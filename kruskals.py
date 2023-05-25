#!/usr/bin/env python
# coding: utf-8

# In[10]:


class Graph:
    def __init__(self,vertices):
        self.vertices=vertices
        self.edges=[]
        self.adjacencylist={v:[] for v in vertices}
    
    def add_edge(self,u,v,weight):
        self.edges.append((u,v,weight))
        self.adjacencylist[u].append((v,weight))
        self.adjacencylist[v].append((u,weight))
        
    def findParent(self,parent,i):
        if parent[i]==i:
            return i;
        return self.findParent(parent,parent[i])
    
    def union(self,parent,rank,x,y):
        root_x=self.findParent(parent,x)
        root_y=self.findParent(parent,y)
        if rank[root_x]<rank[root_y]:
            parent[root_x]=root_y
        elif rank[root_y]<rank[root_x]:
            parent[root_y]=root_x
        else:
            parent[root_y]=root_x
            rank[root_x]+=1
    
    def kruskal(self):
        minimum_spanning_tree=set()
        parent={}
        rank={}
        for i in self.vertices:
            parent[i]=i
            rank[i]=0
        sorted_edges=sorted(self.edges, key=lambda x:x[2])
        for edge in sorted_edges:
            u,v,w=edge
            root_u=self.findParent(parent,u)
            root_v=self.findParent(parent,v)
            if root_u!=root_v:
                minimum_spanning_tree.add(edge)
                self.union(parent,rank,root_u,root_v)
        return minimum_spanning_tree
vertices = [0, 1, 2, 3]  
g = Graph(vertices)  
g.add_edge(0, 1, 5)  
g.add_edge(0, 2, 10)  
g.add_edge(0, 3, 3)  
g.add_edge(1, 3, 1)  
g.add_edge(2, 3, 4)  
minimum_spanning_tree = g.kruskal()  
print(minimum_spanning_tree) 
            


# In[ ]:




