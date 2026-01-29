import { useState, useEffect, useMemo, useRef, useCallback } from 'react';
import { useTheme } from '@mui/material';
import Plot from 'react-plotly.js';
import { getAccountBalances } from '../../api/accounts';
import { useResizeObserver } from '../../hooks/useResizeObserver';

/**
 * @param {{ dateRange: { from: string, to: string } }} props
 */
const BalanceChart = ({ dateRange }) => {
  const [chartData, setChartData] = useState([]);
  const [loading, setLoading] = useState(true);
  const containerRef = useRef(null);
  const [chartHeight, setChartHeight] = useState(500);
  const theme = useTheme();

  useEffect(() => {
    loadBalanceData();
  }, [dateRange]);

  const handleResize = useCallback((rect) => {
    const width = rect?.width ?? 1200;
    if (width < 600) setChartHeight(280);
    else if (width < 960) setChartHeight(380);
    else setChartHeight(500);
  }, []);
  useResizeObserver(containerRef, handleResize);

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

  const descId = 'balance-chart-desc';
  const summary = useMemo(() => {
    if (!chartData || chartData.length === 0) {
      return { from: null, to: null, min: 0, max: 0, end: 0 };
    }
    const first = chartData[0];
    const last = chartData[chartData.length - 1];
    const min = Math.min(...chartData.map(d => d.balance));
    const max = Math.max(...chartData.map(d => d.balance));
    return {
      from: first?.date, to: last?.date, min, max, end: last?.balance,
    };
  }, [chartData]);

  if (loading) {
    return <div style={{ textAlign: 'center', padding: '2rem' }}>Chargement...</div>;
  }

  if (!chartData || chartData.length === 0) {
    return <div style={{ textAlign: 'center', padding: '2rem' }}>Aucune donnée disponible</div>;
  }

  const trace = {
    x: chartData.map(d => d.date),
    y: chartData.map(d => d.balance),
    type: 'scatter',
    mode: 'lines+markers',
    name: 'Solde Total',
    line: {
      color: theme.palette.primary.main,
      width: 3,
    },
    marker: {
      color: theme.palette.primary.main,
      size: 6,
    },
  };

  const isMobile = false;
  
  const layout = {
    autosize: true,
    width: undefined,
    height: undefined,
    margin: { 
      t: 20, 
      r: isMobile ? 10 : 20, 
      b: isMobile ? 30 : 40, 
      l: isMobile ? 50 : 60 
    },
    xaxis: {
      title: 'Date',
      showgrid: true,
      gridcolor: theme.palette.divider,
    },
    yaxis: {
      title: 'Solde (€)',
      showgrid: true,
      gridcolor: theme.palette.divider,
      tickformat: ',.0f',
    },
    plot_bgcolor: theme.palette.background.paper,
    paper_bgcolor: theme.palette.background.paper,
    hovermode: 'x unified',
  };

  return (
    <div ref={containerRef} style={{ width: '100%' }}>
      <p id={descId} className="sr-only">
        Évolution du solde du {summary.from} au {summary.to}. Minimum {summary.min.toLocaleString('fr-FR')} €, maximum {summary.max.toLocaleString('fr-FR')} €, solde final {summary.end.toLocaleString('fr-FR')} €.
      </p>
      <Plot
        aria-label="Graphique de l'évolution du solde"
        aria-describedby={descId}
        data={[trace]}
        layout={{ ...layout, height: chartHeight }}
        config={{ responsive: true, displayModeBar: false }}
        style={{ width: '100%', height: chartHeight }}
      />
    </div>
  );
};

export default BalanceChart;
