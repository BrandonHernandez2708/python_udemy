
texto= "Esto es un texto para el ejemplo que vamos a realizar "
# empienza y termina con 
print("la cadena empieza con: ",texto.startswith("Esto"))
print("la cadena termina con: ",texto.lower().endswith("Realizar ".lower()))
#ainiar texto
#centrado
print(texto.center(80,"+"))
longitud = len(texto)
print(texto.center(longitud + 7, "-"))
#izquierda
print(texto.ljust(80, "-"))
#derecha
print(texto.rjust(80, "-"))
#eliminar espacios
texto ="                             esto es un texto para el ejemplo que vamos a realizar                             "
print(texto)
print("cadena sin espacios al principio y al final: ", texto.strip())
#sustitucion de texto
textomodificado=(texto.replace("-", "hola"))
print(textomodificado)