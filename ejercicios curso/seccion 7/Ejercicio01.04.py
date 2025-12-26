#mostrar los numeros pares de un invtervalo del numero 1 al 50 y contar cuantos son
contador = 0
for pares in range (1,51):
    
   
    if pares %2 ==0 :
        contador+=1
        print(pares)
        
print(f"Los numeros pares del 1 al 50 son : {contador}")       