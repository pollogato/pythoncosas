# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 13:50:57 2025

@author: Pablo
"""

### Ejemplo Herencia ###
"""
Defino una 'superclase' equipo donde inicializo los atribuos duenho y bateria.

Las 'subclases' notebook y celular heredan los atributos de la 'superclase' equipo,
en específico heredan 'duenho' y 'bateria'.
"""
class equipo:
    def __init__(self,duenho,bateria):
        self.duenho = duenho
        self.bateria = bateria

class notebook(equipo):
    pass

class celular(equipo):
    pass

# Inicialización objetos
mi_celular = celular('pablo', 100)
mi_notebook = notebook('pablo', 95)

# Mostrar atributos heredados
print(f'El celular de {mi_celular.duenho} tiene un {mi_celular.bateria}% de bateria')
print(f'El notebook de {mi_notebook.duenho} tiene un {mi_notebook.bateria}% de bateria')