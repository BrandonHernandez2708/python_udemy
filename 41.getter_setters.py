class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad
    #obtener nombre
    def get_nombre(self): # getter : es un metodo que devuelve el valor de un atributo
        return self._nombre
    #dar valor al nombre
    def set_nombre(self, nombre): # setter : es un metodo que establece el valor de un atributo
        self._nombre = nombre
    #obtener edad
    def get_edad(self):
        return self._edad
    def set_edad(self, edad):
        if edad >= 0 :
            self._edad = edad
        else:
            print("La edad no puede ser negativa")
#crear objeto,instanciar la clase
persona1 = Persona("Juan", 28)
print("Nombre:", persona1.get_nombre())
persona1.set_nombre("karla")
#persona1.__nombre="Jose"
print("nombre:", persona1.get_nombre())
persona1.set_edad(30)
print("Edad:", persona1.get_edad())