# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 22:41:38 2023

@author: Pablo
"""

import random

random.seed(2)
DADOS = {
1: (
        "┌─────────┐\n"
        "│         │\n"
        "│    ●    │\n"
        "│         │\n"
        "└─────────┘"
    ),
    
    2: (
        "┌─────────┐\n"
        "│  ●      │\n"
        "│         │\n"
        "│      ●  │\n"
        "└─────────┘"
    ),

    3: (
        "┌─────────┐\n"
        "│  ●      │\n"
        "│    ●    │\n"
        "│      ●  │\n"
        "└─────────┘"
    ),

    4: (
        "┌─────────┐\n"
        "│  ●   ●  │\n"
        "│         │\n"
        "│  ●   ●  │\n"
        "└─────────┘"
    ),

    5: (
        "┌─────────┐\n"
        "│  ●   ●  │\n"
        "│    ●    │\n"
        "│  ●   ●  │\n"
        "└─────────┘"
    ),

    6: (
        "┌─────────┐\n"
        "│  ●   ●  │\n"
        "│  ●   ●  │\n"
        "│  ●   ●  │\n"
        "└─────────┘"
    ),
    
    7: (
        "┌─────────┐\n"
        "│  ●   ●  │\n"
        "│  ● ● ●  │\n"
        "│  ●   ●  │\n"
        "└─────────┘"
    ),
    
    8: (
        "┌─────────┐\n"
        "│  ● ● ●  │\n"
        "│  ●   ●  │\n"
        "│  ● ● ●  │\n"
        "└─────────┘"
    ),
    
    9: (
        "┌─────────┐\n"
        "│  ● ● ●  │\n"
        "│  ● ● ●  │\n"
        "│  ● ● ●  │\n"
        "└─────────┘"
    ),
    
    10: (
        "┌─────────┐\n"
        "│ ●  ●  ● │\n"
        "│ ● ● ● ● │\n"
        "│ ●  ●  ● │\n"
        "└─────────┘"
    ),
    
    11: (
        "┌─────────┐\n"
        "│ ● ● ● ● │\n"
        "│ ●  ●  ● │\n"
        "│ ● ● ● ● │\n"
        "└─────────┘"
    ),
    
    12: (
        "┌─────────┐\n"
        "│ ● ● ● ● │\n"
        "│ ● ● ● ● │\n"
        "│ ● ● ● ● │\n"
        "└─────────┘"
    )
}

def evaluar_cantidad_dados(cantidad_dados_input):
    flag = 0
    while flag == 0:
        if int(cantidad_dados_input) < 5 and int(cantidad_dados_input) > 0:
            flag += 1
            return int(cantidad_dados_input)
        else:
            cantidad_dados_input = input(
                "Selección inválida. Favor de seleccionar número entre 1 y 4: ")
    
def evaluar_caras_dados(caras_dados_input):
    flag = 0
    while flag == 0:
        if int(caras_dados_input) > 3 and int(caras_dados_input) < 13:
            flag += 1
            return int(caras_dados_input)
        else:
            caras_dados_input = input(
                "Selección inválida. Favor de seleccionar número entre 4 y 12: ")
            
def tirar_dados(cantidad_dados_input,caras_dados_input):      
    for num_tiradas in range(int(cantidad_dados_input)):
        num_caras = random.randint(1,int(caras_dados_input))
        print(DADOS[num_caras])

            
cantidad_dados_input = input("¿Cuántos dados quiere lanzar? [1-4]: ")
cant_dados = evaluar_cantidad_dados(cantidad_dados_input)

caras_dados_input = input("¿De cuántas cara desea el dado? [4-12]: ")
caras_dados = evaluar_caras_dados(caras_dados_input)

tirar_dados(cant_dados,caras_dados)