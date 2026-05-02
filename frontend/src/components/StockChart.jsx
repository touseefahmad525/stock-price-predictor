import {
  Chart as ChartJS,
  LineElement,
  CategoryScale,
  LinearScale,
  PointElement,
} from "chart.js";

import { Line } from "react-chartjs-2";

ChartJS.register(LineElement, CategoryScale, LinearScale, PointElement);

export default function StockChart({ data }) {
  const chartData = {
    labels: data.map((d) => d.date),
    datasets: [
      {
        label: "Close Price",
        data: data.map((d) => d.close),
        borderColor: "blue",
        fill: false,
      },
    ],
  };

  return <Line data={chartData} />;
}