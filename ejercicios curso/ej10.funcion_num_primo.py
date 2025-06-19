#Escribe una funcion que devuelva un valor booleano indicando si el numero es primo o no.$
def primos(num):
    if (num < 2 ):
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

num=int(input("Ingrese un numero"))
print(primos(num)) 
