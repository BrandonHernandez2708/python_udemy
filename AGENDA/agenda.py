from tkinter import *
from tkinter import *
from tkinter import messagebox
from baseDeDatos import *
ancho = 550
alto = 540
posx = 400
posy = 400
anchoalto=str(ancho)+"x"+str(alto)
posicionx="+"+str(posx)
posiciony="+"+str(posy)
colorventana="blue"
colorfondo="blue"
colorletra="white"
def mostrarMensaje(titulo, mensaje):
    messagebox.showinfo(titulo, mensaje)
def limpiarCampos():
    nombre.set("")
    apellido.set("")
    telefono.set("")
    email.set("")
    ID.set("")
    text.delete(1.0, END)
def guardardatos():
    crearTabla()
    if (nombre.get() == "") or (apellido.get() == "") :
        mostrarMensaje("Error", "Debes rellenar los datos")
    else:
        datos=(nombre.get(), apellido.get(), telefono.get(), email.get())
        mostrarMensaje("Guardar", "Contacto guardado correctamente")
        insertar(datos)
        limpiarCampos()
        mostrar()
def actualizar():
    crearTabla()
    if((ID.get() == "") or (ID.get() == 0) or (nombre.get() == "")):
        mostrarMensaje("Error", "Debes rellenar los datos")
    else:
        try:
            modificar(ID. get(), nombre.get(), apellido.get(),
                     telefono.get(), email.get())
            mostrarMensaje("Modificar", "Contacto modificado")
            limpiarCampos()
            mostrar()
        except: 
            mostrarMensaje("Error", "Identificador no encontrado")

def damecontactos(id):
    conexion , cursor = conectar()
    sql = "SELECT * FROM agenda WHERE id=" + str(id)
    cursor.execute(sql)
    contacto = cursor.fetchall()    
    conexion.close()
    return contacto
     

def eliminar():
    if((ID.get() == "") or (ID.get() == 0)):
        mostrarMensaje("Error", "Debes in sertar un identificador valido")
    else:
        try:
            borrar(ID.get())
            mostrarMensaje("Borrar", "Contacto borrado")
            limpiarCampos()
            mostrar()
        except:
            mostrarMensaje("Error", "Identificador no encontrado")
def mostrar():
  listado=consultar()
  text.delete(1.0, END)
  text.insert(INSERT, "ID\t Nombre\t Apellido\t Telefono\t Email\n")
  for elemento in listado :
        id = elemento[0]
        nombre = elemento[1]
        apellido = elemento[2]
        telefono = elemento[3]
        email = elemento[4]
        text.insert(INSERT, id)
        text.insert(INSERT, "\t")
        text.insert(INSERT, nombre)
        text.insert(INSERT, "\t")
        text.insert(INSERT, apellido)
        text.insert(INSERT, "\t")
        text.insert(INSERT, telefono)
        text.insert(INSERT, "\t")
        text.insert(INSERT, email)
        text.insert(INSERT, "\n")

def buscar():
    if ((ID.get() == "") or (ID.get() == 0)):
        mostrarMensaje("Error", "Debes insertar un identificador valido")
    else:
        contactos = damecontactos(ID.get()) 
        for contacto in contactos:
            ID.set(contacto[0])
            nombre.set(contacto[1])
            apellido.set(contacto[2])
            telefono.set(contacto[3])
            email.set(contacto[4])
            mostrarMensaje("Buscar", "Contacto encontrado")

ventana=Tk()
ventana.config(bg=colorfondo)
ventana.geometry(anchoalto+posicionx+posiciony)
ventana.title("Agenda")
frame = Frame()
frame.config(width=ancho,height=alto)
frame.config(bg=colorfondo)
frame.pack()
#variable 
ID = StringVar()
nombre = StringVar()
apellido = StringVar()
telefono = StringVar()
email = StringVar()
#widgets
Label(frame, text="ID:").place(x=50, y=40)
Entry(frame, textvariable=ID).place(x=150, y=40, width=200)

Label(frame, text="Nombre:").place(x=50, y=80)
Entry(frame, textvariable=nombre).place(x=150, y=80, width=200)

Label(frame, text="Apellido:").place(x=50, y=120)
Entry(frame, textvariable=apellido).place(x=150, y=120, width=200)

Label(frame, text="Teléfono:").place(x=50, y=160)
Entry(frame, textvariable=telefono).place(x=150, y=160, width=200)

Label(frame, text="Email:").place(x=50, y=200)
Entry(frame, textvariable=email).place(x=150, y=200, width=200)

text = Text(frame)
text.place(x=70, y=300, width=450, height=200)

botonAñadir=Button(frame, text="Añadir", command=guardardatos).place(x=130, y=250)
botonBorrar=Button(frame, text="Borrar", command=eliminar).place(x=200, y=250)
botonConsultar=Button(frame, text="Consultar", command=mostrar).place(x=260, y=250)
botonModificar=Button(frame, text="Modificar", command=actualizar).place(x=340, y=250)
botonbuscar=Button(frame, text="Buscar",command=buscar).place(x=410, y=250)


ventana.mainloop()