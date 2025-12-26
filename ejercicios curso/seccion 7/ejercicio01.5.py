#El ordenador piensa  un numero y el usuario tiene que adivinarlo, muestre tambien el numero de intentos
import random
intentos = 0
victoria = False;
maquina = random.randint(1,10)
usuario = int(input ("Intenta adivinar el numero de la maquina \n"));
while victoria == False:
    if (usuario == maquina):
        intentos+=1
        print("¡Adivinaste el numero!")
        print(f"Numero de intentos: {intentos} ")
        victoria = True;

    else : 
        intentos +=1

        print(f"Numero de intentos: {intentos} ")
        usuario = int(input ("Intenta adivinar el numero de la maquina \n"));