#Dada una cadena indicar si es palindrona o no 
cadena="RaDar"
cadena_invetida = cadena[::-1]
if (cadena.lower() == cadena_invetida.lower()):
    print("La cadena es palindroma")
else :
    print("La cadena No es Palindroma")