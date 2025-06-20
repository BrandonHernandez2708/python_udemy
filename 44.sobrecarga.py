""" __add__ + 
_sub_(self, other)
__mul__
__truediv__ /
__eq__ ==
__ne__ !
__lt__ <
__le__ <=
__gt__ >
__ge__ >=
#  """
class miNumero:
    def __init__(self,valor):
        self.valor = valor
    def __add__(self, other):
        if isinstance(other, miNumero):
            return miNumero(self.valor + other.valor)
          
        elif isinstance(other, (int, float)):
            return miNumero(self.valor + other)
        else:
            raise TypeError("Operación no soportada ")
    def __str__(self):
        return str(self.valor)
       
numero1 =miNumero(5)
numero2 = miNumero(10)
resultado1 = numero1 + numero2
resultado2 = numero1 + 5
print(resultado1)
print(resultado2)
texto = "Hola"
try:
    resultado3 = numero1 + texto
except Exception as e: 
    print(f"Ocurrió un error: {e}")

class persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
    def __eq__(self, other):
        if isinstance(other, persona):
            return self.nombre == other.nombre and self.edad == other.edad
        return False
    def __str__(self):
        return f"{self.nombre}, {self.edad} años"

persona1 = persona("Juan", 30)
persona2 = persona("jose",52)
persona3=persona("jose",52)
igualdad1 = persona1 == persona2
igualdad2 = persona2 == persona3
print(persona3)
print(igualdad1)
print(igualdad2)