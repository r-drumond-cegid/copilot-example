"""Analytics and enrichment endpoints."""

from fastapi import APIRouter, HTTPException, Query
from typing import Optional, List
from datetime import datetime

from ..models.account import BalanceSummary
from ..models.transaction import EnrichedTransaction, TransactionCategory
from ..routes.accounts import get_account_balances
from ..routes.transactions import get_transactions
from ..services.analytics import (
    calculate_balance_summary,
    detect_low_balance_alerts,
    calculate_transaction_trends,
)
from ..services.enrichment import enrich_transaction, filter_transactions, CATEGORIES

router = APIRouter()

# In-memory storage for enriched mock data
_mock_enriched_transactions: List[EnrichedTransaction] = []


def set_mock_enriched_transactions(transactions: List[dict]):
    """Set mock enriched transaction data for testing."""
    global _mock_enriched_transactions
    print(f"  [analytics] Transforming {len(transactions)} transactions...")
    # Transform field names from mock data format to EnrichedTransaction model
    transformed = []
    for i, trans in enumerate(transactions):
        try:
            trans_copy = trans.copy()
            # Rename fields if they exist in old format
            if 'account_description' in trans_copy:
                trans_copy['account'] = trans_copy.pop('account_description')
            if 'holder_company_name' in trans_copy:
                trans_copy['company'] = trans_copy.pop('holder_company_name')
            
            # Convert nested category dict to TransactionCategory object
            if 'category' in trans_copy and isinstance(trans_copy['category'], dict):
                trans_copy['category'] = TransactionCategory(**trans_copy['category'])
            
            transformed.append(EnrichedTransaction(**trans_copy))
        except Exception as e:
            print(f"    [analytics] Error transforming transaction {i}: {e}")
            print(f"    [analytics] Transaction keys: {list(trans.keys())}")
            raise
    _mock_enriched_transactions = transformed
    print(f"  [analytics] Successfully stored {len(_mock_enriched_transactions)} enriched transactions")


@router.get("/balance-summary", response_model=BalanceSummary)
async def get_balance_summary(
    date: Optional[str] = Query(None, description="Date for summary (YYYY-MM-DD)"),
    start_date: Optional[str] = Query(None, description="Start date (YYYY-MM-DD)"),
    end_date: Optional[str] = Query(None, description="End date (YYYY-MM-DD)"),
):
    """
    Get aggregated balance summary with statistics.
    
    Args:
        date: Single date for balance snapshot
        start_date: Start date for range (requires end_date)
        end_date: End date for range (requires start_date)
        
    Returns:
        BalanceSummary with aggregated statistics
    """
    try:
        # Reuse existing account endpoint to get balances
        accounts = await get_account_balances(date, start_date, end_date)
        
        # Calculate summary
        summary = calculate_balance_summary(accounts, date or start_date)
        
        return summary
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur calcul du résumé: {str(e)}")


@router.get("/alerts")
async def get_alerts(
    threshold: float = Query(0.1, description="Alert threshold percentage (0.0-1.0)"),
    date: Optional[str] = Query(None, description="Date for alerts (YYYY-MM-DD)"),
):
    """
    Get low balance alerts for accounts.
    
    Args:
        threshold: Alert threshold as percentage of overdraft (default 0.1 = 10%)
        date: Date for alerts (defaults to today if not provided)
        
    Returns:
        List of alert objects
    """
    try:
        # Get current account balances
        from datetime import datetime
        alert_date = date or datetime.now().strftime("%Y-%m-%d")
        accounts = await get_account_balances(date=alert_date)
        
        # Detect alerts
        alerts = detect_low_balance_alerts(accounts, threshold)
        
        return {"alerts": alerts, "count": len(alerts)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur détection des alertes: {str(e)}")


@router.get("/transactions/enriched", response_model=list[EnrichedTransaction])
async def get_enriched_transactions(
    from_date: str = Query(..., description="Start date (YYYY-MM-DD)"),
    to_date: str = Query(..., description="End date (YYYY-MM-DD)"),
    category: Optional[str] = Query(None, description="Filter by category ID"),
    min_amount: Optional[float] = Query(None, description="Minimum amount filter"),
    max_amount: Optional[float] = Query(None, description="Maximum amount filter"),
    is_debit: Optional[bool] = Query(None, description="Filter by debit (True) or credit (False)"),
):
    """
    Get transactions with enrichment (categories, merchants, tags).
    
    Args:
        from_date: Start date (YYYY-MM-DD)
        to_date: End date (YYYY-MM-DD)
        category: Optional category ID filter
        min_amount: Optional minimum amount filter
        max_amount: Optional maximum amount filter
        is_debit: Optional debit/credit filter
        
    Returns:
        List of enriched transactions
    """
    try:
        # Parse dates for filtering
        start = datetime.strptime(from_date, "%Y-%m-%d")
        end = datetime.strptime(to_date, "%Y-%m-%d")
        
        # Use pre-enriched transactions from mock data (preserves categories)
        enriched = [
            t for t in _mock_enriched_transactions
            if start <= datetime.strptime(t.operation_date, "%Y-%m-%d") <= end
        ]
        
        # Apply filters
        if category or min_amount is not None or max_amount is not None or is_debit is not None:
            category_ids = [category] if category else None
            enriched = filter_transactions(
                enriched,
                category_ids=category_ids,
                min_amount=min_amount,
                max_amount=max_amount,
                is_debit=is_debit,
            )
        
        return enriched
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur enrichissement: {str(e)}")


@router.get("/transactions/trends")
async def get_transaction_trends(
    from_date: str = Query(..., description="Start date (YYYY-MM-DD)"),
    to_date: str = Query(..., description="End date (YYYY-MM-DD)"),
):
    """
    Get transaction trends and statistics.
    
    Args:
        from_date: Start date (YYYY-MM-DD)
        to_date: End date (YYYY-MM-DD)
        
    Returns:
        Dictionary with trend statistics
    """
    try:
        # Parse dates for filtering
        start = datetime.strptime(from_date, "%Y-%m-%d")
        end = datetime.strptime(to_date, "%Y-%m-%d")
        
        # Filter transactions by date range
        enriched = [
            t for t in _mock_enriched_transactions
            if start <= datetime.strptime(t.operation_date, "%Y-%m-%d") <= end
        ]
        
        # Calculate trends
        trends = calculate_transaction_trends(enriched)
        
        return trends
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur calcul des tendances: {str(e)}")


@router.get("/categories", response_model=list[TransactionCategory])
async def get_categories():
    """
    Get all available transaction categories.
    
    Returns:
        List of TransactionCategory objects
    """
    return list(CATEGORIES.values())
