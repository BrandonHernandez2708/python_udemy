with open("lista_productos.txt", "r") as archivo:
    for i, producto in enumerate(archivo.readlines()):
        print(f"{i + 1}. {producto.strip()}")

print("lista actual\n")
 
with open("lista_productos.txt","a") as archivo: # a de append agrega sin sobreescribir si agrego w sobrescribe
    lista_actualizada=input(("agregue los productos que quiera ingresar a la lista separados por comas"))
    lista_actualizada= set(lista_actualizada.split(","))
    for producto in lista_actualizada:
        archivo.write(producto.strip()+"\n")

with open("lista_productos.txt", "r") as archivo:
    for i, producto in enumerate(archivo.readlines()):
        print(f"{i + 1}. {producto.strip()}")   
print("lista final\n")