#Crea una funcion que calcule el area de un triangulo, recibiendo como parametros la base y la altura.
def area_triangulo(base,altura):
    area=(base*altura)/2
    return area

base = int(input("Ingrese la base del triangulo "))
altura = int(input("Ingrese la altura del triangulo "))
print(area_triangulo(base,altura))
