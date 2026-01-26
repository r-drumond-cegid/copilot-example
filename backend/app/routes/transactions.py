"""Transaction API routes."""

from datetime import datetime
from typing import List

from fastapi import APIRouter, Query, HTTPException

from app.models.transaction import Transaction, TransactionResponse

router = APIRouter()

# In-memory storage for mock data (replace with actual database in production)
_mock_transactions: List[Transaction] = []


def set_mock_transactions(transactions: List[dict]):
    """Set mock transaction data for testing."""
    global _mock_transactions
    _mock_transactions = [Transaction(**trans) for trans in transactions]


def _transform_to_response(transaction: Transaction) -> TransactionResponse:
    """Transform Transaction model to TransactionResponse with renamed fields."""
    return TransactionResponse(
        account=transaction.account_description,
        iban=transaction.iban,
        company=transaction.holder_company_name,
        operation_date=transaction.operation_date,
        value_date=transaction.value_date,
        amount=transaction.amount,
        currency=transaction.currency,
        is_debit=transaction.is_debit,
    )


@router.get("/bank-transactions", response_model=List[TransactionResponse])
async def get_transactions(
    from_date: str = Query(..., description="Start date (YYYY-MM-DD)"),
    to_date: str = Query(..., description="End date (YYYY-MM-DD)"),
):
    """Get bank transactions within date range.
    
    Args:
        from_date: Start date for filtering transactions.
        to_date: End date for filtering transactions.
    
    Returns:
        List of transactions with transformed field names.
    """
    try:
        start = datetime.strptime(from_date, "%Y-%m-%d")
        end = datetime.strptime(to_date, "%Y-%m-%d")
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date format. Use YYYY-MM-DD")
    
    if start > end:
        raise HTTPException(status_code=400, detail="from_date must be before or equal to to_date")
    
    # Filter transactions by operation_date
    filtered_transactions = [
        trans for trans in _mock_transactions
        if start <= datetime.strptime(trans.operation_date, "%Y-%m-%d") <= end
    ]
    
    # Transform to response format
    return [_transform_to_response(trans) for trans in filtered_transactions]
