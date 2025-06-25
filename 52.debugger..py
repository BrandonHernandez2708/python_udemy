def dividir():
    num1=int(input("Ingrese el primer numero: "))
    num2=int(input("Ingrese el segundo numero: "))
    try:
        resultado = num1 / num2
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")
        
    finally:
        return resultado
def damepares():
    pares = []
    for i in range(1, 51):
        if i % 3 == 0:
            pares.append(i)
    return pares
def main():
    print(damepares())
if __name__ == "__main__":
    main()