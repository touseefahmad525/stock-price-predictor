import numpy as np
from ml.model.load_model import load_model
from ml.data.fetch_data import get_stock_data
from ml.utils.preprocess import prepare_data
from ml.model.train_models import train_models


def run_prediction(stock_name="AAPL"):
    stock_name = stock_name.strip().upper()

    # fetch data
    data = get_stock_data(stock_name, period="1mo")

    if data.empty:
        raise ValueError(f"No stock data found for {stock_name}.")

    # preprocess
    X, y = prepare_data(data)

    if X.empty or y.empty:
        raise ValueError(f"Not enough stock data found for {stock_name}.")

    # ⚠️ check if model exists (optional safe training)
    try:
        model = load_model()
    except:
        model, _, _ = train_models(X, y)

    # prediction
    last_row = np.array(X.iloc[-1]).reshape(1, -1)
    prediction = model.predict(last_row)

    return {
        "stock": stock_name,
        "prediction": float(prediction.squeeze())
    }
