import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, r2_score
from scipy.optimize import curve_fit
from sklearn.model_selection import train_test_split
import warnings
import matplotlib.pyplot as plt

warnings.filterwarnings("ignore")

# Leer los datos
New_York_City_median_price_gb_BOROUGH = pd.read_csv("gcp/New_York/New_York_City_median_price_gb_BOROUGH.csv")
New_York_City_median_price_gb_BOROUGH['Time'] = pd.to_datetime(New_York_City_median_price_gb_BOROUGH['Time'], format='%d-%m-%Y')
New_York_City_median_price_gb_BOROUGH.dropna(inplace=True)
New_York_City_median_price_gb_BOROUGH['Time'] = (New_York_City_median_price_gb_BOROUGH['Time'] - New_York_City_median_price_gb_BOROUGH['Time'].min()).dt.days // 30

# Dividir los datos en características (X) y etiquetas (Y)
X = New_York_City_median_price_gb_BOROUGH[['Time']]


columnas = New_York_City_median_price_gb_BOROUGH.columns
columnas = columnas[1:]
parametros = {}
for i in columnas:
    Y = New_York_City_median_price_gb_BOROUGH[i]
    # Utilizar train_test_split para dividir los datos en conjuntos de entrenamiento y prueba
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
    
    # Definir una función seno para ajustar
    def sin_func(x, A, B, C, D, E, F):
        return A * np.sin(B * x + F) + C * (x**2) + D * x + E
    
    # Ajustar la función seno a los datos de entrenamiento
    params, params_covariance = curve_fit(sin_func, X_train.values.flatten(), Y_train)
       
    # Parámetros ajustados
    A, B, C, D, E, F = params
    
    # Realizar predicciones en el conjunto de prueba
    Y_pred = sin_func(X_test.values.flatten(), A, B, C, D, E, F)
    
    print(f"{i}")
    
    # Calcular el error cuadrático medio en el conjunto de prueba
    mse = mean_squared_error(Y_test, Y_pred)
    print("Mean Squared Error:", mse**(1/2))
    
    # Calcular el coeficiente de determinación R^2 en el conjunto de prueba
    r2 = r2_score(Y_test, Y_pred)
    print("R^2 Score:", r2)
    parametros[i] = params
    
    # Agregar una línea para los valores reales (Y_test)
    plt.scatter(X_test, Y_test, label='Valores Reales', color='red')

    
    # Agregar las predicciones (Y_pred)
    plt.scatter(X_test, Y_pred, label='Predicciones', color='blue')
    
    plt.title(f'Gráfico de Predicciones vs. Valores Reales para {i}')
    plt.xlabel('X_test')
    plt.ylabel('Valores y Predicciones')
    plt.legend()
    plt.grid()
    plt.show()

    
df = pd.DataFrame(parametros)

df.to_csv("parametros_modelo_precios_mediana.csv")
