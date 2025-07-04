from tkinter import *
from tkinter import messagebox
def info():
    messagebox.showinfo("mensaje","mensaje desde messagebox")
def advertencia():
    messagebox.showwarning("mensaje","mensaje de advertencia ")
def pregunta():
    messagebox.askquestion("mensaje","¿desea continuar?")
    pass 
ventana = Tk()
ventana.geometry("640x520")
boton1=Button(ventana, text="info",command=info).place(x=20,y=100)
boton2=Button(ventana,text="advertencia",command=advertencia).place(x=20,y=140)
boton3=Button(ventana,text="pregunta",command=pregunta).place(x=20,y=180)

ventana.mainloop()