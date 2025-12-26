import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.linspace(1,150,200)
y = x +x **2
print(x)
print(y)
plt.plot(x,y,"blue")
plt.title("Mi grafica")
plt.xlabel("valores X")
plt.ylabel("valores Y")
plt.show()
#subplot
plt.subplot(1,2,1)
plt.plot(x, y, "g")
plt.subplot(1,2,2)
plt.subplot(1,2,2)
plt.plot(x,y,'red')
plt.show()