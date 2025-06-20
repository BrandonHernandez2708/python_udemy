class vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
class transporte:
    def __init__(self, capacidad):
        self.capacidad = capacidad

# clase derviada que hereda de vehiculo y tranporte
class camion(vehiculo,transporte):
    def __init__(self, marca, modelo, capacidad,carga):
        vehiculo.__init__(self, marca, modelo)
        transporte.__init__(self, capacidad)
        self.carga = carga
    def describir_camion(self):
        return f"Camión {self.marca} {self.modelo}, Capacidad: {self.capacidad}, Carga: {self.carga}"
mi_camion = camion("Volvo", "vln",1500,"madera")
print(mi_camion.describir_camion())
