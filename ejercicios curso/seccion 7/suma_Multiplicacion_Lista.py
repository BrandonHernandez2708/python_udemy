#Define una funcion que calcule la suma y multiplicacion de una lista
def suma(lista):
    suma = 0
    for i in lista: 
        suma +=i
    return suma
def multiplicacion(lista):
    multiplicacion = 1
    for i in lista:
        multiplicacion *=i
    return multiplicacion

lista=[1,32,53,65,35,1,3,4,6,9,10,11]
print(suma(lista))
print(multiplicacion(lista))