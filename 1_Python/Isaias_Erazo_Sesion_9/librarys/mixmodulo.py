# Módulo Analisis de datos


import pandas as pd
import numpy as np


def cargar_datos(archivo):
    """ Carga datos en archivos CSV , utilizando pandas"""

    data = pd.read_csv(archivo)
    return data


def calcular_promedio(columna):
    """ Calcula el promedio de una columna de valores utiliozand numpy """

    promedio = np.mean(columna)
    return promedio
