# -*- coding: utf-8 -*-
"""
EJEMPLO RECURSIVIDAD
    n FACTORIAL

@author: Pablo
"""

#valores = []  
def factorial(n):
    
    if n >= 1:
        #valores.append(n)
        return n * factorial(n-1)
        
    else:
        #print(valores)
        return 1
    
      
print(factorial(100))
        