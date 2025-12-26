#Realiza un programa que ocnste de una clase llamada Alumanp que tenga como atributos el nombre y la nota del alum
#Definir los metodos y atributos para mostrar los datos y un mensaje con el resultado de la nota
class alumno:
    def __init__(self,nombre,calificacion):
        self.nombre = nombre
        self.calificacion = calificacion
    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Calificación: {self.calificacion}")
    def resultado(self):
        if self.calificacion >= 61:
            print("El alumno está aprobado.")
        else:
            print("El alumno está reprobado.")


if __name__ == "__main__":
    alumno1 = alumno("Brandon", 61)
    alumno1.mostrar()
    alumno1.resultado()
    alumno2 = alumno("Ana", 55)
    alumno2.mostrar()
    alumno2.resultado()
    