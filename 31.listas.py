lista=[1,2.3,"jose",[7,8],12]
print(type(lista))
print(lista)
print(lista[2])
print(lista[3][1])
print(lista[1:4]) #intervalos
print(lista[2:4:2]) #del 2 al 4 con salto de 2
for elemento in lista:
    print(elemento)

# metodo append para añadir un elemento
lista.append(10)
lista.append("lucia")
lista.append([2,3,6,8,9])
print(lista)
# añadir elemento como un elemento mas de la lista inicial
lista.extend([4,5,2,4])
print(lista)
#eliminar un elemento
lista.remove(2)
print(lista)
lista.remove("jose")
print(lista)
print(lista.index("lucia")) #buscar el indice de un elemento
print(lista.count(2 )) #contar cuantas veces se repite un elemento
print(lista.count(15)) #contar cuantas veces se repite un elemento
print(lista)
lista.reverse() #invertir el orden de la lista
print(lista)
#mas ejemplos
listaCompra=["pan","patatas","naranjas","kiwis"]
print(listaCompra)
print(type(listaCompra))
#crear lista desde variables
cantidadPan=5
preciopan=0.40
totalPan=cantidadPan*preciopan
pedido01 = [cantidadPan,preciopan,totalPan]
pedido02=[3,0.60,3*0.60]
pedido03=[4,0.50,4*0.50]
pedidos = [pedido01,pedido02,pedido03]
print(pedidos)
#lista vacia
listaVacia = []
print(listaVacia)
print(type(listaVacia))
listaCompra.append("peras")
listaCompra.insert(2,"platanos")  #insertar en una posicion concreta
print(listaCompra)
listaCompra.pop()  #elimina el ultimo elemento
#longitud de la lista
print(len(listaCompra))  #longitud de la lista

#ejemplo de lista con for
cuadrados = []
for numero in range(1,11):
    cuadrados.append(numero*numero)
print(cuadrados)
print(min(cuadrados))  #minimo de la lista
print(max(cuadrados))  #maximo de la lista
print(sum(cuadrados))  #suma de la lista
#esta en la lista
print(listaCompra)
print("platanos" in listaCompra)  #True o False
print("cereza" in listaCompra)  #True o False
