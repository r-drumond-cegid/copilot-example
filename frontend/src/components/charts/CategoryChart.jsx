import Plot from 'react-plotly.js';
import { useMemo, useState, useRef, useCallback } from 'react';
import { useTheme } from '@mui/material';
import { useResizeObserver } from '../../hooks/useResizeObserver';

/**
 * @param {{ transactions: import('../../types').Transaction[], compact?: boolean, height?: number }} props
 */
const CategoryChart = ({ transactions, compact = false, height }) => {
  const containerRef = useRef(null);
  const [chartHeight, setChartHeight] = useState(600);
  const [containerWidth, setContainerWidth] = useState(1200);
  const theme = useTheme();
  const handleResize = useCallback((rect) => {
    if (height && typeof height === 'number') {
      setChartHeight(height);
      return;
    }
    const width = rect?.width ?? 1200;
    setContainerWidth(width);
    let h;
    if (width < 520) {
      h = compact ? 260 : 320;
    } else if (width < 960) {
      h = Math.round(width * (compact ? 0.55 : 0.65));
    } else {
      h = compact ? 440 : 560;
    }
    // Clamp between reasonable bounds to avoid oversized donuts
    const minH = 240;
    const maxH = compact ? 480 : 600;
    setChartHeight(Math.max(minH, Math.min(h, maxH)));
  }, [compact, height]);
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

  const labelsInside = compact || containerWidth < 720;

  const trace = {
    labels: categoryData.labels,
    values: categoryData.values,
    type: 'pie',
    hole: 0.4,
    marker: {
      colors: colors,
    },
    textinfo: labelsInside ? 'percent+label' : 'label+percent',
    textposition: labelsInside ? 'inside' : 'outside',
    insidetextorientation: 'radial',
    textfont: { size: labelsInside ? 11 : 12, color: labelsInside ? theme.palette.getContrastText(theme.palette.primary.main) : undefined },
    hovertemplate: '<b>%{label}</b><br>%{value:,.2f} €<br>%{percent}<extra></extra>',
  };

  const isMobile = containerWidth < 600;
  
  const layout = {
    autosize: true,
    width: undefined,
    height: undefined,
    margin: { 
      t: isMobile ? 10 : 20, 
      r: labelsInside ? 10 : 40, 
      b: isMobile ? 10 : 20, 
      l: labelsInside ? 10 : 40 
    },
    showlegend: labelsInside,
    uniformtext: { mode: 'hide', minsize: 10 },
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
