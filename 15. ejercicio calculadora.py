opc = -1
def solicitaDatos():
    num1 = int(input("Dime el primer numero "))
    num2 = int(input("Dime el segundo numero "))
    if num2 == 0:
        print("El numero no puede ser 0 \n")
        num2 = int(input("Dime el segundo numero "))
    return num1, num2
while (opc != 5):
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Salir")
    opc = int(input("Opcion: "))
    match opc:
        case 1:
            num1, num2 = solicitaDatos()
            resultado_suma = num1 + num2
            print(f"La suma  de {num1} + {num2} es {resultado_suma}")
        case 2:
                num1, num2 = solicitaDatos()
                resultado_resta = num1 - num2
                print(f"La suma  de {num1} - {num2} es {resultado_resta}")
        case 3:
                num1, num2 = solicitaDatos()
                resultado_muiltiplicacion = num1 * num2
                print(f"La multiplicacion de {num1} X {num2} es {resultado_muiltiplicacion}")
        case 4:
                    num1, num2 = solicitaDatos()
                    resultado_division = num1 / num2
                    print(f"La division de {num1} / {num2} es {resultado_division}")
               
        case _:
            print("Opcion invalida")

