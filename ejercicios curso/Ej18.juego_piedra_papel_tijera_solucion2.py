import random 
import sys
def iniciar():
    global partidas,ganadas,perdidas,empates
    partidas = 0
    ganadas = 0
    perdidas = 0
    empates = 0

def menu():
    print("""
          indica la opcion seleccionada:
          1.piedra
          2.papel
          3.tijera
          0.salir
          """)
    opcion = input("-> ")
    if opcion not in ['1', '2', '3', '0']:
        print("Seleccione una opción válida.\n")
        opcion_usuario = None
    else:
        if opcion == "1":
            opcion_usuario = "piedra"
        if opcion == "2":
            opcion_usuario = "papel"
        if opcion == "3":
            opcion_usuario = "tijera"
        if opcion == "0":
            print("Hasta pronto!!")
            sys.exit()
    return opcion_usuario     
def elige_maquina():
    lista_opciones = ["piedra", "papel", "tijera"]
    opcion = random.choice(lista_opciones)
    return opcion

def comprobar(opcion_usuario, opcion_maquina):
    global partidas,ganadas,perdidas,empates
    partidas +=1
    print("\n")
    if opcion_usuario == opcion_maquina:
        print("Hemos empatado!")
        empates += 1
    elif (opcion_usuario == "piedra" and opcion_maquina == "tijera"):
        print("Has ganado")
        ganadas += 1
    elif (opcion_usuario == "papel" and opcion_maquina == "piedra"):
        print("Has ganado")
        ganadas += 1
    elif (opcion_usuario == "tijera" and opcion_maquina == "papel"):
        print("Has ganado")
        ganadas += 1
    else:
        print("Has perdido")
        perdidas += 1
    print("\n")
    print("*"*20)
    print(f"mi opcion fue {opcion_maquina}")
    print(f"tu opcion fue {opcion_usuario}")
    print(f"llevamos {partidas} partidas")
    print(f"ganadas: {ganadas}")
    print(f"perdidas: {perdidas}")
    print(f"empates: {empates}")
    print("*"*20)
    print("\n")

def main():
    iniciar()
    opcion_usuario = menu()
    while True:
        if opcion_usuario != None:
            opcion_maquina = elige_maquina()
            comprobar(opcion_usuario, opcion_maquina)
        opcion_usuario = menu()


if __name__ == "__main__":
   main()