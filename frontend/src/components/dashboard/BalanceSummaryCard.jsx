import { 
  Card, 
  CardContent, 
  Typography, 
  Box, 
  Grid, 
  Chip,
  Divider,
  Button,
} from '@cegid/cds-react';
import { 
  AccountBalance as AccountBalanceIcon,
  TrendingUp as TrendingUpIcon,
  TrendingDown as TrendingDownIcon,
  ExpandLess as ExpandLessIcon,
  ExpandMore as ExpandMoreIcon,
} from '@mui/icons-material';

/**
 * @param {{ summary: import('../../types').BalanceSummary, compact?: boolean, collapsed?: boolean, onToggleCollapsed?: () => void }} props
 */
const BalanceSummaryCard = ({ summary, compact = false, collapsed = false, onToggleCollapsed }) => {
  if (!summary) return null;

  return (
    <Card sx={{ borderRadius: 3, boxShadow: 2 }}>
      <CardContent sx={{ p: compact ? 2 : 3 }}>
        {/* Header */}
        <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', mb: compact ? 2 : 3 }}>
          <Box sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
            <AccountBalanceIcon sx={{ color: 'primary.main', fontSize: compact ? 22 : 28 }} />
            <Typography variant={compact ? 'h5' : 'h4'} component="h2" sx={{ fontWeight: 600 }}>
              Résumé des Soldes
            </Typography>
          </Box>
          <Box sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
            {collapsed && (
              <Chip 
                label={`Total: ${summary.total_balance.toLocaleString('fr-FR', { minimumFractionDigits: 2 })} ${summary.currency}`}
                color="primary" 
                size="small"
              />
            )}
            <Chip 
              label={summary.date} 
              color="primary" 
              variant="outlined"
              size={compact ? 'small' : 'medium'}
            />
            <Button size="small" variant="text" onClick={onToggleCollapsed} aria-expanded={!collapsed} aria-controls="balance-details">
              {collapsed ? <ExpandMoreIcon fontSize="small" /> : <ExpandLessIcon fontSize="small" />} {collapsed ? 'Afficher' : 'Masquer'}
            </Button>
          </Box>
        </Box>
        
        {/* Main Balance */}
        {!collapsed && (
        <Box 
          sx={{ 
            p: compact ? 2 : 3, 
            mb: compact ? 2 : 3, 
            backgroundColor: 'primary.main',
            borderRadius: 2,
            textAlign: 'center'
          }}
        >
          <Typography variant="body2" sx={{ color: 'primary.contrastText', mb: compact ? 0.5 : 1, opacity: 0.9 }}>
            Solde Total
          </Typography>
          <Typography 
            variant={compact ? 'h3' : 'h2'} 
            component="div" 
            sx={{ 
              color: 'primary.contrastText',
              fontWeight: 700,
              fontSize: compact ? { xs: '1.6rem', md: '2.4rem' } : { xs: '2rem', md: '3rem' }
            }}
          >
            {summary.total_balance.toLocaleString('fr-FR', { minimumFractionDigits: 2 })} {summary.currency}
          </Typography>
        </Box>
        )}

        <Divider sx={{ mb: compact ? 2 : 3 }} />

        {/* Details Grid */}
        <Grid container spacing={compact ? 1.5 : 2}>
          <Grid size={{ xs: 12, sm: 6, md: 4 }}>
            <Box sx={{ p: compact ? 1.5 : 2, backgroundColor: 'background.default', borderRadius: 2 }}>
              <Typography variant="body2" color="text.secondary" gutterBottom>
                Nombre de Comptes
              </Typography>
              <Typography variant={compact ? 'h6' : 'h5'} sx={{ fontWeight: 600, color: 'primary.main' }}>
                {summary.account_count}
              </Typography>
            </Box>
          </Grid>
          
          <Grid size={{ xs: 12, sm: 6, md: 4 }}>
            <Box sx={{ p: compact ? 1.5 : 2, backgroundColor: 'background.default', borderRadius: 2 }}>
              <Typography variant="body2" color="text.secondary" gutterBottom>
                Solde Moyen
              </Typography>
              <Typography variant={compact ? 'h6' : 'h5'} sx={{ fontWeight: 600 }}>
                {summary.average_balance.toLocaleString('fr-FR', { minimumFractionDigits: 2 })} {summary.currency}
              </Typography>
            </Box>
          </Grid>
          
          <Grid size={{ xs: 12, sm: 6, md: 4 }}>
            <Box sx={{ p: compact ? 1.5 : 2, backgroundColor: 'success.light', borderRadius: 2, display: 'flex', alignItems: 'center', gap: 1 }}>
              <TrendingUpIcon sx={{ color: 'success.dark', fontSize: compact ? 20 : undefined }} />
              <Box>
                <Typography variant="body2" color="success.dark" gutterBottom>
                  Solde Maximum
                </Typography>
                <Typography variant={compact ? 'h6' : 'h5'} sx={{ fontWeight: 600, color: 'success.dark' }}>
                  {summary.highest_balance.toLocaleString('fr-FR', { minimumFractionDigits: 2 })} {summary.currency}
                </Typography>
              </Box>
            </Box>
          </Grid>
          
          <Grid size={{ xs: 12, sm: 6, md: 4 }}>
            <Box sx={{ p: compact ? 1.5 : 2, backgroundColor: 'error.light', borderRadius: 2, display: 'flex', alignItems: 'center', gap: 1 }}>
              <TrendingDownIcon sx={{ color: 'error.dark', fontSize: compact ? 20 : undefined }} />
              <Box>
                <Typography variant="body2" color="error.dark" gutterBottom>
                  Solde Minimum
                </Typography>
                <Typography variant={compact ? 'h6' : 'h5'} sx={{ fontWeight: 600, color: 'error.dark' }}>
                  {summary.lowest_balance.toLocaleString('fr-FR', { minimumFractionDigits: 2 })} {summary.currency}
                </Typography>
              </Box>
            </Box>
          </Grid>
          
          <Grid size={{ xs: 12, sm: 6, md: 4 }}>
            <Box sx={{ p: compact ? 1.5 : 2, backgroundColor: 'background.default', borderRadius: 2 }}>
              <Typography variant="body2" color="text.secondary" gutterBottom>
                Découvert Autorisé Total
              </Typography>
              <Typography variant={compact ? 'h6' : 'h5'} sx={{ fontWeight: 600, color: 'warning.main' }}>
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
