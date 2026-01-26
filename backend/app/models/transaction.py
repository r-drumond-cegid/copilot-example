"""Transaction data models and schemas."""

from datetime import date
from typing import Optional

from pydantic import BaseModel, Field


class Transaction(BaseModel):
    """Bank transaction model."""

    account_description: str = Field(..., description="Account description")
    iban: str = Field(..., description="International Bank Account Number")
    holder_company_name: str = Field(..., description="Account holder company name")
    operation_date: str = Field(..., description="Operation date (YYYY-MM-DD)")
    value_date: str = Field(..., description="Value date (YYYY-MM-DD)")
    amount: float = Field(..., description="Transaction amount")
    currency: str = Field(..., description="Currency code (e.g., EUR, USD)")
    is_debit: bool = Field(..., description="True if transaction is a debit")

    class Config:
        json_schema_extra = {
            "example": {
                "account_description": "Main Business Account",
                "iban": "FR7612345678901234567890123",
                "holder_company_name": "ACME Corporation",
                "operation_date": "2026-01-15",
                "value_date": "2026-01-15",
                "amount": 1500.75,
                "currency": "EUR",
                "is_debit": True,
            }
        }


class TransactionResponse(BaseModel):
    """Transaction response model with renamed fields."""

    account: str = Field(..., description="Account description")
    iban: str = Field(..., description="International Bank Account Number")
    company: str = Field(..., description="Account holder company name")
    operation_date: str = Field(..., description="Operation date (YYYY-MM-DD)")
    value_date: str = Field(..., description="Value date (YYYY-MM-DD)")
    amount: float = Field(..., description="Transaction amount")
    currency: str = Field(..., description="Currency code")
    is_debit: bool = Field(..., description="True if transaction is a debit")


class TransactionQueryParams(BaseModel):
    """Query parameters for transaction endpoint."""

    from_date: str = Field(..., description="Start date (YYYY-MM-DD)")
    to_date: str = Field(..., description="End date (YYYY-MM-DD)")


class TransactionCategory(BaseModel):
    """Transaction category classification."""

    id: str = Field(..., description="Category unique identifier")
    name: str = Field(..., description="Category display name")
    icon: Optional[str] = Field(None, description="Icon identifier for UI")
    color: Optional[str] = Field(None, description="Color code for UI (e.g., #FF5733)")
    description: Optional[str] = Field(None, description="Category description")

    class Config:
        json_schema_extra = {
            "example": {
                "id": "salary",
                "name": "Salaire",
                "icon": "money-bill-wave",
                "color": "#28a745",
                "description": "Revenus salariaux",
            }
        }


class EnrichedTransaction(BaseModel):
    """Transaction with enriched data (category, labels)."""

    account: str = Field(..., description="Account description")
    iban: str = Field(..., description="International Bank Account Number")
    company: str = Field(..., description="Account holder company name")
    operation_date: str = Field(..., description="Operation date (YYYY-MM-DD)")
    value_date: str = Field(..., description="Value date (YYYY-MM-DD)")
    amount: float = Field(..., description="Transaction amount")
    currency: str = Field(..., description="Currency code")
    is_debit: bool = Field(..., description="True if transaction is a debit")
    category: Optional[TransactionCategory] = Field(None, description="Transaction category")
    merchant: Optional[str] = Field(None, description="Detected merchant name")
    tags: list[str] = Field(default_factory=list, description="Custom tags")

    class Config:
        json_schema_extra = {
            "example": {
                "account": "Main Business Account",
                "iban": "FR7612345678901234567890123",
                "company": "ACME Corporation",
                "operation_date": "2026-01-15",
                "value_date": "2026-01-15",
                "amount": 1500.75,
                "currency": "EUR",
                "is_debit": True,
                "category": {"id": "supplies", "name": "Fournitures", "color": "#6c757d"},
                "merchant": "Office Depot",
                "tags": ["business", "recurring"],
            }
        }
