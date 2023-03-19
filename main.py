import ccxt
import pandas as pd

# Initialize the TradingView API client
tv = ccxt.tradingview()

# Get the list of symbols in your watchlist
watchlist = "My Watchlist"
watchlist_symbols = tv.fetch_watchlist_symbols(watchlist)

# Get the OHLCV data for a specific symbol
symbol = "AAPL"   # Replace with the actual symbol you want to fetch data for
interval = "1w"   # Replace with the actual interval you want to fetch data for
data = tv.fetch_ohlcv(symbol=symbol, timeframe=interval)

# Convert the data to a pandas dataframe
df = pd.DataFrame(data, columns=["timestamp", "open", "high", "low", "close", "volume"])
df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
df.set_index("timestamp", inplace=True)

# Print the dataframe for verification
print(df.head())