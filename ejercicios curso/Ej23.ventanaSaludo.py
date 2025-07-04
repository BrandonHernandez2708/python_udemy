# Crea una ventana con Tkinter, con una etiqueta y caja de texto 
# para insertar el nombre de usuario y boton, al pulsar el boton se muestra una ventana de mensaje 
# saludando y mostrando el texto de la caja o input. ej: "Hola, Jose"
from tkinter import *
from tkinter import messagebox
def saludar():
    nombre=entrada.get()
    etiqueta.config(text=f"Hola, {nombre}!") 
    messagebox.showinfo("Saludo", f"Hola, {nombre}!")
   


ventana = Tk()
ventana.title("Ventana de Saludo")
frame=Frame()
frame.pack()
frame.config()
ventana.geometry("640x520")
etiqueta = Label(frame, text="Introduce tu nombre:",font=("Arial,12"))
etiqueta.grid(column=2, row=1)
entrada = Entry(frame, width=50)
entrada.grid(column=2, row=2)
botton = Button(frame, text="Pulsame",font=("Arial,12"),command=saludar).grid(column=2, row=3)
ventana.mainloop()