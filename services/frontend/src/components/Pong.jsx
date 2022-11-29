import { useEffect, useState } from "react";

export default function Pong() {
  //function to test connection to backend
  const [connection, setConnection] = useState("");
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    let url = `${process.env.REACT_APP_BACKEND_SERVICE_URL}/ping`;
    fetch(url, { credentials: "include" })
      .then((response) => response.json())
      .then((responseData) => {
        console.log(responseData);
        if (responseData.status === "success") {
          setConnection(responseData.message);
          setLoading(false);
        } else {
          setConnection("no connection to backend");
          setLoading(false);
        }
      });
  }, []);
  return (
    loading === false && (
      <div>
        <h2>Pinging Backend: {connection}</h2>
      </div>
    )
  );
}
