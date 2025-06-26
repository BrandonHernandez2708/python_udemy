# Crea un modulo que contenga la funcion saludo pasandole 
# como parametro un nombre y llamala desde otro archivo.
from saludar.saludar import *
nombre = input("Ingrese su nombre: ")
print(saludar(nombre))
