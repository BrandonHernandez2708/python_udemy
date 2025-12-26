#sumar los numeros pares y por otro los impares dentro del intervalo del 1 al 50
contador = 1
pares = 0
impares = 0
while contador <=50:
    print(contador)
    if contador%2==0:
        pares += contador
    else : 
        impares += contador
    contador +=1
print(f"La suma de los pares es {pares}")
print(f"la suma de los impares es {impares}")