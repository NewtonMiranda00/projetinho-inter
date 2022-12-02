import React, { useEffect, useState } from 'react';
import { Line } from 'react-chartjs-2';


export function Home() {
  const [FSpace, setFSpace] = useState<{ x: number; y: number; }[]>([]);
  const [FSpeed, setFSpeed] = useState<{ x: number; y: number; }[]>([]);

  async function simulation() {

  }

  return (
    <Line 
      style={{
        margin: '15px 30px',
        maxHeight: '440px',
        maxWidth: '900px',
        width: '60%'
      }}
      data={{
        labels: FSpace.map(({ x }) => x),
        datasets: [
          {
            label: 'Equação do espaço',
            data: FSpace.map(({ y }) => y),
            tension: .1,
            borderWidth: 2.5
          },
          {
            label: 'Equação do espaço',
            data: FSpeed.map(({ y }) => y),
            tension: .1,
            borderWidth: 2.5
          }
        ]
      }} 
      options={{
        elements: {
          point:{
            radius: .45
          }
        },
        scales: {
          y: {
            min: 0,
            beginAtZero: true
          },
          x: {
            min: 0
          }
        }
      }}
    />
  );
}