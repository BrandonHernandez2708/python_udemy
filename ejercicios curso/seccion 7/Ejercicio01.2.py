#crea una calculadora basica, incluyendo menu de opciones y comprobando que no se intente dividir entro de 0
n1 = int(input("dame el primer numero\n"))
n2 = int(input("dame el segundo numero\n"))
opc = int(input("Ingrese la opcion deseada"))
match opc:
    case 1:
        suma = n1+n2
        print(f"El resultado de la suma es {suma}\n" )
    case 2 :
        resta = n1-n2
        print(f"el resuldado de la resta es {resta}\n")
    case 3 :
        multi = n1*n2  
        print(f"el resultado de la multiplicacion es {multi}\n")
    case 4: 
        try : 
            division = n1/n2
            print(f"el resultado de la divisione es  {division}\n")
        except:
            print("no se puede dividir entro de 0")
            division = 0;
