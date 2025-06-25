#cambiar el nombre del archivo a test.py para evitar conflictos con el nombre del modulo que el numero lo confunde 

def multiplicar(num1,num2):
    """
    funcion que multiplica dos numeros
    Argumentos:
    numero1 (int)
    numero2 (int)
    retorna la multiplicacion de los parametros dados 
    
    >>> multiplicar(2,3)
    6
    >>> multiplicar(2,4)
    8
    """
    return num1 * num2

print(f"El resultado de multiplicar es igual {multiplicar(6,12)}")
