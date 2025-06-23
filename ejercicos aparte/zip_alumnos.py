# Crea dos listas: una con nombres de estudiantes y otra con sus notas.
# Usa zip para unirlas en un diccionario y muestra los pares.
nombres_estudiantes = ["Ana", "Luis", "Pedro", "María"]
notas_estudiantes = [8.5, 9.0, 7.5, 9.5]
combinado = zip(nombres_estudiantes, notas_estudiantes)
diccionario_estudiantes = dict(combinado)
print (diccionario_estudiantes)
for nombre, nota in diccionario_estudiantes.items():
    print(f"{nombre} tiene una nota de {nota}")
    