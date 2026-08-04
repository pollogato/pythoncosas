# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 20:02:05 2025

@author: Pablo
"""

class notebook:
    # Constructor
    def __init__(self,duenho,bateria=100):
        self.duenho = duenho
        self.bateria = bateria

    # Se define el comportamiento cuando el objeto se invoca como una cadena de texto
    def __str__(self):
        return f"Este notebook pertenece a {self.duenho} y le queda un {self.bateria}% de bateria."
    
    # Se define el comportamiento cuando el objeto se invoca en una suma con otro número
    def __add__(self, carga):
        self.bateria += carga
        return self


# Se inicializa el objeto
mi_notebook = notebook('Pablo',78)

# Invoca el objeto en una suma
mi_notebook += 5

# Invoca el objeto como una cadena de texto
print(mi_notebook)