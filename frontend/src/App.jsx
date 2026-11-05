import { useState, useEffect } from "react";

// import GardenList from "./components/GardenList";
import Drive_desk from "./components/Drive_desk";
// import AddPlant from "./components/AddP";

const API_URL = "http://127.0.0.1:8001";

function App() {
  const [plants, setPlants] = useState([]);
  const [rollNo, setRollNo] = useState(""); 

  function refreshAll() {
    fetch(API_URL + "/plants")
      .then((res) => res.json())
      .then((data) => setPlants(data));
  }                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             

useEffect(() => {
  refreshAll();
}, []);

  return (
   
    <div>
      <h1>Blood Donation Drive</h1>


      <input
        placeholder="Enter Roll No: AUXXX"
        value={rollNo}
        onChange={(e) => setRollNo(e.target.value)}
      />

     
      <Drive_desk rollNo={rollNo} />
    </div>
  );
}

export default App;