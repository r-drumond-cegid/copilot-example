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
        # Income types
        {"description": "Salary Payment", "min": 3000, "max": 8000, "is_debit": False},
        {"description": "Customer Payment", "min": 1000, "max": 10000, "is_debit": False},
        {"description": "Investment Return", "min": 500, "max": 2000, "is_debit": False},
        {"description": "Interest Income", "min": 50, "max": 300, "is_debit": False},
        {"description": "Refund", "min": 100, "max": 800, "is_debit": False},
        {"description": "Commission", "min": 200, "max": 1500, "is_debit": False},
        # Expense types
        {"description": "Rent Payment", "min": 1500, "max": 3000, "is_debit": True},
        {"description": "Supplier Payment", "min": 500, "max": 5000, "is_debit": True},
        {"description": "Utility Bill", "min": 100, "max": 500, "is_debit": True},
        {"description": "Bank Fees", "min": 10, "max": 50, "is_debit": True},
        {"description": "Tax Payment", "min": 1000, "max": 5000, "is_debit": True},
        {"description": "Insurance Premium", "min": 200, "max": 800, "is_debit": True},
        {"description": "Subscription Service", "min": 20, "max": 200, "is_debit": True},
        {"description": "ATM Withdrawal", "min": 50, "max": 500, "is_debit": True},
        {"description": "Card Payment", "min": 15, "max": 300, "is_debit": True},
        {"description": "Direct Debit", "min": 30, "max": 400, "is_debit": True},
        {"description": "Wire Transfer", "min": 1000, "max": 15000, "is_debit": True},
        {"description": "Check Payment", "min": 200, "max": 3000, "is_debit": True},
        {"description": "Equipment Purchase", "min": 500, "max": 20000, "is_debit": True},
        {"description": "Travel Expense", "min": 100, "max": 2000, "is_debit": True},
        {"description": "Office Supplies", "min": 50, "max": 800, "is_debit": True},
        {"description": "Marketing Expense", "min": 300, "max": 5000, "is_debit": True},
        {"description": "Legal Fees", "min": 500, "max": 3000, "is_debit": True},
        {"description": "Accounting Services", "min": 300, "max": 1500, "is_debit": True},
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

