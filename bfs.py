#!/usr/bin/env python
# coding: utf-8

# In[1]:


graph={
    'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D':[],
    'E':['F'],
    'F':[]
}
visited=[]
queue=[]
def bfs(graph,visited,node):
    queue.append(node)
    visited.append(node)
    while (queue):
        st=queue.pop(0)
        print(st,end=" ")
        for neighbours in graph[st]:
            if neighbours not in visited:
                queue.append(neighbours)
                visited.append(neighbours)
bfs(graph,visited,'B')
        


# In[ ]:





# In[ ]:





# In[ ]:




