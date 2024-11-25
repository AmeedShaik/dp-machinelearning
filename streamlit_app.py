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
