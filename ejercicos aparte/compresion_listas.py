#Filtrar múltiplos de 3
numeros=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
multiplos_de_tres = [numero for numero in numeros if numero % 3 == 0]
print(f"los numeros multiplos de tres son: {multiplos_de_tres}")
#Longitud de palabra
palabras = ["sol", "luna", "estrella"]
longitudes = [len(palabra) for palabra in palabras]
print(f"las longitudes de las palabras son: {longitudes}")
#Eliminar espacios
frase = "hola mundo "
letras=[letra for letra in frase if letra != ""]
print(f"las letras de :{frase} son :{letras}")
#invertir palabras
palabras = ["hola", "mundo"]
invertidas=[palabra[::-1] for palabra in palabras ]
print(f"las palabras :{palabras} invertidas son :{invertidas}")
#numeros impares
numeros=[1,2,3,4,5,6,7,8,9,10]
impares=[numero for numero in numeros if numero %2 ]
print(f"los numeros impares son :{impares}")