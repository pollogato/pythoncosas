# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 14:35:15 2024

@author: Pablo
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Definir parámetros u y v
u = np.linspace(0, 2 * np.pi,150)  # Parámetro u (giro alrededor del anillo)
v = np.linspace(-1, 1, 150)  # Parámetro v (altura de la superficie de Möbius)

# Crear malla 2D para u y v
u, v = np.meshgrid(u, v)  

# Ecuaciones paramétricas de la superficie de Möbius
x = (1 + (v / 2) * np.cos(u / 2)) * np.cos(u)
y = (1 + (v / 2) * np.cos(u / 2)) * np.sin(u)
z = (v / 2) * np.sin(u / 2)

# Crear el gráfico

fig, ax = plt.subplots(subplot_kw={"projection": "3d"}, figsize=(15,15))

def crear_frames(frame):
      print(f"Generando frame: {frame}")
      
      # Elimina frame anterior
      ax.clear()
      
      # Dibujar superficie
      ax.plot_surface(x, y, z, cmap='Greens', rcount = 150, ccount = 150,
                      antialiased=False)  
      # Rango del gráfico
      ax.set_zlim(-1,1)
      
      # Eliminar ejes
      ax.grid(False)
      ax.set_xticks([])
      ax.set_yticks([])
      ax.set_zticks([])
      
      # Eliminar líneas de los ejes (invisibles)
      ax.xaxis.line.set_color((1.0, 1.0, 1.0, 0.0))
      ax.yaxis.line.set_color((1.0, 1.0, 1.0, 0.0))
      ax.zaxis.line.set_color((1.0, 1.0, 1.0, 0.0))
      
      # Quitar fondo completamente
      # fig.patch.set_alpha(0.0)
      # ax.set_facecolor((0,0,0,0))

      # Quitar paneles
      ax.xaxis.pane.set_alpha(0.0)
      ax.yaxis.pane.set_alpha(0.0)
      ax.zaxis.pane.set_alpha(0.0)


      ax.view_init(30, 70+frame)
      return fig,

ani = FuncAnimation(fig, crear_frames, frames=range(0, 360))
ani.save('C:/Users/Pablo/Pictures/mobius.gif', fps=60)


plt.show()
