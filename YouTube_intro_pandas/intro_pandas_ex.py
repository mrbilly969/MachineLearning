import numpy as np
import pandas as pd

#Creación de Arreglo de datos
data = np.array([['','Col1','Col2'], ['Fila1',11,22], ['Fila2',33,44]])
print(pd.DataFrame(data=data[1:,1:], index=data[1:,0], columns=data[0,1:]))

#Creación de Data Frame
df = pd.DataFrame(np.array([[1,2,3],[4,5,6],[7,8,9]]))
print('\nDataFrame:')
print(df)

# Creación de Series
series = pd.Series({"Argentina":"Buenos Aires",
                    "Chile":"Santiago de Chile",
                    "Colombia":"Bogotá",
                    "Perú":"Lima"})
print('\nSeries:')
print(series)

#Forma del DataFrame
print('\nForma del DataFrame:')
print(df.shape)

#Altura del DataFrame
print('\nAltura del DataFrame:')
print(len(df.index))

#Estadísticas del DataFrame
print('\nEstadísticas del DataFrame:')
print(df.describe())

#Medida de las columnas del DataFrame
print('\nMedia de las columnas del DataFrame:')
print(df.mean())

#Correlación del DataFrame
print('\nCorrelación del DataFrame:')
print(df.corr())

#Cuenta los datos del DataFrame
print('\nConteo de datos del DataFrame:')
print(df.count())

#Valor más alto de cada columna del DataFrame
print('\nValor más alto de la columna del DataFrame:')
print(df.max())

#Valor mínimo de cada columna del DataFrame
print('\nValor mínimo de la columna del DataFrame:')
print(df.min())

#Mediana de cada columna del DataFrame
print('\nMediana de la columna del DataFrame:')
print(df.median())

#Desviación estandar de cada columna del DataFrame
print('\nDesviación estandar de la columna del DataFrame:')
print(df.std())

#Seleccionar dos columnas del DataFrame
print('\nDos columnas del DataFrame:')
print(df[[0,1]])

#Seleccionar el valor de la primera fila y última columna del DataFrame
print('\nValor de la primera fila y última columna del DataFrame:')
print(df.iloc[1][2])
