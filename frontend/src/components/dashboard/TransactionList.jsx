import { useState } from 'react';
import {
  Box,
  Paper,
  Typography,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Chip,
  Select,
  MenuItem,
  FormControl,
  InputLabel,
  Stack,
} from '@cegid/cds-react';
import {
  TrendingUp as IncomeIcon,
  TrendingDown as ExpenseIcon,
  Store as StoreIcon,
} from '@mui/icons-material';

/**
 * @param {{ transactions: import('../../types').Transaction[] }} props
 */
const TransactionList = ({ transactions }) => {
  const [filter, setFilter] = useState('all');
  const [sortBy, setSortBy] = useState('date');

  const filteredTransactions = transactions.filter(t => {
    if (filter === 'income') return !t.is_debit;
    if (filter === 'expense') return t.is_debit;
    return true;
  });

  const sortedTransactions = [...filteredTransactions].sort((a, b) => {
    if (sortBy === 'date') {
      return new Date(b.operation_date) - new Date(a.operation_date);
    }
    if (sortBy === 'amount') {
      return Math.abs(b.amount) - Math.abs(a.amount);
    }
    return 0;
  });

  return (
    <Paper component="section" aria-labelledby="transactions-title" sx={{ p: 3, borderRadius: 3 }}>
      {/* Header */}
      <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', mb: 3, flexWrap: 'wrap', gap: 2 }}>
        <Typography id="transactions-title" variant="h5" component="h2" sx={{ fontWeight: 600 }}>
          Transactions ({transactions.length})
        </Typography>
        
        {/* Controls */}
        <Box sx={{ display: 'flex', gap: 2, flexWrap: 'wrap' }}>
          <FormControl size="small" sx={{ minWidth: 140 }}>
            <InputLabel>Filtre</InputLabel>
            <Select
              value={filter}
              label="Filtre"
              onChange={(e) => setFilter(e.target.value)}
            >
              <MenuItem value="all">Toutes</MenuItem>
              <MenuItem value="income">Revenus</MenuItem>
              <MenuItem value="expense">Dépenses</MenuItem>
            </Select>
          </FormControl>
          
          <FormControl size="small" sx={{ minWidth: 140 }}>
            <InputLabel>Trier par</InputLabel>
            <Select
              value={sortBy}
              label="Trier par"
              onChange={(e) => setSortBy(e.target.value)}
            >
              <MenuItem value="date">Par Date</MenuItem>
              <MenuItem value="amount">Par Montant</MenuItem>
            </Select>
          </FormControl>
        </Box>
      </Box>

      {/* Transactions Table */}
      {sortedTransactions.length === 0 ? (
        <Box sx={{ textAlign: 'center', py: 8 }}>
          <Typography variant="body1" color="text.secondary">
            Aucune transaction trouvée
          </Typography>
        </Box>
      ) : (
        <TableContainer>
          <Table>
            <TableHead>
              <TableRow>
                <TableCell aria-sort={sortBy === 'date' ? 'descending' : 'none'}>Date</TableCell>
                <TableCell aria-sort="none">Catégorie</TableCell>
                <TableCell aria-sort="none">Compte</TableCell>
                <TableCell aria-sort="none">Marchand</TableCell>
                <TableCell aria-sort="none">Tags</TableCell>
                <TableCell align="right" aria-sort={sortBy === 'amount' ? 'descending' : 'none'}>Montant</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {sortedTransactions.map((transaction, index) => (
                <TableRow
                  key={index}
                  sx={{
                    '&:hover': {
                      backgroundColor: 'action.hover',
                    },
                  }}
                >
                  <TableCell>
                    <Typography variant="body2">
                      {new Date(transaction.operation_date).toLocaleDateString('fr-FR')}
                    </Typography>
                  </TableCell>
                  
                  <TableCell>
                    {transaction.category ? (
                      <Chip
                        label={transaction.category.name}
                        size="small"
                        sx={{
                          backgroundColor: transaction.category.color || 'primary.light',
                          color: 'white',
                          fontWeight: 500,
                        }}
                      />
                    ) : (
                      <Typography variant="body2" color="text.secondary">-</Typography>
                    )}
                  </TableCell>
                  
                  <TableCell>
                    <Typography variant="body2" sx={{ fontWeight: 500 }}>
                      {transaction.account}
                    </Typography>
                  </TableCell>
                  
                  <TableCell>
                    {transaction.merchant ? (
                      <Box sx={{ display: 'flex', alignItems: 'center', gap: 0.5 }}>
                        <StoreIcon fontSize="small" sx={{ color: 'text.secondary' }} />
                        <Typography variant="body2">
                          {transaction.merchant}
                        </Typography>
                      </Box>
                    ) : (
                      <Typography variant="body2" color="text.secondary">-</Typography>
                    )}
                  </TableCell>
                  
                  <TableCell>
                    {transaction.tags && transaction.tags.length > 0 ? (
                      <Stack direction="row" spacing={0.5} flexWrap="wrap">
                        {transaction.tags.map((tag, i) => (
                          <Chip
                            key={i}
                            label={tag}
                            size="small"
                            variant="outlined"
                            sx={{ fontSize: '0.75rem' }}
                          />
                        ))}
                      </Stack>
                    ) : (
                      <Typography variant="body2" color="text.secondary">-</Typography>
                    )}
                  </TableCell>
                  
                  <TableCell align="right">
                    <Box sx={{ display: 'flex', alignItems: 'center', justifyContent: 'flex-end', gap: 0.5 }}>
                      {transaction.is_debit ? (
                        <ExpenseIcon fontSize="small" sx={{ color: 'error.main' }} />
                      ) : (
                        <IncomeIcon fontSize="small" sx={{ color: 'success.main' }} />
                      )}
                      <Typography
                        variant="body2"
                        sx={{
                          fontWeight: 600,
                          color: transaction.is_debit ? 'error.main' : 'success.main',
                        }}
                      >
                        {transaction.is_debit ? '-' : '+'}
                        {Math.abs(transaction.amount).toLocaleString('fr-FR', { minimumFractionDigits: 2 })} {transaction.currency}
                      </Typography>
                    </Box>
                  </TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </TableContainer>
      )}
    </Paper>
  );
};

export default TransactionList;
