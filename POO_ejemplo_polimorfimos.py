# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 14:10:26 2025

@author: Pablo
"""

### Ejemplo Polimorfismo ###
"""
Defino una 'superclase' equipo donde inicializo los atribuos duenho y bateria.

Las 'subclases' notebook y celular heredan los atributos de la 'superclase' equipo,
en específico heredan 'duenho' y 'bateria'.

Cada subclase posee el método usar, el cual realiza distinta acciones
"""
class equipo:
    def __init__(self,duenho,bateria):
        self.duenho = duenho
        self.bateria = bateria

class notebook(equipo):
    def usar(self):
        print('Trabaja')

class celular(equipo):
    def usar(self):
        print('Envia mensaje')

# Inicialización objetos
mi_celular = celular('pablo', 100)
mi_notebook = notebook('pablo', 95)

# Usar métodos polimorficos
mi_celular.usar()
mi_notebook.usar()