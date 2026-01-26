import { useState, useEffect } from 'react';
import Plot from 'react-plotly.js';
import { getAccountBalances } from '../../api/accounts';
import { subDays, format, eachDayOfInterval } from 'date-fns';

const BalanceChart = ({ dateRange }) => {
  const [chartData, setChartData] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    loadBalanceData();
  }, [dateRange]);

  const loadBalanceData = async () => {
    setLoading(true);
    
    try {
      // Generate dates for the range
      const dates = eachDayOfInterval({
        start: new Date(dateRange.from),
        end: new Date(dateRange.to),
      });

      // For simplicity, get balance at end date (in production, would query each date)
      const balances = await getAccountBalances({ date: dateRange.to });
      
      // Simulate timeline data (in production, would fetch historical data)
      const timelineData = dates.map((date) => ({
        date: format(date, 'yyyy-MM-dd'),
        balance: balances.reduce((sum, acc) => sum + acc.balance, 0),
      }));

      setChartData(timelineData);
    } catch (error) {
      console.error('Error loading balance data:', error);
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return <div style={{ textAlign: 'center', padding: '2rem' }}>Chargement...</div>;
  }

  const trace = {
    x: chartData.map(d => d.date),
    y: chartData.map(d => d.balance),
    type: 'scatter',
    mode: 'lines+markers',
    name: 'Solde Total',
    line: {
      color: '#2563eb',
      width: 3,
    },
    marker: {
      color: '#2563eb',
      size: 6,
    },
  };

  const layout = {
    autosize: true,
    margin: { t: 20, r: 20, b: 40, l: 60 },
    xaxis: {
      title: 'Date',
      showgrid: true,
      gridcolor: '#e2e8f0',
    },
    yaxis: {
      title: 'Solde (€)',
      showgrid: true,
      gridcolor: '#e2e8f0',
      tickformat: ',.0f',
    },
    plot_bgcolor: '#ffffff',
    paper_bgcolor: '#ffffff',
    hovermode: 'x unified',
  };

  return (
    <Plot
      data={[trace]}
      layout={layout}
      config={{ responsive: true, displayModeBar: false }}
      style={{ width: '100%', height: '400px' }}
    />
  );
};

export default BalanceChart;
