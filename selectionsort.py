#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def selectionsort(arr,size):
    min_ind=0;
    for i in range(size):
        min_ind=i
        for j in range(i+1,size):
            if arr[min_ind]>arr[j]:
                min_ind=j
        (arr[min_ind],arr[i])=(arr[i],arr[min_ind])

arr=[]
n=int(input("Enter number of elements"))
for i in range(n):
    ele=int(input())
    arr.append(ele)
selectionsort(arr,size)
print(arr)        


# In[ ]:





# In[ ]:




