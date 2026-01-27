"""Verify the mock transactions data"""
from tests.fixtures.mock_transactions import MOCK_TRANSACTIONS_ENRICHED
from collections import Counter

# Count by IBAN
ibans = [t['iban'] for t in MOCK_TRANSACTIONS_ENRICHED]
counter = Counter(ibans)

print(f"✓ Total transactions: {len(MOCK_TRANSACTIONS_ENRICHED)}")
print(f"\n✓ Breakdown by IBAN:")
for iban, count in sorted(counter.items()):
    # Find account description for this IBAN
    trans = next(t for t in MOCK_TRANSACTIONS_ENRICHED if t['iban'] == iban)
    acc_desc = trans.get('account_description', 'Unknown')
    print(f"  - {iban}: {count} transactions ({acc_desc})")

# New account IBANs
new_ibans = [
    "FR7655555555555555555555555",  # Investment Portfolio
    "GB1234567890123456789012",     # UK Operations
    "CH1234567890123456789"         # Swiss Operations
]

print(f"\n✓ New accounts (should have 10 transactions each):")
for iban in new_ibans:
    count = counter.get(iban, 0)
    trans_list = [t for t in MOCK_TRANSACTIONS_ENRICHED if t['iban'] == iban]
    if trans_list:
        acc_desc = trans_list[0].get('account_description', 'Unknown')
        dates = sorted([t['operation_date'] for t in trans_list])
        print(f"  - {acc_desc}: {count} transactions")
        print(f"    Dates: {dates[0]} to {dates[-1]}")
    else:
        print(f"  - {iban}: NOT FOUND")