# Enriched transactions with full category, merchant, and tags data
# Supports frontend components: CategoryChart, TransactionList
MOCK_TRANSACTIONS_ENRICHED = [
    # Salary/Income transactions
    {
        "account_description": "Main Business Account",
        "iban": "FR7612345678901234567890123",
        "holder_company_name": "ACME Corporation",
        "operation_date": "2026-01-01",
        "value_date": "2026-01-01",
        "amount": 6500.00,
        "currency": "EUR",
        "is_debit": False,
        "category": {
            "id": "salary",
            "name": "Salaire",
            "icon": "money-bill-wave",
            "color": "#28a745",
            "description": "Revenus salariaux"
        },
        "merchant": "Payroll Department",
        "tags": ["income", "large", "recurring"]
    },
    {
        "account_description": "Main Business Account",
        "iban": "FR7612345678901234567890123",
        "holder_company_name": "ACME Corporation",
        "operation_date": "2026-01-15",
        "value_date": "2026-01-15",
        "amount": 6500.00,
        "currency": "EUR",
        "is_debit": False,
        "category": {
            "id": "salary",
            "name": "Salaire",
            "icon": "money-bill-wave",
            "color": "#28a745",
            "description": "Revenus salariaux"
        },
        "merchant": "Payroll Department",
        "tags": ["income", "large", "recurring"]
    },
    # Rent payments
    {
        "account_description": "Main Business Account",
        "iban": "FR7612345678901234567890123",
        "holder_company_name": "ACME Corporation",
        "operation_date": "2026-01-05",
        "value_date": "2026-01-05",
        "amount": 2500.00,
        "currency": "EUR",
        "is_debit": True,
        "category": {
            "id": "rent",
            "name": "Loyer",
            "icon": "building",
            "color": "#17a2b8",
            "description": "Loyers et charges"
        },
        "merchant": "Paris Office Landlord",
        "tags": ["expense", "large", "recurring"]
    },
    # Supplier payments
    {
        "account_description": "Main Business Account",
        "iban": "FR7612345678901234567890123",
        "holder_company_name": "ACME Corporation",
        "operation_date": "2026-01-07",
        "value_date": "2026-01-07",
        "amount": 3450.25,
        "currency": "EUR",
        "is_debit": True,
        "category": {
            "id": "supplies",
            "name": "Fournitures",
            "icon": "box",
            "color": "#6c757d",
            "description": "Achats et fournitures"
        },
        "merchant": "Office Supplies Co.",
        "tags": ["expense", "business"]
    },
    {
        "account_description": "Main Business Account",
        "iban": "FR7612345678901234567890123",
        "holder_company_name": "ACME Corporation",
        "operation_date": "2026-01-12",
        "value_date": "2026-01-12",
        "amount": 1850.50,
        "currency": "EUR",
        "is_debit": True,
        "category": {
            "id": "supplies",
            "name": "Fournitures",
            "icon": "box",
            "color": "#6c757d",
            "description": "Achats et fournitures"
        },
        "merchant": "Tech Supplies Ltd",
        "tags": ["expense", "business"]
    },
    # Customer payments
    {
        "account_description": "Main Business Account",
        "iban": "FR7612345678901234567890123",
        "holder_company_name": "ACME Corporation",
        "operation_date": "2026-01-08",
        "value_date": "2026-01-08",
        "amount": 8750.00,
        "currency": "EUR",
        "is_debit": False,
        "category": {
            "id": "other_income",
            "name": "Autres revenus",
            "icon": "hand-holding-usd",
            "color": "#20c997",
            "description": "Autres sources de revenus"
        },
        "merchant": "Client ABC Industries",
        "tags": ["income", "large", "business"]
    },
    {
        "account_description": "Main Business Account",
        "iban": "FR7612345678901234567890123",
        "holder_company_name": "ACME Corporation",
        "operation_date": "2026-01-14",
        "value_date": "2026-01-14",
        "amount": 5230.00,
        "currency": "EUR",
        "is_debit": False,
        "category": {
            "id": "other_income",
            "name": "Autres revenus",
            "icon": "hand-holding-usd",
            "color": "#20c997",
            "description": "Autres sources de revenus"
        },
        "merchant": "Client XYZ Corp",
        "tags": ["income", "large", "business"]
    },
    # Utility bills
    {
        "account_description": "Main Business Account",
        "iban": "FR7612345678901234567890123",
        "holder_company_name": "ACME Corporation",
        "operation_date": "2026-01-10",
        "value_date": "2026-01-10",
        "amount": 285.40,
        "currency": "EUR",
        "is_debit": True,
        "category": {
            "id": "utilities",
            "name": "Services publics",
            "icon": "lightbulb",
            "color": "#ffc107",
            "description": "Électricité, eau, gaz"
        },
        "merchant": "EDF Électricité",
        "tags": ["expense", "recurring"]
    },
    {
        "account_description": "Main Business Account",
        "iban": "FR7612345678901234567890123",
        "holder_company_name": "ACME Corporation",
        "operation_date": "2026-01-11",
        "value_date": "2026-01-11",
        "amount": 120.50,
        "currency": "EUR",
        "is_debit": True,
        "category": {
            "id": "utilities",
            "name": "Services publics",
            "icon": "lightbulb",
            "color": "#ffc107",
            "description": "Électricité, eau, gaz"
        },
        "merchant": "Veolia Water Services",
        "tags": ["expense", "recurring"]
    },
    # Insurance payments
    {
        "account_description": "Main Business Account",
        "iban": "FR7612345678901234567890123",
        "holder_company_name": "ACME Corporation",
        "operation_date": "2026-01-06",
        "value_date": "2026-01-06",
        "amount": 450.00,
        "currency": "EUR",
        "is_debit": True,
        "category": {
            "id": "insurance",
            "name": "Assurance",
            "icon": "shield-alt",
            "color": "#007bff",
            "description": "Assurances professionnelles"
        },
        "merchant": "AXA Assurances",
        "tags": ["expense", "recurring"]
    },
    # Tax payments
    {
        "account_description": "Main Business Account",
        "iban": "FR7612345678901234567890123",
        "holder_company_name": "ACME Corporation",
        "operation_date": "2026-01-20",
        "value_date": "2026-01-20",
        "amount": 3200.00,
        "currency": "EUR",
        "is_debit": True,
        "category": {
            "id": "tax",
            "name": "Taxes",
            "icon": "file-invoice-dollar",
            "color": "#dc3545",
            "description": "Impôts et taxes"
        },
        "merchant": "Direction Générale des Finances Publiques",
        "tags": ["expense", "large"]
    },
    # Equipment purchases
    {
        "account_description": "Main Business Account",
        "iban": "FR7612345678901234567890123",
        "holder_company_name": "ACME Corporation",
        "operation_date": "2026-01-18",
        "value_date": "2026-01-18",
        "amount": 12500.00,
        "currency": "EUR",
        "is_debit": True,
        "category": {
            "id": "equipment",
            "name": "Équipement",
            "icon": "tools",
            "color": "#6610f2",
            "description": "Matériel et équipement"
        },
        "merchant": "Dell Business Solutions",
        "tags": ["expense", "large", "business"]
    },
    # Travel expenses
    {
        "account_description": "Main Business Account",
        "iban": "FR7612345678901234567890123",
        "holder_company_name": "ACME Corporation",
        "operation_date": "2026-01-22",
        "value_date": "2026-01-22",
        "amount": 850.75,
        "currency": "EUR",
        "is_debit": True,
        "category": {
            "id": "travel",
            "name": "Déplacements",
            "icon": "plane",
            "color": "#fd7e14",
            "description": "Frais de déplacement"
        },
        "merchant": "Air France",
        "tags": ["expense", "business"]
    },
    {
        "account_description": "Main Business Account",
        "iban": "FR7612345678901234567890123",
        "holder_company_name": "ACME Corporation",
        "operation_date": "2026-01-23",
        "value_date": "2026-01-23",
        "amount": 320.00,
        "currency": "EUR",
        "is_debit": True,
        "category": {
            "id": "travel",
            "name": "Déplacements",
            "icon": "plane",
            "color": "#fd7e14",
            "description": "Frais de déplacement"
        },
        "merchant": "Hilton Hotels",
        "tags": ["expense", "business"]
    },
    # Bank fees
    {
        "account_description": "Main Business Account",
        "iban": "FR7612345678901234567890123",
        "holder_company_name": "ACME Corporation",
        "operation_date": "2026-01-31",
        "value_date": "2026-01-31",
        "amount": 35.00,
        "currency": "EUR",
        "is_debit": True,
        "category": {
            "id": "other_expense",
            "name": "Autres dépenses",
            "icon": "receipt",
            "color": "#e83e8c",
            "description": "Autres dépenses"
        },
        "merchant": "Banque de France",
        "tags": ["expense", "recurring"]
    },
    # Investment returns
    {
        "account_description": "Savings Account",
        "iban": "FR7698765432109876543210987",
        "holder_company_name": "ACME Corporation",
        "operation_date": "2026-01-25",
        "value_date": "2026-01-25",
        "amount": 1250.00,
        "currency": "EUR",
        "is_debit": False,
        "category": {
            "id": "other_income",
            "name": "Autres revenus",
            "icon": "hand-holding-usd",
            "color": "#20c997",
            "description": "Autres sources de revenus"
        },
        "merchant": "Investment Fund Returns",
        "tags": ["income", "large"]
    },
    # USD account transactions
    {
        "account_description": "USD Operating Account",
        "iban": "US1234567890123456789012345",
        "holder_company_name": "ACME USA Inc",
        "operation_date": "2026-01-03",
        "value_date": "2026-01-03",
        "amount": 4500.00,
        "currency": "USD",
        "is_debit": False,
        "category": {
            "id": "other_income",
            "name": "Autres revenus",
            "icon": "hand-holding-usd",
            "color": "#20c997",
            "description": "Autres sources de revenus"
        },
        "merchant": "US Client Payment",
        "tags": ["income", "large", "business"]
    },
    {
        "account_description": "USD Operating Account",
        "iban": "US1234567890123456789012345",
        "holder_company_name": "ACME USA Inc",
        "operation_date": "2026-01-09",
        "value_date": "2026-01-09",
        "amount": 1200.00,
        "currency": "USD",
        "is_debit": True,
        "category": {
            "id": "supplies",
            "name": "Fournitures",
            "icon": "box",
            "color": "#6c757d",
            "description": "Achats et fournitures"
        },
        "merchant": "US Supplier Inc",
        "tags": ["expense", "business"]
    },
    {
        "account_description": "USD Operating Account",
        "iban": "US1234567890123456789012345",
        "holder_company_name": "ACME USA Inc",
        "operation_date": "2026-01-16",
        "value_date": "2026-01-16",
        "amount": 1800.00,
        "currency": "USD",
        "is_debit": True,
        "category": {
            "id": "rent",
            "name": "Loyer",
            "icon": "building",
            "color": "#17a2b8",
            "description": "Loyers et charges"
        },
        "merchant": "NYC Office Rent",
        "tags": ["expense", "large", "recurring"]
    },
]

