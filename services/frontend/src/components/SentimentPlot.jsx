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
  scales: {
    y: {
      min: 0,
      max: 100,
    },
  },
  responsive: true,
  aspectRatio: 1,
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
  const sentimentData = sentiment[0];
  const dates = sentiment[1].reverse();
  console.log(dates);
  const datasets = [];
  Object.keys(sentimentData).forEach(function (key) {
    const datasetsObj = {};
    datasetsObj["label"] = key;
    const reverseSentimenArr = sentimentData[key].reverse();
    datasetsObj["data"] = reverseSentimenArr;
    datasetsObj["lineTension"] = 0.1;
    datasetsObj["borderColor"] = teamBorderColors[key];
    datasetsObj["backgroundColor"] = teamBackgroundColors[key];

    datasets.push(datasetsObj);
  });
  const labels = [];
  dates.map((date) => {
    const testDateTime = new Date(date);
    const month = testDateTime.getUTCMonth();
    const day = testDateTime.getUTCDate();
    const year = testDateTime.getFullYear();
    labels.push(month + "/" + day + "/" + year);
    return labels;
  });

  const data = {
    labels,
    datasets,
  };

  return <Line options={options} data={data} />;
}
