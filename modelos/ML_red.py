import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
import warnings
warnings.filterwarnings("ignore")

# Leer los datos
New_York_City_median_price_gb_BOROUGH = pd.read_csv("gcp/New_York/New_York_City_median_price_gb_BOROUGH.csv")
New_York_City_median_price_gb_BOROUGH['Time'] = pd.to_datetime(New_York_City_median_price_gb_BOROUGH['Time'], format='%d-%m-%Y')
New_York_City_median_price_gb_BOROUGH['Time'] = (New_York_City_median_price_gb_BOROUGH['Time'] - New_York_City_median_price_gb_BOROUGH['Time'].min()).dt.days

# Eliminar filas con valores nulos
New_York_City_median_price_gb_BOROUGH.dropna(inplace=True)

# Dividir los datos en características (X) y etiquetas (Y)
X = New_York_City_median_price_gb_BOROUGH[['Time']]
Y = New_York_City_median_price_gb_BOROUGH['Bronx']

# Escalar las características
scaler = MinMaxScaler()
X = scaler.fit_transform(X)

# Dividir los datos en conjuntos de entrenamiento y prueba
split_ratio = 0.8
split_index = int(len(X) * split_ratio)

X_train = X[:split_index] 
Y_train = Y[:split_index]
X_test = X[split_index:]
Y_test = Y[split_index:]

# Crear el modelo LSTM
model = Sequential()
model.add(LSTM(50, activation='relu', input_shape=(X_train.shape[1], 1)))
model.add(Dense(1))
model.compile(optimizer='adam', loss='mean_squared_error')

# Entrenar el modelo
model.fit(X_train, Y_train, epochs=100, batch_size=32, verbose=1)

# Evaluar el modelo en el conjunto de prueba
Y_pred = model.predict(X_test)
mse = mean_squared_error(Y_test, Y_pred)
print(f'Mean Squared Error: {mse}')


