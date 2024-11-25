import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow import load_model
import matplotlib as plt

# Title of the app
st.title("Stock Price Prediction Application")
