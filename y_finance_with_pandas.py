import yfinance as yf
import pandas as pd

# Download historical stock data for Apple from Yahoo Finance
df = yf.download("AAPL", start="2023-01-01", end="2023-08-20")

# The returned object "df" is already a pandas DataFrame
print(df.head())

# You can access just one column, e.g., the closing prices
close_prices = df['Close']
print(close_prices.head())