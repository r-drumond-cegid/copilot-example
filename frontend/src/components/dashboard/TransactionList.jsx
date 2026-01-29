import { useEffect, useMemo, useState } from 'react';
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
  Button,
  Pagination,
} from '@cegid/cds-react';
import { getCategories } from '../../api/transactions';
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
  const [sortOrder, setSortOrder] = useState('desc');
  const [category, setCategory] = useState('');
  const [categories, setCategories] = useState([]);
  const [minAmount, setMinAmount] = useState('');
  const [maxAmount, setMaxAmount] = useState('');
  const [page, setPage] = useState(1);
  const [pageSize, setPageSize] = useState(10);

  useEffect(() => {
    (async () => {
      try {
        const cats = await getCategories();
        setCategories(cats || []);
      } catch (e) {
        console.warn('Unable to load categories:', e.message);
      }
    })();
  }, []);

  const filteredTransactions = useMemo(() => {
    return transactions.filter(t => {
      if (filter === 'income' && t.is_debit) return false;
      if (filter === 'expense' && !t.is_debit) return false;
      if (category && (!t.category || t.category.id !== category)) return false;
      const amt = Math.abs(t.amount);
      if (minAmount && amt < Number(minAmount)) return false;
      if (maxAmount && amt > Number(maxAmount)) return false;
      return true;
    });
  }, [transactions, filter, category, minAmount, maxAmount]);

  const sortedTransactions = useMemo(() => {
    const arr = [...filteredTransactions];
    arr.sort((a, b) => {
      if (sortBy === 'date') {
        const res = new Date(a.operation_date) - new Date(b.operation_date);
        return sortOrder === 'asc' ? res : -res;
      }
      if (sortBy === 'amount') {
        const res = Math.abs(a.amount) - Math.abs(b.amount);
        return sortOrder === 'asc' ? res : -res;
      }
      return 0;
    });
    return arr;
  }, [filteredTransactions, sortBy, sortOrder]);

  const totalPages = Math.max(1, Math.ceil(sortedTransactions.length / pageSize));
  const pagedTransactions = useMemo(() => {
    const start = (page - 1) * pageSize;
    return sortedTransactions.slice(start, start + pageSize);
  }, [sortedTransactions, page, pageSize]);

  const toggleSort = (key) => {
    if (sortBy === key) {
      setSortOrder(prev => (prev === 'asc' ? 'desc' : 'asc'));
    } else {
      setSortBy(key);
      setSortOrder('desc');
    }
  };

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

          <FormControl size="small" sx={{ minWidth: 180 }}>
            <InputLabel>Catégorie</InputLabel>
            <Select
              value={category}
              label="Catégorie"
              onChange={(e) => setCategory(e.target.value)}
            >
              <MenuItem value="">Toutes</MenuItem>
              {categories.map(cat => (
                <MenuItem key={cat.id} value={cat.id}>{cat.name}</MenuItem>
              ))}
            </Select>
          </FormControl>

          <TextFieldSmall label="Montant min" value={minAmount} onChange={setMinAmount} />
          <TextFieldSmall label="Montant max" value={maxAmount} onChange={setMaxAmount} />

          <FormControl size="small" sx={{ minWidth: 140 }}>
            <InputLabel>Par page</InputLabel>
            <Select
              value={pageSize}
              label="Par page"
              onChange={(e) => { setPageSize(Number(e.target.value)); setPage(1); }}
            >
              <MenuItem value={10}>10</MenuItem>
              <MenuItem value={25}>25</MenuItem>
              <MenuItem value={50}>50</MenuItem>
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
            <Table aria-labelledby="transactions-title">
              <caption className="sr-only">Liste des transactions avec date, catégorie, compte, marchand, tags et montant</caption>
              <TableHead>
                <TableRow>
                  <TableCell scope="col" aria-sort={sortBy === 'date' ? (sortOrder === 'asc' ? 'ascending' : 'descending') : 'none'} onClick={() => toggleSort('date')} sx={{ cursor: 'pointer' }}>Date</TableCell>
                  <TableCell scope="col" aria-sort="none">Catégorie</TableCell>
                  <TableCell scope="col" aria-sort="none">Compte</TableCell>
                  <TableCell scope="col" aria-sort="none">Marchand</TableCell>
                  <TableCell scope="col" aria-sort="none">Tags</TableCell>
                  <TableCell scope="col" align="right" aria-sort={sortBy === 'amount' ? (sortOrder === 'asc' ? 'ascending' : 'descending') : 'none'} onClick={() => toggleSort('amount')} sx={{ cursor: 'pointer' }}>Montant</TableCell>
                </TableRow>
              </TableHead>
              <TableBody>
                {pagedTransactions.map((transaction, index) => (
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
      {/* Pagination */}
      <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', mt: 2 }}>
        <Typography variant="caption" color="text.secondary">Page {page} sur {totalPages} ({sortedTransactions.length} transactions filtrées)</Typography>
        <Pagination count={totalPages} page={page} onChange={(_, value) => setPage(value)} size="small" />
      </Box>
    </Paper>
  );
};

export default TransactionList;

// Small numeric text field component for amounts
const TextFieldSmall = ({ label, value, onChange }) => (
  <FormControl size="small" sx={{ minWidth: 120 }}>
    <InputLabel shrink>{label}</InputLabel>
    <Select
      value={value}
      onChange={(e) => onChange(e.target.value)}
      displayEmpty
      renderValue={(selected) => selected || ''}
      inputProps={{ inputMode: 'numeric', pattern: '[0-9]*' }}
    >
      <MenuItem value="">—</MenuItem>
      <MenuItem value="50">50</MenuItem>
      <MenuItem value="100">100</MenuItem>
      <MenuItem value="250">250</MenuItem>
      <MenuItem value="500">500</MenuItem>
      <MenuItem value="1000">1000</MenuItem>
    </Select>
  </FormControl>
);
