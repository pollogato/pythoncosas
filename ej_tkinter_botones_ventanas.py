# -*- coding: utf-8 -*-

"""

Este código muestra ejemplos del uso de funciones básica de tkinter.
Insto a cada grupo a investigar más por su cuenta para encontrar funciones que
les sean útiles para el desarrollo de su solución
"""
import tkinter as tk
from tkinter import messagebox

#En una función defino la ventana root
def open_root():
    
    # Mostrar el widget ((contenido) inicial

    # Label permite mostrar texto en la ventana
    # tk.Label(ventana don se ubica, texto a mostrar, ...)
    # fg -> define color del texto
    tk.Label(root, text="¡Hola mundo!", fg="red").place(x=70, y=15)
    
    
    # Defino un botón que quiero que aparezca en la ventana root,
    # bg -> color de fondo del botón ; place -> ubicación del botón
    # Comando -> acción que realiza el botón
    # Ojo que al invicar funciones con command, estas no llevan () 
    # tk.Button(ventana don se ubica, texto a mostrar, acción que se realiza al apretar el botón)
    tk.Button(root, text="Ventana2", command=open_ventana2, bg="green").place(x=40, y=75)
    tk.Button(root, text="Ventana hija", command=open_vent_hija, bg="black",
              fg="white").place(x=150, y=200)

# Función para limpiar el widget ("contenido") de la ventana
def limpiar_frame():
    for widget in root.winfo_children():
        widget.destroy()

def open_vent_hija():

    vent_hija = tk.Toplevel(root)
    vent_hija.geometry("300x100")
    vent_hija.title('Ventana hija')
    
    # command = vent_hija.destroy elimina la ventana. OJO es distinto eliminar a ocultar
    tk.Button(vent_hija, text="Cerrar", command=vent_hija.destroy,
              bg="yellow").place(x=125, y=25)

def open_ventana2():
    limpiar_frame()  # Limpiar el Frame antes de mostrar el contenido nuevo
    root.title('Ventana 2')  # Título de la ventana
    # Actualizar el contenido del Frame principal
    color_v2 = 'red'

    def cambio_color_v2():
        nonlocal color_v2  # nonlocal permite modificar y modificar color_v2 dentro del contexto de
                           # las funciones open_ventana2() y cambio_color_v2()
        if color_v2 == 'red':
            color_v2 = 'grey'
        else:
            color_v2 = 'red'
        root.config(bg=color_v2)  # Permite cambiar el color de fondo

    tk.Label(root, text="¡Eso!", fg="red").place(x=150, y=300)
    tk.Button(root, text="Cambiar Color", command=cambio_color_v2,
              bg="orange").place(x=200, y=250)
    
    # La función lambda permite generar y ejecutar una función de manera local y anonima
    #Con el truco de lambda puedo hacer que se ejecuten dos acciones
    #Llamo a la función limpiar_frame() para limpiar el contenido y open_root() para abrir la primera ventana
    #Ojo funciones llevan () con este método
    ###### OJO NO UTILICEN lambda FUERA DE ESTE CONTEXTO SI NO SABEN BIEN COMO SE UTILIZA #####
    ###### Y POR SOBRETODO NO LO UTILICEN EN PRUEBAS NI TAREAS NI ENSAYOS #####
    tk.Button(root, text="Volver", command=lambda: [limpiar_frame(),open_root()],
              bg="yellow").place(x=25, y=25)
    tk.Button(root, text="calcular", command=open_ventana3,
              bg="yellow").place(x=100, y=100)

def open_ventana3():
    limpiar_frame()  # Limpiar el Frame antes de mostrar el contenido nuevo
    root.title('Ventana 3 - Calcular')
    def validar_num():
        #Capturo texto ingresado por el usuario en el cuadro de texto con .get()
        entrada_usr = ingresa_usr.get()
        if entrada_usr < 25:
            msj = str(entrada_usr) + " Es menor que 25"
        elif entrada_usr > 25:
            msj = str(entrada_usr) + " Es mayor que 25"
        else:
            msj = "Es 25"
        texto_cambiante_vent3.configure(text = msj)

    #Función para validar la entrada del usuario
    def validar_entrada(texto):
        if texto == "" or texto.isdigit():
            return True
        else:
            # messegebox permite mostrar una ventana emergente. 
            messagebox.showerror("Error", "Solo se permiten números")
            return False

    root.grid_rowconfigure(0, weight=1)  # Espacio vacío arriba

    root.grid_rowconfigure(3, weight=1)  # Espacio vacío abajo

    root.grid_columnconfigure(0, weight=1)

    tk.Label(root, text="""Evaluaremos si un número es mayor o menor que 25""",
             fg="red", bg='#40E0D0').grid(row=0, column=0, sticky="S")


    validate_cmd = root.register(validar_entrada)
    
    #Se inicializa variable de entrada como número(int o float) con tk.IntVar()
    #En caso que deseen ingresar strings, pueden usar .StringVar()
    ingresa_usr = tk.IntVar()
    
    # Entry genera cuadro de entrada de texto. textvariable = variable inicializada
    # Dejo de tarea entender que hace validete = "key" y calidatecommand
    tk.Entry(root, textvariable = ingresa_usr,
             validate="key", validatecommand=(validate_cmd, "%P")).grid(row=1, column=0, sticky="S")


    tk.Button(root, text="Guardar",
              command=validar_num, bg="orange").grid(row=2, column=0)
    tk.Button(root, text="Volver",
              command=open_ventana2, bg="yellow").place(x=25, y=25)
    
    # Fijense que acá el label se definió en una variable, esto permite modificarla su contenido
    # tal y como se realiza en la función validar_num()
    msj = "Ingrese número y apriete el botón"
    texto_cambiante_vent3 = tk.Label(root, fg="black", text=msj).grid(row=3, column=0, sticky="N")
    texto_cambiante_vent3
    
#Inicializo la variable root dandole los atributos de Tk. "Ventana Madre"
root = tk.Tk()
root.geometry("300x400")   #Tamaño de la ventana
root.title('Ventana root') #Titulo de la ventana
root.config(bg='#40E0D0')  #Defino configuraciones de la ventana
                           #bg -> Color de fondo de la ventana
open_root()
root.mainloop()