import pandas as pd
import matplotlib.pyplot as plt
from faker import Faker
fake = Faker()
#generamos datos
numero = 100
datos = {
    'nombre': [fake.name() for _ in range(numero)],
    'direccion': [fake.address() for _ in range(numero)],
    'email': [fake.email() for _ in range(numero)],
    'ventas': [fake.random_int(min=1000, max=5000) for _ in range(numero)],
    'telefono': [fake.phone_number() for _ in range(numero)],
    'fecha_nacimiento': [fake.date_of_birth() for _ in range(numero)],
}
#creanos dataframe
df = pd.DataFrame(datos)
print(df.head())
#resumen estatistico
print(df['ventas'].describe())
#comprobamos faltantes
print(df.isnull().sum())
#grafica de distribucion de ventas
plt.figure(figsize=(10, 6))
plt.hist(df['ventas'], bins=20, color='blue', edgecolor='black')
plt.title('Distribución de Ventas')
plt.xlabel('Ventas')
plt.ylabel('cantidad')
plt.grid(True)
plt.show()
#grafica de box splot 
plt.figure(figsize=(8, 6))
plt.boxplot(df['ventas'])
plt.title('Boxplot de Ventas')
plt.ylabel('Ventas')
plt.grid(True)
plt.show()
#scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(range(len(df)), df['ventas'], color='red')
plt.title("ventas por registro")
plt.xlabel('indice')
plt.ylabel('Ventas')
plt.grid(True)
plt.show()