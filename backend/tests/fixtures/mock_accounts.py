"""Mock account data for testing."""

from datetime import datetime, timedelta
from typing import List, Dict, Any


def generate_mock_accounts(start_date: str = "2026-01-01", days: int = 30) -> List[Dict[str, Any]]:
    """Generate mock account data for testing.
    
    Args:
        start_date: Start date in YYYY-MM-DD format.
        days: Number of days to generate data for.
    
    Returns:
        List of account dictionaries.
    """
    start = datetime.strptime(start_date, "%Y-%m-%d")
    accounts = []
    
    # Define multiple accounts
    account_configs = [
        {
            "account_description": "Main Business Account",
            "iban": "FR7612345678901234567890123",
            "holder_company_name": "ACME Corporation",
            "currency": "EUR",
            "initial_balance": 150000.00,
            "allowed_overdraft": 10000.0,
            "daily_change": lambda day: -1500 + (day % 7) * 500,  # Vary by day of week
        },
        {
            "account_description": "Savings Account",
            "iban": "FR7698765432109876543210987",
            "holder_company_name": "ACME Corporation",
            "currency": "EUR",
            "initial_balance": 500000.00,
            "allowed_overdraft": 0.0,
            "daily_change": lambda day: 200 if day % 5 == 0 else 0,  # Growth every 5 days
        },
        {
            "account_description": "USD Operating Account",
            "iban": "US1234567890123456789012345",
            "holder_company_name": "ACME USA Inc",
            "currency": "USD",
            "initial_balance": 75000.00,
            "allowed_overdraft": 5000.0,
            "daily_change": lambda day: -800 + (day % 10) * 300,
        },
    ]
    
    for account_config in account_configs:
        balance = account_config["initial_balance"]
        
        for day in range(days):
            current_date = start + timedelta(days=day)
            balance += account_config["daily_change"](day)
            
            accounts.append({
                "account_description": account_config["account_description"],
                "iban": account_config["iban"],
                "holder_company_name": account_config["holder_company_name"],
                "date": current_date.strftime("%Y-%m-%d"),
                "value_balance": round(balance, 2),
                "currency": account_config["currency"],
                "allowed_overdraft": account_config["allowed_overdraft"],
            })
    
    return accounts


# Pre-generated mock data for common test scenarios
MOCK_ACCOUNTS_SINGLE_DAY = [
    {
        "account_description": "Main Business Account",
        "iban": "FR7612345678901234567890123",
        "holder_company_name": "ACME Corporation",
        "date": "2026-01-15",
        "value_balance": 150000.50,
        "currency": "EUR",
        "allowed_overdraft": 10000.0,
    },
    {
        "account_description": "Savings Account",
        "iban": "FR7698765432109876543210987",
        "holder_company_name": "ACME Corporation",
        "date": "2026-01-15",
        "value_balance": 500000.00,
        "currency": "EUR",
        "allowed_overdraft": 0.0,
    },
    {
        "account_description": "USD Operating Account",
        "iban": "US1234567890123456789012345",
        "holder_company_name": "ACME USA Inc",
        "date": "2026-01-15",
        "value_balance": 75000.00,
        "currency": "USD",
        "allowed_overdraft": 5000.0,
    },
]

MOCK_ACCOUNTS_EMPTY = []

# Mock accounts with edge cases
MOCK_ACCOUNTS_EDGE_CASES = [
    {
        "account_description": "Zero Balance Account",
        "iban": "FR7600000000000000000000000",
        "holder_company_name": "Test Company",
        "date": "2026-01-15",
        "value_balance": 0.0,
        "currency": "EUR",
        "allowed_overdraft": 0.0,
    },
    {
        "account_description": "Negative Balance Account",
        "iban": "FR7611111111111111111111111",
        "holder_company_name": "Test Company",
        "date": "2026-01-15",
        "value_balance": -5000.00,
        "currency": "EUR",
        "allowed_overdraft": 10000.0,
    },
    {
        "account_description": "Large Balance Account",
        "iban": "FR7622222222222222222222222",
        "holder_company_name": "Big Corporation",
        "date": "2026-01-15",
        "value_balance": 9999999.99,
        "currency": "EUR",
        "allowed_overdraft": 100000.0,
    },
]
