import os 
#crear carpeta o directorio
os.makedirs("MiCarpeta")
#listar el contenido de la carpeta
print(os.listdir("./"))
#mostrar directorio actual 
print(os.getcwd())
#mostrar tamaño de la carpeta o directorio 
print(os.path.getsize("MiCarpeta"))
#comprobar si es archivo
print(os.path.isfile("MiCarpeta"))
#comprobar si es directorio
print(os.path.isdir("MiCarpeta"))
# cambiar de directorio
os.chdir("MiCarpeta")
print(os.getcwd())
print(os.listdir("./"))
os.chdir("..")  # Volver al directorio anterior
print(os.getcwd())
#renombrar carpeta 
os.rename("Micarpeta","Mi_carpeta")
#os.remove(os.path.join(os.getcwd(), "archivos.txt"))  # Eliminar archivo
#print(os.listdir("./"))
#borrar carpeta
#os.rmdir("Mi_carpeta") 
#os.chdir("../")
#print(os.listdir("./"))
