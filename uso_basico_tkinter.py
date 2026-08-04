# -*- coding: utf-8 -*-

"""
Este código muestra ejemplos del uso de funciones básica de tkinter.
Insto a cada grupo a investigar más por su cuenta para encontrar funciones que
les sean útiles para el desarrollo de su solución
"""

#Importo la biblioteca tkinter con el sobrenombre tk
import tkinter as tk

#En una función defino la ventana root
def open_root():
    
    #Inicializo la variable root dandole los atributos de Tk. "Ventana Madre"
    root = tk.Tk()
    root.geometry("300x400")   #Tamaño de la ventana
    root.title('Ventana root')   #Titulo de la ventana
    root.config(bg='#40E0D0')   #Defino configuraciones de la ventana
                                #bg -> Color de fondo de la ventana

    def open_vent_emergente():
        
        #Inicializo la variable vent_emergentedandole los atributos de Toplevel. "Ventana Hija"
        #Es dependiente de la Ventana Madre
        vent_emergente = tk.Toplevel()
        vent_emergente.geometry("300x100")
        vent_emergente.title('Ventana emergente')
        
        #Defino un botón que quiero que aparezca en la ventana emergente
        #command = acción a ejecutar con el botón
        #ventana.destroy() Elimina la ventana y sus widget
        #bg -> color de fondo del botón; place -> ubicación del botón
        tk.Button(vent_emergente, text="Cerrar", command=vent_emergente.destroy,
                bg="yellow").place(x=125,y=25)

    #Defino un texto que quiero que aparezca en la ventana, fg -> color del texto
    #place -> ubicación del texto
    tk.Label(root, text="¡Hola mundo!",fg="red").place(x=70,y=15)

    #Defino un botón que quiero que aparezca en la ventana root, 
    #bg -> color de fondo del botón ; place -> ubicación del botón
    #Comando -> acción que realiza el botón
    #Con el truco de lambda puedo hacer que se ejecuten dos acciones
    #Llamo a la función open_ventana2() y con .destroy() elimino la ventana root
    #Ojo funciones llevan () con este método
    tk.Button(root, text="Ventana2", command=lambda:[open_ventana2(), root.destroy()],
              bg="green").place(x=40,y=75)
######OJO NO UTILICEN lambda FUERA DE ESTE CONTEXTO SI NO SABEN BIEN COMO SE UTILIZA#####
    
    
    #Botón con comando para abrir ventana emergente. Ojo que no lleva ()
    #bg -> color de fondo del botón; fg -> color del texto del botón 
    #place -> ubicación del botón
    tk.Button(root, text="Ventana hija", command=open_vent_emergente,
              bg="black",fg="white").place(x=150,y=200)
    
    #Si elimino/cierro ventana madre, ventana hija igual se cierra/elimina
    #Hay opciones para hacer "invisible" a la ventana madre y deja solo visible la hija
    # .withdraw() para ocultar, .deoconify() para hacer visible
    
    #Inicializo la ventana
    root.mainloop()

def open_ventana2():
    #Por un tema practico hago global la variable color_v2. 
    # ¡¡¡NO ABUSAR DE VARIABLES GLOBALES!!! Solo usar en casos estrictamente necesarios
    global color_v2
    
    def cambio_color_v2():
        global color_v2
        if color_v2 == 'red':
            color_v2 = 'grey'
        else:
            color_v2 = 'red'
            
        #Reconfiguro el color de fondo de la ventana
        ventana2.config(bg=color_v2)
    
    #Inicializo la variable ventana2 dandole los atributos de TK. "Ventana Madre"
    ventana2 = tk.Tk()
    ventana2.geometry("300x400")
    ventana2.title('Ventana2')

    color_v2 = 'red'
    ventana2.config(bg=color_v2) #Condifuro color de fondo de ventana

    tk.Label(ventana2, text="¡Eso!",fg="red").place(x=150, y=300)

    #Botón con comando para cambiar volor de ventana. Ojo que no lleva ()
    tk.Button(ventana2, text="Cambiar Color", command=cambio_color_v2,
              bg="orange").place(x=200,y=250)

    #Botón con truco para ejecutar 2 acciones. Ojo que ese si lleva ()
    tk.Button(ventana2, text="Quit", command=lambda:[open_ventana3(), ventana2.destroy()],
            bg="yellow").place(x=25,y=25)

def open_ventana3():
    
    #Función para capturar texto de entrada, evaluar entrada y modificar label
    def validar_num():
        #Capturo texto ingresado por el usuario en el cuadro de texto con .get() 
        entrada_usr = ingresa_usr.get()
        
        if entrada_usr < 25:
            msj = str(entrada_usr)+" Es menor que 25"
        elif  entrada_usr > 25:
            msj = str(entrada_usr)+" Es mayor que 25"
        else:
            msj = "Es 25"
    
        #Actualizo label (texto) que muestra en pantalla
        texto_cambiante_vent3.configure(text=msj)
        
    ventana3 = tk.Tk()
    ventana3.geometry("400x400")
    ventana3.title('Ventana3')

    #Inicializo variable de entrada como número(int o float) con tk.IntVar()
    #En caso que deseen ingresar strings, pueden usar .StringVar()
    ingresa_usr = tk.IntVar()

    #Incializo cuadro de entrada de texto. textvariable = variable inicializada
    tk.Entry(ventana3, textvariable=ingresa_usr).place(x=220, y=200)

    tk.Label(ventana3, text="¡a!",fg="red").place(x=150, y=200)
    
    #Inicializo variable con mensaje que cambiará
    msj = "Ingrese número y aprete el botón"
    texto_cambiante_vent3 = tk.Label(ventana3,fg="black",text=msj)
    texto_cambiante_vent3.place(x=220, y=230)
    
    #Botón con comando para cambiar label y capturar entrada de texto
    tk.Button(ventana3, text="Save", command=validar_num, bg="orange").place(x=250,y=250)

    #Botón que destruye ventana3 e inicia ventana2
    tk.Button(ventana3, text="NO", command=lambda:[open_ventana2(), ventana3.destroy()],
            bg="yellow").place(x=25,y=25)


#Llamo a la función que inicializa tkinter en la primera ventana
#También puede no hacerlo función y escribir todos los parametros y demases de
#la ventana root aquí fuera de una función. Dependerá de lo que quieran hacer
open_root()

