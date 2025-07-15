import pandas as pd
import numpy as np
etiquetas= ['a', 'b', 'c', 'd', 'e']
datos = np.arange(4,9)
serie = pd.Series(datos, index=etiquetas)
print(serie)
#acceder valor
print(serie['c'])  # Acceder al valor con la etiqueta 'c'
#datos distintos tipos
datos = ['Jose',49,"Mar",46]
serie = pd.Series(datos)
print(serie)
serie = pd.Series([1000,500,1200,700],["Emp01","Emp02","Emp03","Emp04"])
print(serie)
serie2 = pd.Series([1050,1500,2200,900],["Emp01","Emp02","Emp03","Emp04"])
print(serie2)
serie3= serie + serie2
print(serie3)
#dataframe
filas = ["tienda1", "tienda2", "tienda3", "tienda4"]
columnas=["Articulo1", "Articulo2", "Articulo3"]
datos = [[124,100,200],[200,100,300],[300,100,400],[400,100,500]]
dataframe = pd.DataFrame(datos, index=filas, columns=columnas)
print(dataframe)
#seleccionar fila
print(dataframe.loc["tienda2"])  # Seleccionar la fila 'tienda2'
print(dataframe.loc[["tienda2", "tienda3"]])  # Seleccionar varias filas
#seleccionar columna
print(dataframe["Articulo3"])  # Seleccionar la columna 'Articulo3'
#valor concreto
print(dataframe.at["tienda2", "Articulo3"])  # Acceder al valor en la fila 'tienda2' y columna 'Articulo3
#nueva columna
dataframe['Articulo4']=25
print(dataframe)
dataframe['total'] = dataframe['Articulo1'] + dataframe['Articulo2'] + dataframe['Articulo3'] + dataframe['Articulo4']
print(dataframe)
#eliminar columna
#dataframe = dataframe.drop(columns=['total'],axis=1
dataframe.drop(columns=['total'], axis=1, inplace=True) #axis indica que es una columna
print(dataframe)
condicion = (dataframe["Articulo2"] >= 200) | (dataframe["Articulo2"] >= 100)  # Condición para filtrar
print(dataframe[condicion])  # Mostrar solo los valores mayores a 200
nuevaColumna= "1 2 3 4".split()  # Crear una nueva columna a partir de una cadena
dataframe["indices"] = nuevaColumna
print(dataframe)
dataframe = dataframe.set_index("indices")  # Establecer la nueva columna como índice
print(dataframe)
# dataframe.fillna(axis=1, inplace=True)  # Rellenar valores NaN con el valor anterior en la misma fila
# dataframe.filna(value=90, inplace=True)  # Rellenar valores NaN con el valor anterior en la misma fila
media = dataframe.mean()  # Calcular la media de la columna 'Articulo1'
print(f"la media es igual a: {media}")
dataframe.fillna(value=media, inplace=True)  # Rellenar valores NaN con la media de la columna
print(dataframe)
data1 = dataframe.copy()  # Crear una copia del DataFrame
data2 = dataframe.copy()  # Crear otra copia del DataFrame
print(data1)
print(data2)
datatotal = pd.concat([data1, data2], axis=0)  # Concatenar los DataFrames
print(datatotal["Articulo4"].unique())  # Obtener los valores únicos de la columna 'Articulo2'
print(datatotal["Articulo4"].value_counts())  # Contar los valores únicos de la columna 'Articulo3'
datatotal = datatotal.apply(lambda x: x * 3)  # Aplicar una función a cada elemento del DataFrame
print(datatotal.columns)
print(datatotal.describe())  # Describir el DataFrame


dataframe = pd.read_csv("datosTotal.csv", index_col=0)  # Leer el archivo CSV y establecer la primera columna como índice
print(dataframe)  # Mostrar el DataFrame leído desde el archivo CSV