def espar(num):
    if num %2 == 0:
        return True
        #print("el numero es par")
    else:
        return False
        #print("el numero es impar")

num=int(input("ingrese un numero y te indicare si es par o no "))
resultado=espar(num)
if resultado == True : 
    print(f"el numero {num} es par")
else : 
    print(f"el numero {num} es impar")
