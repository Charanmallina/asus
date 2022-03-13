#!/usr/bin/env python
# coding: utf-8

# In[ ]:


c= 4
while(True):
    password = input()
    numerics = '0123456789'
    cap_alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_char = "#$%@"
    low_alpha = "abcdefghijklmnopqrstuvwxyz"
    sum = 0;w = 0;x = 0;y=0;z = 0
    if len(password) >= 6 and len(password) <= 15:
        for i in range(len(password)):
            if password[i] in numerics:
                w = 1
            elif password[i] in cap_alpha:
                x = 1
            elif password[i] in low_alpha:
                y = 1
            elif password[i] in special_char:
                z = 1
    sum = w+x+y+z
    if sum >= 4:
        print("password accepted")
        break
    else:
        c-=1 
        if c==0:
            print("Sorry your chances are completed ")
            break
        print("you have",(c),"atempts left")


Output:
charan
you have 3 atempts left
charan123
you have 2 atempts left
cherry
you have 1 atempts left
Charan@123
password accepted




