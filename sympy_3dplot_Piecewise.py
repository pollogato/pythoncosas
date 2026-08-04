# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 21:04:00 2023

@author: Pablo
"""

from IPython.display import display
#display(objeto)



import sympy as sp
from sympy.plotting import plot3d

sp.init_printing(use_unicode=True, wrap_line=True)
# sp.init_printing()

n, L, x = sp.symbols('n L x')    

fx = sp.cos(sp.pi * x/L) ** 2
Sfx = sp.integrate(fx, (x, -L/2, L/2))
Sf = sp.integrate(fx,(x))
# sp.pprint(Sf,use_unicode=True)
display(Sf)
# print(fx)
# plot3d(L*(sympy.sin(sympy.pi*x/L)*sympy.cos(sympy.pi*x/L)/2 + sympy.pi*x/(2*L))/sympy.pi)

plot3d(Sf.args[0][0]) ##Get func of a Piecewise 

# import plotly.graph_objects as go

# fig = go.Figure(Sf.args[0][0])