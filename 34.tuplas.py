colores=  ("verde","amarillo","rojo","azul")
print(type(colores))
print(colores)
print(colores[:2])
tupla=()
print(tupla)
print(type(tupla))
print(colores[3]) #cuidado con indices inexistentes

#colores[2]="rosa" cuidado con asignacion de valores
print(len(colores))  #longitud de la tupla
tuplaUnitaria=(50,)
print(type(tuplaUnitaria))  
print(len(tuplaUnitaria)) 
#empaquetado 
a = 10
b ="jose"
c = 22.34
tupla=(a,b,c)
print(tupla)
print(type(tupla))

#desenpaquetado de tupla
a,b,c = tupla #la tupla debe tener el mismo numero de elementos que las variables
print(a)
print(b)
print(c)
