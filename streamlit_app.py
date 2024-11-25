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
stock_ticker = st.sidebar.text_input("Enter Stock Ticker (e.g., AAPL, TSLA, INFY.BO)", value="YESBANK.NS")

# Select date range
start_date = st.sidebar.date_input("Start Date", value=pd.to_datetime("2015-01-01"))
end_date = st.sidebar.date_input("End Date", value=pd.to_datetime("2023-01-01"))
