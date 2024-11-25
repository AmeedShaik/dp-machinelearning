import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt

# Title of the app
st.title("Stock Price Prediction App")

# Sidebar for user input
st.sidebar.header("Stock Prediction Settings")

# Select stock ticker
stock_ticker = st.sidebar.text_input("Enter Stock Ticker (e.g., AAPL, TSLA, INFY.BO)", value="AAPL")

# Select date range
start_date = st.sidebar.date_input("Start Date", value=pd.to_datetime("2015-01-01"))
end_date = st.sidebar.date_input("End Date", value=pd.to_datetime("2023-01-01"))

# Load the model
@st.cache(allow_output_mutation=True)
def load_lstm_model():
    return load_model("stock_prediction_lstm_h5")  # Make sure your trained model is in the same directory

model = load_lstm_model()

# Fetch stock data
if st.sidebar.button("Fetch Data"):
    try:
        # Download stock data
        data = yf.download(stock_ticker, start=start_date, end=end_date)
        st.subheader(f"Historical Data for {stock_ticker}")
        st.write(data.tail())

        # Plot historical prices
        st.subheader("Closing Price Trend")
        plt.figure(figsize=(10, 4))
        plt.plot(data['Close'], label="Closing Price")
        plt.title(f"{stock_ticker} Closing Price")
        plt.xlabel("Date")
        plt.ylabel("Price")
        plt.legend()
        st.pyplot(plt)
    except Exception as e:
        st.error(f"Error fetching data: {e}")

# Preprocess data and predict future stock prices
if st.sidebar.button("Predict Stock Prices"):
    try:
        # Preprocess data
        scaler = MinMaxScaler(feature_range=(0, 1))
        data_close = data['Close'].values.reshape(-1, 1)
        scaled_data = scaler.fit_transform(data_close)

        # Create sequences for prediction
        time_step = 60
        X_input = scaled_data[-time_step:].reshape(1, time_step, 1)

        # Predict next price
        predicted_price = model.predict(X_input)
        predicted_price = scaler.inverse_transform(predicted_price)

        # Display prediction
        st.subheader("Predicted Stock Price")
        st.write(f"Predicted Closing Price for {stock_ticker}: ${predicted_price[0][0]:.2f}")
    except Exception as e:
        st.error(f"Error in prediction: {e}")
