"""Mock transaction data for testing."""

from datetime import datetime, timedelta
from typing import List, Dict, Any
import random


def generate_mock_transactions(
    start_date: str = "2026-01-01",
    end_date: str = "2026-01-31",
    num_transactions: int = 50,
) -> List[Dict[str, Any]]:
    """Generate mock transaction data for testing.
    
    Args:
        start_date: Start date in YYYY-MM-DD format.
        end_date: End date in YYYY-MM-DD format.
        num_transactions: Number of transactions to generate.
    
    Returns:
        List of transaction dictionaries.
    """
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    date_range = (end - start).days
    
    transactions = []
    
    # Define transaction categories with realistic amounts
    transaction_types = [
        {"description": "Salary Payment", "min": 3000, "max": 8000, "is_debit": False},
        {"description": "Rent Payment", "min": 1500, "max": 3000, "is_debit": True},
        {"description": "Supplier Payment", "min": 500, "max": 5000, "is_debit": True},
        {"description": "Customer Payment", "min": 1000, "max": 10000, "is_debit": False},
        {"description": "Utility Bill", "min": 100, "max": 500, "is_debit": True},
        {"description": "Bank Fees", "min": 10, "max": 50, "is_debit": True},
        {"description": "Investment Return", "min": 500, "max": 2000, "is_debit": False},
        {"description": "Tax Payment", "min": 1000, "max": 5000, "is_debit": True},
    ]
    
    accounts = [
        {
            "account_description": "Main Business Account",
            "iban": "FR7612345678901234567890123",
            "holder_company_name": "ACME Corporation",
            "currency": "EUR",
        },
        {
            "account_description": "Savings Account",
            "iban": "FR7698765432109876543210987",
            "holder_company_name": "ACME Corporation",
            "currency": "EUR",
        },
        {
            "account_description": "USD Operating Account",
            "iban": "US1234567890123456789012345",
            "holder_company_name": "ACME USA Inc",
            "currency": "USD",
        },
    ]
    
    for _ in range(num_transactions):
        # Random date within range
        random_days = random.randint(0, max(0, date_range))
        operation_date = start + timedelta(days=random_days)
        
        # Value date could be same or 1-2 days after operation date
        value_date = operation_date + timedelta(days=random.randint(0, 2))
        
        # Select random transaction type and account
        trans_type = random.choice(transaction_types)
        account = random.choice(accounts)
        
        amount = round(random.uniform(trans_type["min"], trans_type["max"]), 2)
        
        transactions.append({
            "account_description": account["account_description"],
            "iban": account["iban"],
            "holder_company_name": account["holder_company_name"],
            "operation_date": operation_date.strftime("%Y-%m-%d"),
            "value_date": value_date.strftime("%Y-%m-%d"),
            "amount": amount,
            "currency": account["currency"],
            "is_debit": trans_type["is_debit"],
        })
    
    # Sort by operation date
    transactions.sort(key=lambda x: x["operation_date"])
    
    return transactions


# Pre-generated mock data for common test scenarios
MOCK_TRANSACTIONS_SAMPLE = [
    {
        "account_description": "Main Business Account",
        "iban": "FR7612345678901234567890123",
        "holder_company_name": "ACME Corporation",
        "operation_date": "2026-01-05",
        "value_date": "2026-01-05",
        "amount": 5000.00,
        "currency": "EUR",
        "is_debit": False,
    },
    {
        "account_description": "Main Business Account",
        "iban": "FR7612345678901234567890123",
        "holder_company_name": "ACME Corporation",
        "operation_date": "2026-01-07",
        "value_date": "2026-01-07",
        "amount": 1500.75,
        "currency": "EUR",
        "is_debit": True,
    },
    {
        "account_description": "Main Business Account",
        "iban": "FR7612345678901234567890123",
        "holder_company_name": "ACME Corporation",
        "operation_date": "2026-01-10",
        "value_date": "2026-01-11",
        "amount": 3200.50,
        "currency": "EUR",
        "is_debit": False,
    },
    {
        "account_description": "Savings Account",
        "iban": "FR7698765432109876543210987",
        "holder_company_name": "ACME Corporation",
        "operation_date": "2026-01-12",
        "value_date": "2026-01-12",
        "amount": 10000.00,
        "currency": "EUR",
        "is_debit": False,
    },
    {
        "account_description": "USD Operating Account",
        "iban": "US1234567890123456789012345",
        "holder_company_name": "ACME USA Inc",
        "operation_date": "2026-01-15",
        "value_date": "2026-01-15",
        "amount": 2500.00,
        "currency": "USD",
        "is_debit": True,
    },
]

MOCK_TRANSACTIONS_EMPTY = []

# Mock transactions with edge cases
MOCK_TRANSACTIONS_EDGE_CASES = [
    {
        "account_description": "Test Account",
        "iban": "FR7600000000000000000000000",
        "holder_company_name": "Test Company",
        "operation_date": "2026-01-15",
        "value_date": "2026-01-15",
        "amount": 0.01,  # Minimal amount
        "currency": "EUR",
        "is_debit": True,
    },
    {
        "account_description": "Test Account",
        "iban": "FR7600000000000000000000000",
        "holder_company_name": "Test Company",
        "operation_date": "2026-01-16",
        "value_date": "2026-01-20",  # Large value date difference
        "amount": 999999.99,  # Large amount
        "currency": "EUR",
        "is_debit": False,
    },
    {
        "account_description": "Test Account",
        "iban": "FR7600000000000000000000000",
        "holder_company_name": "Test Company",
        "operation_date": "2026-01-17",
        "value_date": "2026-01-17",
        "amount": 0.0,  # Zero amount
        "currency": "EUR",
        "is_debit": True,
    },
]
