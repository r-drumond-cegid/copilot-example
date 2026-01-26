"""Analytics and balance summary services."""

from datetime import datetime
from typing import Optional
from ..models.account import AccountResponse, BalanceSummary


def calculate_balance_summary(
    accounts: list[AccountResponse],
    date: Optional[str] = None
) -> BalanceSummary:
    """
    Calculate aggregated balance summary from account list.
    
    Args:
        accounts: List of account balances
        date: Date for the summary (current date if None)
        
    Returns:
        BalanceSummary: Aggregated balance statistics
    """
    if not accounts:
        return BalanceSummary(
            total_balance=0.0,
            currency="EUR",
            account_count=0,
            highest_balance=0.0,
            lowest_balance=0.0,
            average_balance=0.0,
            total_overdraft_allowed=0.0,
            date=date or datetime.now().strftime("%Y-%m-%d"),
            accounts=[],
        )
    
    # Assume all accounts use same currency (use first account's currency)
    currency = accounts[0].currency
    
    balances = [acc.balance for acc in accounts]
    overdrafts = [acc.allowed_overdraft for acc in accounts]
    
    return BalanceSummary(
        total_balance=sum(balances),
        currency=currency,
        account_count=len(accounts),
        highest_balance=max(balances),
        lowest_balance=min(balances),
        average_balance=sum(balances) / len(balances),
        total_overdraft_allowed=sum(overdrafts),
        date=date or datetime.now().strftime("%Y-%m-%d"),
        accounts=accounts,
    )


def detect_low_balance_alerts(
    accounts: list[AccountResponse],
    threshold_percentage: float = 0.1
) -> list[dict]:
    """
    Detect accounts with low balance relative to overdraft.
    
    Args:
        accounts: List of account balances
        threshold_percentage: Alert threshold (e.g., 0.1 = 10% of overdraft)
        
    Returns:
        List of alert dictionaries with account details
    """
    alerts = []
    
    for account in accounts:
        # Alert if balance is close to or below allowed overdraft
        if account.allowed_overdraft > 0:
            threshold = account.allowed_overdraft * threshold_percentage
            if account.balance < threshold:
                alerts.append({
                    "account": account.account,
                    "iban": account.iban,
                    "balance": account.balance,
                    "allowed_overdraft": account.allowed_overdraft,
                    "severity": "high" if account.balance < 0 else "medium",
                    "message": f"Balance faible sur {account.account}: {account.balance} {account.currency}",
                })
        # Alert if balance is negative without overdraft protection
        elif account.balance < 0:
            alerts.append({
                "account": account.account,
                "iban": account.iban,
                "balance": account.balance,
                "allowed_overdraft": 0.0,
                "severity": "critical",
                "message": f"Découvert non autorisé sur {account.account}",
            })
    
    return alerts


def calculate_transaction_trends(transactions: list) -> dict:
    """
    Calculate transaction trends and statistics.
    
    Args:
        transactions: List of enriched transactions
        
    Returns:
        Dictionary with trend statistics
    """
    if not transactions:
        return {
            "total_income": 0.0,
            "total_expenses": 0.0,
            "net_flow": 0.0,
            "transaction_count": 0,
            "avg_transaction": 0.0,
            "largest_income": 0.0,
            "largest_expense": 0.0,
        }
    
    income = [t.amount for t in transactions if not t.is_debit]
    expenses = [abs(t.amount) for t in transactions if t.is_debit]
    
    total_income = sum(income)
    total_expenses = sum(expenses)
    
    return {
        "total_income": total_income,
        "total_expenses": total_expenses,
        "net_flow": total_income - total_expenses,
        "transaction_count": len(transactions),
        "avg_transaction": sum(abs(t.amount) for t in transactions) / len(transactions),
        "largest_income": max(income) if income else 0.0,
        "largest_expense": max(expenses) if expenses else 0.0,
    }
