"""
documentacion de mi clase 
esto es mi documentacion
"""
class vehiculo:
    def __init__(self, color, velocidadMaxima, marca):
        self.color = color 
        self.velocidadMaxima = velocidadMaxima
        self.velocidad = 0
        self.marca = marca

    def arrancar(self):
        print("Arrancando")

    def acelerar(self):
        if self.velocidad == 0:
            self.velocidad = 10
        else:
            self.velocidad = self.velocidad + 10
        print("velocidad : ", self.velocidad)

    def frenar(self):
        if self.velocidad > 10:
            self.velocidad = self.velocidad - 10
        else:
            self.velocidad = 0
        print("velocidad : ", self.velocidad)

    def muestraEstado(self):
        print(f"soy de la marca {self.marca} con un color {self.color} y velocidad maxima de {self.velocidadMaxima}")

class Moto(vehiculo):
    """
    documentacion del constuctor de la clase Moto
    """
    def __init__(self, color, velocidadMaxima, marca, ruedas=4):
        vehiculo.__init__(self, color, velocidadMaxima, marca)
        self.ruedas = ruedas
    def muestraEstado(self):
        print(f"soy de la marca {self.marca} con un color {self.color}, velocidad maxima de {self.velocidadMaxima} y tengo {self.ruedas} ruedas")   

class Coche(vehiculo):
    def __init__(self, color, velocidadMaxima, marca, ruedas=4):
        vehiculo.__init__(self, color, velocidadMaxima, marca)
        self.ruedas = ruedas
    def muestraEstado(self):
        print(f"soy de la marca {self.marca} con un color {self.color}, velocidad maxima de {self.velocidadMaxima} y tengo {self.ruedas} ruedas")   
peugeout = Coche("rojo", 120, "Peugeot", 4)
peugeout.arrancar()
peugeout.muestraEstado()
peugeout.acelerar()
peugeout.frenar()
renault = Coche("azul", 130, "Renault", 4)
renault.arrancar()
renault.muestraEstado()
renault.acelerar()
renault.acelerar()
renault.frenar()
renault.acelerar()
renault.frenar()
yamaha = Moto("azul",140, "Yamaha", 2)
yamaha.arrancar()
yamaha.acelerar()
yamaha.acelerar()
yamaha.muestraEstado()