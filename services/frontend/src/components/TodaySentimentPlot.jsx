import React from "react";
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend,
} from "chart.js";
import { Bar } from "react-chartjs-2";

ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
);

export const options = {
  indexAxis: "y",
  elements: {
    bar: {
      borderWidth: 2,
    },
  },
  responsive: true,
  plugins: {
    legend: {
      position: "right",
    },
    title: {
      display: true,
      text: "Today's Team Sentiment",
    },
    scales: {
      x: [
        {
          stacked: true,
          min: 0,
          max: 100,
        },
      ],
      y: [
        {
          stacked: true,
        },
      ],
    },
  },
};

export function TodaySentimentPlot({ sentiment }) {
  const sentimentData = sentiment[0];
  const labels = [];
  const teamLatestPosSentiment = [];
  const teamLatestNegSentiment = [];
  Object.keys(sentimentData).forEach(function (key) {
    labels.push(key);
    const posSentiment = sentimentData[key].at(-1);
    teamLatestPosSentiment.push(posSentiment);
    teamLatestNegSentiment.push(100 - posSentiment);
  });
  const data = {
    labels,
    datasets: [
      {
        stack: "stack",
        label: "Positive Sentiment",
        data: teamLatestPosSentiment,
        borderColor: "rgb(53, 162, 235)",
        backgroundColor: "rgba(53, 162, 235, 0.5)",
      },
      {
        stack: "stack",
        label: "Negative Sentiment",
        data: teamLatestNegSentiment,
        borderColor: "rgb(255, 99, 132)",
        backgroundColor: "rgba(255, 99, 132, 0.5)",
      },
    ],
  };

  return <Bar options={options} data={data} />;
}
