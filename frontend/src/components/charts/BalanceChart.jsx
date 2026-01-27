import { useState, useEffect } from 'react';
import Plot from 'react-plotly.js';
import { getAccountBalances } from '../../api/accounts';

const BalanceChart = ({ dateRange }) => {
  const [chartData, setChartData] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    loadBalanceData();
  }, [dateRange]);

  const loadBalanceData = async () => {
    setLoading(true);
    
    try {
      // Query account balances for the entire date range
      const balances = await getAccountBalances({ 
        start_date: dateRange.from, 
        end_date: dateRange.to 
      });

      // Group balances by date and calculate total for each day
      const balancesByDate = {};
      balances.forEach(acc => {
        if (!balancesByDate[acc.date]) {
          balancesByDate[acc.date] = 0;
        }
        balancesByDate[acc.date] += acc.balance;
      });

      // Convert to array and sort by date
      const timelineData = Object.entries(balancesByDate)
        .map(([date, balance]) => ({ date, balance }))
        .sort((a, b) => a.date.localeCompare(b.date));

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
