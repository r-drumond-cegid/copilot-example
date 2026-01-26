import Plot from 'react-plotly.js';
import { useMemo } from 'react';

const CategoryChart = ({ transactions }) => {
  const categoryData = useMemo(() => {
    // Filter only expenses (debits)
    const expenses = transactions.filter(t => t.is_debit);
    
    // Group by category
    const categoryTotals = {};
    expenses.forEach(t => {
      if (t.category) {
        const catName = t.category.name;
        categoryTotals[catName] = (categoryTotals[catName] || 0) + Math.abs(t.amount);
      }
    });

    // Sort by amount
    const sorted = Object.entries(categoryTotals)
      .sort((a, b) => b[1] - a[1])
      .slice(0, 10); // Top 10 categories

    return {
      labels: sorted.map(([name]) => name),
      values: sorted.map(([, value]) => value),
    };
  }, [transactions]);

  if (categoryData.labels.length === 0) {
    return (
      <div style={{ textAlign: 'center', padding: '2rem', color: '#64748b' }}>
        Aucune donnée de dépense disponible
      </div>
    );
  }

  const colors = [
    '#2563eb', '#10b981', '#f59e0b', '#ef4444', '#8b5cf6',
    '#ec4899', '#14b8a6', '#f97316', '#06b6d4', '#84cc16',
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

  const layout = {
    autosize: true,
    margin: { t: 20, r: 20, b: 20, l: 20 },
    showlegend: false,
    paper_bgcolor: '#ffffff',
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

export default CategoryChart;
