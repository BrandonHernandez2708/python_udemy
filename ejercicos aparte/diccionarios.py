# Crea un diccionario con claves "nombre", "edad", "ciudad" y asigna valores a cada una.
# Luego:
# Cambia el valor de "ciudad".
# Agrega una nueva clave "profesion".
# Recorre el diccionario e imprime cada clave y su valor.
diccionario = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}
# Cambiar el valor de "ciudad"
diccionario["ciudad"] = "Barcelona"
# Agregar una nueva clave "profesion"
diccionario["profesion"] = "Ingeniero"
# Recorrer el diccionario e imprimir cada clave y su valor
for clave, valor in diccionario.items():
    print(f"{clave}: {valor}")


