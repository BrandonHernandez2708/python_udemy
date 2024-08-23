inicio = int(input("Ingrese el inicio de la cuenta: "))
final = int(input("Ingrese el final de la cuenta: "))
for numeros in range(final, inicio - 1, -1):
    if numeros % 2 == 0:
        print(numeros)
