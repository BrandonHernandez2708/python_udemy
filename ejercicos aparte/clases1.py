# Define una clase Persona con atributos 
# nombre, edad, y un método saludar() que imprima un saludo personalizado.
# Crea un objeto y llama al método.
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def saludar(self):
        print(f"Hola {self.nombre} con la edad de {self.edad} años")
    
persona1=Persona("Brandon",21)
persona1.saludar()