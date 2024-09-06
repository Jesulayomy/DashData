'use client';

import { useEffect, useState } from 'react';
import {
  PieChart,
  Pie,
  Sector,
  Cell,
  ResponsiveContainer,
  XAxis,
  YAxis,
  Tooltip
} from 'recharts';
import { api } from '../utils/api';

export default function PieComponent() {
  const [data, setData] = useState<{ name: string; value: number }[]>([]);
  useEffect(() => {
    const fetchData = async () => {
      const response = await api.get('/pie-chart-data/');
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
    <PieChart width={300} height={300}>
      <Pie
        dataKey='value'
        startAngle={360}
        endAngle={0}
        data={data}
        cx='50%'
        cy='50%'
        outerRadius={80}
        fill='#8884d8'
        labelLine={false}
        label
      />
      <Tooltip
        contentStyle={{
          backgroundColor: '#333',
          border: '1px solid #333'
        }}
      />
    </PieChart>
  );
}
