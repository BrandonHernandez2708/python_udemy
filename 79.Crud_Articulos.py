import sqlite3
def conectar():
    conexion = sqlite3.connect("articulos.db")
    cursor=conexion.cursor()
    print("conectado a bd")
    return conexion, cursor

def cerrar_conexion(conexion):
    conexion.close()

def crear_Tabla():
    conexion, cursor = conectar()
    cursor.execute('CREATE TABLE IF NOT EXISTS ARTICULOS (IDENTIFICADOR INT PRIMARY KEY, NOMBRE VARCHAR(20), CANTIDAD INT, IMPORTE FLOAT TEXT )')
    cerrar_conexion(conexion)
    print("Tabla creada ")

def carga_inicial():
    conexion,cursor = conectar()
    articulos = [
        (12345,"Cuaderno",25,2.36),
        (1254,"boligrafo",100,0.90),
        (1345,"goma",75,0.50),
    ]
    cursor.executemany('INSERT INTO ARTICULOS VALUES(?,?,?,?)', articulos)
    conexion.commit()
    cerrar_conexion(conexion)
def insertar(artiuclo):
    conexion,cursor = conectar()
    cursor.execute('INSERT INTO ARTICULOS VALUES(?,?,?,?)', artiuclo)
    print("el dato se ha insertado ")
    conexion.commit()
    cerrar_conexion(conexion)

def consultar():
    conexion,cursor = conectar()
    cursor.execute('SELECT * FROM ARTICULOS')
    articulos=cursor.fetchall()
    cerrar_conexion(conexion)
    return articulos
   
def actualizar(identificador,nombre,cantidad,importe):
    conexion,cursor = conectar()
    cursor.execute(f"UPDATE ARTICULOS SET NOMBRE = '{nombre}', CANTIDAD = {cantidad}, IMPORTE = {importe} WHERE IDENTIFICADOR = {identificador}"),
    print("el dato se ha actualizado")
    
   
def borrar(identificador):
    conexion,cursor = conectar()
    cursor.execute(f"DELETE FROM ARTICULOS WHERE IDENTIFICADOR ={identificador}")
    print("articulo borrado")
    conexion.commit()
    cerrar_conexion(conexion)

if __name__ == "__main__":
    # crear_Tabla()
    # #carga_inicial()
    # articulo = (13874,"lapiz",150,0.60)
    # insertar(articulo)
    #actualizar(13874,"lapiz verde",149,0.55)
    articulos = consultar()
    for articulo in articulos:
        print(articulo[1])
    borrar(13874)
    articulos = consultar()
    for articulo in articulos:
        print(articulo[1])