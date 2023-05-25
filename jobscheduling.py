#!/usr/bin/env python
# coding: utf-8

# In[3]:


profit = [25,15,100,10, 150]
jobs = ["j1", "j2", "j3", "j4", "j5"]
deadline = [2,3,3,3,4] 
printNjobs=list(zip(profit,jobs,deadline))
printNjobs=sorted(printNjobs,key=lambda x:x[0],reverse=True)

slot=[]
for i in range(len(jobs)):
    slot.append(0)
    
profit=0
ans=[]

for i in range(len(jobs)):
    ans.append("null")
    
for i in range(len(jobs)):
    job=printNjobs[i]
    for j in range(job[2],0,-1):
        if slot[j]==0:
            ans[j]=job[1]
            profit+=job[0]
            slot[j]=1
            break
            
print("job scheduled",ans[1:])
print(profit)


# In[ ]:




