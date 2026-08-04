# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 10:46:04 2024

@author: Pablo
"""


def fibo(n):
    # fib ante-anterior
    fib_n_2 = 0
    # fib anterior
    fib_n_1 = 1
    # fib actual
    fib_n = 0
    # contador de la iteracion
    i = 1
    
    while i < n:
        # Se calcula el fib(i)
        fib_n = fib_n_1 + fib_n_2
        
        # Se actualiza el fib(i-2)
        fib_n_2 = fib_n_1
        # Se actualiza el fib(i-1)
        fib_n_1 = fib_n
        
        # Se suma 1 al contador de la iteracion i
        i += 1
    
    # Se muestra y retorna el fib(n), si n != 1 
    if n != 1:
        #print(f'El Fibonacci de {n} es {fib_n}')
        return fib_n
    
    #Se muestra y retorna el fib(1)
    else:
        #print(f'El Fibonacci de {n} es 1')
        return fib_n_1

def fibo_rec(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo_rec(n - 1) + fibo_rec(n - 2)