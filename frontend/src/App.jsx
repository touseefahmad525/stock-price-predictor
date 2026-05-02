import { useState } from "react";
import StockInput from "./components/StockInput";
import StockChart from "./components/StockChart";
import { getPrediction, getChart } from "./api/stockApi";
import "./App.css";

function App() {
  const [prediction, setPrediction] = useState(null);
  const [chart, setChart] = useState([]);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSearch = async (stock) => {
    const symbol = stock.trim().toUpperCase();

    if (!symbol) {
      setError("Please enter a stock symbol.");
      setPrediction(null);
      setChart([]);
      return;
    }

    setLoading(true);
    setError("");
    setPrediction(null);
    setChart([]);

    try {
      const pred = await getPrediction(symbol);
      setPrediction(pred);

      const chartData = await getChart(symbol);
      setChart(chartData.data || []);
    } catch (err) {
      const message =
        err.response?.data?.detail ||
        err.message ||
        "Could not load stock data.";
      setError(message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>📈 Stock Price Predictor</h1>

      <StockInput onSearch={handleSearch} />

      {loading && <p>Loading...</p>}

      {error && <p style={{ color: "crimson" }}>{error}</p>}

      {prediction && (
        <div>
          <h3>
            {prediction.stock} Prediction: {prediction.prediction.toFixed(2)}
          </h3>
        </div>
      )}

      {chart.length > 0 && <StockChart data={chart} />}
    </div>
  );
}

export default App;
