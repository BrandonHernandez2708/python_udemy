class Persona:
    identificador = 0
    def __init__(self, nombre,apellidos, edad):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        Persona.identificador += 1
class alumno(Persona):
    def __init__(self, nombre, apellidos, edad, carrera):
        super().__init__(nombre, apellidos, edad)
        self.carrera = carrera
        self.nota = None
        self.alta = False
    def poner_nota(self, nota):
        self.nota = nota
    def obtener_nota(self):
        if self.nota is not None:
            return self.nota
        else:
            return "No se ha puesto nota"
    def dar_alta(self):
        if self.nota: 
            print("Ya estaba de alta")
        else:
            self.alta = True
    def obtener_alta(self):
        return self.alta
    def __str__(self):
        return f"Alumno: {self.nombre} {self.apellidos}, Edad: {self.edad}, Carrera: {self.carrera}, Nota: {self.obtener_nota()}, Alta: {self.obtener_alta()}"

alumno1 = alumno("Juan", "Pérez", 20, "Ingeniería")
print(alumno1)
alumno1.poner_nota(8.5)
alumno1.dar_alta()
print(alumno1.obtener_alta())
print(alumno1.obtener_nota())
alumno2 = alumno("Ana", "Gómez", 22, "Medicina")
print(alumno2)
print(Persona.identificador)  # Imprime el número de identificadores creados
