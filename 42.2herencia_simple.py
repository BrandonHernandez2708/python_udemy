#clase padre
class vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def describir(self):
        return f"marca: {self.marca}, modelo: {self.modelo}"
#clase hija
class coche(vehiculo):
    def __init__(self,marca,modelo,color):
        super().__init__(marca, modelo)
        self.color = color
    def describir_coche(self):
        return f"{super().describir()}, color: {self.color}"
# instancia de la clase mi coche
mi_coche=coche("Toyota", "Corolla", "Rojo")
#acceder a metodos y atributos
print(mi_coche.describir_coche()) 
print(mi_coche.describir())  # Llamada al método describir de la clase hija
print(mi_coche.marca)  # Acceso al atributo de la clase padre
