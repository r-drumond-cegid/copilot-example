import { 
  Card, 
  CardContent, 
  Typography, 
  Box, 
  Grid, 
  Chip,
  Divider 
} from '@cegid/cds-react';
import { 
  AccountBalance as AccountBalanceIcon,
  TrendingUp as TrendingUpIcon,
  TrendingDown as TrendingDownIcon 
} from '@mui/icons-material';

/**
 * @param {{ summary: import('../../types').BalanceSummary }} props
 */
const BalanceSummaryCard = ({ summary }) => {
  if (!summary) return null;

  return (
    <Card sx={{ borderRadius: 3, boxShadow: 2 }}>
      <CardContent>
        {/* Header */}
        <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', mb: 3 }}>
          <Box sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
            <AccountBalanceIcon sx={{ color: 'primary.main', fontSize: 28 }} />
            <Typography variant="h4" component="h2" sx={{ fontWeight: 600 }}>
              Résumé des Soldes
            </Typography>
          </Box>
          <Chip 
            label={summary.date} 
            color="primary" 
            variant="outlined"
            size="medium"
          />
        </Box>
        
        {/* Main Balance */}
        <Box 
          sx={{ 
            p: 3, 
            mb: 3, 
            backgroundColor: 'primary.main',
            borderRadius: 2,
            textAlign: 'center'
          }}
        >
          <Typography variant="body2" sx={{ color: 'primary.contrastText', mb: 1, opacity: 0.9 }}>
            Solde Total
          </Typography>
          <Typography 
            variant="h2" 
            component="div" 
            sx={{ 
              color: 'primary.contrastText',
              fontWeight: 700,
              fontSize: { xs: '2rem', md: '3rem' }
            }}
          >
            {summary.total_balance.toLocaleString('fr-FR', { minimumFractionDigits: 2 })} {summary.currency}
          </Typography>
        </Box>

        <Divider sx={{ mb: 3 }} />

        {/* Details Grid */}
        <Grid container spacing={2}>
          <Grid size={{ xs: 12, sm: 6, md: 4 }}>
            <Box sx={{ p: 2, backgroundColor: 'background.default', borderRadius: 2 }}>
              <Typography variant="body2" color="text.secondary" gutterBottom>
                Nombre de Comptes
              </Typography>
              <Typography variant="h5" sx={{ fontWeight: 600, color: 'primary.main' }}>
                {summary.account_count}
              </Typography>
            </Box>
          </Grid>
          
          <Grid size={{ xs: 12, sm: 6, md: 4 }}>
            <Box sx={{ p: 2, backgroundColor: 'background.default', borderRadius: 2 }}>
              <Typography variant="body2" color="text.secondary" gutterBottom>
                Solde Moyen
              </Typography>
              <Typography variant="h5" sx={{ fontWeight: 600 }}>
                {summary.average_balance.toLocaleString('fr-FR', { minimumFractionDigits: 2 })} {summary.currency}
              </Typography>
            </Box>
          </Grid>
          
          <Grid size={{ xs: 12, sm: 6, md: 4 }}>
            <Box sx={{ p: 2, backgroundColor: 'success.light', borderRadius: 2, display: 'flex', alignItems: 'center', gap: 1 }}>
              <TrendingUpIcon sx={{ color: 'success.dark' }} />
              <Box>
                <Typography variant="body2" color="success.dark" gutterBottom>
                  Solde Maximum
                </Typography>
                <Typography variant="h5" sx={{ fontWeight: 600, color: 'success.dark' }}>
                  {summary.highest_balance.toLocaleString('fr-FR', { minimumFractionDigits: 2 })} {summary.currency}
                </Typography>
              </Box>
            </Box>
          </Grid>
          
          <Grid size={{ xs: 12, sm: 6, md: 4 }}>
            <Box sx={{ p: 2, backgroundColor: 'error.light', borderRadius: 2, display: 'flex', alignItems: 'center', gap: 1 }}>
              <TrendingDownIcon sx={{ color: 'error.dark' }} />
              <Box>
                <Typography variant="body2" color="error.dark" gutterBottom>
                  Solde Minimum
                </Typography>
                <Typography variant="h5" sx={{ fontWeight: 600, color: 'error.dark' }}>
                  {summary.lowest_balance.toLocaleString('fr-FR', { minimumFractionDigits: 2 })} {summary.currency}
                </Typography>
              </Box>
            </Box>
          </Grid>
          
          <Grid size={{ xs: 12, sm: 6, md: 4 }}>
            <Box sx={{ p: 2, backgroundColor: 'background.default', borderRadius: 2 }}>
              <Typography variant="body2" color="text.secondary" gutterBottom>
                Découvert Autorisé Total
              </Typography>
              <Typography variant="h5" sx={{ fontWeight: 600, color: 'warning.main' }}>
                {summary.total_overdraft_allowed.toLocaleString('fr-FR', { minimumFractionDigits: 2 })} {summary.currency}
              </Typography>
            </Box>
          </Grid>
        </Grid>
      </CardContent>
    </Card>
  );
};

export default BalanceSummaryCard;
