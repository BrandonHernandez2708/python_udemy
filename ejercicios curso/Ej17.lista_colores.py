#Pedir al usuario una lista de colores (separados por comas), guardarlos en una lista. 
#No se deben guardar colores repetidos. 
# Mostrar por consola la lista de colores ordenados alfabeticamente.
lista_usuario=input("dame una lista de colores separados por comas: ")
lista_usuario = set(lista_usuario.split(",")) #asignar la lista usuario separar palabras por comar y convertir en conjunto
lista_colores = []
for color in lista_usuario:
    lista_colores.append(color)
lista_colores.sort()  #ordenar la lista de colores
print(lista_colores)