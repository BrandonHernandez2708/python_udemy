import matplotlib.pyplot as plt
import random

# Paso 1: Crear datos de prueba
usuarios = [f'Usuario{i}' for i in range(1, 21)]  # 20 usuarios ficticios
ventas = [random.randint(10, 100) for _ in usuarios]  # Ventas aleatorias entre 10 y 100

# Paso 2: Crear histograma
plt.figure(figsize=(10, 6))
plt.hist(ventas, bins=10, color='skyblue', edgecolor='black')

# Paso 3: Personalizar gráfico
plt.title('Histograma de Ventas por Usuario')
plt.xlabel('Rango de Ventas')
plt.ylabel('Cantidad de Usuarios')
plt.grid(True, linestyle='--', alpha=0.5)

# Paso 4: Mostrar gráfico
plt.show()
