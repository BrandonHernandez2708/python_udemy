class Animal:
    def hacer_sonido(self):
        pass
class Perro(Animal):
    def hacer_sonido(self):
        return "Guau"

class Gato(Animal):
    def hacer_sonido(self):
        return "Miau"
    
def interactuar_con_animal(animal):
    return animal.hacer_sonido()

miperro = Perro()
migato = Gato()
print(miperro.hacer_sonido())  # Salida: Guau
resultado_perro = interactuar_con_animal(miperro)
resultado_gato = interactuar_con_animal(migato)
print(resultado_perro)  # Salida: Guau
print(resultado_gato)  # Salida: Miau