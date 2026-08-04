# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 20:52:17 2023

@author: Pablo
"""

def abrir_cambiar(arch):
    with open(arch, 'r') as f:
        line = f.read()
        print(line)
    with open(arch, 'w') as f:
        f.write('Chao')
    with open(arch, 'r') as f:
        lineas = f.read()
    return lineas




lineas=abrir_cambiar('text.txt')
print(lineas)