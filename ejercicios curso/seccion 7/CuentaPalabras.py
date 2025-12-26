def cuenta_palabras(texto):
    palabras = texto.split()  # separa por espacios
    palabras_contadas = {}

    for palabra in palabras:
        palabra = palabra.lower()  # opcional: evita diferencias por mayúsculas
        if palabra in palabras_contadas:
            palabras_contadas[palabra] += 1
        else:
            palabras_contadas[palabra] = 1

    return palabras_contadas


try:
    fichero = open("ejemplocuentapalabra.txt","r",encoding="utf-8")
    texto = fichero.read()
    print("fichero correcto")
except:
    print("no se ha podido leer el fichero")
finally:
    fichero.close()
    print("fichero cerrado")
#texto = "Esto es un texto de ejemplo donde vemos cuantas veces aparece cada palabra dentro de este texto palabra palabra texto dentro donde vemos"
resultado = cuenta_palabras(texto)
print(resultado)
