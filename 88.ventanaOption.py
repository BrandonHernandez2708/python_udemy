from tkinter import *
def click():
    cadena = "Pulsaste  "
    if opcion.get() == 1:
        cadena += "Rojo"
        ventana.config(bg="red")
    elif opcion.get() == 2:
        cadena += "Azul"
        ventana.config(bg="blue")
    elif opcion.get() == 3:
        cadena += "Amarillo"
        ventana.config(bg="yellow")
    etiqueta.config(text=cadena)
ventana = Tk()
ventana.title("optionButton")
ventana.geometry("640x360")
frame = Frame()
frame.pack()
opcion = IntVar()
rbdrojo=Radiobutton(frame, text="Rojo",variable=opcion,value=1,command=click)
rbdrojo.grid(column=1, row=3)

rbdazul=Radiobutton(frame, text="Azul",variable=opcion,value=2,command=click)
rbdazul.grid(column=1, row=4)

rbdamarillo=Radiobutton(frame, text="Amarillo",variable=opcion,value=3,command=click)
rbdamarillo.grid(column=1, row=5)

etiqueta=Label(frame,text="Selecciona opción")
etiqueta.grid(column=1, row=7
              )
ventana.mainloop()