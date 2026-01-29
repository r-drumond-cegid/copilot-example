import { useState, useEffect } from 'react';
import { format, subDays } from 'date-fns';
import { Button } from '@cegid/cds-react';
import {
  Box,
  Typography,
  CircularProgress,
  Alert,
  Grid,
  Paper,
  Card,
  CardContent,
} from '@cegid/cds-react';
import { Refresh as RefreshIcon, Warning as WarningIcon } from '@mui/icons-material';
import BalanceSummaryCard from '../components/dashboard/BalanceSummaryCard';
import TransactionList from '../components/dashboard/TransactionList';
import DateRangePicker from '../components/dashboard/DateRangePicker';
import BalanceChart from '../components/charts/BalanceChart';
import CategoryChart from '../components/charts/CategoryChart';
import Chatbot from '../components/chatbot/Chatbot';
import { getBalanceSummary, getAlerts } from '../api/accounts';
import { getEnrichedTransactions, getTransactionTrends } from '../api/transactions';

const Dashboard = () => {
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [dateRange, setDateRange] = useState({
    from: '2025-12-01',  // Date fixe pour capturer toutes les données mock (Dec 2025 - Jan 2026)
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
      
      // Log data for debugging
      console.log('✓ Dashboard data loaded:', {
        transactions: transactionsData.length,
        trends: trendsData,
        balanceSummary: summaryData,
        alerts: alertsData.alerts?.length || 0,
      });
    } catch (err) {
      const errorMessage = err.message || 'Erreur de chargement des données';
      setError(errorMessage);
      console.error('❌ Error loading dashboard:', {
        error: err,
        message: errorMessage,
        stack: err.stack,
      });
    } finally {
      setLoading(false);
    }
  };

  const handleDateRangeChange = (from, to) => {
    setDateRange({ from, to });
  };

  return (
    <Box component="main" aria-labelledby="page-title" sx={{ width: '100%', py: 2, px: 0 }}>
      {/* Header */}
      <Box sx={{ mb: 2, px: 2, display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: 2 }}>
        <Typography id="page-title" variant="h1" component="h1" sx={{ fontSize: { xs: '2rem', md: '2.5rem' } }}>
          Dashboard Financier
        </Typography>
        <DateRangePicker
          fromDate={dateRange.from}
          toDate={dateRange.to}
          onChange={handleDateRangeChange}
        />
      </Box>

      {/* Loading State */}
      {loading && (
        <Box sx={{ display: 'flex', justifyContent: 'center', alignItems: 'center', minHeight: 400 }}>
          <Box sx={{ textAlign: 'center' }}>
            <CircularProgress size={60} />
            <Typography variant="body1" sx={{ mt: 2 }}>
              Chargement des données...
            </Typography>
          </Box>
        </Box>
      )}

      {/* Error State */}
      {error && (
        <Alert 
          severity="error" 
          sx={{ mb: 3 }}
          action={
            <Button 
              color="inherit" 
              size="small" 
              startIcon={<RefreshIcon />}
              onClick={loadDashboardData}
            >
              Réessayer
            </Button>
          }
        >
          <Typography variant="subtitle1" sx={{ fontWeight: 'bold', mb: 1 }}>
            Erreur de chargement des données
          </Typography>
          <Typography variant="body2">
            {error}
          </Typography>
          <Typography variant="caption" sx={{ display: 'block', mt: 1 }}>
            Vérifiez que le serveur backend est démarré et accessible. Consultez la console pour plus de détails.
          </Typography>
        </Alert>
      )}

      {/* Main Content */}
      {!loading && !error && (
        <>
          {/* Alerts Section */}
          {alerts.length > 0 && (
            <Box component="section" aria-labelledby="alerts-title" sx={{ mb: 2, px: 2 }}>
              <Box sx={{ display: 'flex', alignItems: 'center', mb: 1 }}>
                <WarningIcon sx={{ mr: 1, color: 'warning.main' }} />
                <Typography id="alerts-title" variant="h5" component="h2">
                  Alertes
                </Typography>
              </Box>
              <Box sx={{ display: 'flex', flexDirection: 'column', gap: 1 }}>
                {alerts.map((alert, index) => (
                  <Alert 
                    key={index} 
                    severity={alert.severity || 'warning'}
                    sx={{ borderRadius: 2 }}
                  >
                    {alert.message}
                  </Alert>
                ))}
              </Box>
            </Box>
          )}

          {/* Balance Summary */}
          {balanceSummary && (
            <Box component="section" aria-label="Résumé des soldes" sx={{ mb: 2, px: 2 }}>
              <BalanceSummaryCard summary={balanceSummary} />
            </Box>
          )}

          {/* Charts Section */}
          <Box sx={{ width: '100%', mb: 2, px: 2, display: 'flex', flexDirection: 'column', gap: 2 }}>
            <Paper component="section" aria-labelledby="balance-chart-title" sx={{ p: 2, width: '100%' }}>
              <Typography id="balance-chart-title" variant="h5" component="h2" sx={{ mb: 2 }}>
                Évolution du Solde
              </Typography>
              <BalanceChart dateRange={dateRange} />
            </Paper>
            
            <Paper component="section" aria-labelledby="category-chart-title" sx={{ p: 2, width: '100%' }}>
              <Typography id="category-chart-title" variant="h5" component="h2" sx={{ mb: 2 }}>
                Dépenses par Catégorie
              </Typography>
              <CategoryChart transactions={transactions} />
            </Paper>
          </Box>

          {/* Trends Summary */}
          {trends && (
            <Box component="section" aria-labelledby="trends-title" sx={{ mb: 3, px: 2 }}>
              <Typography id="trends-title" variant="h5" component="h2" sx={{ mb: 2 }}>
                Résumé des Transactions
              </Typography>
              <Grid container spacing={2}>
                <Grid size={{ xs: 12, sm: 6, md: 3, xl: 3 }}>
                  <Card>
                    <CardContent>
                      <Typography variant="body2" color="text.secondary" gutterBottom>
                        Revenus Totaux
                      </Typography>
                      <Typography variant="h5" sx={{ color: 'success.main', fontWeight: 600 }}>
                        {trends.total_income.toLocaleString('fr-FR', { minimumFractionDigits: 2 })} €
                      </Typography>
                    </CardContent>
                  </Card>
                </Grid>
                <Grid size={{ xs: 12, sm: 6, md: 3, xl: 3 }}>
                  <Card>
                    <CardContent>
                      <Typography variant="body2" color="text.secondary" gutterBottom>
                        Dépenses Totales
                      </Typography>
                      <Typography variant="h5" sx={{ color: 'error.main', fontWeight: 600 }}>
                        {trends.total_expenses.toLocaleString('fr-FR', { minimumFractionDigits: 2 })} €
                      </Typography>
                    </CardContent>
                  </Card>
                </Grid>
                <Grid size={{ xs: 12, sm: 6, md: 3, xl: 3 }}>
                  <Card>
                    <CardContent>
                      <Typography variant="body2" color="text.secondary" gutterBottom>
                        Flux Net
                      </Typography>
                      <Typography 
                        variant="h5" 
                        sx={{ 
                          color: trends.net_flow >= 0 ? 'success.main' : 'error.main',
                          fontWeight: 600 
                        }}
                      >
                        {trends.net_flow.toLocaleString('fr-FR', { minimumFractionDigits: 2 })} €
                      </Typography>
                    </CardContent>
                  </Card>
                </Grid>
                <Grid size={{ xs: 12, sm: 6, md: 3, xl: 3 }}>
                  <Card>
                    <CardContent>
                      <Typography variant="body2" color="text.secondary" gutterBottom>
                        Nombre de Transactions
                      </Typography>
                      <Typography variant="h5" sx={{ fontWeight: 600 }}>
                        {trends.transaction_count}
                      </Typography>
                    </CardContent>
                  </Card>
                </Grid>
              </Grid>
            </Box>
          )}

          {/* Transaction List */}
          <Box component="section" aria-label="Liste des transactions" sx={{ px: 2 }}>
            <TransactionList transactions={transactions} />
          </Box>
        </>
      )}

      {/* Chatbot */}
      <Chatbot isOpen={chatbotOpen} onToggle={() => setChatbotOpen(!chatbotOpen)} />
    </Box>
  );
};

export default Dashboard;
