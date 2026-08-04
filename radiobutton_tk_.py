# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 20:24:45 2023

@author: Pablo
"""

import tkinter as tk


def comprobar():
    print(radioValue.get())

app = tk.Tk()
app.geometry("150x100")

radioValue = tk.IntVar()


rdioOne = tk.Radiobutton(app, text="January", variable=radioValue, value=1)
rdioTwo = tk.Radiobutton(app, text="Febuary", variable=radioValue, value=2)
rdioThree = tk.Radiobutton(app, text="March", variable=radioValue, value=3)

rdioOne.grid(column=0, row=0)
rdioTwo.grid(column=0, row=1)
rdioThree.grid(column=0, row=2)

boton = tk.Button(app, text="Comprobar",command=comprobar)
boton.grid(column=0, row=3)

app.mainloop()
