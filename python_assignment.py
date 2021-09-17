#!/usr/bin/env python
# coding: utf-8

# # Assignment 1

# In[10]:


i = 2000
for i in range(2000,3200+1):
    if i%7==0 and i%5!=0:
        print(i, end=",")
        


# In[16]:


first_name=input("First Name :")
last_name=input("Last Name :")
print(first_name,' ', last_name)
x=first_name[::-1]
y=last_name[::-1]
print('Reverse oder:',x,y)


# In[19]:


diameter = int(input("Enter diameter of sphere :"))
r = diameter/2
pi=22/7
volume = 4/3*pi*r**3
print("Volume of sphere :",volume)


# In[ ]:




