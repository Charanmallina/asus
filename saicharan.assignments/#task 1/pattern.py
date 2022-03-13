#!/usr/bin/env python
# coding: utf-8

# In[2]:


n = 6
for i in range(n):
    for j in range(n-i):
        print("*",end="")
    print()    

Output:

******
*****
****
***
**
*


# In[4]:


n = 7
for i in range(n):
    for j in range(1,i+1):
        print(j,end="")
    print() 

output:

1
12
123
1234
12345
123456

# In[30]:


n = 5
for i in range(n+1):
    print(" "*(n-i)+"* "*i)


output:
 
    * 
   * * 
  * * * 
 * * * * 
* * * * * 







