import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
from scipy.optimize import curve_fit

import warnings
warnings.filterwarnings("ignore")

# Leer los datos
New_York_City_median_price_gb_BOROUGH = pd.read_csv("gcp/New_York/New_York_City_median_price_gb_BOROUGH.csv")
New_York_City_median_price_gb_BOROUGH['Time'] = pd.to_datetime(New_York_City_median_price_gb_BOROUGH['Time'], format='%d-%m-%Y')
New_York_City_median_price_gb_BOROUGH['Time'] = (New_York_City_median_price_gb_BOROUGH['Time'] - New_York_City_median_price_gb_BOROUGH['Time'].min()).dt.days

# Eliminar filas con valores nulos
New_York_City_median_price_gb_BOROUGH.dropna(inplace=True)


X = New_York_City_median_price_gb_BOROUGH[['Time']] 
Y = New_York_City_median_price_gb_BOROUGH['Bronx'] 

X_train = X.iloc[:int(len(X)*0.8)]  
Y_train = Y.iloc[:int(len(X)*0.8)]
X_test = X.iloc[int(len(X)*0.8):]
Y_test = Y.iloc[int(len(X)*0.8):]

# Definir una función seno para ajustar
def sin_func(x, A, B,C,D,E):
    return A * np.sin(B*x) + C*(x**2) + D*x + E

# Ajustar la función seno a los datos
params, params_covariance = curve_fit(sin_func, X_train.values.flatten(), Y_train)

# Parámetros ajustados
A, B,C,D,E= params

# Realizar predicciones en el conjunto de prueba
Y_pred = sin_func(X_test, A, B,C,D,E)

# Calcular el error cuadrático medio en el conjunto de prueba
mse = mean_squared_error(Y_train, sin_func(X_train.values.flatten(),A, B,C,D,E))
print("Mean Squared Error:", mse)

from sklearn.metrics import r2_score

# Calcular el coeficiente de determinación R^2 en el conjunto de prueba
r2 = r2_score(Y_test, Y_pred)
print("R^2 Score:", r2)


