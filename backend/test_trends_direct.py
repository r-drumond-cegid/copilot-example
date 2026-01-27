"""Test direct du calcul des tendances"""
import sys
sys.path.insert(0, ".")

from datetime import datetime
from app.services.analytics import calculate_transaction_trends
from tests.fixtures.mock_transactions import MOCK_TRANSACTIONS_ENRICHED
from app.models.transaction import EnrichedTransaction, TransactionCategory

# Transformer les données mock
print("\n=== TRANSFORMATION DES DONNÉES ===")
enriched_objs = []
for i, trans in enumerate(MOCK_TRANSACTIONS_ENRICHED[:5]):  # Premiers 5 pour debug
    print(f"\nTransaction {i+1}:")
    print(f"  Date: {trans['operation_date']}")
    print(f"  Amount: {trans['amount']}")
    print(f"  Is_debit: {trans['is_debit']}")
    print(f"  Category: {trans.get('category', {}).get('name', 'N/A')}")
    
    trans_copy = trans.copy()
    if 'account_description' in trans_copy:
        trans_copy['account'] = trans_copy.pop('account_description')
    if 'holder_company_name' in trans_copy:
        trans_copy['company'] = trans_copy.pop('holder_company_name')
    
    # Convertir category dict en objet
    if 'category' in trans_copy and isinstance(trans_copy['category'], dict):
        trans_copy['category'] = TransactionCategory(**trans_copy['category'])
    
    enriched_objs.append(EnrichedTransaction(**trans_copy))

# Filtrer par date (Dec 2025 - Jan 2026)
print("\n=== FILTRAGE PAR DATE ===")
from_date = "2025-12-01"
to_date = "2026-01-27"
start = datetime.strptime(from_date, "%Y-%m-%d")
end = datetime.strptime(to_date, "%Y-%m-%d")

filtered = [
    t for t in enriched_objs
    if start <= datetime.strptime(t.operation_date, "%Y-%m-%d") <= end
]

print(f"Transactions filtrées: {len(filtered)} sur {len(enriched_objs)}")

# Calculer les tendances
print("\n=== CALCUL DES TENDANCES ===")
trends = calculate_transaction_trends(filtered)
print(f"Transaction count: {trends['transaction_count']}")
print(f"Total income: {trends['total_income']} EUR")
print(f"Total expenses: {trends['total_expenses']} EUR")
print(f"Net flow: {trends['net_flow']} EUR")
