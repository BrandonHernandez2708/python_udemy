#Realiza un script de python para resolver ecuaciones de segundo grado 
#ax ^2+bx+c=0
from math import sqrt 
def ecuacionsegundogrado(a,b,c):
    x1 = 0
    x2 = 0
    parcial = (b**2)-(4*a*c)
    if parcial > 0:
        x1 = (-b + sqrt(parcial)) / (2*a)
        x2 = (-b - sqrt(parcial)) / (2*a)
    else:
        x1= 0
        x2= 0
        print("No se puede resolver")
    return x1,x2

a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))
c = int(input("Ingrese el valor de c: "))
x1,x2=ecuacionsegundogrado(a,b,c)
print(f"La solucion de x1 es {x1} y la de x2 es {x2}")