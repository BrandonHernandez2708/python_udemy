#crea una funcicon que indique que numero de los pasados por parametros es mayor o si son iguales 
def comparar_numeros(num1, num2):
    if num1 == num2:
        return "Los números son iguales."
    elif num1 > num2:
        return f"El número {num1} es mayor que {num2}."
    else:
        return f"El número {num2} es mayor que {num1}."
    

#ejemplo de uso
resultado = comparar_numeros(10, 10)
print(resultado)  # Salida: El número 20 es mayor que 10.
