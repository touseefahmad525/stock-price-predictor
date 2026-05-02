import axios from "axios";

// backend base URL
const BASE_URL = "http://127.0.0.1:8000";

// get prediction
export const getPrediction = async (stock) => {
  const res = await axios.get(`${BASE_URL}/predict/${stock}`);
  return res.data;
};

// get chart data
export const getChart = async (stock) => {
  const res = await axios.get(`${BASE_URL}/chart/${stock}`);
  return res.data;
};