# #Agrega a la clase Persona una variable de clase que cuente cuántos objetos se han creado.
# Imprime el contador al final.

class Persona:
    contador = 0
    def __init__(self, nombre):
        global contador
        self.nombre = nombre
        Persona.contador += 1
    def mostrar_contador(self):
        return f"Total de instancias de Persona: {Persona.contador}"
    
Persona1 = Persona("Juan")
Persona2 = Persona("Karla")
Persona3 = Persona("Carlos")
Persona4 = Persona("Ana")
print(Persona1.mostrar_contador())