import { SentimentPlot } from "./components/SentimentPlot";

import "./App.css";
import Pong from "./components/Pong";
import { useEffect, useState } from "react";

function App() {
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
      </>
    </div>
  );
}

export default App;
