import yfinance as yf
import pandas as pd
from ml.data.yfinance_config import configure_yfinance_cache


def get_stock_chart(stock_name="AAPL", period="1mo"):
    """
    Robust stock chart API (handles all yfinance formats)
    """
    stock_name = stock_name.strip().upper()
    configure_yfinance_cache()

    data = yf.download(stock_name, period=period)

    if data.empty:
        raise ValueError(f"No stock data found for {stock_name}.")

    # reset index (Date becomes column)
    data = data.reset_index()

    # 🔥 FIX 1: handle MultiIndex columns (yfinance issue)
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)

    # 🔥 FIX 2: ensure clean column names
    data.columns = [str(col).lower() for col in data.columns]

    # 🔥 FIX 3: ensure date exists
    if "date" not in data.columns:
        # fallback: sometimes it's "index"
        data.rename(columns={data.columns[0]: "date"}, inplace=True)

    # 🔥 FIX 4: format date safely
    data["date"] = pd.to_datetime(data["date"]).dt.strftime("%Y-%m-%d")

    # final clean dataset
    result = data[["date", "open", "high", "low", "close", "volume"]]

    return result.to_dict(orient="records")
