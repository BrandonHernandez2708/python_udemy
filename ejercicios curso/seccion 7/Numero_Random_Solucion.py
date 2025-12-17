#El ordenador piensa  un numero y el usuario tiene que adivinarlo, muestre tambien el numero de intentos
from random import randint as azar
piensaNumero = azar(1,100)
numeroUsuario = int(input("Adivina el numero que he pensado\n"))
continua = True 
intentos = 0
while (continua):
    if numeroUsuario < piensaNumero:
        print(f"El numero que he pensado es mayor ")
        intentos = intentos + 1
        numeroUsuario = int(input("Adivina el numero que he pensado\n"))
    elif numeroUsuario > piensaNumero:
        print("El numero que he pensado es menor")
        intentos = intentos + 1
        numeroUsuario = int(input("Adivina el numero que he pensado\n"))
    else:
        print("Lo has adivinado")
        intentos = intentos + 1
        print(f"Numero de intentos: {intentos}")
        print("Quieres continuar (s/n)?")
        respuesta = input()  # Guardar la respuesta en una variable
        if (respuesta == "s" or respuesta == "S"):
            continua = True
            intentos = 0
            piensaNumero = azar(1, 100)
            numeroUsuario = int(input("Adivina el numero que he pensado\n"))
        else:
            continua = False
print("Fin del juego")

