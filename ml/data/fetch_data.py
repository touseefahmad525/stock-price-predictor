import yfinance as yf
from ml.data.yfinance_config import configure_yfinance_cache

def get_stock_data(stock="AAPL", period="1mo"):
    """
    Fetch stock data from Yahoo Finance
    """
    configure_yfinance_cache()
    data = yf.download(stock, period=period)
    return data
