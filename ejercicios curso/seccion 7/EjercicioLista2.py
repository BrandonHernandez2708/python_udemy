#Solicitar una lista al usuario ordenarla e indicarla con otras lista los numeros pares e impares
def solicitar():
    lista = []
    num= None
    while num!=0 :
        num = int(input("Dime un numero: (0 para terminar) "))
        if num >0:
            lista.append(num)
        elif num==0:
            break
        else:
            print("El numero debe ser mayor que 0\n")
    return lista

def ordenar(lista):
    lista.sort()
    pares=[]
    impares=[]
    for i in lista:
        if i %2:
            impares.append(i)
        else :
            pares.append(i)
    return pares,impares
        

lista   = solicitar()
print("Imprimimos la lista \n")
print(lista)
print("Imprimomos la lista de numeros pares ")
pares,impares=ordenar(lista)
print(pares)
print("Imprimomos la lista de numeros ipares ")
print(impares)