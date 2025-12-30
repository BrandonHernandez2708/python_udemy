import pandas as pd


def dameInteresEquivalente(interes, tiempo):
    interes = interes / 100
    interesEquivalente = ((1+interes)**(1/tiempo))-1
    return round(interesEquivalente*100, 2)


def dameValorActual(interes, tiempo):
    interes = interes / 100
    valorActual = ((1-(1+interes)**(-tiempo))/interes)
    return valorActual


def dameInteresPagado(capitalPte, interes):
    return (capitalPte*(interes/100))


def prestamoFrances(capital, interes, tiempo):
    valorActual = dameValorActual(interes, tiempo)
    cuotaAmortizacion = capital / valorActual
    capitalPte = capital
    lista = []
    columnas = ['Periodo', 'Cuota amortizacion',
                'Capital amortizado', 'Interes pagado', 'Capital pendiente']
    
    for i in range(1, tiempo+1):
        interesPagado = dameInteresPagado(capitalPte, interes)
        capitalAmortizado = cuotaAmortizacion - interesPagado
        
        # Ajuste para el último periodo
        if i == tiempo: 
            capitalAmortizado = capitalPte
            cuotaAmortizacionFinal = capitalAmortizado + interesPagado
            capitalPte = 0
            lista.append([i, round(cuotaAmortizacionFinal, 2), round(
                capitalAmortizado, 2), round(interesPagado, 2), round(capitalPte, 2)])
        else:
            capitalPte = capitalPte - capitalAmortizado
            lista.append([i, round(cuotaAmortizacion, 2), round(
                capitalAmortizado, 2), round(interesPagado, 2), round(capitalPte, 2)])
    
    prestamo = pd. DataFrame(lista, columns=columnas)
    prestamo.set_index('Periodo', inplace=True)
    return prestamo


if __name__ == '__main__':
    cuadro = prestamoFrances(1200,5,10)
    print(cuadro)