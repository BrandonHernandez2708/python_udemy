class persona:
    contador = 0
    def __init__(self, nombre):
        self.nombre = nombre
        persona.contador += 1 # Incrementa el contador de instancias

persona1 = persona("Juan")
persona2 = persona("karla")
persona3 = persona("carlos")

#valor contador
print(f"Total de instancias de persona: {persona.contador}")