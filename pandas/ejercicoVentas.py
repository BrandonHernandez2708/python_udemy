import numpy
import pandas as pd 
import matplotlib.pyplot as plt
datos = pd.read_csv('datos.csv')
print("Inicio dataframe")
print(datos.head(5))
print("Fin dataframe")
print(datos.tail(5))
print(datos.info())
print(datos.describe())
print(datos.columns)
print(datos.index)

datosAgrupados = datos.groupby('TIENDA').TOTAL.sum()
print(datosAgrupados.head(5))

plt.pie(datosAgrupados, labels=datosAgrupados.index, )
plt.show()