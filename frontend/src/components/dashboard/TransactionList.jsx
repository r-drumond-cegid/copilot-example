import { useState } from 'react';
import './TransactionList.css';

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
    <div className="transaction-list">
      <div className="list-header">
        <h3>Transactions ({transactions.length})</h3>
        <div className="list-controls">
          <select value={filter} onChange={(e) => setFilter(e.target.value)}>
            <option value="all">Toutes</option>
            <option value="income">Revenus</option>
            <option value="expense">Dépenses</option>
          </select>
          <select value={sortBy} onChange={(e) => setSortBy(e.target.value)}>
            <option value="date">Par Date</option>
            <option value="amount">Par Montant</option>
          </select>
        </div>
      </div>

      <div className="transactions-container">
        {sortedTransactions.length === 0 ? (
          <p className="no-transactions">Aucune transaction trouvée</p>
        ) : (
          <div className="transactions-table">
            {sortedTransactions.map((transaction, index) => (
              <div key={index} className="transaction-row">
                <div className="transaction-main">
                  <div className="transaction-info">
                    {transaction.category && (
                      <span 
                        className="category-badge" 
                        style={{ backgroundColor: transaction.category.color }}
                      >
                        {transaction.category.name}
                      </span>
                    )}
                    <span className="transaction-account">{transaction.account}</span>
                    {transaction.merchant && (
                      <span className="transaction-merchant">• {transaction.merchant}</span>
                    )}
                  </div>
                  <div className="transaction-tags">
                    {transaction.tags && transaction.tags.map((tag, i) => (
                      <span key={i} className="tag">{tag}</span>
                    ))}
                  </div>
                </div>
                <div className="transaction-details">
                  <span className="transaction-date">{transaction.operation_date}</span>
                  <span className={`transaction-amount ${transaction.is_debit ? 'expense' : 'income'}`}>
                    {transaction.is_debit ? '-' : '+'}
                    {Math.abs(transaction.amount).toLocaleString('fr-FR', { minimumFractionDigits: 2 })} {transaction.currency}
                  </span>
                </div>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
};

export default TransactionList;
