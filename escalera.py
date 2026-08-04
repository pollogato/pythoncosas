# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 16:36:26 2023

@author: Pablo
"""


j = 10
for i in range(1,j):
    print("*"*i)
    
    
pira = lambda y: print('\n'.join([i*"*" for i in range(1,y+1)]))