# Crea una clase Alumno con su nombre y calificacion.
# Ademas de iniciar sus atributos, 
# debes crear los metodos para mostrarlos e indicar si esta aprobado o no.
class alumno:
    def __init__(self,nombre,calificacion):
        self.nombre = nombre
        self.calificacion = calificacion
    def obtener_nombre(self):
        return self.nombre 
    def obtener_calificacion(self):  
        if self.calificacion > 100 or  self.calificacion < 0 :
            return "ERROR : la calificación no puede ser mayor a 100 o negativa"
        else:
             return self.calificacion
    def comprobacion(self):
        if self.calificacion >= 61 :
            return "aprobado"
        else:
            return "reprobado"


        
alumno1=alumno("Brandon",61)
print(f"el alumno{alumno1.obtener_nombre()},con la nota {alumno1.obtener_calificacion()} {alumno1.comprobacion()}")