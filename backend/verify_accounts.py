"""Verify the mock accounts data"""
from tests.fixtures.mock_accounts import MOCK_ACCOUNTS_TIMELINE_30_DAYS
from collections import Counter

accounts = [a['account_description'] for a in MOCK_ACCOUNTS_TIMELINE_30_DAYS]
counter = Counter(accounts)

print(f"✓ Total entries in MOCK_ACCOUNTS_TIMELINE_30_DAYS: {len(MOCK_ACCOUNTS_TIMELINE_30_DAYS)}")
print(f"  (Was 90 entries before: 3 accounts × 30 days)")
print(f"\n✓ Breakdown by account:")
for acc, count in sorted(counter.items()):
    print(f"  - {acc}: {count} days")

# Verify date ranges
print(f"\n✓ Verifying date ranges:")
for acc_name in set(accounts):
    acc_entries = [a for a in MOCK_ACCOUNTS_TIMELINE_30_DAYS if a['account_description'] == acc_name]
    dates = sorted([a['date'] for a in acc_entries])
    print(f"  - {acc_name}:")
    print(f"    From {dates[0]} to {dates[-1]} ({len(dates)} days)")
