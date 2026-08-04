# -*- coding: utf-8 -*-
"""
Created on Mon Oct 27 11:36:37 2025

@author: Pablo
"""

import cowsay

#cowsay.tux("mu")

for animal in cowsay.char_names:
    print(f"\n=== {animal} ===")
    getattr(cowsay, animal)("oa")
