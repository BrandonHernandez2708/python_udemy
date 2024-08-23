#funciones especiales que permiten modificar el comportamiento de una función o método
#decoradores: funciones que reciben una función y devuelven otra función
import time
def calcular_tiempo(funcion):
    def envuelve(*args, **kwargs):
        inicio = time.time()
        resultado = funcion(*args, **kwargs)
        fin = time.time()
        print(f"el tiempo de ejcucioon de {funcion.__name__}: {round(fin - inicio,2)}")
    return envuelve #wrapper  
@calcular_tiempo

def operacion():
     time.sleep(4)
     print("operacion terminada")
operacion()