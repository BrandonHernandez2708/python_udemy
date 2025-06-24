# Ejercicio 11:
# Crea una clase Calculadora con un método sumar().
# Sobrecarga este método para:
# Sumar dos números.
# Sumar tres números si se pasa un tercer argumento.
# (Pista: puedes usar valores por defecto o *args)
class Calculadora:
    def sumar(self, *args):
        return sum(args)
    
# Ejemplo de uso
resultado1 = Calculadora().sumar(5, 10)
resultado2 = Calculadora().sumar(5, 10, 15)
print(f"Suma de dos números: {resultado1}")  # Suma de dos números: 15
print(f"Suma de tres números: {resultado2}")  # Suma de tres números
