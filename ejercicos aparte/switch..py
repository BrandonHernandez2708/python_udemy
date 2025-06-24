# Simula un "switch" para un menú de opciones:
# 1 → Sumar  
# 2 → Restar  
# 3 → Multiplicar  
# Solicita al usuario una opción e imprime la operación elegida.
def menu(num):
    operaciones = {
        1: "Sumar",
        2: "Restar",
        3: "Multiplicar"
    }
    return operaciones.get(num, "opción no válida")

opcion = int(input("Elige una opción (1: Sumar, 2: Restar, 3: Multiplicar): "))
print(menu(opcion))
n1 = float(input("Introduce el primer número: "))
n2 = float(input("Introduce el segundo número: "))
if opcion == 1:
    suma = n1 + n2
    print(f"Resultado de la suma: {suma}")
if opcion == 2:
    resta = n1 - n2
    print(f"Resultado de la resta: {resta}")
if opcion == 3:
    multiplicacion = n1 * n2
    print(f"Resultado de la multiplicación : {multiplicacion}")

