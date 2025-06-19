#Con los conocimientos adquiridos, intenta desarrollar el juego de Piedra, papel, tijera
from random import randint as azar
continua="s"
while(continua=="s" or continua=="S"):
    print("Elige una opcion:")
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijera")
    opcion_usuario = int(input("Selecciona tu opción (1-3): "))
    jugada_maquina = azar(1, 3)  # Genera un número aleatorio entre 1 y 3
    if opcion_usuario == jugada_maquina:
        print("Empate!")
    elif (opcion_usuario == 1 and jugada_maquina == 2):
        print("haz elegido Piedra y la máquina eligió Papel")
        print("Perdiste! La máquina eligió Papel.")
    elif (opcion_usuario == 1 and jugada_maquina == 3):
        print("haz elegido Piedra y la máquina eligió Tijera")
        print("Ganaste! La máquina eligió Tijera.")
    elif (opcion_usuario == 2 and jugada_maquina == 1):
        print("haz elegido Papel y la máquina eligió Piedra")
        print("Ganaste! La máquina eligió Piedra.")
    elif (opcion_usuario == 2 and jugada_maquina == 3):
        print("haz elegido Papel y la máquina eligió Tijera")
        print("Perdiste! La máquina eligió Tijera.")
    elif (opcion_usuario == 3 and jugada_maquina == 1):
        print("haz elegido Tijera y la máquina eligió Piedra")
        print("Perdiste! La máquina eligió Piedra.")
    elif (opcion_usuario == 3 and jugada_maquina == 2):
        print("haz elegido Tijera y la máquina eligió Papel")
        print("Ganaste! La máquina eligió Papel.")
    


   
    continua=input("continuamos? (s/n): ")
print("Fin del juego")