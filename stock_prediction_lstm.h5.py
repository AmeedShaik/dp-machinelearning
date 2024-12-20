import yfinance as yf
import pandas as pd

# Download stock data
ticker = "YESBANK.NS"  # Replace with desired stock ticker
df = yf.download(ticker, start="2015-01-01", end="2024-01-01")
df = df[['Close']]  # We'll use the 'Close' price for prediction
df.head()

from sklearn

scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(df)

# Visualize normalized data
import matplotlib.pyplot as plt
plt.plot(scaled_data)
plt.title("Normalized Stock Price")
plt.show()



import numpy as np

def create_sequences(data, time_step=60):
    X, y = [], []
    for i in range(len(data) - time_step):
        X.append(data[i:i+time_step, 0])
        y.append(data[i+time_step, 0])
    return np.array(X), np.array(y)

time_step = 60
X, y = create_sequences(scaled_data, time_step)

# Reshape input for LSTM
X = X.reshape((X.shape[0], X.shape[1], 1))

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout

model = Sequential([
    LSTM(50, return_sequences=True, input_shape=(X.shape[1], 1)),
    Dropout(0.2),
    LSTM(50, return_sequences=False),
    Dropout(0.2),
    Dense(25),
    Dense(1)  # Final layer to predict stock price
])

model.compile(optimizer='adam', loss='mean_squared_error')
model.summary()

split = int(len(X) * 0.8)
X_train, X_test = X[:split], X[split:]
y_train, y_test = y[:split], y[split:]

history = model.fit(X_train, y_train, batch_size=64, epochs=50, validation_data=(X_test, y_test), verbose=1)

predictions = model.predict(X_test)
predictions = scaler.inverse_transform(predictions.reshape(-1, 1))  # Rescale to original
y_test_actual = scaler.inverse_transform(y_test.reshape(-1, 1))

from sklearn.metrics import mean_squared_error

rmse = np.sqrt(mean_squared_error(y_test_actual, predictions))
print("Root Mean Squared Error:", rmse)

plt.figure(figsize=(12, 6))
plt.plot(y_test_actual, label="Actual Prices")
plt.plot(predictions, label="Predicted Prices")
plt.title("Stock Price Prediction")
plt.xlabel("Time")
plt.ylabel("Price")
plt.legend()
plt.show()
