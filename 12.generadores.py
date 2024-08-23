# generado
def impares():
    for numero in range(1, 50,2):
        yield numero #generador

generador = impares()
print(next(generador))
print(next(generador))
print(next(generador))
print("terminanos en next y empezamos en for ")
for numero in generador:
    print(numero)

    

        