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

# Historical balance timeline: realistic 30-day progression for frontend BalanceChart
# Shows daily balance evolution with transaction impacts
MOCK_ACCOUNTS_TIMELINE_30_DAYS = [
    # Main Business Account - 30 days progression
    {"account_description": "Main Business Account", "iban": "FR7612345678901234567890123", "holder_company_name": "ACME Corporation", "date": "2026-01-01", "value_balance": 150000.00, "currency": "EUR", "allowed_overdraft": 10000.0},
    {"account_description": "Main Business Account", "iban": "FR7612345678901234567890123", "holder_company_name": "ACME Corporation", "date": "2026-01-02", "value_balance": 156500.00, "currency": "EUR", "allowed_overdraft": 10000.0},  # +6500 salary
    {"account_description": "Main Business Account", "iban": "FR7612345678901234567890123", "holder_company_name": "ACME Corporation", "date": "2026-01-03", "value_balance": 156500.00, "currency": "EUR", "allowed_overdraft": 10000.0},
    {"account_description": "Main Business Account", "iban": "FR7612345678901234567890123", "holder_company_name": "ACME Corporation", "date": "2026-01-04", "value_balance": 156500.00, "currency": "EUR", "allowed_overdraft": 10000.0},
    {"account_description": "Main Business Account", "iban": "FR7612345678901234567890123", "holder_company_name": "ACME Corporation", "date": "2026-01-05", "value_balance": 154000.00, "currency": "EUR", "allowed_overdraft": 10000.0},  # -2500 rent
    {"account_description": "Main Business Account", "iban": "FR7612345678901234567890123", "holder_company_name": "ACME Corporation", "date": "2026-01-06", "value_balance": 153550.00, "currency": "EUR", "allowed_overdraft": 10000.0},  # -450 insurance
    {"account_description": "Main Business Account", "iban": "FR7612345678901234567890123", "holder_company_name": "ACME Corporation", "date": "2026-01-07", "value_balance": 150099.75, "currency": "EUR", "allowed_overdraft": 10000.0},  # -3450.25 supplies
    {"account_description": "Main Business Account", "iban": "FR7612345678901234567890123", "holder_company_name": "ACME Corporation", "date": "2026-01-08", "value_balance": 158849.75, "currency": "EUR", "allowed_overdraft": 10000.0},  # +8750 customer payment
    {"account_description": "Main Business Account", "iban": "FR7612345678901234567890123", "holder_company_name": "ACME Corporation", "date": "2026-01-09", "value_balance": 158849.75, "currency": "EUR", "allowed_overdraft": 10000.0},
    {"account_description": "Main Business Account", "iban": "FR7612345678901234567890123", "holder_company_name": "ACME Corporation", "date": "2026-01-10", "value_balance": 158564.35, "currency": "EUR", "allowed_overdraft": 10000.0},  # -285.40 electricity
    {"account_description": "Main Business Account", "iban": "FR7612345678901234567890123", "holder_company_name": "ACME Corporation", "date": "2026-01-11", "value_balance": 158443.85, "currency": "EUR", "allowed_overdraft": 10000.0},  # -120.50 water
    {"account_description": "Main Business Account", "iban": "FR7612345678901234567890123", "holder_company_name": "ACME Corporation", "date": "2026-01-12", "value_balance": 156593.35, "currency": "EUR", "allowed_overdraft": 10000.0},  # -1850.50 supplies
    {"account_description": "Main Business Account", "iban": "FR7612345678901234567890123", "holder_company_name": "ACME Corporation", "date": "2026-01-13", "value_balance": 156593.35, "currency": "EUR", "allowed_overdraft": 10000.0},
    {"account_description": "Main Business Account", "iban": "FR7612345678901234567890123", "holder_company_name": "ACME Corporation", "date": "2026-01-14", "value_balance": 161823.35, "currency": "EUR", "allowed_overdraft": 10000.0},  # +5230 customer payment
    {"account_description": "Main Business Account", "iban": "FR7612345678901234567890123", "holder_company_name": "ACME Corporation", "date": "2026-01-15", "value_balance": 168323.35, "currency": "EUR", "allowed_overdraft": 10000.0},  # +6500 salary
    {"account_description": "Main Business Account", "iban": "FR7612345678901234567890123", "holder_company_name": "ACME Corporation", "date": "2026-01-16", "value_balance": 168323.35, "currency": "EUR", "allowed_overdraft": 10000.0},
    {"account_description": "Main Business Account", "iban": "FR7612345678901234567890123", "holder_company_name": "ACME Corporation", "date": "2026-01-17", "value_balance": 168323.35, "currency": "EUR", "allowed_overdraft": 10000.0},
    {"account_description": "Main Business Account", "iban": "FR7612345678901234567890123", "holder_company_name": "ACME Corporation", "date": "2026-01-18", "value_balance": 155823.35, "currency": "EUR", "allowed_overdraft": 10000.0},  # -12500 equipment
    {"account_description": "Main Business Account", "iban": "FR7612345678901234567890123", "holder_company_name": "ACME Corporation", "date": "2026-01-19", "value_balance": 155823.35, "currency": "EUR", "allowed_overdraft": 10000.0},
    {"account_description": "Main Business Account", "iban": "FR7612345678901234567890123", "holder_company_name": "ACME Corporation", "date": "2026-01-20", "value_balance": 152623.35, "currency": "EUR", "allowed_overdraft": 10000.0},  # -3200 tax
    {"account_description": "Main Business Account", "iban": "FR7612345678901234567890123", "holder_company_name": "ACME Corporation", "date": "2026-01-21", "value_balance": 152623.35, "currency": "EUR", "allowed_overdraft": 10000.0},
    {"account_description": "Main Business Account", "iban": "FR7612345678901234567890123", "holder_company_name": "ACME Corporation", "date": "2026-01-22", "value_balance": 151772.60, "currency": "EUR", "allowed_overdraft": 10000.0},  # -850.75 travel
    {"account_description": "Main Business Account", "iban": "FR7612345678901234567890123", "holder_company_name": "ACME Corporation", "date": "2026-01-23", "value_balance": 151452.60, "currency": "EUR", "allowed_overdraft": 10000.0},  # -320 hotel
    {"account_description": "Main Business Account", "iban": "FR7612345678901234567890123", "holder_company_name": "ACME Corporation", "date": "2026-01-24", "value_balance": 151452.60, "currency": "EUR", "allowed_overdraft": 10000.0},
    {"account_description": "Main Business Account", "iban": "FR7612345678901234567890123", "holder_company_name": "ACME Corporation", "date": "2026-01-25", "value_balance": 151452.60, "currency": "EUR", "allowed_overdraft": 10000.0},
    {"account_description": "Main Business Account", "iban": "FR7612345678901234567890123", "holder_company_name": "ACME Corporation", "date": "2026-01-26", "value_balance": 151452.60, "currency": "EUR", "allowed_overdraft": 10000.0},
    {"account_description": "Main Business Account", "iban": "FR7612345678901234567890123", "holder_company_name": "ACME Corporation", "date": "2026-01-27", "value_balance": 151452.60, "currency": "EUR", "allowed_overdraft": 10000.0},
    {"account_description": "Main Business Account", "iban": "FR7612345678901234567890123", "holder_company_name": "ACME Corporation", "date": "2026-01-28", "value_balance": 151452.60, "currency": "EUR", "allowed_overdraft": 10000.0},
    {"account_description": "Main Business Account", "iban": "FR7612345678901234567890123", "holder_company_name": "ACME Corporation", "date": "2026-01-29", "value_balance": 151452.60, "currency": "EUR", "allowed_overdraft": 10000.0},
    {"account_description": "Main Business Account", "iban": "FR7612345678901234567890123", "holder_company_name": "ACME Corporation", "date": "2026-01-30", "value_balance": 151452.60, "currency": "EUR", "allowed_overdraft": 10000.0},
    {"account_description": "Main Business Account", "iban": "FR7612345678901234567890123", "holder_company_name": "ACME Corporation", "date": "2026-01-31", "value_balance": 151417.60, "currency": "EUR", "allowed_overdraft": 10000.0},  # -35 bank fees
    
    # Savings Account - 30 days progression (mostly stable with occasional growth)
    {"account_description": "Savings Account", "iban": "FR7698765432109876543210987", "holder_company_name": "ACME Corporation", "date": "2026-01-01", "value_balance": 500000.00, "currency": "EUR", "allowed_overdraft": 0.0},
    {"account_description": "Savings Account", "iban": "FR7698765432109876543210987", "holder_company_name": "ACME Corporation", "date": "2026-01-02", "value_balance": 500000.00, "currency": "EUR", "allowed_overdraft": 0.0},
    {"account_description": "Savings Account", "iban": "FR7698765432109876543210987", "holder_company_name": "ACME Corporation", "date": "2026-01-03", "value_balance": 500000.00, "currency": "EUR", "allowed_overdraft": 0.0},
    {"account_description": "Savings Account", "iban": "FR7698765432109876543210987", "holder_company_name": "ACME Corporation", "date": "2026-01-04", "value_balance": 500000.00, "currency": "EUR", "allowed_overdraft": 0.0},
    {"account_description": "Savings Account", "iban": "FR7698765432109876543210987", "holder_company_name": "ACME Corporation", "date": "2026-01-05", "value_balance": 500083.33, "currency": "EUR", "allowed_overdraft": 0.0},  # +83.33 interest
    {"account_description": "Savings Account", "iban": "FR7698765432109876543210987", "holder_company_name": "ACME Corporation", "date": "2026-01-06", "value_balance": 500083.33, "currency": "EUR", "allowed_overdraft": 0.0},
    {"account_description": "Savings Account", "iban": "FR7698765432109876543210987", "holder_company_name": "ACME Corporation", "date": "2026-01-07", "value_balance": 500083.33, "currency": "EUR", "allowed_overdraft": 0.0},
    {"account_description": "Savings Account", "iban": "FR7698765432109876543210987", "holder_company_name": "ACME Corporation", "date": "2026-01-08", "value_balance": 500083.33, "currency": "EUR", "allowed_overdraft": 0.0},
    {"account_description": "Savings Account", "iban": "FR7698765432109876543210987", "holder_company_name": "ACME Corporation", "date": "2026-01-09", "value_balance": 500083.33, "currency": "EUR", "allowed_overdraft": 0.0},
    {"account_description": "Savings Account", "iban": "FR7698765432109876543210987", "holder_company_name": "ACME Corporation", "date": "2026-01-10", "value_balance": 500166.66, "currency": "EUR", "allowed_overdraft": 0.0},  # +83.33 interest
    {"account_description": "Savings Account", "iban": "FR7698765432109876543210987", "holder_company_name": "ACME Corporation", "date": "2026-01-11", "value_balance": 500166.66, "currency": "EUR", "allowed_overdraft": 0.0},
    {"account_description": "Savings Account", "iban": "FR7698765432109876543210987", "holder_company_name": "ACME Corporation", "date": "2026-01-12", "value_balance": 500166.66, "currency": "EUR", "allowed_overdraft": 0.0},
    {"account_description": "Savings Account", "iban": "FR7698765432109876543210987", "holder_company_name": "ACME Corporation", "date": "2026-01-13", "value_balance": 500166.66, "currency": "EUR", "allowed_overdraft": 0.0},
    {"account_description": "Savings Account", "iban": "FR7698765432109876543210987", "holder_company_name": "ACME Corporation", "date": "2026-01-14", "value_balance": 500166.66, "currency": "EUR", "allowed_overdraft": 0.0},
    {"account_description": "Savings Account", "iban": "FR7698765432109876543210987", "holder_company_name": "ACME Corporation", "date": "2026-01-15", "value_balance": 500249.99, "currency": "EUR", "allowed_overdraft": 0.0},  # +83.33 interest
    {"account_description": "Savings Account", "iban": "FR7698765432109876543210987", "holder_company_name": "ACME Corporation", "date": "2026-01-16", "value_balance": 500249.99, "currency": "EUR", "allowed_overdraft": 0.0},
    {"account_description": "Savings Account", "iban": "FR7698765432109876543210987", "holder_company_name": "ACME Corporation", "date": "2026-01-17", "value_balance": 500249.99, "currency": "EUR", "allowed_overdraft": 0.0},
    {"account_description": "Savings Account", "iban": "FR7698765432109876543210987", "holder_company_name": "ACME Corporation", "date": "2026-01-18", "value_balance": 500249.99, "currency": "EUR", "allowed_overdraft": 0.0},
    {"account_description": "Savings Account", "iban": "FR7698765432109876543210987", "holder_company_name": "ACME Corporation", "date": "2026-01-19", "value_balance": 500249.99, "currency": "EUR", "allowed_overdraft": 0.0},
    {"account_description": "Savings Account", "iban": "FR7698765432109876543210987", "holder_company_name": "ACME Corporation", "date": "2026-01-20", "value_balance": 500333.32, "currency": "EUR", "allowed_overdraft": 0.0},  # +83.33 interest
    {"account_description": "Savings Account", "iban": "FR7698765432109876543210987", "holder_company_name": "ACME Corporation", "date": "2026-01-21", "value_balance": 500333.32, "currency": "EUR", "allowed_overdraft": 0.0},
    {"account_description": "Savings Account", "iban": "FR7698765432109876543210987", "holder_company_name": "ACME Corporation", "date": "2026-01-22", "value_balance": 500333.32, "currency": "EUR", "allowed_overdraft": 0.0},
    {"account_description": "Savings Account", "iban": "FR7698765432109876543210987", "holder_company_name": "ACME Corporation", "date": "2026-01-23", "value_balance": 500333.32, "currency": "EUR", "allowed_overdraft": 0.0},
    {"account_description": "Savings Account", "iban": "FR7698765432109876543210987", "holder_company_name": "ACME Corporation", "date": "2026-01-24", "value_balance": 500333.32, "currency": "EUR", "allowed_overdraft": 0.0},
    {"account_description": "Savings Account", "iban": "FR7698765432109876543210987", "holder_company_name": "ACME Corporation", "date": "2026-01-25", "value_balance": 501583.32, "currency": "EUR", "allowed_overdraft": 0.0},  # +1250 investment return
    {"account_description": "Savings Account", "iban": "FR7698765432109876543210987", "holder_company_name": "ACME Corporation", "date": "2026-01-26", "value_balance": 501583.32, "currency": "EUR", "allowed_overdraft": 0.0},
    {"account_description": "Savings Account", "iban": "FR7698765432109876543210987", "holder_company_name": "ACME Corporation", "date": "2026-01-27", "value_balance": 501583.32, "currency": "EUR", "allowed_overdraft": 0.0},
    {"account_description": "Savings Account", "iban": "FR7698765432109876543210987", "holder_company_name": "ACME Corporation", "date": "2026-01-28", "value_balance": 501583.32, "currency": "EUR", "allowed_overdraft": 0.0},
    {"account_description": "Savings Account", "iban": "FR7698765432109876543210987", "holder_company_name": "ACME Corporation", "date": "2026-01-29", "value_balance": 501583.32, "currency": "EUR", "allowed_overdraft": 0.0},
    {"account_description": "Savings Account", "iban": "FR7698765432109876543210987", "holder_company_name": "ACME Corporation", "date": "2026-01-30", "value_balance": 501583.32, "currency": "EUR", "allowed_overdraft": 0.0},
    {"account_description": "Savings Account", "iban": "FR7698765432109876543210987", "holder_company_name": "ACME Corporation", "date": "2026-01-31", "value_balance": 501583.32, "currency": "EUR", "allowed_overdraft": 0.0},
    
    # USD Operating Account - 30 days progression
    {"account_description": "USD Operating Account", "iban": "US1234567890123456789012345", "holder_company_name": "ACME USA Inc", "date": "2026-01-01", "value_balance": 75000.00, "currency": "USD", "allowed_overdraft": 5000.0},
    {"account_description": "USD Operating Account", "iban": "US1234567890123456789012345", "holder_company_name": "ACME USA Inc", "date": "2026-01-02", "value_balance": 75000.00, "currency": "USD", "allowed_overdraft": 5000.0},
    {"account_description": "USD Operating Account", "iban": "US1234567890123456789012345", "holder_company_name": "ACME USA Inc", "date": "2026-01-03", "value_balance": 79500.00, "currency": "USD", "allowed_overdraft": 5000.0},  # +4500 customer
    {"account_description": "USD Operating Account", "iban": "US1234567890123456789012345", "holder_company_name": "ACME USA Inc", "date": "2026-01-04", "value_balance": 79500.00, "currency": "USD", "allowed_overdraft": 5000.0},
    {"account_description": "USD Operating Account", "iban": "US1234567890123456789012345", "holder_company_name": "ACME USA Inc", "date": "2026-01-05", "value_balance": 79500.00, "currency": "USD", "allowed_overdraft": 5000.0},
    {"account_description": "USD Operating Account", "iban": "US1234567890123456789012345", "holder_company_name": "ACME USA Inc", "date": "2026-01-06", "value_balance": 79500.00, "currency": "USD", "allowed_overdraft": 5000.0},
    {"account_description": "USD Operating Account", "iban": "US1234567890123456789012345", "holder_company_name": "ACME USA Inc", "date": "2026-01-07", "value_balance": 79500.00, "currency": "USD", "allowed_overdraft": 5000.0},
    {"account_description": "USD Operating Account", "iban": "US1234567890123456789012345", "holder_company_name": "ACME USA Inc", "date": "2026-01-08", "value_balance": 79500.00, "currency": "USD", "allowed_overdraft": 5000.0},
    {"account_description": "USD Operating Account", "iban": "US1234567890123456789012345", "holder_company_name": "ACME USA Inc", "date": "2026-01-09", "value_balance": 78300.00, "currency": "USD", "allowed_overdraft": 5000.0},  # -1200 supplier
    {"account_description": "USD Operating Account", "iban": "US1234567890123456789012345", "holder_company_name": "ACME USA Inc", "date": "2026-01-10", "value_balance": 78300.00, "currency": "USD", "allowed_overdraft": 5000.0},
    {"account_description": "USD Operating Account", "iban": "US1234567890123456789012345", "holder_company_name": "ACME USA Inc", "date": "2026-01-11", "value_balance": 78300.00, "currency": "USD", "allowed_overdraft": 5000.0},
    {"account_description": "USD Operating Account", "iban": "US1234567890123456789012345", "holder_company_name": "ACME USA Inc", "date": "2026-01-12", "value_balance": 78300.00, "currency": "USD", "allowed_overdraft": 5000.0},
    {"account_description": "USD Operating Account", "iban": "US1234567890123456789012345", "holder_company_name": "ACME USA Inc", "date": "2026-01-13", "value_balance": 78300.00, "currency": "USD", "allowed_overdraft": 5000.0},
    {"account_description": "USD Operating Account", "iban": "US1234567890123456789012345", "holder_company_name": "ACME USA Inc", "date": "2026-01-14", "value_balance": 78300.00, "currency": "USD", "allowed_overdraft": 5000.0},
    {"account_description": "USD Operating Account", "iban": "US1234567890123456789012345", "holder_company_name": "ACME USA Inc", "date": "2026-01-15", "value_balance": 78300.00, "currency": "USD", "allowed_overdraft": 5000.0},
    {"account_description": "USD Operating Account", "iban": "US1234567890123456789012345", "holder_company_name": "ACME USA Inc", "date": "2026-01-16", "value_balance": 76500.00, "currency": "USD", "allowed_overdraft": 5000.0},  # -1800 rent
    {"account_description": "USD Operating Account", "iban": "US1234567890123456789012345", "holder_company_name": "ACME USA Inc", "date": "2026-01-17", "value_balance": 76500.00, "currency": "USD", "allowed_overdraft": 5000.0},
    {"account_description": "USD Operating Account", "iban": "US1234567890123456789012345", "holder_company_name": "ACME USA Inc", "date": "2026-01-18", "value_balance": 76500.00, "currency": "USD", "allowed_overdraft": 5000.0},
    {"account_description": "USD Operating Account", "iban": "US1234567890123456789012345", "holder_company_name": "ACME USA Inc", "date": "2026-01-19", "value_balance": 76500.00, "currency": "USD", "allowed_overdraft": 5000.0},
    {"account_description": "USD Operating Account", "iban": "US1234567890123456789012345", "holder_company_name": "ACME USA Inc", "date": "2026-01-20", "value_balance": 76500.00, "currency": "USD", "allowed_overdraft": 5000.0},
    {"account_description": "USD Operating Account", "iban": "US1234567890123456789012345", "holder_company_name": "ACME USA Inc", "date": "2026-01-21", "value_balance": 76500.00, "currency": "USD", "allowed_overdraft": 5000.0},
    {"account_description": "USD Operating Account", "iban": "US1234567890123456789012345", "holder_company_name": "ACME USA Inc", "date": "2026-01-22", "value_balance": 76500.00, "currency": "USD", "allowed_overdraft": 5000.0},
    {"account_description": "USD Operating Account", "iban": "US1234567890123456789012345", "holder_company_name": "ACME USA Inc", "date": "2026-01-23", "value_balance": 76500.00, "currency": "USD", "allowed_overdraft": 5000.0},
    {"account_description": "USD Operating Account", "iban": "US1234567890123456789012345", "holder_company_name": "ACME USA Inc", "date": "2026-01-24", "value_balance": 76500.00, "currency": "USD", "allowed_overdraft": 5000.0},
    {"account_description": "USD Operating Account", "iban": "US1234567890123456789012345", "holder_company_name": "ACME USA Inc", "date": "2026-01-25", "value_balance": 76500.00, "currency": "USD", "allowed_overdraft": 5000.0},
    {"account_description": "USD Operating Account", "iban": "US1234567890123456789012345", "holder_company_name": "ACME USA Inc", "date": "2026-01-26", "value_balance": 76500.00, "currency": "USD", "allowed_overdraft": 5000.0},
    {"account_description": "USD Operating Account", "iban": "US1234567890123456789012345", "holder_company_name": "ACME USA Inc", "date": "2026-01-27", "value_balance": 76500.00, "currency": "USD", "allowed_overdraft": 5000.0},
    {"account_description": "USD Operating Account", "iban": "US1234567890123456789012345", "holder_company_name": "ACME USA Inc", "date": "2026-01-28", "value_balance": 76500.00, "currency": "USD", "allowed_overdraft": 5000.0},
    {"account_description": "USD Operating Account", "iban": "US1234567890123456789012345", "holder_company_name": "ACME USA Inc", "date": "2026-01-29", "value_balance": 76500.00, "currency": "USD", "allowed_overdraft": 5000.0},
    {"account_description": "USD Operating Account", "iban": "US1234567890123456789012345", "holder_company_name": "ACME USA Inc", "date": "2026-01-30", "value_balance": 76500.00, "currency": "USD", "allowed_overdraft": 5000.0},
    {"account_description": "USD Operating Account", "iban": "US1234567890123456789012345", "holder_company_name": "ACME USA Inc", "date": "2026-01-31", "value_balance": 76500.00, "currency": "USD", "allowed_overdraft": 5000.0},
]

