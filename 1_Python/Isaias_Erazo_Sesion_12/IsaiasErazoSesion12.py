import pandas as pd

data = pd.read_csv("C:/Users/isaia/Desktop/Clases 1/Python/Isaias_Erazo_Sesion_12/auto-mpg.csv")
print(data.head())
print("Media de 'horsepower': ", data["horsepower"].mean())
print("Suma de 'horsepower':", data["horsepower"].sum())

import matplotlib.pyplot as plt

plt.figure()
plt.hist(data["horsepower"])
plt.xlabel("Horsepower")
plt.ylabel("Frecuencia")
plt.title("Histograma de Horsepower")
plt.show()