#nueva=lista=[expresion for elemento in secuencia ]

#crear una lista de cuadrados de los numeros del 1 al 5
numeros=[1,2,3,4,5]
cuadrados = []
for numero in numeros:
    cuadrados.append(numero**2)
    
print("los cuadrados son: ",cuadrados)

#con compresion de listas 
cuadrados = [numero **2 for numero in numeros]
print(f"los cuadrados son: {cuadrados}")
""