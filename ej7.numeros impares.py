inicio=int(input("Ingrese el inicio de la cuenta"))
final=int(input("Ingrese el final de la cuenta"))
for numeros in range (inicio,final,2):
   
    if numeros %2:
        print(numeros)

