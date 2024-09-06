'use client';

import Grid from './Grid';
import LineComponent from './LineChart';
import BarComponent from './BarChart';
import PieComponent from './PieChart';
import CandleStickComponent from './CandleStick';

export default function Charts() {
  return (
    <>
      <Grid title='Line Chart'>
        <LineComponent />
      </Grid>
      <Grid title='Bar Chart'>
        <BarComponent />
      </Grid>
      <Grid title='Pie Chart'>
        <PieComponent />
      </Grid>
      <Grid title='CandleStick Chart'>
        <CandleStickComponent />
      </Grid>
    </>
  );
}
