#!/usr/bin/env python
# coding: utf-8

# In[1]:


n=int(input())
for i in range(n):
    for j in range(i+1):
        print("*", end=" ")
    print(" ")

for i in range(n,0,-1):
    for j in range(i-1):
        print("*", end=" ")
    print(" ")


# In[2]:


input=input()
input[::-1]


# In[ ]:




