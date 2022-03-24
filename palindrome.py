# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 15:18:09 2022

@author: chara
"""
n = input()
l = list(n)
k = len(l)
for i in range(k):
    if l[i] != l[k-i-1]:
        print("not palindrome")
        break
else:
    print("palindrome")    

Output:
naman
palindrome    