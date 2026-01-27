import { useState, useEffect } from 'react';
import { format, subDays } from 'date-fns';
import {
  Container,
  Box,
  Typography,
  CircularProgress,
  Alert,
  Button,
  Grid,
  Paper,
  Card,
  CardContent,
} from '@mui/material';
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
    <Container maxWidth="xl" sx={{ py: 4 }}>
      {/* Header */}
      <Box sx={{ mb: 4, display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: 2 }}>
        <Typography variant="h1" component="h1" sx={{ fontSize: { xs: '2rem', md: '2.5rem' } }}>
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
            <Box sx={{ mb: 3 }}>
              <Box sx={{ display: 'flex', alignItems: 'center', mb: 2 }}>
                <WarningIcon sx={{ mr: 1, color: 'warning.main' }} />
                <Typography variant="h5" component="h3">
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
            <Box sx={{ mb: 3 }}>
              <BalanceSummaryCard summary={balanceSummary} />
            </Box>
          )}

          {/* Charts Section */}
          <Grid container spacing={3} sx={{ mb: 3 }}>
            <Grid item xs={12} lg={6}>
              <Paper sx={{ p: 3, height: '100%' }}>
                <Typography variant="h5" component="h3" sx={{ mb: 2 }}>
                  Évolution du Solde
                </Typography>
                <BalanceChart dateRange={dateRange} />
              </Paper>
            </Grid>
            <Grid item xs={12} lg={6}>
              <Paper sx={{ p: 3, height: '100%' }}>
                <Typography variant="h5" component="h3" sx={{ mb: 2 }}>
                  Dépenses par Catégorie
                </Typography>
                <CategoryChart transactions={transactions} />
              </Paper>
            </Grid>
          </Grid>

          {/* Trends Summary */}
          {trends && (
            <Box sx={{ mb: 3 }}>
              <Typography variant="h5" component="h3" sx={{ mb: 2 }}>
                Résumé des Transactions
              </Typography>
              <Grid container spacing={2}>
                <Grid item xs={12} sm={6} md={3}>
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
                <Grid item xs={12} sm={6} md={3}>
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
                <Grid item xs={12} sm={6} md={3}>
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
                <Grid item xs={12} sm={6} md={3}>
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
          <TransactionList transactions={transactions} />
        </>
      )}

      {/* Chatbot */}
      <Chatbot isOpen={chatbotOpen} onToggle={() => setChatbotOpen(!chatbotOpen)} />
    </Container>
  );
};

export default Dashboard;
