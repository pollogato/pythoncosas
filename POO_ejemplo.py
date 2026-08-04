# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 20:30:18 2024

@author: Pablo
"""

class notebook:
    """
    Incializo la clase notebook, señalando que reciba los atributos dueño y bateria

    Defino los métodos usar y cargar junto a sus acciones
    """

    def __init__(self,duenho,bateria=100):   #Constructor
        self.duenho = duenho
        self.bateria = bateria
    
    def usar(self):  #Métodp
        self.bateria = self.bateria - 5
        print(f"La bateria del notebook de {self.duenho} tiene un" +
              f"{self.bateria}% de bateria restante")
    
    def cargar(self): #Método
        self.bateria = self.bateria + 10
        print(f"La bateria del notebook de {self.duenho} se ha cargado," + 
              f"quedando {self.bateria}% de bateria restante")
        
    
mi_notebook = notebook('Pablo',78)  #Creo un objeto a partir de la clase notebook

#usos
mi_notebook.usar()
mi_notebook.usar()
mi_notebook.cargar()
mi_notebook.usar()