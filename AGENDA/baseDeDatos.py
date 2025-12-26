import sqlite3
from tkinter import *
from tkinter import messagebox
def conectar():
    conexion = sqlite3.connect("agenda.db")
    cursor = conexion.cursor()
    return conexion, cursor

def crearTabla():
    conexion, cursor = conectar()
    sql = """ 
    CREATE TABLE IF NOT EXISTS agenda(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre VARCHAR(20) NOT NULL,
    apellidos VARCHAR(20) NOT NULL,
    telefono VARCHAR(14) NOT NULL,
    email VARCHAR(50) NOT NULL
    )
    """
    try:
        cursor.execute(sql)
        print("Tabla creada o ya existe")
    except sqlite3.Error as e:
        print("No se pudo crear la tabla:", e)
    conexion.close()
    
crearTabla()
def insertar(datos):
    conexion, cursor = conectar()
    sql = """
    INSERT INTO agenda(nombre, apellidos, telefono, email) VALUES(?, ?, ?, ?)
    """
    if (cursor.execute(sql, datos)):
        print("Datos Guardados")
    else:
        print("No se pudieron guardar los datos")
    conexion.commit() # Guardar cambios 
    conexion.close()

def consultar():
    conexion, cursor = conectar()
    cursor.execute("SELECT id,nombre,apellidos,telefono,email from agenda")
    listado=[]
    for fila in cursor:
        listado.append(fila)
        listado.sort()
    conexion.close()
    return listado
def modificar(id, nombre, apellido, telefono, email):
    conexion, cursor = conectar()
    sql = "UPDATE agenda SET Nombre ='"+nombre+"', Apellidos ='"+apellido+"', Telefono ='"+telefono+"', Email ='"+email+"' WHERE id = "+str(id)
    cursor.execute(sql)
    cursor.close()
    conexion.commit()
    conexion.close()

def borrar(id):
    conexion, cursor = conectar()
    sql = "DELETE from agenda WHERE id="+str(id)
    cursor.execute(sql)
    cursor.close()
    conexion.commit()
    conexion.close()