# Diverse account types for testing different scenarios
MOCK_ACCOUNTS_DIVERSE_TYPES = [
    # Standard business account
    {
        "account_description": "Main Business Account",
        "iban": "FR7612345678901234567890123",
        "holder_company_name": "ACME Corporation",
        "date": "2026-01-26",
        "value_balance": 151417.60,
        "currency": "EUR",
        "allowed_overdraft": 10000.0,
    },
    # Savings account
    {
        "account_description": "Savings Account",
        "iban": "FR7698765432109876543210987",
        "holder_company_name": "ACME Corporation",
        "date": "2026-01-26",
        "value_balance": 501583.32,
        "currency": "EUR",
        "allowed_overdraft": 0.0,
    },
    # Credit card account (negative balance = credit used)
    {
        "account_description": "Business Credit Card",
        "iban": "FR7633333333333333333333333",
        "holder_company_name": "ACME Corporation",
        "date": "2026-01-26",
        "value_balance": -3500.00,
        "currency": "EUR",
        "allowed_overdraft": 50000.0,
    },
    # Line of credit
    {
        "account_description": "Business Line of Credit",
        "iban": "FR7644444444444444444444444",
        "holder_company_name": "ACME Corporation",
        "date": "2026-01-26",
        "value_balance": -25000.00,
        "currency": "EUR",
        "allowed_overdraft": 100000.0,
    },
    # Investment account
    {
        "account_description": "Investment Portfolio Account",
        "iban": "FR7655555555555555555555555",
        "holder_company_name": "ACME Corporation",
        "date": "2026-01-26",
        "value_balance": 250000.00,
        "currency": "EUR",
        "allowed_overdraft": 0.0,
    },
    # Multi-currency account (GBP)
    {
        "account_description": "UK Operations Account",
        "iban": "GB1234567890123456789012",
        "holder_company_name": "ACME UK Ltd",
        "date": "2026-01-26",
        "value_balance": 45000.00,
        "currency": "GBP",
        "allowed_overdraft": 5000.0,
    },
    # Multi-currency account (CHF)
    {
        "account_description": "Swiss Account",
        "iban": "CH1234567890123456789",
        "holder_company_name": "ACME Switzerland SA",
        "date": "2026-01-26",
        "value_balance": 80000.00,
        "currency": "CHF",
        "allowed_overdraft": 0.0,
    },
    # Payroll account
    {
        "account_description": "Payroll Account",
        "iban": "FR7666666666666666666666666",
        "holder_company_name": "ACME Corporation",
        "date": "2026-01-26",
        "value_balance": 120000.00,
        "currency": "EUR",
        "allowed_overdraft": 0.0,
    },
]

