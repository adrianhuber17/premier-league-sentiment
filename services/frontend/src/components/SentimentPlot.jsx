import React from "react";
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
} from "chart.js";
import { Line } from "react-chartjs-2";
import { faker } from "@faker-js/faker";

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
);

export const options = {
  responsive: true,
  plugins: {
    legend: {
      position: "top",
    },
    title: {
      display: true,
      text: "Premier League Sentiment",
    },
  },
};

export function SentimentPlot({ sentiment }) {
  //labels need to be dynamic for the current day minus the 7 previous days
  const labels = [
    "November",
    "December",
    "January",
    "February",
    "March",
    "April",
    "May",
  ];
  const data = {
    labels,
    datasets: [
      {
        label: "Arsenal FC",
        lineTension: 0.1,
        data: labels.map(() =>
          faker.datatype.number({ min: -1000, max: 1000 })
        ),
        borderColor: "rgb(255, 99, 132)",
        backgroundColor: "rgba(255, 99, 132, 0.5)",
      },
      {
        label: "Chelsea FC",
        lineTension: 0.1,
        data: labels.map(() =>
          faker.datatype.number({ min: -1000, max: 1000 })
        ),
        borderColor: "rgb(53, 162, 235)",
        backgroundColor: "rgba(53, 162, 235, 0.5)",
      },
    ],
  };
  console.log(sentiment);
  return <Line options={options} data={data} />;
}
