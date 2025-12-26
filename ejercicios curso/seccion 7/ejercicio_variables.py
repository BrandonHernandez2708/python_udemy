#Una empresa tiene 3 productos de distinto peso que manda a los clientes a través de otra empresa de mensajería, necesita un script que le indique qué peso envía a cada cliente para indicarlo a la mensajería.
#Se debe solicitar al usuario la cantidad a enviar de cada producto, conociendo que el peso es el siguiente:

#Producto 1 pesa 1.5 kg
#Producto 2 pesa 1.7 kg
#Producto 3 pesa 2.1 kg

peso1 = 1.5
peso2 = 1.7
peso3 = 2.1 

cantidad1 = int(input("Ingrese la cantidad enviada del producto 1 \n"))
cantidad2= int(input("Ingrese la cantidad enviada del producto 2 \n"))
cantidad3= int(input("Ingrese la cantidad enviada del producto 3 \n"))

peso_t1 = peso1 * cantidad1
peso_t2 = peso2* cantidad2
peso_t3 = peso3 * cantidad3
total = peso_t1 + peso_t2 + peso_t3

print(f"La cantidad total de peso del producto 1 es : {round(peso_t1,2)} kg\n")

print(f"La cantidad total de peso del producto 2 es : {round(peso_t2,2)}kg\n")

print(f"La cantidad total de peso del producto 3 es : {round(peso_t3,2)} kg\n")
print(f"Total envidado {round(total)}kg")
 
