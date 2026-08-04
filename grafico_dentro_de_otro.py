# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 19:20:14 2023

@author: Pablo
"""

import matplotlib.pyplot as plt

# Create two subplots within a single figure
fig, axs1 = plt.subplots()
axs2 = axs1.inset_axes([0, 0, 1, 1], facecolor='none')  # Define the position and size of axs2

# Data for axs1 and axs2
x1 = [0, 1, 2, 3, 4]
y1 = [0, 1, 4, 9, 16]

x2 = [0, 1, 2, 3, 4]
y2 = [0, 2, 4, 6, 8]

# Plot data on axs1
axs1.plot(x1, y1, label='axs1')
axs1.set_title('Main Plot')
axs1.set_xlabel('X')
axs1.set_ylabel('Y')
axs1.legend()

# Plot data on axs2 within axs1
axs2.plot(x2, y2, label='axs2')
axs2.set_title('Inset Plot')
axs2.set_xlabel('X')
axs2.set_ylabel('Y')
axs2.legend()

# Show the figure
plt.show()