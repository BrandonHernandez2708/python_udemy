#Escribe una lusta de numeros del 10 al 20 mostrala despues de modificar los valores que estan en la posicion 
#3,6,7 para que su valor sea el resultado de multiplicar el valor que tenian por 4 , seguidamente de mostrar la lista final 
lista = list(range(10,21))
lista[3]=lista[3]*4
lista[6]=lista[6]*4
lista[7]=lista[7]*4
print(lista)