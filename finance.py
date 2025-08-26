import yfinance as yf

# Define the ticker symbol, e.g., Apple
ticker_symbol = "AAPL"

# Create a Ticker object
ticker = yf.Ticker(ticker_symbol)

# Fetch historical market data for the last year
historical_data = ticker.history(period="1y")

# Print the data (includes Open, High, Low, Close prices, Volume, Dividends, Splits)
print(historical_data)

