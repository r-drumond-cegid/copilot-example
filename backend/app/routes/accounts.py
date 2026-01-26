"""Account API routes."""

from datetime import datetime, timedelta
from typing import List, Optional

from fastapi import APIRouter, Query, HTTPException

from app.models.account import Account, AccountResponse

router = APIRouter()

# In-memory storage for mock data (replace with actual database in production)
_mock_accounts: List[Account] = []


def set_mock_accounts(accounts: List[dict]):
    """Set mock account data for testing."""
    global _mock_accounts
    _mock_accounts = [Account(**acc) for acc in accounts]


def _transform_to_response(account: Account) -> AccountResponse:
    """Transform Account model to AccountResponse with renamed fields."""
    return AccountResponse(
        account=account.account_description,
        iban=account.iban,
        company=account.holder_company_name,
        date=account.date,
        balance=account.value_balance,
        currency=account.currency,
        allowed_overdraft=account.allowed_overdraft,
    )


@router.get("/bank-account-balances", response_model=List[AccountResponse])
async def get_account_balances(
    date: Optional[str] = Query(None, description="Single date query (YYYY-MM-DD)"),
    start_date: Optional[str] = Query(None, description="Start date for range query"),
    end_date: Optional[str] = Query(None, description="End date for range query"),
):
    """Get bank account balances.
    
    Supports two modes:
    - Single date: ?date=2026-01-15
    - Date range: ?start_date=2026-01-01&end_date=2026-01-31
    
    Returns:
        List of account balances with transformed field names.
    """
    if date:
        # Single date query
        filtered_accounts = [acc for acc in _mock_accounts if acc.date == date]
    elif start_date and end_date:
        # Date range query
        try:
            start = datetime.strptime(start_date, "%Y-%m-%d")
            end = datetime.strptime(end_date, "%Y-%m-%d")
        except ValueError:
            raise HTTPException(status_code=400, detail="Invalid date format. Use YYYY-MM-DD")
        
        filtered_accounts = [
            acc for acc in _mock_accounts
            if start <= datetime.strptime(acc.date, "%Y-%m-%d") <= end
        ]
    else:
        raise HTTPException(
            status_code=400,
            detail="Either 'date' or both 'start_date' and 'end_date' must be provided"
        )
    
    # Transform to response format
    return [_transform_to_response(acc) for acc in filtered_accounts]
