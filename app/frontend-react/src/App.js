import { useEffect, useState } from "react";

function App() {
  const [locations, setLocations] = useState([]);
  const [name, setName] = useState("");
  const [location, setLocation] = useState("");

  useEffect(() => {
    fetch("/api/locations")
      .then(res => res.json())
      .then(setLocations);
  }, []);

  const book = () => {
    fetch(`/api/order?name=${name}&location=${location}`, { method: "POST" });
  };

  return (
    <div>
      <h1>Gas Booking</h1>

      <input placeholder="Name" onChange={e => setName(e.target.value)} />

      <select onChange={e => setLocation(e.target.value)}>
        {locations.map(l => <option key={l}>{l}</option>)}
      </select>

      <button onClick={book}>Book</button>
    </div>
  );
}

export default App;
