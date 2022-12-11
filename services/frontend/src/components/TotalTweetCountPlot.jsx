import { Chart as ChartJS, ArcElement, Tooltip, Legend } from "chart.js";
import { Doughnut } from "react-chartjs-2";

ChartJS.register(ArcElement, Tooltip, Legend);

export function TotalTweetCountPlot({ count }) {
  const currDate = count.curr_date;
  const startDate = count.start_date;
  const teamTweetCount = count.tweet_count;

  const currDateTime = new Date(currDate);
  const currMonth = currDateTime.getUTCMonth();
  const currDay = currDateTime.getUTCDate();

  const startDateTime = new Date(startDate);
  const startMonth = startDateTime.getUTCMonth();
  const startDay = startDateTime.getUTCDate();

  const options = {
    responsive: true,
    aspectRatio: 1.3,
    plugins: {
      title: {
        display: true,
        text: `Premier League Tweet Count from ${startMonth}/${startDay} to ${currMonth}/${currDay}`,
      },
    },
  };

  const data = {
    labels: [],
    datasets: [
      {
        label: "# of tweets",
        data: [],
        backgroundColor: [],
        borderColor: [],
        borderWidth: 1,
      },
    ],
  };

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

  teamTweetCount.map((tweetCount) => {
    const team = tweetCount[0];
    const count = tweetCount[1];
    data.labels.push(team);
    data.datasets[0].data.push(count);
    data.datasets[0].backgroundColor.push(teamBackgroundColors[team]);
    data.datasets[0].borderColor.push(teamBorderColors[team]);
    return data;
  });

  return <Doughnut data={data} options={options} />;
}
