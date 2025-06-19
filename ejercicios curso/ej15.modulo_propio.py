from calculadora.funciones import *

print("Bienvenido a la calculadora")

print("digite una opcion")
print("1.sumar\n2.restar\n3.multiplicar\n4.dividir")
opcion = int(input("Ingrese la opcion: "))

if opcion == 1:
    n1 = int(input("Ingrese el primer numero: "))
    n2 = int(input("Ingrese el segundo numero: "))
    print(suma(n1, n2))
elif opcion == 2:
    n1 = int(input("Ingrese el primer numero: "))
    n2 = int(input("Ingrese el segundo numero: "))
    print(resta(n1, n2))
elif opcion == 3:
    n1 = int(input("Ingrese el primer numero: "))
    n2 = int(input("Ingrese el segundo numero: "))
    print(multiplicacion(n1, n2))
elif opcion == 4:
    n1 = int(input("Ingrese el primer numero: "))
    n2 = int(input("Ingrese el segundo numero: "))
    print(division(n1, n2))
else:
    print("Opción no válida")