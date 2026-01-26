"""Transaction enrichment and categorization services."""

from typing import Optional
from ..models.transaction import TransactionCategory, TransactionResponse, EnrichedTransaction


# Predefined category definitions
CATEGORIES = {
    "salary": TransactionCategory(
        id="salary",
        name="Salaire",
        icon="money-bill-wave",
        color="#28a745",
        description="Revenus salariaux",
    ),
    "supplies": TransactionCategory(
        id="supplies",
        name="Fournitures",
        icon="box",
        color="#6c757d",
        description="Achats de fournitures",
    ),
    "utilities": TransactionCategory(
        id="utilities",
        name="Services publics",
        icon="bolt",
        color="#ffc107",
        description="Électricité, eau, gaz",
    ),
    "rent": TransactionCategory(
        id="rent",
        name="Loyer",
        icon="building",
        color="#17a2b8",
        description="Paiements de loyer",
    ),
    "insurance": TransactionCategory(
        id="insurance",
        name="Assurance",
        icon="shield-alt",
        color="#007bff",
        description="Primes d'assurance",
    ),
    "tax": TransactionCategory(
        id="tax",
        name="Taxes",
        icon="file-invoice-dollar",
        color="#dc3545",
        description="Impôts et taxes",
    ),
    "equipment": TransactionCategory(
        id="equipment",
        name="Équipement",
        icon="tools",
        color="#6610f2",
        description="Achats d'équipement",
    ),
    "travel": TransactionCategory(
        id="travel",
        name="Déplacements",
        icon="plane",
        color="#fd7e14",
        description="Frais de déplacement",
    ),
    "other_income": TransactionCategory(
        id="other_income",
        name="Autres revenus",
        icon="plus-circle",
        color="#20c997",
        description="Revenus divers",
    ),
    "other_expense": TransactionCategory(
        id="other_expense",
        name="Autres dépenses",
        icon="minus-circle",
        color="#e83e8c",
        description="Dépenses diverses",
    ),
}


def categorize_transaction(amount: float, is_debit: bool, account_desc: str = "") -> TransactionCategory:
    """
    Categorize a transaction based on amount, type, and account description.
    
    Args:
        amount: Transaction amount
        is_debit: True if transaction is a debit (expense)
        account_desc: Account description for additional context
        
    Returns:
        TransactionCategory: Assigned category
    """
    account_lower = account_desc.lower()
    
    # Income categories (credits)
    if not is_debit:
        if amount > 10000:
            return CATEGORIES["salary"]
        return CATEGORIES["other_income"]
    
    # Expense categories (debits)
    # Rule-based categorization using keywords
    if "fourniture" in account_lower or "office" in account_lower or "supply" in account_lower:
        return CATEGORIES["supplies"]
    elif "electric" in account_lower or "water" in account_lower or "gaz" in account_lower:
        return CATEGORIES["utilities"]
    elif "rent" in account_lower or "loyer" in account_lower:
        return CATEGORIES["rent"]
    elif "insurance" in account_lower or "assurance" in account_lower:
        return CATEGORIES["insurance"]
    elif "tax" in account_lower or "impot" in account_lower or "fiscal" in account_lower:
        return CATEGORIES["tax"]
    elif "equipment" in account_lower or "equipement" in account_lower or "materiel" in account_lower:
        return CATEGORIES["equipment"]
    elif "travel" in account_lower or "deplacement" in account_lower or "voyage" in account_lower:
        return CATEGORIES["travel"]
    
    # Amount-based fallback for large expenses
    if amount > 50000:
        return CATEGORIES["equipment"]
    
    return CATEGORIES["other_expense"]


def extract_merchant(account_desc: str) -> Optional[str]:
    """
    Extract potential merchant name from account description.
    
    Args:
        account_desc: Account description text
        
    Returns:
        Merchant name if detected, None otherwise
    """
    # Simple extraction: capitalize first significant words
    words = account_desc.split()
    if len(words) >= 2:
        # Skip common prefixes
        skip_words = {"to", "from", "payment", "transfer", "paiement", "virement"}
        filtered = [w for w in words if w.lower() not in skip_words]
        if filtered:
            return " ".join(filtered[:3]).title()
    return None


def enrich_transaction(transaction: TransactionResponse) -> EnrichedTransaction:
    """
    Enrich a transaction with category, merchant, and tags.
    
    Args:
        transaction: Base transaction data
        
    Returns:
        EnrichedTransaction: Transaction with enriched metadata
    """
    category = categorize_transaction(
        transaction.amount,
        transaction.is_debit,
        transaction.account
    )
    
    merchant = extract_merchant(transaction.account)
    
    # Add tags based on amount and type
    tags = []
    if transaction.amount > 10000:
        tags.append("large")
    if not transaction.is_debit:
        tags.append("income")
    else:
        tags.append("expense")
    
    return EnrichedTransaction(
        account=transaction.account,
        iban=transaction.iban,
        company=transaction.company,
        operation_date=transaction.operation_date,
        value_date=transaction.value_date,
        amount=transaction.amount,
        currency=transaction.currency,
        is_debit=transaction.is_debit,
        category=category,
        merchant=merchant,
        tags=tags,
    )


def filter_transactions(
    transactions: list[EnrichedTransaction],
    category_ids: Optional[list[str]] = None,
    min_amount: Optional[float] = None,
    max_amount: Optional[float] = None,
    is_debit: Optional[bool] = None,
) -> list[EnrichedTransaction]:
    """
    Filter transactions based on various criteria.
    
    Args:
        transactions: List of enriched transactions
        category_ids: Filter by category IDs
        min_amount: Minimum transaction amount
        max_amount: Maximum transaction amount
        is_debit: Filter by debit/credit type
        
    Returns:
        Filtered list of transactions
    """
    filtered = transactions
    
    if category_ids:
        filtered = [t for t in filtered if t.category and t.category.id in category_ids]
    
    if min_amount is not None:
        filtered = [t for t in filtered if abs(t.amount) >= min_amount]
    
    if max_amount is not None:
        filtered = [t for t in filtered if abs(t.amount) <= max_amount]
    
    if is_debit is not None:
        filtered = [t for t in filtered if t.is_debit == is_debit]
    
    return filtered
