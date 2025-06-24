# #Crea una clase base Animal con método hablar().
# Crea dos clases hijas: Perro y Gato que sobrescriban el método.
# Cada clase hija debe implementar su propia versión del método hablar().
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
class MascotaEspecial(Perro, Gato):
    def hablar(self):
        return f"{self.nombre} es una mascota especial que dice: ¡Guau! y Miau!"

mi_perro = Perro("fido")
mi_gato = Gato("michi")
mi_mascota_especial = MascotaEspecial("pelusa")
print(mi_perro.hablar())  # Fido dice: Guau!
print(mi_gato.hablar())   # Miau dice: Miau!
print(mi_mascota_especial.hablar())  # Pelusa es una mascota especial que dice: ¡Guau! y Miau!