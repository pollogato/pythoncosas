# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 15:00:36 2023

@author: Pablo
"""

def porctj(n,m): # n de m
    res = n * 100 / m
    res = str(res)+'%'
    return res    

print(porctj(40,96))