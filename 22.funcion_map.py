# map (funcion,secuencia)
# La funcion map aplica una funcion a cada elemento de una secuencia y devuelve un objeto map
# que se puede convertir en una lista o un iterable.
numeros=[1,2,3,4,5]
cuadrados=list(map(lambda x: x**2, numeros))
print(numeros)
print(cuadrados)
print("*"*60)
#sin map
cuadrados = []
for numero in numeros:
    cuadrados.append(numero**2)
print(numeros)
print(cuadrados)
