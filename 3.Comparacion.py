n1=int(input("ingrese un numero "))
n2=int(input("ingrese oto numero y te dire cual es el mayor  "))
if (n1 > n2):
    print(f"el numero {n1} es mayor que [{n2} ")
elif(n1< n2):
    print(f"el numero {n1} es menor que {n2}")
else :
    print("los dos numeros son iguales")
print("Hemos terminado de comparar ")

#segundop ejercicio
edad=int(input("ingrese su edad"))
if (edad<5):
    print("precio igual a 5")
elif(edad<5):
  precio=5
elif edad <65:
    precio=20

print("tu tarifa para entrar es de ",str(precio))
