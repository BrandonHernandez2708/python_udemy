import os 
numero1=45
numero2=40
try:
    resultado = numero1 / numero2
    
except:
    resultado = 0
    print("Ha ocurrido un error ")
finally:
    print(resultado)
    print("esto se ejucuta siempre")

try:
    os.remove(os.getcwd() + "/48.exepciones.txt")   
except  FileNotFoundError:
        print("El fichero no existe, no se ha podido eliminar")
finally:
    print("fin del script ")
