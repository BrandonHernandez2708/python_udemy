# Crea una tabla llamada Alumnos que constará de tres columnas: la columna id de tipo entero, 
# la columna nombre que será de tipo texto y la columna notas de tipo entero. 
# Usa funcion para insertar y mostrar datos.
# Una vez creada la tabla, tenéis que insertarle 3 datos mediante input dentro de un bucle.
import sqlite3
def conectar():
    conexion = sqlite3.connect("alumnos.db")
    cursor = conexion.cursor()
    print("Conectado a la base de datos")
    return conexion, cursor

def cerrar_conexion(conexion):
    conexion.close()
    print("Conexión cerrada")

def crear_tabla():
    conexion, cursor = conectar()
    cursor.execute('CREATE TABLE IF NOT EXISTS Alumnos (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre VARCHAR(50) NOT NULL, notas INTEGER NOT NULL)')
    conexion.commit()
    cerrar_conexion(conexion)
    print("Tabla Alumnos creada")

def insertar(alumno):
    conexion,cursor = conectar()
    sql= 'INSERT INTO Alumnos (nombre, notas) VALUES(?, ?)'
    if cursor.execute(sql, alumno):
        print("El dato se ha insertado")
    else:
        print("No se pudo insertar el dato")
    conexion.commit()
    cerrar_conexion(conexion)

def mostrar_datos():
    conexion,cursor = conectar()
    cursor.execute('SELECT * FROM Alumnos')
    alumnos=cursor.fetchall()
    cerrar_conexion(conexion)
    for alumno in alumnos:
        print("ID = " ,(alumno[0]))
        print("Nombre = ", (alumno[1]))
        print("notas = ", (alumno[2]),"\n")

def actualizar(id, nombre, notas):
    conexion, cursor = conectar()
    cursor.execute("UPDATE Alumnos SET nombre = ?, notas = ? WHERE id = ?", (nombre, notas, id))
    print("el dato se ha actualizado")
    conexion.commit()
    cerrar_conexion(conexion)



def borrar(id):
    conexion,cursor = conectar()
    cursor.execute(f"DELETE FROM Alumnos WHERE id ={id}")
    print("articulo borrado")
    conexion.commit()
    cerrar_conexion(conexion)

if __name__ == "__main__":
    crear_tabla()
    # for i in range(3):
    #     nombre = input("Introduce el nombre del alumno: ")
    #     notas = int(input("Introduce las notas del alumno: "))
    #     alumno = nombre, notas
    #     insertar(alumno)
    
    # Actualizar un alumno
    actualizar(3, "Juan Perez", 85)
    # Borrar un alumno
    borrar(2)



    mostrar_datos()

