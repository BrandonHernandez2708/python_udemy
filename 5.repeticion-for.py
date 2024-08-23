#tabla de multiplicar con for 
tabla=int(input("que tabla quieres calcular "))
#repetir mientras sea menor que 11
for contador in range (1,11):
    resultado = tabla * contador 
    print(f"{tabla} por {contador} es igual la variable {resultado}")

print("fin de la tabla ")

#ejemplo for con lista
nombres={"Josue","Mario","Lucia","eva"}
for nombre in nombres:
    print(f"hola , {nombre}")

# Mostrar 100 numeros
for numero in range(100):
    print(numero)