from tkinter import *
def click():
    cadena = "Pulsaste  "
    if (color01.get()):
        cadena += "Rojo"
        ventana.config(bg="red")
    if (color02.get()):
        cadena += "Azul"
        ventana.config(bg="blue")
    if (color03.get()):
        cadena += "Amarillo"
        ventana.config(bg="yellow")
    if not (color01.get() or color02.get() or color03.get()):
        cadena += "No hy nada pulsado"
        ventana.config(bg="white")
    etiqueta.config(text=cadena)
ventana = Tk()
ventana.title("optionButton")
ventana.geometry("640x360")
frame = Frame()
frame.pack()
color01= IntVar() # 1 o 0
color02= IntVar() 
color03= IntVar() 
chkrojo=Checkbutton(frame,text="Rojo",variable=color01,onvalue=1,offvalue=0,command=click)
chkrojo.grid(column=1, row=2)

chkazul=Checkbutton(frame,text="Azul",variable=color02,onvalue=1,offvalue=0,command=click)
chkazul.grid(column=1, row=3)

chkamarillo=Checkbutton(frame,text="Amarillo",variable=color03,onvalue=1,offvalue=0,command=click)
chkamarillo.grid(column=1, row=4)

etiqueta=Label(frame,text="Selecciona opción")
etiqueta.grid(column=1, row=7
              )
ventana.mainloop()