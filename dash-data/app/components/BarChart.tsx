'use client';

import { useEffect, useState } from 'react';
import {
  BarChart,
  Bar,
  Rectangle,
  XAxis,
  YAxis,
  Tooltip,
  Legend,
} from 'recharts';
import { api } from '../utils/api';

export default function BarComponent() {
  const [data, setData] = useState<{ name: string; value: number }[]>([]);

  useEffect(() => {
    const fetchData = async () => {
      const response = await api.get('/bar-chart-data/');
      const result: { name: string; value: number }[] =
        response.data.labels.map((label: string, index: number) => ({
          name: label,
          value: response.data.data[index]
        }));
      setData(result);
    };
    fetchData();
  }, []);

  return (
    <BarChart
      width={450}
      height={300}
      data={data}
      margin={{
        top: 5,
        right: 30,
        left: 20,
        bottom: 5
      }}
    >
      <XAxis dataKey='name' />
      <YAxis />
      <Tooltip
        contentStyle={{
          backgroundColor: '#333',
          border: '1px solid #333'
        }}
      />
      <Legend />
      <Bar
        dataKey='value'
        fill='#8884d8'
        activeBar={<Rectangle fill='pink' stroke='blue' />}
      />
    </BarChart>
  );
}
