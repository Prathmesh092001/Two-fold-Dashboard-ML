import React, { useEffect, useState } from 'react';
import Plot from 'react-plotly.js';
import axios from 'axios';

const CellDetails = ({ cell }) => {
  const [data, setData] = useState(null);

  useEffect(() => {
    // Fetch additional data for the selected cell
    axios.get(`/api/cells/${cell.id}/details`).then(response => setData(response.data));
  }, [cell]);

  return (
    <div>
      <h2>Cell {cell.id} Details</h2>
      {data && (
        <>
          <Plot data={[{ x: data.time, y: data.current, type: 'scatter', mode: 'lines+markers', marker: { color: 'red' } }]} layout={{ title: 'Current' }} />
          <Plot data={[{ x: data.time, y: data.voltage, type: 'scatter', mode: 'lines+markers', marker: { color: 'blue' } }]} layout={{ title: 'Voltage' }} />
          <Plot data={[{ x: data.time, y: data.capacity, type: 'scatter', mode: 'lines+markers', marker: { color: 'green' } }]} layout={{ title: 'Capacity' }} />
          <Plot data={[{ x: data.time, y: data.temperature, type: 'scatter', mode: 'lines+markers', marker: { color: 'orange' } }]} layout={{ title: 'Temperature' }} />
        </>
      )}
    </div>
  );
};

export default CellDetails;
