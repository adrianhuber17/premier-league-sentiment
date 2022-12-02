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
// import { faker } from "@faker-js/faker";

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
  const teamBorderColors = {
    chelsea: "rgba(3, 70, 148)",
    "manchester city": "rgba(108, 171, 221)",
    arsenal: "rgba(239, 1, 7)",
    "aston villa": "rgba(149,191,229)",
    bournemouth: "rgba(218, 41, 28)",
    brighton: "rgba(0, 87, 184)",
    "crystal palace": "rgba(27, 69, 143)",
    everton: "rgba(39,68,136)",
    fulham: "rgba(0, 0, 0)",
    "leeds united": "rgba(255,205,0)",
    "leicester city": "rgba(0,83,160)",
    liverpool: "rgba(200, 16, 46)",
    "manchester united": "rgba(218, 41, 28)",
    newcastle: "rgba(45, 41, 38)",
    "nottingham forest": "rgba(229, 50, 51)",
    southampton: "rgba(215, 25, 32)",
    tottenham: "rgba(19, 34, 87)",
    "west ham": "rgba(122, 38, 58)",
    wolverhampton: "rgba(253,185,19)",
    brentford: "rgb(239, 1, 7)",
  };
  const teamBackgroundColors = {
    "manchester united": "rgba(218, 41, 28,0.5)",
    chelsea: "rgba(3, 70, 148, 0.5)",
    "manchester city": "rgba(108, 171, 221,0.5)",
    arsenal: "rgba(239, 1, 7,0.5)",
    "aston villa": "rgba(149,191,229,0.5)",
    bournemouth: "rgba(218, 41, 28,0.5)",
    brighton: "rgba(0, 87, 184,0.5)",
    "crystal palace": "rgba(27, 69, 143,0.5)",
    everton: "rgba(39,68,136,0.5)",
    fulham: "rgba(0, 0, 0,0.5)",
    "leeds united": "rgba(255,205,0,0.5)",
    "leicester city": "rgba(0,83,160,0.5)",
    liverpool: "rgba(200, 16, 46,0.5)",
    newcastle: "rgba(45, 41, 38,0.5)",
    "nottingham forest": "rgba(229, 50, 51,0.5)",
    southampton: "rgba(215, 25, 32,0.5)",
    tottenham: "rgba(19, 34, 87,0.5)",
    "west ham": "rgba(122, 38, 58,0.5)",
    wolverhampton: "rgba(253,185,19,0.5)",
    brentford: "rgb(239, 1, 7,0.5)",
  };

  const datasets = [];
  Object.keys(sentiment).forEach(function (key) {
    //   console.log(key);
    //   console.log(teams[key]);
    const datasetsObj = {};
    datasetsObj["label"] = key;
    datasetsObj["data"] = sentiment[key];
    datasetsObj["lineTension"] = 0.1;
    if (key in teamBorderColors) {
      datasetsObj["borderColor"] = teamBorderColors[key];
    } else {
      datasetsObj["borderColor"] = "rgb(255, 99, 132)";
    }
    if (key in teamBackgroundColors) {
      datasetsObj["backgroundColor"] = teamBackgroundColors[key];
    } else {
      datasetsObj["backgroundColor"] = "rgba(255, 99, 132, 0.5)";
    }
    datasets.push(datasetsObj);
  });
  const labels = ["11/29/2022", "11/30/2022", "11/31/2022", "12/01/2022"];
  const data = {
    labels,
    datasets,
  };

  console.log(sentiment);
  return <Line options={options} data={data} />;
}
