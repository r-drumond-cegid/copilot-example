import { useState, useEffect } from 'react';
import { format, subDays } from 'date-fns';
import BalanceSummaryCard from '../components/dashboard/BalanceSummaryCard';
import TransactionList from '../components/dashboard/TransactionList';
import DateRangePicker from '../components/dashboard/DateRangePicker';
import BalanceChart from '../components/charts/BalanceChart';
import CategoryChart from '../components/charts/CategoryChart';
import Chatbot from '../components/chatbot/Chatbot';
import { getBalanceSummary, getAlerts } from '../api/accounts';
import { getEnrichedTransactions, getTransactionTrends } from '../api/transactions';
import './Dashboard.css';

const Dashboard = () => {
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [dateRange, setDateRange] = useState({
    from: format(subDays(new Date(), 30), 'yyyy-MM-dd'),
    to: format(new Date(), 'yyyy-MM-dd'),
  });
  
  const [balanceSummary, setBalanceSummary] = useState(null);
  const [transactions, setTransactions] = useState([]);
  const [trends, setTrends] = useState(null);
  const [alerts, setAlerts] = useState([]);
  const [chatbotOpen, setChatbotOpen] = useState(false);

  useEffect(() => {
    loadDashboardData();
  }, [dateRange]);

  const loadDashboardData = async () => {
    setLoading(true);
    setError(null);
    
    try {
      const [summaryData, transactionsData, trendsData, alertsData] = await Promise.all([
        getBalanceSummary({ date: dateRange.to }),
        getEnrichedTransactions({
          from_date: dateRange.from,
          to_date: dateRange.to,
        }),
        getTransactionTrends(dateRange.from, dateRange.to),
        getAlerts(0.1),
      ]);
      
      setBalanceSummary(summaryData);
      setTransactions(transactionsData);
      setTrends(trendsData);
      setAlerts(alertsData.alerts || []);
    } catch (err) {
      setError(err.message);
      console.error('Error loading dashboard:', err);
    } finally {
      setLoading(false);
    }
  };

  const handleDateRangeChange = (from, to) => {
    setDateRange({ from, to });
  };

  return (
    <div className="dashboard">
      <div className="dashboard-header">
        <h1>Dashboard Financier</h1>
        <DateRangePicker
          fromDate={dateRange.from}
          toDate={dateRange.to}
          onChange={handleDateRangeChange}
        />
      </div>

      {loading && (
        <div className="loading-container">
          <p>Chargement des données...</p>
        </div>
      )}

      {error && (
        <div className="error-container">
          <p>Erreur: {error}</p>
          <button onClick={loadDashboardData}>Réessayer</button>
        </div>
      )}

      {!loading && !error && (
        <>
          {/* Alerts Section */}
          {alerts.length > 0 && (
            <div className="alerts-section">
              <h3>⚠️ Alertes</h3>
              <div className="alerts-list">
                {alerts.map((alert, index) => (
                  <div key={index} className={`alert alert-${alert.severity}`}>
                    {alert.message}
                  </div>
                ))}
              </div>
            </div>
          )}

          {/* Balance Summary */}
          {balanceSummary && (
            <BalanceSummaryCard summary={balanceSummary} />
          )}

          {/* Charts Section */}
          <div className="charts-grid">
            <div className="chart-container">
              <h3>Évolution du Solde</h3>
              <BalanceChart dateRange={dateRange} />
            </div>
            <div className="chart-container">
              <h3>Dépenses par Catégorie</h3>
              <CategoryChart transactions={transactions} />
            </div>
          </div>

          {/* Trends Summary */}
          {trends && (
            <div className="trends-section">
              <h3>Résumé des Transactions</h3>
              <div className="trends-grid">
                <div className="trend-card">
                  <span className="trend-label">Revenus Totaux</span>
                  <span className="trend-value income">
                    {trends.total_income.toLocaleString('fr-FR', { minimumFractionDigits: 2 })} €
                  </span>
                </div>
                <div className="trend-card">
                  <span className="trend-label">Dépenses Totales</span>
                  <span className="trend-value expense">
                    {trends.total_expenses.toLocaleString('fr-FR', { minimumFractionDigits: 2 })} €
                  </span>
                </div>
                <div className="trend-card">
                  <span className="trend-label">Flux Net</span>
                  <span className={`trend-value ${trends.net_flow >= 0 ? 'income' : 'expense'}`}>
                    {trends.net_flow.toLocaleString('fr-FR', { minimumFractionDigits: 2 })} €
                  </span>
                </div>
                <div className="trend-card">
                  <span className="trend-label">Nombre de Transactions</span>
                  <span className="trend-value">{trends.transaction_count}</span>
                </div>
              </div>
            </div>
          )}

          {/* Transaction List */}
          <TransactionList transactions={transactions} />
        </>
      )}

      {/* Chatbot */}
      <Chatbot isOpen={chatbotOpen} onToggle={() => setChatbotOpen(!chatbotOpen)} />
    </div>
  );
};

export default Dashboard;
