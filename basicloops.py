# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 15:20:06 2022

@author: chara
"""

n = input()
k = len(n)
for i in range(k-1):
    if int(n)%2 == 0:
        print(1,end=" ")
    else:
        print(0,end=" ")
    n=int(n)//2

output:
10110