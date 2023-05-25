#!/usr/bin/env python
# coding: utf-8

# In[22]:


graph={
    'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D':[],
    'E':['F'],
    'F':[]
}
visited=set()
def dfs(graph,visited,node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbours in graph[node]:
            dfs(graph,visited,neighbours)
            
dfs(graph,visited,'B')


# In[ ]:




