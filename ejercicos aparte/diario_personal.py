# #Ejercicio 2: Crear un diario personal
# Cada vez que el usuario escribe una entrada, guarda la fecha y el texto.
# Cada ejecución del programa agrega una nueva entrada.
# Al final, muestra todo lo que hay en el diario.
from datetime import datetime
hora_actual=str(datetime.now())
with open("diario_personal.txt","a") as archivo:
    archivo.write("\n" + "*"*25 + " " + hora_actual + " " + "*"*25 + "\n")
    texto=input("ingrese el texto deseado en el diario\n")
    archivo.write(texto)

with open("diario_personal.txt","r") as archivo:
   print(archivo.read())

