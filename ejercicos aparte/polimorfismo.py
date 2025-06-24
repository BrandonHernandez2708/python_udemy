# Ejercicio 12:
# Crea una función describir(objeto) que acepte un objeto de cualquier clase con un método hablar() y lo ejecute.
# Pasa objetos de Perro, Gato y otra clase para demostrar el polimorfismo.
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    def hablar(self):
        pass 

class Perro(Animal):
    def hablar(self):
        return f"{self.nombre} dice: Guau!"
class Gato(Animal):
    def hablar(self):
        return f"{self.nombre} dice: Miau!"
class Pollo(Animal):
    def hablar(self):
        return f"{self.nombre} dice: Pío!"

def descrbir(objeto):
    print(objeto.hablar())

mi_perro = Perro("Fido")
mi_gato = Gato("Michi")
mi_pollo = Pollo("Polly")
descrbir(mi_perro)  # Fido dice: Guau!
descrbir(mi_gato)   # Michi dice: Miau!
descrbir(mi_pollo)  # Polly dice: Pío!



