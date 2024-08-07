import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Dashboard from './components/Dashboard';
import CellDetails from './components/CellDetails';

const App = () => {
  const [cells, setCells] = useState([]);
  const [selectedCell, setSelectedCell] = useState(null);

  useEffect(() => {
    axios.get('/api/cells').then(response => setCells(response.data));
  }, []);

  const handleCellSelect = (cellId) => {
    axios.get(`/api/cells/${cellId}`).then(response => setSelectedCell(response.data));
  };

  return (
    <div>
      <Dashboard cells={cells} onSelect={handleCellSelect} />
      {selectedCell && <CellDetails cell={selectedCell} />}
    </div>
  );
};

export default App;
