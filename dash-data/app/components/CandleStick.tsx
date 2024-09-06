'use client';

import dynamic from 'next/dynamic';
import { ApexOptions } from 'apexcharts';
import { useState, useEffect } from 'react';
import { api } from '../utils/api';

const ApexChart = dynamic(() => import('react-apexcharts'), { ssr: false });

export default function CandleStickComponent() {
  const [series, setSeries] = useState<
    { data: { x: string; y: number[] }[] }[]
  >([]);
  useEffect(() => {
    const fetchData = async () => {
      const response = await api.get('/candlestick-data/');
      const result = [
        {
          data: response.data.data.map(
            (item: {
              x: string;
              open: string;
              high: string;
              low: string;
              close: string;
            }) => ({
              x: item.x,
              y: [
                parseFloat(item.open),
                parseFloat(item.high),
                parseFloat(item.low),
                parseFloat(item.close)
              ]
            })
          )
        }
      ];
      setSeries(result);
    };
    fetchData();
  }, []);

  const option: ApexOptions = {
    chart: {
      height: 300,
      type: 'candlestick',
      id: 'candle-stick-chart'
    },
    title: {
      text: 'CandleStick Chart',
      align: 'left'
    },
    tooltip: {
      enabled: true,
      theme: 'dark'
    },
    xaxis: {
      type: 'datetime'
    },
    yaxis: {
      tooltip: {
        enabled: true
      }
    }
  };

  return (
    <ApexChart
      type='candlestick'
      options={option}
      series={series}
      height={300}
      width={400}
    />
  );
}
