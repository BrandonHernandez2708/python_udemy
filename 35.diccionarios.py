diccionario = {"nombre": "jose", "apellidos": "ojeda", "tutoriales": ["python", "javascript", "php"]}
print(diccionario)
print(type(diccionario))
print(diccionario["nombre"])
print(diccionario["tutoriales"])
print(diccionario["tutoriales"][1])
for clave in diccionario:
    print (clave, ":", diccionario[clave])
#metetodo de los diccionarios
persona = dict(nombre="jose",apellidos="ojeda",edad=48) #dict es una estructura de datos que almacena pares de clave y valor.
print(persona)
print(type(persona))
diccionari02=dict(zip("aeiou", [1,2,3,4,5]))
print(diccionari02)
print(diccionari02.items()) #Devuelve todos los pares clave-valor del diccionario.
print(diccionari02.keys()) #Devuelve todas las claves del diccionario.
print(diccionari02.values()) #Devuelve todos los valores del diccionario.
#diccionari02.clear()
copiaDiccionario = diccionari02.copy()
print(copiaDiccionario)
diccionario03=dict.fromkeys(["a","e","i","o","u"],34) #Crea un nuevo diccionario con las claves especificadas y el valor dado.
print(diccionario03)
print(diccionario.get("nombre"))
print(diccionario.get("amigo)"))
borrado = diccionario.pop("nombre")
print(borrado)
print(diccionario)
diccionario02={"provincia":"sevilla","nombre":"Lucia"}
print(diccionario)
diccionario.update(diccionario02)
print(diccionario)