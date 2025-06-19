# Haz un programa que guarde en un archivo .txt 
# una lista de compras. Luego, que lea el archivo y muestre cada producto con su índice.
lista_compras=["papas","tomates","aguacates"]
with open("lista_compra.txt","w") as archivo:

    for productos in lista_compras:
     archivo.write(productos+"\n")

with open("lista_compra.txt", "r") as archivo:
    for i, producto in enumerate(archivo.readlines()):
        print(f"{i + 1}. {producto.strip()}")



