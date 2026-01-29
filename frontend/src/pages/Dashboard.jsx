import { useState, useEffect, useMemo } from 'react';
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
  FormControl,
  InputLabel,
  Select,
  MenuItem,
  Chip,
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
  const [compact, setCompact] = useState(() => {
    try {
      return localStorage.getItem('dashboardCompact') === 'true';
    } catch { return false; }
  });
  const [summaryCollapsed, setSummaryCollapsed] = useState(() => {
    try {
      const v = localStorage.getItem('summaryCollapsed');
      return v ? v === 'true' : false;
    } catch { return false; }
  });
  const [entity, setEntity] = useState('Toutes');
  const [bankGroup, setBankGroup] = useState('Tous');
  const [cutoffLabel, setCutoffLabel] = useState('');

  useEffect(() => {
    loadDashboardData();
  }, [dateRange]);

  // Persist compact mode
  useEffect(() => {
    try { localStorage.setItem('dashboardCompact', compact ? 'true' : 'false'); } catch {}
  }, [compact]);

  // Persist summary collapsed
  useEffect(() => {
    try { localStorage.setItem('summaryCollapsed', summaryCollapsed ? 'true' : 'false'); } catch {}
  }, [summaryCollapsed]);

  // Update cut-off countdown every minute
  useEffect(() => {
    const updateCutoff = () => {
      const now = new Date();
      const cutoff = new Date();
      cutoff.setHours(17, 0, 0, 0); // 17:00 local time
      const ms = cutoff - now;
      if (ms <= 0) { setCutoffLabel('Cut-off passé'); return; }
      const h = Math.floor(ms / 3600000);
      const m = Math.floor((ms % 3600000) / 60000);
      setCutoffLabel(`Cut-off dans ${String(h).padStart(2,'0')}:${String(m).padStart(2,'0')}`);
    };
    updateCutoff();
    const id = setInterval(updateCutoff, 60000);
    return () => clearInterval(id);
  }, []);

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
      {/* Sticky Consolidated Header */}
      <Box sx={{ position: 'sticky', top: 0, zIndex: 10, backgroundColor: 'background.paper', borderBottom: 1, borderColor: 'divider', py: compact ? 1 : 1.5, px: 2, mb: 2 }}>
        <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: 2 }}>
          <Typography id="page-title" variant="h1" component="h1" sx={{ fontSize: { xs: compact ? '1.6rem' : '2rem', md: compact ? '2rem' : '2.5rem' } }}>
            Dashboard Financier
          </Typography>
          <Box sx={{ display: 'flex', alignItems: 'center', gap: 2, flexWrap: 'wrap' }}>
            {/* Bank/Entity switchers */}
            <FormControl size="small" sx={{ minWidth: 160 }}>
              <InputLabel>Entité</InputLabel>
              <Select value={entity} label="Entité" onChange={(e) => setEntity(e.target.value)}>
                <MenuItem value="Toutes">Toutes</MenuItem>
                <MenuItem value="Entité A">Entité A</MenuItem>
                <MenuItem value="Entité B">Entité B</MenuItem>
              </Select>
            </FormControl>
            <FormControl size="small" sx={{ minWidth: 160 }}>
              <InputLabel>Banques</InputLabel>
              <Select value={bankGroup} label="Banques" onChange={(e) => setBankGroup(e.target.value)}>
                <MenuItem value="Tous">Tous</MenuItem>
                <MenuItem value="Groupe 1">Groupe 1</MenuItem>
                <MenuItem value="Groupe 2">Groupe 2</MenuItem>
              </Select>
            </FormControl>
            <DateRangePicker
              fromDate={dateRange.from}
              toDate={dateRange.to}
              onChange={handleDateRangeChange}
            />
            <Chip label={cutoffLabel} color="warning" variant="outlined" size="small" />
            <Button size="small" variant="outlined" onClick={() => setCompact(v => !v)}>
              Mode compact: {compact ? 'ON' : 'OFF'}
            </Button>
          </Box>
        </Box>
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
              <BalanceSummaryCard 
                summary={balanceSummary} 
                compact={compact} 
                collapsed={summaryCollapsed}
                onToggleCollapsed={() => setSummaryCollapsed(v => !v)}
              />
            </Box>
          )}

          {/* Charts Section */}
          <Box sx={{ width: '100%', mb: 2, px: 2, display: 'flex', flexDirection: 'column', gap: 2 }}>
            <Paper component="section" aria-labelledby="balance-chart-title" sx={{ p: 2, width: '100%' }}>
              <Typography id="balance-chart-title" variant="h5" component="h2" sx={{ mb: 2 }}>
                Évolution du Solde
              </Typography>
              <BalanceChart dateRange={dateRange} compact={compact} />
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
            <TransactionList transactions={transactions} compact={compact} />
          </Box>
        </>
      )}

      {/* Chatbot */}
      <Chatbot isOpen={chatbotOpen} onToggle={() => setChatbotOpen(!chatbotOpen)} />
    </Box>
  );
};

export default Dashboard;
