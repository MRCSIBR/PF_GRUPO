import pandas as pd
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

# Cargar el DataFrame y convertir 'Time' a un valor numérico (como lo hicimos anteriormente)
New_York_City_median_price_gb_BOROUGH = pd.read_csv("gcp/New_York/New_York_City_median_price_gb_BOROUGH.csv")
New_York_City_median_price_gb_BOROUGH['Time'] = pd.to_datetime(New_York_City_median_price_gb_BOROUGH['Time'], format='%d-%m-%Y')
New_York_City_median_price_gb_BOROUGH['Time'] = (New_York_City_median_price_gb_BOROUGH['Time'] - New_York_City_median_price_gb_BOROUGH['Time'].min()).dt.days

# Eliminar filas con valores faltantes
New_York_City_median_price_gb_BOROUGH.dropna(inplace=True)

# Ordenar los datos por fecha (si aún no están ordenados)
New_York_City_median_price_gb_BOROUGH.sort_values(by='Time', inplace=True)

# Definir las características (features) y el objetivo (target)
X = New_York_City_median_price_gb_BOROUGH[['Time']]  # Usamos 'Time' como característica
Y = New_York_City_median_price_gb_BOROUGH['Bronx']  # 'Bronx' es el precio de las casas en el Bronx

# Aplicar PolynomialFeatures para crear características polinómicas de grado 2
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

# Dividir los datos en conjuntos de entrenamiento y prueba
split_ratio = 0.8
split_index = int(len(X) * split_ratio)

X_train = X_poly[:split_index]
Y_train = Y[:split_index]
X_test = X_poly[split_index:]
Y_test = Y[split_index:]

# Crear y ajustar el modelo de regresión lineal
regression_model = LinearRegression()
regression_model.fit(X_train, Y_train)

# Realizar predicciones en el conjunto de prueba
Y_pred = regression_model.predict(X_test)

# Calcular R² y MSE para evaluar el rendimiento del modelo
r_squared = r2_score(Y_test, Y_pred)
mse = mean_squared_error(Y_test, Y_pred)

print(f"Coeficiente de determinación (R²): {r_squared}")
print(f"Error cuadrático medio (MSE): {mse}")
