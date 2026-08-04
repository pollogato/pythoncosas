# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 14:11:20 2024

@author: Pablo
"""

#valores = []  
def factorial(n):
    
    while str(n).isdigit() == False:  ## python no reconoce '-5' como digito
        n = input('Entrada incorrecta, ingrese nuevamente: ')
        
    n = int(n)
            
    if n >= 1:
        #valores.append(n)
        return n * factorial(n-1)
        
    else:
        return 1
    
      
v = factorial(25)
print(v)