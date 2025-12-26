#definir una funcion que  muestre una cadena al revez
def reversa(cadena):
    cadena_alrevez = cadena[::-1]
    return cadena_alrevez

cadena=input("Ingrese una cadena\n")
print(reversa(cadena))