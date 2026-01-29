import Plot from 'react-plotly.js';
import { useMemo, useState, useRef, useCallback } from 'react';
import { useTheme } from '@mui/material';
import { useResizeObserver } from '../../hooks/useResizeObserver';

/**
 * @param {{ transactions: import('../../types').Transaction[] }} props
 */
const CategoryChart = ({ transactions }) => {
  const containerRef = useRef(null);
  const [chartHeight, setChartHeight] = useState(600);
  const theme = useTheme();
  const handleResize = useCallback((rect) => {
    const width = rect?.width ?? 1200;
    if (width < 600) setChartHeight(380);
    else if (width < 960) setChartHeight(500);
    else setChartHeight(600);
  }, []);
  useResizeObserver(containerRef, handleResize);

  const categoryData = useMemo(() => {
    // Validate transactions array
    if (!transactions || !Array.isArray(transactions)) {
      console.warn('CategoryChart: Invalid transactions data');
      return { labels: [], values: [] };
    }
    
    // Filter only expenses (debits)
    const expenses = transactions.filter(t => t && t.is_debit);
    
    // Group by category
    const categoryTotals = {};
    expenses.forEach(t => {
      // Validate category structure
      if (t.category && t.category.name && typeof t.category.name === 'string') {
        const catName = t.category.name;
        categoryTotals[catName] = (categoryTotals[catName] || 0) + Math.abs(t.amount);
      }
    });

    // Check if we have any data
    if (Object.keys(categoryTotals).length === 0) {
      console.warn('CategoryChart: No category data found in expenses', {
        totalTransactions: transactions.length,
        expenseCount: expenses.length,
      });
    }

    // Sort by amount
    const sorted = Object.entries(categoryTotals)
      .sort((a, b) => b[1] - a[1])
      .slice(0, 10); // Top 10 categories

    return {
      labels: sorted.map(([name]) => name),
      values: sorted.map(([, value]) => value),
    };
  }, [transactions]);

  const descId = 'category-chart-desc';
  const desc = useMemo(() => {
    const total = categoryData.values.reduce((a, b) => a + b, 0);
    const top = categoryData.labels.slice(0, 3)
      .map((l, i) => `${l} (${categoryData.values[i]?.toLocaleString('fr-FR')} €)`) 
      .join(', ');
    return { total, top };
  }, [categoryData]);

  if (categoryData.labels.length === 0) {
    return (
      <div style={{ textAlign: 'center', padding: '2rem', color: '#64748b' }}>
        Aucune donnée de dépense disponible
      </div>
    );
  }

  const colors = [
    theme.palette.primary.main,
    theme.palette.success.main,
    theme.palette.warning.main,
    theme.palette.error.main,
    theme.palette.secondary.main,
    theme.palette.info.main,
    theme.palette.success.light,
    theme.palette.warning.light,
    theme.palette.info.light,
    theme.palette.secondary.light,
  ];

  const trace = {
    labels: categoryData.labels,
    values: categoryData.values,
    type: 'pie',
    hole: 0.4,
    marker: {
      colors: colors,
    },
    textinfo: 'label+percent',
    textposition: 'outside',
    hovertemplate: '<b>%{label}</b><br>%{value:,.2f} €<br>%{percent}<extra></extra>',
  };

  const isMobile = false;
  
  const layout = {
    autosize: true,
    width: undefined,
    height: undefined,
    margin: { 
      t: isMobile ? 10 : 20, 
      r: isMobile ? 10 : 20, 
      b: isMobile ? 10 : 20, 
      l: isMobile ? 10 : 20 
    },
    showlegend: false,
    paper_bgcolor: theme.palette.background.paper,
  };

  return (
    <div ref={containerRef} style={{ width: '100%' }}>
      <p id={descId} className="sr-only">
        Répartition des dépenses par catégorie. Total {desc.total.toLocaleString('fr-FR')} €. Principales catégories: {desc.top || 'N/A'}.
      </p>
      <Plot
        aria-label="Graphique des dépenses par catégorie"
        aria-describedby={descId}
        data={[trace]}
        layout={{ ...layout, height: chartHeight }}
        config={{ responsive: true, displayModeBar: false }}
        style={{ width: '100%', height: chartHeight }}
      />
    </div>
  );
};

export default CategoryChart;
