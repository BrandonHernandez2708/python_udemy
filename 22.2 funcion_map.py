#map
palabras = ["python", "es", "un", "lenguaje"]
mayuscular=list(map(str.upper,palabras))
print(palabras)
print(mayuscular)
print("*"*60)
#sin map
mayusculas = []
for palabra in palabras:
    mayusculas.append(palabra.upper())
print(palabras)
print(mayusculas)