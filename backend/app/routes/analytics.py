"""Analytics and enrichment endpoints."""

from fastapi import APIRouter, HTTPException, Query
from typing import Optional

from ..models.account import BalanceSummary
from ..models.transaction import EnrichedTransaction, TransactionCategory
from ..routes.accounts import get_account_balances
from ..routes.transactions import get_bank_transactions
from ..services.analytics import (
    calculate_balance_summary,
    detect_low_balance_alerts,
    calculate_transaction_trends,
)
from ..services.enrichment import enrich_transaction, filter_transactions, CATEGORIES

router = APIRouter()


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
        accounts = await get_bank_account_balances(date, start_date, end_date)
        
        # Calculate summary
        summary = calculate_balance_summary(accounts, date or start_date)
        
        return summary
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur calcul du résumé: {str(e)}")


@router.get("/alerts")
async def get_alerts(
    threshold: float = Query(0.1, description="Alert threshold percentage (0.0-1.0)"),
):
    """
    Get low balance alerts for accounts.
    
    Args:
        threshold: Alert threshold as percentage of overdraft (default 0.1 = 10%)
        
    Returns:
        List of alert objects
    """
    try:
        # Get current account balances
        accounts = await get_bank_account_balances(date=None)
        
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
        # Get base transactions
        base_transactions = await get_bank_transactions(from_date, to_date)
        
        # Enrich each transaction
        enriched = [enrich_transaction(t) for t in base_transactions]
        
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
        # Get enriched transactions
        enriched = await get_enriched_transactions(from_date, to_date)
        
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
