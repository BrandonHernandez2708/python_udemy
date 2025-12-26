#funcion que cuente numero de vocales por una palabra o texto pasado por parametros 

def cuentaVocales(cadena,vocales=0):
    for caracteres in cadena:
        
        cadena=cadena.lower()
        if caracteres == "a" or caracteres == "e" or caracteres == "i" or caracteres == "o" or caracteres == "u":
            vocales+=1
            
    return vocales


cadena = input("Ingrese una cadena para contar sus vocales ")
print("El numero de vocales en el texto es :" ,cuentaVocales(cadena))