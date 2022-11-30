// import { useEffect, useState } from "react";

export default function Pong({ connection }) {
  console.log(connection);
  return (
    <div className="ping">
      <h2>Pinging Backend: </h2>
      <h2 className="conn-status">{connection}</h2>
    </div>
  );
}
