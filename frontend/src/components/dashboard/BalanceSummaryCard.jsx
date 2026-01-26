import './BalanceSummaryCard.css';

const BalanceSummaryCard = ({ summary }) => {
  if (!summary) return null;

  return (
    <div className="balance-summary-card">
      <div className="summary-header">
        <h2>Résumé des Soldes</h2>
        <span className="summary-date">{summary.date}</span>
      </div>
      
      <div className="summary-main">
        <div className="total-balance">
          <span className="label">Solde Total</span>
          <span className="value">
            {summary.total_balance.toLocaleString('fr-FR', { minimumFractionDigits: 2 })} {summary.currency}
          </span>
        </div>
      </div>

      <div className="summary-grid">
        <div className="summary-item">
          <span className="item-label">Nombre de Comptes</span>
          <span className="item-value">{summary.account_count}</span>
        </div>
        <div className="summary-item">
          <span className="item-label">Solde Moyen</span>
          <span className="item-value">
            {summary.average_balance.toLocaleString('fr-FR', { minimumFractionDigits: 2 })} {summary.currency}
          </span>
        </div>
        <div className="summary-item">
          <span className="item-label">Solde Maximum</span>
          <span className="item-value">
            {summary.highest_balance.toLocaleString('fr-FR', { minimumFractionDigits: 2 })} {summary.currency}
          </span>
        </div>
        <div className="summary-item">
          <span className="item-label">Solde Minimum</span>
          <span className="item-value">
            {summary.lowest_balance.toLocaleString('fr-FR', { minimumFractionDigits: 2 })} {summary.currency}
          </span>
        </div>
        <div className="summary-item">
          <span className="item-label">Découvert Autorisé Total</span>
          <span className="item-value">
            {summary.total_overdraft_allowed.toLocaleString('fr-FR', { minimumFractionDigits: 2 })} {summary.currency}
          </span>
        </div>
      </div>
    </div>
  );
};

export default BalanceSummaryCard;
