#!/usr/bin/env python
# coding: utf-8

# In[9]:


from numpy import Inf
def Dijkstras(graph,start):
    l=len(graph)
    dis=[Inf for i in range(l)]
    dis[start]=0
    vis=[False for i in range(l)]
    
    for i in range(l):
        u=-1
        for x in range(l):
            if not vis[x] and (u==-1 or dis[x]<dis[u]):
                u=x
        if dis[u]==Inf:
            break
        vis[u]=True
        for v,d in graph[u]:
            if dis[u]+d<dis[v]:
                dis[v]=dis[u]+d
                
    return dis

graph = {
    0: [(1, 1)],
    1: [(0, 1), (2, 2), (3, 3)],
    2: [(1, 2), (3, 1), (4, 5)],
    3: [(1, 3), (2, 1), (4, 1)],
    4: [(2, 5), (3, 1)]
}
print(Dijkstras(graph,1))


# In[ ]:




