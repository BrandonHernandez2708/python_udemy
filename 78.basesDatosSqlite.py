import sqlite3
def conectar():
    conexion = sqlite3.connect("miBD.db")
    cursor = conexion.cursor()
    return conexion, cursor

def crearTabla():
    conexion, cursor = conectar()
    sql = """ 
    CREATE TABLE IF NOT EXISTS agenda(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre VARCHAR(20) NOT NULL,
    telefono VARCHAR(14) NOT NULL
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
    INSERT INTO agenda(nombre, telefono) VALUES(?, ?)
    """
    if (cursor.execute(sql, datos)):
        print("Datos Guardados")
    else:
        print("No se pudieron guardar los datos")
    conexion.commit() # Guardar cambios 
    conexion.close()

def consultar():
    conexion, cursor = conectar()
    cursor.execute("SELECT id,nombre,telefono from agenda")
    for fila in cursor:
        print("ID = " ,(fila[0]))
        print("Nombre = ", (fila[1]))
        print("Telefono = ", (fila[2]),"\n")
    conexion.close()
def modificar(id, telefono):
    conexion, cursor = conectar()
    sql = "UPDATE agenda SET telefono = ? WHERE id = ?"
    cursor.execute(sql, (telefono, id))
    cursor.close()
    conexion.commit()
    conexion.close()

def borrar(id):
    conexion, cursor = conectar()
    sql = "DELETE from agenda WHERE id="+id
    cursor.execute(sql)
    cursor.close()
    conexion.commit()
    conexion.close()

crearTabla()
datos = ("Jose","555-555-5555")
insertar(datos)
datos = ("Brandon","987-654-3210")
insertar(datos)
datos = ("Maria","123-456-7890")
insertar(datos)
datos = ("Ana","321-654-9870")
insertar(datos)
consultar()
modificar(4,"0234-567-8901")
consultar()
borrar("3")
consultar()