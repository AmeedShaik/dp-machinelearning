import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np

# Title of the app
st.title("Stock Price Prediction Application")
# Sidebar for user input
st.sidebar.header("Stock Prediction Settings")
# Select stock ticker
stock_ticker = st.sidebar.text_input("Enter Stock Ticker (e.g., AAPL, TSLA, INFY.BO)", value="YESBANK.NS")
# Select date range
start_date = st.sidebar.date_input("Start Date", value=pd.to_datetime("2015-01-01"))
end_date = st.sidebar.date_input("End Date", value=pd.to_datetime("2023-01-01"))
# Load the model
@st.cache(allow_output_mutation=True)
def load_lstm_model():
