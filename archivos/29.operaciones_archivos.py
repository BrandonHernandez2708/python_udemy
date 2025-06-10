import os 
carpeta = "D:\\udemy\\python\\python_udemy\\archivos\\mi carpeta"
print(carpeta)
listado = os.listdir(carpeta)
print(listado)
print(type(listado))
#filtrado 
#for archivo in listado:
    #if archivo.endswith(".txt"):
        #print("fichero txt encontrado: ")
        #print(f"nombre de archivo: {archivo}")
#otra forma de filtrar
filtrado=[archivo for archivo in listado if archivo.endswith(".txt")]
print(type(filtrado))
print(filtrado)
#cambio de directori
os.chdir("D:\\udemy\\python\\python_udemy\\archivos\\mi carpeta")
#os.rename("comprimido.zip","cambiadoNombreComrpimido.zip")
# borrar
#os.remove("cambiadoNombreComrpimido.zip")
filtrado=[archivo for archivo in listado if archivo.endswith(".zip")]
print(filtrado)

# # renombar varios archivos a la vez
# contador =1
# listado = os.listdir(carpeta)
# print(listado)
# print("fin listado inicial ")
# for archivo in os.listdir():
#     nombre, extension = os.path.splitext(archivo) #obtieniendo una tuopla con el nombre y la extension
#     print(nombre, extension)
#     nuevoNombre = f'renombrardo{str(contador)}_{nombre}{extension}'
#     contador +=1
#     os.rename(archivo, nuevoNombre)
# listado = os.listdir(carpeta)

print("fin listado final ")
print("\n\n")
print(listado)

#copiar contenido de un archivo a otro
# try:
#     os.chdir("D:\\udemy\\python\\python_udemy\\archivos\\micarpeta")
#     fichero = open("text.txt","r")
#     nuevofichero= open("nuevoText.txt","w")
#     for linea in fichero :
#         nuevofichero.write(linea)
#     fichero.close()
#     nuevofichero.close()
# except FileNotFoundError:
#     print("El fichero no existe")

#otra forma de copiar contenido de un archivo a otro
try:
    os.chdir("D:\\udemy\\python\\python_udemy\\archivos\\mi carpeta")
    with open("text.txt")as fichero:
        with open("nuevofichero.txt","w")as nuevofichero:
            for linea in fichero:
                nuevofichero.write(linea)
except FileNotFoundError:
    print("El fichero no existe")