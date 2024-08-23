#tabla de multiplicar 
tabla=int(input("que tabla quieres calcular "))
contador =1
print(f"Tabla del {tabla}")
#Repeticion
while (contador <11):
    resultado = tabla * contador
   #mostramos la table
    print(f"{tabla} por {contador} es igual a {resultado}\n")
    #comprobamos si es 4 y salidos
    if contador ==4:
      print("EL CONTADOR ES IGUAL A 4 Y NO CONTINUA ")
     
      break
    #incrementa el contador 
    contador = contador +1 
print("Fin de la tabla ")