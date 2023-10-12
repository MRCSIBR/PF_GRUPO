import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

New_York_City_median_price_gb_BOROUGH = pd.read_csv("gcp/New_York/New_York_City_median_price_gb_BOROUGH.csv")
VNQ = pd.read_csv("gcp/New_York/VNQ.csv")
New_York_City_median_price_gb_BOROUGH['Time'] = pd.to_datetime(New_York_City_median_price_gb_BOROUGH['Time'], format='%d-%m-%Y')
New_York_City_median_price_gb_BOROUGH['Time'] = (New_York_City_median_price_gb_BOROUGH['Time'] - New_York_City_median_price_gb_BOROUGH['Time'].min()).dt.days

# Eliminar filas con valores faltantes
New_York_City_median_price_gb_BOROUGH.dropna(inplace=True)

X = New_York_City_median_price_gb_BOROUGH[['Time']] 
Y = New_York_City_median_price_gb_BOROUGH['Bronx'] 

X_train = X.iloc[:int(len(X)*0.8)]  
Y_train = Y.iloc[:int(len(X)*0.8)]
X_test = X.iloc[int(len(X)*0.8):]  
    
# Crear y ajustar el modelo de regresión lineal
regression_model = LinearRegression()
regression_model.fit(X_train, Y_train)


# Realizar la predicción para el próximo paso en el tiempo
Y_pred = regression_model.predict(X_test)

# Cargar los valores reales de la serie temporal (en este ejemplo, asumiendo que los tienes)
real_values = Y[int(len(X)*0.8):]

# Calcular R² y MSE
r_squared = r2_score(real_values, Y_pred)
mse = mean_squared_error(real_values, Y_pred)

print(f"Coeficiente de determinación (R²): {r_squared}")
print(f"Error cuadrático medio (MSE): {mse}")

