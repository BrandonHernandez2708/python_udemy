#Escribe un programa que almacene una contraseña en una variable, 
#preguntando al usuario una contraseña y comparar si coincide con la guardada en la variable.
contraseña="123456789"
contraseña_usuario=input("Introduce la contraseña: ")
if contraseña_usuario == contraseña:
    print("Contraseña correcta")
else:
    print("Contraseña incorrecta")

#Pedir 2 numeros al usuario para devolver el resultado de la division, ten en cuenta
# que si el usuario inserta un 0 como valor del divisor deberas indicarle que no se puede dividir por 0.
print("Introduce el primer numero: ")
num1 = int(input())
print("Introduce el segundo numero: ")
num2 = int(input())
try:
    resultado = num1 / num2
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")

print("El resultado de la division es: ", resultado)

#Solicitar la edad al usuario e indicar si es mayor de edad o no.
edad=int(input("Introduce tu edad: "))
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

#Pedir un numero al usuario y mostrar si es par o impar.
numero = int(input("Introduce un numero: "))
if numero %2 ==0:
    print("El numero es par")
else:
    print("El numero es impar")