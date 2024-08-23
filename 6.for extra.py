lista_colores = ["rojo", "amarillo", "verde", "azul"]
mi_color = "verde"

for color in lista_colores:
    print(color)
    if mi_color == color:
        print("color encontrado")
        break
else:
    print("el color indicado no esta en la lista")


rango_largo=range (1,10000)
print(rango_largo)
for numero in rango_largo:
    print(numero)
    if numero == 9999999:
        print("Encontramos el numro 5")
        break
else:
    print("no se ha encontrado el numero ")