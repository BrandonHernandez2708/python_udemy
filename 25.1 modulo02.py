from random import randint as azar #se importa la funcion randint y se le asigna el alias aza
#from random import *  #todas las funciones de la libreria 
#import random 
continua="s"
while(continua=="s" or continua=="S"):
    lanzardaro=azar(1,6)
    print("Has sacado un "+str(lanzardaro))
    continua=input("continuamos? (s/n): ")
print("Fin del juego")
