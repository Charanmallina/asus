#!/usr/bin/env python
# coding: utf-8

# In[4]:


n = int(input())
if n%3 == 0:
    print(n,"is divisible by 3")
else:
    print(n,"not divisible by 3")

output:

171
171 is divisible by 3


# In[8]:


n = int(input())
if n < 0:
    print("number is invalid")
elif n == 0 or n == 1:
    print("neither prime nor composite")
else:
    for i in range(2,n):
        if n%i == 0:
            print("not prime number")
    else:
        print("prime number")

output:
3
prime number






















