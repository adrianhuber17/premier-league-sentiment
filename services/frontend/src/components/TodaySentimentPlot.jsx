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
// import { faker } from "@faker-js/faker";

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
      text: "Chart.js Horizontal Bar Chart",
    },
    scales: {
      x: {
        stacked: true,
        min: 0,
        max: 100,
      },
      y: {
        stacked: true,
      },
    },
  },
};

export function TodaySentimentPlot({ sentiment }) {
  const sentimentData = sentiment[0];
  const labels = [];
  const teamLatestSentiment = [];
  Object.keys(sentimentData).forEach(function (key) {
    labels.push(key);
    teamLatestSentiment.push(sentimentData[key].at(-1));
  });
  const data = {
    labels,
    datasets: [
      {
        label: "Dataset 1",
        data: teamLatestSentiment,
        borderColor: "rgb(53, 162, 235)",
        backgroundColor: "rgba(53, 162, 235, 0.5)",
      },
      //   {
      //     label: "Dataset 2",
      //     data: labels.map(() => faker.datatype.number({ min: 0, max: 100 })),
      //     borderColor: "rgb(255, 99, 132)",
      //     backgroundColor: "rgba(255, 99, 132, 0.5)",
      //   },
    ],
  };

  return <Bar options={options} data={data} />;
}
