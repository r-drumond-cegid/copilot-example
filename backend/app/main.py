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
        transactions.set_mock_transactions(MOCK_TRANSACTIONS_ENRICHED)
        
        # Load 30-day timeline data for balance charts
        accounts.set_mock_accounts(MOCK_ACCOUNTS_TIMELINE_30_DAYS)
        
        print("✓ Loaded enriched mock data:")
        print(f"  - {len(MOCK_TRANSACTIONS_ENRICHED)} enriched transactions")
        print(f"  - {len(MOCK_ACCOUNTS_TIMELINE_30_DAYS)} account balance records (30-day timeline)")
    except Exception as e:
        print(f"⚠ Warning: Could not load enriched mock data: {e}")
        print("  Using empty data - API will work but return no results.")


@app.get("/")
async def root():
    """Root endpoint."""
    return {"message": "Finance Dashboard API", "version": "1.0.0"}


@app.get("/health")
async def health():
    """Health check endpoint."""
    return {"status": "healthy"}
