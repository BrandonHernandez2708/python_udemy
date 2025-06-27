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