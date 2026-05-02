import { useState } from "react";

export default function StockInput({ onSearch }) {
  const [stock, setStock] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    onSearch(stock.trim().toUpperCase());
  };

  return (
    <form className="stock-search" onSubmit={handleSubmit}>
      <label className="stock-search__label" htmlFor="stock-symbol">
        Stock symbol
      </label>

      <div className="stock-search__control">
        <span className="stock-search__icon" aria-hidden="true">
          $
        </span>
        <input
          id="stock-symbol"
          className="stock-search__input"
          value={stock}
          onChange={(e) => setStock(e.target.value)}
          placeholder="AAPL, GOOGL, MSFT"
          autoComplete="off"
        />

        <button className="stock-search__button" type="submit">
          Search
        </button>
      </div>
    </form>
  );
}
