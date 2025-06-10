import os
import pandas as pd
#directorio acutal
directorio_actual = os.getcwd()
print(directorio_actual)
#directorio datos
directorio_datos= os.path.join(directorio_actual,"datos")
print(directorio_datos)
print("existe directorio datos: ")
print(os.path.exists(directorio_datos))
print("es una carpeta o directorio?")
print(os.path.isdir(directorio_datos))
listado = [os.path.join(directorio_datos, item) for item in os.listdir(directorio_datos)]
print(listado)
print(os.listdir(directorio_datos))
#crear carpeta nueva
try:
    carpeta_nueva = os.mkdir(os.path.join(directorio_actual, "nueva"))

    print(carpeta_nueva)
except FileExistsError:
    print("La carpeta ya existe")

#abrimos fichero fuera de datos
fichero_exterior = os.path.join(directorio_actual, "datos.csv")
df_exteriror = pd.read_csv(fichero_exterior)
print("mostramos fichero exterior" )
print(df_exteriror.head())

#abrimos fichero dentro de datos
fichero_interior = os.path.join(directorio_datos, "datos.csv")
df_interior = pd.read_csv(fichero_interior)
print("mostramos fichero interior" )
print(df_interior.head())
#abrimos sin indcar la ruta
fichero="datos.csv"
df = pd.read_csv(fichero)
print("fichero sin indicar ruta")
print(df)
