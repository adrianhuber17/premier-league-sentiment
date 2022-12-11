import { SentimentPlot } from "./components/SentimentPlot";
import { TotalTweetCountPlot } from "./components/TotalTweetCountPlot";

import "./App.css";
import Pong from "./components/Pong";
import { useEffect, useState } from "react";
import { TodaySentimentPlot } from "./components/TodaySentimentPlot";

function App() {
  const [count, setCount] = useState({});
  const [loadingCount, setLoadingCount] = useState(true);
  useEffect(() => {
    let url = `${process.env.REACT_APP_BACKEND_SERVICE_URL}/get-tweet-count`;
    fetch(url, { credentials: "include" })
      .then((response) => response.json())
      .then((responseData) => {
        setCount(responseData.message);
        setLoadingCount(false);
      });
  }, []);

  const [sentiment, setSentiment] = useState({});
  const [loading, setLoading] = useState(true);
  useEffect(() => {
    let url = `${process.env.REACT_APP_BACKEND_SERVICE_URL}/get-sentiment`;
    fetch(url, { credentials: "include" })
      .then((response) => response.json())
      .then((responseData) => {
        setSentiment(responseData.message);
        setLoading(false);
      });
  }, []);

  const [connection, setConnection] = useState("");
  const [loadingPing, setLoadingPing] = useState(true);

  useEffect(() => {
    let url = `${process.env.REACT_APP_BACKEND_SERVICE_URL}/ping`;
    fetch(url, { credentials: "include" })
      .then((response) => response.json())
      .then((responseData) => {
        if (responseData.status === "success") {
          setConnection(responseData.message);
          setLoadingPing(false);
        } else {
          setConnection("no connection to backend");
          setLoadingPing(false);
        }
      });
  }, []);
  return (
    <div className="App">
      <h1>Premier League Sentiment Dashboard</h1>
      <>
        {loadingPing === false && <Pong connection={connection} />}
        {loading === false && <SentimentPlot sentiment={sentiment} />}
        {loading === false && <TodaySentimentPlot sentiment={sentiment} />}
        {loadingCount === false && <TotalTweetCountPlot count={count} />}
      </>
    </div>
  );
}

export default App;
