#Crea un script de python donde se pregunte mediante un  menu si se quiere convertir de euros a dolares o de dolares a euros.

def euros_a_dolares(euros):
    conversion = round(euros * 1.18,2)
    return conversion

def dolares_a_euros(dolares):
    conversion = round(dolares *0.85,2)
    return conversion

opc = int(input("Elige una opcion:\n1. Convertir de Euros a Dolares\n2. Convertir de Dolares a Euros\n"))
match opc:
    case 1:
        euros=float(input("Introduce la cantidad en euros: "))
        print(euros_a_dolares(euros))
    case 2:
        dolares=float(input("Introduce la cantidad en dolares: "))
        print(dolares_a_euros(dolares))
    case _:
       print("Opcion no valida")



