"""Account data models and schemas."""

from datetime import date
from typing import Optional

from pydantic import BaseModel, Field


class Account(BaseModel):
    """Bank account model."""

    account_description: str = Field(..., description="Account description")
    iban: str = Field(..., description="International Bank Account Number")
    holder_company_name: str = Field(..., description="Account holder company name")
    date: str = Field(..., description="Date of the balance (YYYY-MM-DD)")
    value_balance: float = Field(..., description="Account balance value")
    currency: str = Field(..., description="Currency code (e.g., EUR, USD)")
    allowed_overdraft: float = Field(default=0.0, description="Allowed overdraft amount")

    class Config:
        json_schema_extra = {
            "example": {
                "account_description": "Main Business Account",
                "iban": "FR7612345678901234567890123",
                "holder_company_name": "ACME Corporation",
                "date": "2026-01-15",
                "value_balance": 150000.50,
                "currency": "EUR",
                "allowed_overdraft": 10000.0,
            }
        }


class AccountResponse(BaseModel):
    """Account response model with renamed fields."""

    account: str = Field(..., description="Account description")
    iban: str = Field(..., description="International Bank Account Number")
    company: str = Field(..., description="Account holder company name")
    date: str = Field(..., description="Date of the balance (YYYY-MM-DD)")
    balance: float = Field(..., description="Account balance value")
    currency: str = Field(..., description="Currency code")
    allowed_overdraft: float = Field(default=0.0, description="Allowed overdraft amount")


class AccountQueryParams(BaseModel):
    """Query parameters for account endpoint."""

    date: Optional[str] = Field(None, description="Single date query (YYYY-MM-DD)")
    start_date: Optional[str] = Field(None, description="Start date for range query (YYYY-MM-DD)")
    end_date: Optional[str] = Field(None, description="End date for range query (YYYY-MM-DD)")
