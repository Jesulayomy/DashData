'use client';

import { useEffect, useState } from 'react';
import { LineChart, Line, XAxis, YAxis, Tooltip } from 'recharts';
import { api } from '../utils/api';

export default function LineComponent() {
  const [data, setData] = useState<{ name: string; value: number }[]>([]);
  useEffect(() => {
    const fetchData = async () => {
      const response = await api.get('/line-chart-data/');
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
    <LineChart
      width={450}
      height={300}
      data={data}
      margin={{ top: 5, right: 20, bottom: 5, left: 0 }}
    >
      <Line type='monotone' dataKey='value' stroke='#8884d8' />
      <XAxis dataKey='name' />
      <YAxis />
      <Tooltip
        contentStyle={{
          backgroundColor: '#333',
          border: '1px solid #333'
        }}
      />
    </LineChart>
  );
}
