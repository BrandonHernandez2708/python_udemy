from tkinter import *
#constantes
ANCHO = 600
ALTO = 400
POSX = 300
POSY = 100

def click():
    texto = "Hola "+nombre.get()+" Tienes "+str(edad.get())+" años"
    etiquetaResultado.config(text=texto)

anchoAlto=str(ANCHO)+"x"+str(ALTO)
posicionX="+"+str(POSX)
posicionY="+"+str(POSY)
ventana = Tk()

#variables
nombre= StringVar()
edad  = IntVar()
ventana.title("Posicionando ventana ")
ventana.resizable(True, True)
#ventana.iconbitmap("icono.ico")
#ventana.geometry("640x320")

ventana.geometry(anchoAlto+posicionX+posicionY)
frame = Frame()

frame.pack()
frame.config()


etiquetanombre= Label(frame, text="Nombre: ",font=("Arial", 12))
etiquetanombre.grid(row=1, column=2)
entradonombre = Entry(frame, textvariable=nombre, width=50)
entradonombre.grid(row=2, column=2)
etiquetaEdad= Label(frame, text="Edad: ",font=("Arial", 12))
etiquetaEdad.grid(row=1, column=3)
entradaEdad = Entry(frame, textvariable=edad, width=50)
entradaEdad.grid(row=2, column=3)
edad.set(16)
etiquetaResultado= Label(frame, text="Texto cambiado: ",font=("Arial", 12))
button = Button(frame, text="Pulsame",bg="red",fg="yellow",command=click)
etiquetaResultado.grid(row=4, column=1)
button.grid(row=3, column=2)
ventana.mainloop()
