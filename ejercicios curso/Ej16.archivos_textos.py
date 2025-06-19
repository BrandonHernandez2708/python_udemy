#Crea un archivo de python donde abras un archivo txt y 
# escribas texto dentro del archivo. 
# Despues abrir el archivo mediante codigo y mostrar el texto que contiene.

escritura = open("texto_ejercicio.txt", "w")

escritura.write("Este es un texto de ejemplo para el ejercicio.\n")
escritura.close()
lectura = open("texto_ejercicio.txt", "r")
contenido = lectura.read()

print("Contenido del archivo:\n" + contenido)

lectura.close()