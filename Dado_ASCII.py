# -*- coding: utf-8 -*-
#Dado_ASCII.py
"""
@author: Pablo LO
Inspiration: https://realpython.com/python-dice-roll/
"""

import random

DICE_ART = {

    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
    ),

    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ),

    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
    ),

    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ),

    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    
    7: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ● ● ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    
    8: (
        "┌─────────┐",
        "│  ● ● ●  │",
        "│  ●   ●  │",
        "│  ● ● ●  │",
        "└─────────┘",
    ),
    
    9: (
        "┌─────────┐",
        "│  ● ● ●  │",
        "│  ● ● ●  │",
        "│  ● ● ●  │",
        "└─────────┘",
    ),
    
    10: (
        "┌─────────┐",
        "│ ●  ●  ● │",
        "│ ● ● ● ● │",
        "│ ●  ●  ● │",
        "└─────────┘",
    ),
    
    11: (
        "┌─────────┐",
        "│ ● ● ● ● │",
        "│ ●  ●  ● │",
        "│ ● ● ● ● │",
        "└─────────┘",
    ),
    
    12: (
        "┌─────────┐",
        "│ ● ● ● ● │",
        "│ ● ● ● ● │",
        "│ ● ● ● ● │",
        "└─────────┘",
    )
}


def parse_input(input_string):

    max_tiradas = [str(i) for i in range(1,9)]
    
    if input_string in max_tiradas:

        return int(input_string)

    else:
        print("Selección inválida. Favor de seleccionar número entre 1 y 8.")

        raise SystemExit()


def dice_face(input_face):
    
    max_face = [str(i) for i in range(4,13)]
    
    if input_face in max_face:
        
        return int(input_face)

    else:
        print("Selección inválida. Favor de seleccionar número entre 4 y 12.")

        raise SystemExit()    

def roll_dice(num_dice,num_dice_face):

    roll_results = []
    
    for _ in range(num_dice):
        roll = random.randint(1, num_dice_face)
        roll_results.append(roll)

    return roll_results


def show_dice(roll_results):
    
    num_lists_res = 5
    list_results = [[] for _ in range(num_lists_res)]
    
    for i in roll_results:
        tirada = str(DICE_ART[i]).split(",")
        for j in range(5):
            list_results[j].append(tirada[j])
               
    for pre_dices in list_results:
        result_string = ''.join(pre_dices)
        result_string = result_string.replace("'", "").replace(
            "(", " ").replace(")", "").replace(",", "")
        
        print(result_string)        
        

num_dice_input = input("¿Cuántos dados quiere lanzar? [1-8]: ")

num_dice = parse_input(num_dice_input)

num_dice_face_input = input("¿De cuántas cara desea el dado? [4-12]: ")

num_dice_face = dice_face(num_dice_face_input)

roll_results = roll_dice(num_dice,num_dice_face)

show_dice(roll_results)