# Additional edge cases for comprehensive testing
MOCK_TRANSACTIONS_ADVANCED_EDGE_CASES = [
    # Refund (negative expense = income)
    {
        "account_description": "Main Business Account",
        "iban": "FR7612345678901234567890123",
        "holder_company_name": "ACME Corporation",
        "operation_date": "2026-01-20",
        "value_date": "2026-01-20",
        "amount": 450.00,
        "currency": "EUR",
        "is_debit": False,
        "category": {
            "id": "other_income",
            "name": "Autres revenus",
            "icon": "hand-holding-usd",
            "color": "#20c997",
            "description": "Autres sources de revenus"
        },
        "merchant": "Supplier Refund",
        "tags": ["income", "refund"]
    },
    # High-frequency scenario: Multiple transactions same day
    {
        "account_description": "Main Business Account",
        "iban": "FR7612345678901234567890123",
        "holder_company_name": "ACME Corporation",
        "operation_date": "2026-01-15",
        "value_date": "2026-01-15",
        "amount": 45.50,
        "currency": "EUR",
        "is_debit": True,
        "category": {
            "id": "other_expense",
            "name": "Autres dépenses",
            "icon": "receipt",
            "color": "#e83e8c",
            "description": "Autres dépenses"
        },
        "merchant": "Coffee Shop",
        "tags": ["expense", "small"]
    },
    {
        "account_description": "Main Business Account",
        "iban": "FR7612345678901234567890123",
        "holder_company_name": "ACME Corporation",
        "operation_date": "2026-01-15",
        "value_date": "2026-01-15",
        "amount": 120.00,
        "currency": "EUR",
        "is_debit": True,
        "category": {
            "id": "travel",
            "name": "Déplacements",
            "icon": "plane",
            "color": "#fd7e14",
            "description": "Frais de déplacement"
        },
        "merchant": "Taxi Service",
        "tags": ["expense", "business"]
    },
    {
        "account_description": "Main Business Account",
        "iban": "FR7612345678901234567890123",
        "holder_company_name": "ACME Corporation",
        "operation_date": "2026-01-15",
        "value_date": "2026-01-15",
        "amount": 85.00,
        "currency": "EUR",
        "is_debit": True,
        "category": {
            "id": "other_expense",
            "name": "Autres dépenses",
            "icon": "receipt",
            "color": "#e83e8c",
            "description": "Autres dépenses"
        },
        "merchant": "Restaurant",
        "tags": ["expense", "business"]
    },
    # Duplicate transaction scenario
    {
        "account_description": "Main Business Account",
        "iban": "FR7612345678901234567890123",
        "holder_company_name": "ACME Corporation",
        "operation_date": "2026-01-25",
        "value_date": "2026-01-25",
        "amount": 1500.00,
        "currency": "EUR",
        "is_debit": True,
        "category": {
            "id": "supplies",
            "name": "Fournitures",
            "icon": "box",
            "color": "#6c757d",
            "description": "Achats et fournitures"
        },
        "merchant": "Office Depot",
        "tags": ["expense", "large", "duplicate"]
    },
    {
        "account_description": "Main Business Account",
        "iban": "FR7612345678901234567890123",
        "holder_company_name": "ACME Corporation",
        "operation_date": "2026-01-25",
        "value_date": "2026-01-25",
        "amount": 1500.00,
        "currency": "EUR",
        "is_debit": True,
        "category": {
            "id": "supplies",
            "name": "Fournitures",
            "icon": "box",
            "color": "#6c757d",
            "description": "Achats et fournitures"
        },
        "merchant": "Office Depot",
        "tags": ["expense", "large", "duplicate"]
    },
    # Fractional cents (precision test)
    {
        "account_description": "Savings Account",
        "iban": "FR7698765432109876543210987",
        "holder_company_name": "ACME Corporation",
        "operation_date": "2026-01-31",
        "value_date": "2026-01-31",
        "amount": 83.33,
        "currency": "EUR",
        "is_debit": False,
        "category": {
            "id": "other_income",
            "name": "Autres revenus",
            "icon": "hand-holding-usd",
            "color": "#20c997",
            "description": "Autres sources de revenus"
        },
        "merchant": "Interest Payment",
        "tags": ["income", "interest", "recurring"]
    },
    # Very small amount
    {
        "account_description": "Main Business Account",
        "iban": "FR7612345678901234567890123",
        "holder_company_name": "ACME Corporation",
        "operation_date": "2026-01-28",
        "value_date": "2026-01-28",
        "amount": 2.50,
        "currency": "EUR",
        "is_debit": True,
        "category": {
            "id": "other_expense",
            "name": "Autres dépenses",
            "icon": "receipt",
            "color": "#e83e8c",
            "description": "Autres dépenses"
        },
        "merchant": "Parking Meter",
        "tags": ["expense", "small"]
    },
    # Foreign currency with conversion note
    {
        "account_description": "USD Operating Account",
        "iban": "US1234567890123456789012345",
        "holder_company_name": "ACME USA Inc",
        "operation_date": "2026-01-27",
        "value_date": "2026-01-27",
        "amount": 350.00,
        "currency": "USD",
        "is_debit": True,
        "category": {
            "id": "utilities",
            "name": "Services publics",
            "icon": "lightbulb",
            "color": "#ffc107",
            "description": "Électricité, eau, gaz"
        },
        "merchant": "ConEd New York",
        "tags": ["expense", "recurring", "usd"]
    },
    # Subscription payment (recurring)
    {
        "account_description": "Main Business Account",
        "iban": "FR7612345678901234567890123",
        "holder_company_name": "ACME Corporation",
        "operation_date": "2026-01-01",
        "value_date": "2026-01-01",
        "amount": 99.00,
        "currency": "EUR",
        "is_debit": True,
        "category": {
            "id": "other_expense",
            "name": "Autres dépenses",
            "icon": "receipt",
            "color": "#e83e8c",
            "description": "Autres dépenses"
        },
        "merchant": "Microsoft 365 Subscription",
        "tags": ["expense", "recurring", "subscription"]
    },
    {
        "account_description": "Main Business Account",
        "iban": "FR7612345678901234567890123",
        "holder_company_name": "ACME Corporation",
        "operation_date": "2026-01-03",
        "value_date": "2026-01-03",
        "amount": 49.90,
        "currency": "EUR",
        "is_debit": True,
        "category": {
            "id": "other_expense",
            "name": "Autres dépenses",
            "icon": "receipt",
            "color": "#e83e8c",
            "description": "Autres dépenses"
        },
        "merchant": "Adobe Creative Cloud",
        "tags": ["expense", "recurring", "subscription"]
    },
    # ATM withdrawal
    {
        "account_description": "Main Business Account",
        "iban": "FR7612345678901234567890123",
        "holder_company_name": "ACME Corporation",
        "operation_date": "2026-01-13",
        "value_date": "2026-01-13",
        "amount": 200.00,
        "currency": "EUR",
        "is_debit": True,
        "category": {
            "id": "other_expense",
            "name": "Autres dépenses",
            "icon": "receipt",
            "color": "#e83e8c",
            "description": "Autres dépenses"
        },
        "merchant": "ATM Withdrawal - BNP Paribas",
        "tags": ["expense", "cash", "atm"]
    },
    # Weekend transaction
    {
        "account_description": "Main Business Account",
        "iban": "FR7612345678901234567890123",
        "holder_company_name": "ACME Corporation",
        "operation_date": "2026-01-11",  # Saturday
        "value_date": "2026-01-13",  # Monday (value date after weekend)
        "amount": 75.00,
        "currency": "EUR",
        "is_debit": True,
        "category": {
            "id": "other_expense",
            "name": "Autres dépenses",
            "icon": "receipt",
            "color": "#e83e8c",
            "description": "Autres dépenses"
        },
        "merchant": "Online Purchase - Amazon",
        "tags": ["expense", "weekend"]
    },
]

# High-volume transaction scenario (100+ transactions in one day)
MOCK_TRANSACTIONS_HIGH_VOLUME_DAY = [
    {
        "account_description": "Main Business Account",
        "iban": "FR7612345678901234567890123",
        "holder_company_name": "ACME Corporation",
        "operation_date": "2026-01-15",
        "value_date": "2026-01-15",
        "amount": round(15.0 + (i * 3.25), 2),
        "currency": "EUR",
        "is_debit": i % 3 != 0,  # Mix of debits and credits
        "category": {
            "id": "other_expense" if i % 3 != 0 else "other_income",
            "name": "Autres dépenses" if i % 3 != 0 else "Autres revenus",
            "icon": "receipt" if i % 3 != 0 else "hand-holding-usd",
            "color": "#e83e8c" if i % 3 != 0 else "#20c997",
        },
        "merchant": f"Transaction {i+1}",
        "tags": ["high_volume", "expense" if i % 3 != 0 else "income"]
    }
    for i in range(120)  # 120 transactions in one day
]

# Inactive period scenario (no transactions)
# Represented by empty list for specific date range
MOCK_TRANSACTIONS_INACTIVE_PERIOD = []

