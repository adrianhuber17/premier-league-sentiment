import { Chart as ChartJS, ArcElement, Tooltip, Legend } from "chart.js";
import { Doughnut } from "react-chartjs-2";

ChartJS.register(ArcElement, Tooltip, Legend);

export const options = {
  responsive: true,
  plugins: {
    title: {
      display: true,
      text: "Premier League Team Tweet 7 Day Tweet Count",
    },
  },
};
export const data = {
  labels: ["Red", "Blue", "Yellow", "Green", "Purple", "Orange"],
  datasets: [
    {
      label: "# of Votes",
      data: [12, 19, 3, 5, 2, 3],
      backgroundColor: [
        "rgba(255, 99, 132, 0.2)",
        "rgba(54, 162, 235, 0.2)",
        "rgba(255, 206, 86, 0.2)",
        "rgba(75, 192, 192, 0.2)",
        "rgba(153, 102, 255, 0.2)",
        "rgba(255, 159, 64, 0.2)",
      ],
      borderColor: [
        "rgba(255, 99, 132, 1)",
        "rgba(54, 162, 235, 1)",
        "rgba(255, 206, 86, 1)",
        "rgba(75, 192, 192, 1)",
        "rgba(153, 102, 255, 1)",
        "rgba(255, 159, 64, 1)",
      ],
      borderWidth: 1,
    },
  ],
};
//TODO: populate dougnut plot with incoming tweet count information
//need to deconstruct and construct the data object for the plot
export function TotalTweetCountPlot({ count }) {
  const currDate = count.curr_date;
  const startDate = count.start_date;
  const teamTweetCount = count.tweet_count;
  console.log(currDate);
  console.log(startDate);
  console.log(teamTweetCount);

  // const teamBorderColors = {
  //   chelsea: "rgba(3, 70, 148,1)",
  //   "manchester city": "rgba(108, 171, 221,1)",
  //   arsenal: "rgba(239, 1, 7,1)",
  //   "aston villa": "rgba(149,191,229,1)",
  //   bournemouth: "rgba(218, 41, 28,1)",
  //   brighton: "rgba(0, 87, 184,1)",
  //   "crystal palace": "rgba(27, 69, 143,1)",
  //   everton: "rgba(39,68,136,1)",
  //   fulham: "rgba(0, 0, 0,1)",
  //   "leeds united": "rgba(255,205,0,1)",
  //   "leicester city": "rgba(0,83,160,1)",
  //   liverpool: "rgba(200, 16, 46,1)",
  //   "manchester united": "rgba(218, 41, 28,1)",
  //   newcastle: "rgba(45, 41, 38,1)",
  //   "nottingham forest": "rgba(229, 50, 51,1)",
  //   southampton: "rgba(215, 25, 32,1)",
  //   tottenham: "rgba(19, 34, 87,1)",
  //   "west ham": "rgba(122, 38, 58,1)",
  //   wolverhampton: "rgba(253,185,19,1)",
  //   brentford: "rgb(239, 1, 7,1)",
  // };
  // const teamBackgroundColors = {
  //   "manchester united": "rgba(218, 41, 28,0.2)",
  //   chelsea: "rgba(3, 70, 148, 0.2)",
  //   "manchester city": "rgba(108, 171, 221,0.2)",
  //   arsenal: "rgba(239, 1, 7,0.2)",
  //   "aston villa": "rgba(149,191,229,0.2)",
  //   bournemouth: "rgba(218, 41, 28,0.2)",
  //   brighton: "rgba(0, 87, 184,0.2)",
  //   "crystal palace": "rgba(27, 69, 143,0.2)",
  //   everton: "rgba(39,68,136,0.2)",
  //   fulham: "rgba(0, 0, 0,0.2)",
  //   "leeds united": "rgba(255,205,0,0.2)",
  //   "leicester city": "rgba(0,83,160,0.2)",
  //   liverpool: "rgba(200, 16, 46,0.2)",
  //   newcastle: "rgba(45, 41, 38,0.2)",
  //   "nottingham forest": "rgba(229, 50, 51,0.2)",
  //   southampton: "rgba(215, 25, 32,0.2)",
  //   tottenham: "rgba(19, 34, 87,0.2)",
  //   "west ham": "rgba(122, 38, 58,0.2)",
  //   wolverhampton: "rgba(253,185,19,0.2)",
  //   brentford: "rgb(239, 1, 7,0.2)",
  // };
  // const datasets = [];
  // teamTweetCount.map((tweetCount) => {
  //   const datasetsObj = {}
  //   const team = tweetCount[0];
  //   const count = tweetCount[1];
  //   datasetsObj["data"] = count
  //   datasets.push(datasetsObj);
  // });

  // const data = {
  //   labels,
  //   datasets,
  // };

  return <Doughnut data={data} options={options} />;
}
