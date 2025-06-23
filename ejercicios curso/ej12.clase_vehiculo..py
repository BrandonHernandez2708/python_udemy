#Crea una clase Vehiculo con los siguientes atributos: 
# Marca Color Crea la clase Coche que herede de vehiculo y tenga los siguientes atributos: 
# Potencia Motor Crear un objeto de clase Coche y mostrar sus atributos.
class vehiculo:
    def __init__(self, marca, color):
        self.__marca = marca
        self.__color = color
    def obtener_marca(self):
        return self.__marca
    def obtener_color(self):
        return self.__color
class Coche(vehiculo):
    def __init__(self, marca, color, potencia, motor):
        super().__init__(marca, color)
        self.__potencia = potencia
        self.__motor = motor
    def obtener_potencia(self):
        return self.__potencia
    def obtener_motor(self):
        return self.__motor

mi_coche = Coche("Toyota", "Rojo", "150 CV", "V6")
print(f"el coche es marca {mi_coche.obtener_marca()} de color {mi_coche.obtener_color()} con potencia {mi_coche.obtener_potencia()} y motor {mi_coche.obtener_motor()   }")