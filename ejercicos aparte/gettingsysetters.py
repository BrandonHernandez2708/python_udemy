# Modifica la clase anterior usando 
# @property para edad, que no permita establecer edades negativas.
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    @property
    def edad(self):
        return self._edad
    @edad.setter
    def edad(self,edad):
        if edad >= 0:
            self._edad = edad
        else:
            print("La edad no puede ser negativa")
    def saludar(self):
        print(f"Hola {self.nombre} con la edad de {self.edad} años")
    
persona1=Persona("Brandon",21)
persona1.saludar()