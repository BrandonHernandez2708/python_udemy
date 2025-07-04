from tkinter import *
from tkinter import messagebox 
def mostrar():
    messagebox.showinfo("Mensaje","el valor selecicionado es : "+valor.get())
ventana = Tk()
ventana.geometry("640x520")
valor = StringVar()
etiqueta = Label(ventana, textvariable=valor).place(x=20, y=20)
combo = Spinbox(ventana, from_=1, to=10, textvariable=valor)
combo.place(x=20, y=60)
boton = Button(ventana, text="valor", command=mostrar).place(x=20, y=100)
ventana.mainloop()