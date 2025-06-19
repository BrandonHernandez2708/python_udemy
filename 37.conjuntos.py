#conjunto vacio
conjunto_vacio = set()
#conjunto con elementos
numeros = {1, 2, 3, 4, 5}
letras  = set(["a","b","c"])
print(conjunto_vacio)
print(numeros)
print(letras)
#agregar elementos 
print("*"*25)
frutas = {"manzana","platano","naranja"}
frutas.add("pera")
print(frutas)
#eliminar elementos
frutas.remove("platano") 
print(frutas)
#union de conjuntos 
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}
union = conjunto1 | conjunto2
print("Unión:", union)
#interseccion
interseccion = conjunto1 & conjunto2
print("Intersección:", interseccion)
#diferencia de conjuntos
diferencia = conjunto1 - conjunto2
print("Diferencia:", diferencia)
print(diferencia)
# diferencia simetrica
diferencia_simetrica = conjunto1 ^ conjunto2 
print("Diferencia simétrica:", diferencia_simetrica) #devulve todos los elementos que no están en ambos conjuntos
#pertenecia
if 3 in conjunto1:
    print("3 está en conjunto1")
else:
    print("3 no está en conjunto1")
#longitud de un conjunto
longitud = len(conjunto1)
print("Longitud de conjunto1:", longitud)
#conversion lista y conjunto
lista = [1,2,2,2,2,3,4,5,5,6,7,8,9]
conjunto = set(lista)
print(lista)
print(conjunto)
lista_nueva = list(conjunto)
print(lista_nueva)

