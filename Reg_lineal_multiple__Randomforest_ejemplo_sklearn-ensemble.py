# -*- coding: utf-8 -*-

import pandas as pd
#from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt

# Datos de ejemplo (puedes usar tu propio conjunto de datos)
# X: variables independientes (por ejemplo, horas de estudio, tiempo de sueño)
# y: variable dependiente (por ejemplo, puntaje del examen)
data = {
    'Horas_Estudio': [1, 2, 3, 4, 5],
    'Tiempo_Sueño': [7, 6, 5, 4, 3],
    'Edad': [22, 23, 21, 24, 25],
    'Puntaje_Examen': [60, 65, 70, 75, 80]
}

df = pd.DataFrame(data)

# X: Variables independientes (en este caso, horas de estudio, tiempo de sueño y edad)
X = df[['Horas_Estudio', 'Tiempo_Sueño', 'Edad']]

# y: Variable dependiente (puntaje de examen)
y = df['Puntaje_Examen']

# Crear el modelo de regresión lineal/Múltiple
#model = LinearRegression()

# Crear el modelo de Random Forest para regresión
model = RandomForestRegressor(n_estimators=5)#, random_state=123)

# Ajustar el modelo a los datos
model.fit(X, y)

# Ver los coeficientes (importancia de cada variable)
#coef = model.coef_
#intercept = model.intercept_

# Mostrar los coeficientes y la intersección
#print("Intercepto:", intercept)
#for i, col in enumerate(X.columns):
#    print(f"Coeficiente para {col}: {coef[i]}")

# Mostrar la importancia de las variables
importancia = model.feature_importances_
print("Importancia de las variables:")
for i, col in enumerate(X.columns):
    print(f"{col}: {importancia[i]}")

# Hacer predicciones
y_pred = model.predict(X)

# Graficar los resultados (para un análisis visual, aunque el modelo sea multivariado)
plt.plot(df['Horas_Estudio'], y, color='blue', label='Real')
plt.scatter(df['Horas_Estudio'], y_pred, color='red', label='Predicción')
plt.xlabel('Horas de Estudio')
plt.ylabel('Puntaje Examen')
#plt.title('Regresión Lineal Múltiple')
plt.title('Regresión con Random Forest')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.show()

plt.plot(df['Tiempo_Sueño'], y, color='blue', label='Real')
plt.scatter(df['Tiempo_Sueño'], y_pred, color='red', label='Predicción')
plt.xlabel('Tiempo_Sueño')
plt.ylabel('Puntaje Examen')
#plt.title('Regresión Lineal Múltiple')
plt.title('Regresión con Random Forest')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.show()


##############################################################################
############################### Predicción ###################################
##############################################################################

data_pred = {
    'Horas_Estudio': [5, 4, 7, 2, 3],
    'Tiempo_Sueño': [7, 8, 2, 5, 6],
    'Edad': [22, 23, 21, 24, 25]
}

# Convertir los datos de predicción en un DataFrame
df_pred = pd.DataFrame(data_pred)

# Realizar predicciones
predicciones = model.predict(df_pred)

# Mostrar las predicciones
print(predicciones)