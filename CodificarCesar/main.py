from  tkinter import * 
from tkinter import messagebox
from Modulos.archiva import *   
from Modulos.cesar import *
ventana = Tk()
ventana.title("Codifica")
ventana.config(bg="gray")
ventana.geometry("380x380")
frame=Frame()
frame.config(width="340",height="340")
frame.config(bg="cyan")
frame.pack()
def codificar():
    texto=textoSincodificar.get()
    if texto != "":
            textocodificar.set(codifica(texto))
            mensaje("Info","mensaje Codificado")
    else:
            mensaje("Error","Error al codificar texto")
def descodificar():
    texto=textocodificar.get()
    if texto != "":
            textoSincodificar.set(decodifica(texto))
            mensaje("Info","mensaje Decodificado")
    else:
            mensaje("Error","Error al decodificar texto")
def caargar():
    try:
         textocodificar.set(carga())
         descodificar()
    
    except:
        mensaje("Error","Error al cargar el archivo")

def guardar():
    texto=textocodificar.get()
    if texto != "":
            guarda(texto)   
            mensaje("Info","mensaje Guardado")
    else :
         mensaje("Error","Error al guardar texto")
def borrar():
     textocodificar.set("")
     textoSincodificar.set("")
def mensaje(titulo,texto):
     messagebox.showinfo(titulo,texto)
     
textoSincodificar=StringVar()
textocodificar=StringVar()
etiquetasincodificar=Label(frame,text="Texto sin codificar:").grid(row=3,column=1)
cajasin=Entry(frame,textvariable=textoSincodificar).grid(row=3,column=2)
etiquetaCodificada=Label(frame,text="Texto codificado:").grid(row=4,column=1)
cajacon=Entry(frame,textvariable=textocodificar).grid(row=4,column=2)
botoncodificar=Button(frame,text="Codificar",command=codificar).grid(row=5,column=1)
botondescodificar=Button(frame,text="Decodificar",command=descodificar).grid(row=5,column=2)
botonGrabar=Button(frame,text="Grabar",command=guardar).grid(row=6,column=1)
botonCargar=Button(frame,text="Cargar",command=caargar).grid(row=6,column=2)
botonBorrar=Button(frame,text="Borrar",command=borrar).grid(row=7,column=1)

ventana.mainloop()
