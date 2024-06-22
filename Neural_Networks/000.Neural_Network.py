import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split


# SPIEGAZIONE DELL'ESEMPIO


#############################################################################################
#############################################################################################
####  DATASET

# Apriamo il dataset (supponiamo di aver già montato gdrive su colab)
datadir = datadir + 'Neural_Networks/'
file_path = datadir +'Esempio_1.csv'
df = pd.read_csv(file_path)

# Plottiamo i grafici delle variabili
features = ['X1','X2', 'X3']  ## Sono i nomi delle colonne del dataset
titles = ['Variabile 1', 'Variabile 2','Variabile 3']
plt.figure(figsize=(12,10))
for i, feature in enumerate(features):
    plt.subplot(2, 2, i + 1)
    plt.scatter(df[feature], df['Y'], s = 1, color = 'k')
    plt.title(titles[i]); plt.ylabel('Variabile Y')
plt.tight_layout(); plt.show()


#############################################################################################
#############################################################################################
####  MODELLO

# Creiamo i vettori dei dati
X = df[['X1', 'X2', 'X3']].values
y = df['Y'].values 

# Splittiamo i dati in 3 insiemi (train, cross-validation e test)
X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.4, random_state=42)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

# Creazione del modello
model = Sequential([
Dense(units = 20, input_shape=(X_train.shape[1],), activation='relu'),
Dense(units = 10, activation='relu'),
Dense(units = 1,  activation='linear')])
# Negli hidden layer si usa relu activation functuion mentre nell'output
# layer si usa linear activation function; può cambiare a seconda del problema

# Compilazione del modello
model.compile(optimizer='adam', loss='mse', metrics=['mae'])
# Ottimizzazione = Adam
# Funzione di perdita dell'errore quadratico medio (MSE)
# Metrica MAE (Mean Absolute Error) per monitorare le prestazioni

# Addestramento del modello
model.fit(X_train, y_train, epochs=100, batch_size=32, validation_split=0.2)
# epochs = numero di iterazioni
# batch_size = numero di campioni da utilizzare per aggiornare i pesi del modello durante l'addestramento

# Valutazione del modello sul set di test
loss, mae = model.evaluate(X_test, y_test)
print(f'Loss: {loss}, MAE: {mae}')

# Previsione con il modello
predictions = model.predict(X_test)

# Plottaggio delle previsioni rispetto ai valori reali
plt.figure(figsize=(8, 6))
plt.scatter(y_test, predictions, s=5, color='blue')
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red')
plt.title('Confronto tra Valori Reali e Predetti'); plt.xlabel('Valori Reali')
plt.ylabel('Valori Predetti'); plt.show()

# Stampa alcune previsioni
for i in range(5):
    print(f'Valore Reale: {y_test[i]}, Valore Predetto: {predictions[i]}')







