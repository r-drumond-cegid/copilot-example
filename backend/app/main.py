"""FastAPI main application entry point."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import accounts, transactions, chat, analytics

app = FastAPI(
    title="Finance Dashboard API",
    description="API for managing bank accounts and transactions with AI chatbot",
    version="1.0.0",
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(accounts.router, prefix="/api/v1", tags=["accounts"])
app.include_router(transactions.router, prefix="/api/v1", tags=["transactions"])
app.include_router(chat.router, prefix="/api/v1", tags=["chat"])
app.include_router(analytics.router, prefix="/api/v1", tags=["analytics"])


@app.on_event("startup")
async def startup_event():
    """Load enriched mock data on application startup."""
    try:
        from tests.fixtures import (
            MOCK_ACCOUNTS_TIMELINE_30_DAYS,
            MOCK_TRANSACTIONS_ENRICHED,
        )
        
        # Load enriched transaction data with categories, merchants, and tags
        # Store in both routes for compatibility
        transactions.set_mock_transactions(MOCK_TRANSACTIONS_ENRICHED)
        analytics.set_mock_enriched_transactions(MOCK_TRANSACTIONS_ENRICHED)
        
        # Load 60-day timeline data for balance charts (Dec 2025 - Jan 2026)
        accounts.set_mock_accounts(MOCK_ACCOUNTS_TIMELINE_30_DAYS)
        
        # Validate data loaded successfully
        if not MOCK_TRANSACTIONS_ENRICHED:
            raise RuntimeError("MOCK_TRANSACTIONS_ENRICHED is empty")
        if not MOCK_ACCOUNTS_TIMELINE_30_DAYS:
            raise RuntimeError("MOCK_ACCOUNTS_TIMELINE_30_DAYS is empty")
        
        print("✓ Loaded enriched mock data:")
        print(f"  - {len(MOCK_TRANSACTIONS_ENRICHED)} enriched transactions")
        print(f"  - {len(MOCK_ACCOUNTS_TIMELINE_30_DAYS)} account balance records (60-day timeline)")
        
        # Display date range
        transaction_dates = [t["operation_date"] for t in MOCK_TRANSACTIONS_ENRICHED]
        account_dates = [a["date"] for a in MOCK_ACCOUNTS_TIMELINE_30_DAYS]
        print(f"  - Transactions: {min(transaction_dates)} to {max(transaction_dates)}")
        print(f"  - Account balances: {min(account_dates)} to {max(account_dates)}")
    except Exception as e:
        print(f"⚠ ERROR: Could not load enriched mock data: {e}")
        print("  API will not function correctly without data.")
        raise  # Fail fast to prevent running with empty data


@app.get("/")
async def root():
    """Root endpoint."""
    return {"message": "Finance Dashboard API", "version": "1.0.0"}


@app.get("/health")
async def health():
    """Health check endpoint."""
    return {"status": "healthy"}
