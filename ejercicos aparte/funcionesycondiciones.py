#Crea una función que reciba la edad de una persona y diga si puede votar, trabajar o jubilarse.
def evaluaredad():
 edad=int(input("ingrese la edad del usurio "))
 if edad < 18:
  print("usted no puede votar ni trabajar")
 elif edad < 62 :
  print("usted puede trabajar y votar")
 else:
  print("usted puede jubilarse")

evaluaredad()