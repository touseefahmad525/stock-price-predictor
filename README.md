# Stock Price Predictor

A full-stack stock price prediction project with a FastAPI backend, React frontend, and a simple machine learning pipeline using historical stock data from Yahoo Finance.

## Features

- Search for a stock symbol such as `AAPL`, `GOOGL`, `MSFT`, or `TSLA`
- Fetch recent market data with `yfinance`
- Train or load a scikit-learn model for prediction
- Display predicted stock price from the API
- Render stock chart data in the React frontend

## Tech Stack

- Backend: FastAPI, Uvicorn
- Frontend: React, Vite, Axios, Chart.js
- Machine Learning: pandas, NumPy, scikit-learn, joblib, yfinance
- Optional app: Streamlit

## Project Structure

```text
stock-price-predictor/
  backend/          FastAPI routes and services
  frontend/         React + Vite frontend
  ml/               Data fetching, preprocessing, and model training
  requirements.txt  Python dependencies
  model.pkl         Trained model file generated locally
```

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/stock-price-predictor.git
cd stock-price-predictor
```

### 2. Create a Python virtual environment

```bash
python -m venv .venv
```

On Windows:

```bash
.venv\Scripts\activate
```

On macOS/Linux:

```bash
source .venv/bin/activate
```

### 3. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 4. Install frontend dependencies

```bash
cd frontend
npm install
```

## Run the Project

### Start the backend

From the project root:

```bash
uvicorn backend.main:app --reload
```

The API runs at:

```text
http://127.0.0.1:8000
```

### Start the frontend

In a second terminal:

```bash
cd frontend
npm run dev
```

Open the local Vite URL shown in the terminal, usually:

```text
http://localhost:5173
```

### Optional: run the Streamlit app

```bash
streamlit run ml/app.py
```

## API Endpoints

```text
GET /predict/{stock_symbol}
GET /chart/{stock_symbol}
```

Example:

```text
http://127.0.0.1:8000/predict/AAPL
```

## Notes

- `model.pkl` is generated locally when the model is trained.
- `frontend/node_modules/`, `frontend/dist/`, Python cache files, and local environment files are ignored by Git.
- Stock data is fetched from Yahoo Finance, so results depend on network access and available market data.
