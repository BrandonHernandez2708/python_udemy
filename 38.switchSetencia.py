#usuario nos da el numero del mes y nosotros lo pasamos a letras
def dames(num):
    meses = {
        1: "Enero",
        2: "Febrero",
        3: "Marzo",
        4: "Abril",
        5: "Mayo",
        6: "Junio",
        7: "Julio",
        8: "Agosto",
        9: "Septiembre",
        10: "Octubre",
        11: "Noviembre",
        12: "Diciembre"
    }
    return meses.get(num,"mes no valido")

mes = int(input("Introduce el número del mes (1-12): "))
print(dames(mes))