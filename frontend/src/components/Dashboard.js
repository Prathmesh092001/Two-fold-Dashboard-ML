import React from 'react';
import Plot from 'react-plotly.js';

const Dashboard = ({ cells, onSelect }) => {
  const pieData = cells.map(cell => ({
    values: [(cell.discharge_capacity / cell.nominal_capacity) * 100, 100 - (cell.discharge_capacity / cell.nominal_capacity) * 100],
    labels: ['SoH', 'Remaining'],
    type: 'pie',
    name: `Cell ${cell.id}`
  }));

  return (
    <div>
      {pieData.map((data, index) => (
        <div key={index}>
          <h3>Cell {cells[index].id}</h3>
          <Plot data={[data]} layout={{ title: `State of Health for Cell ${cells[index].id}` }} />
        </div>
      ))}
    </div>
  );
};

export default Dashboard;
