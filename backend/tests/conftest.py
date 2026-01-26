"""Pytest configuration and fixtures."""

import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.routes import accounts, transactions
from tests.fixtures.mock_accounts import (
    generate_mock_accounts,
    MOCK_ACCOUNTS_SINGLE_DAY,
    MOCK_ACCOUNTS_EMPTY,
    MOCK_ACCOUNTS_EDGE_CASES,
)
from tests.fixtures.mock_transactions import (
    generate_mock_transactions,
    MOCK_TRANSACTIONS_SAMPLE,
    MOCK_TRANSACTIONS_EMPTY,
    MOCK_TRANSACTIONS_EDGE_CASES,
)


@pytest.fixture
def client():
    """Create a test client for the FastAPI app."""
    return TestClient(app)


@pytest.fixture
def mock_accounts_single_day():
    """Provide mock account data for a single day."""
    accounts.set_mock_accounts(MOCK_ACCOUNTS_SINGLE_DAY)
    yield MOCK_ACCOUNTS_SINGLE_DAY
    accounts.set_mock_accounts([])


@pytest.fixture
def mock_accounts_range():
    """Provide mock account data for a date range (30 days)."""
    mock_data = generate_mock_accounts(start_date="2026-01-01", days=30)
    accounts.set_mock_accounts(mock_data)
    yield mock_data
    accounts.set_mock_accounts([])


@pytest.fixture
def mock_accounts_empty():
    """Provide empty mock account data."""
    accounts.set_mock_accounts(MOCK_ACCOUNTS_EMPTY)
    yield MOCK_ACCOUNTS_EMPTY
    accounts.set_mock_accounts([])


@pytest.fixture
def mock_accounts_edge_cases():
    """Provide mock account data with edge cases."""
    accounts.set_mock_accounts(MOCK_ACCOUNTS_EDGE_CASES)
    yield MOCK_ACCOUNTS_EDGE_CASES
    accounts.set_mock_accounts([])


@pytest.fixture
def mock_transactions_sample():
    """Provide sample mock transaction data."""
    transactions.set_mock_transactions(MOCK_TRANSACTIONS_SAMPLE)
    yield MOCK_TRANSACTIONS_SAMPLE
    transactions.set_mock_transactions([])


@pytest.fixture
def mock_transactions_range():
    """Provide mock transaction data for a date range."""
    mock_data = generate_mock_transactions(
        start_date="2026-01-01",
        end_date="2026-01-31",
        num_transactions=50,
    )
    transactions.set_mock_transactions(mock_data)
    yield mock_data
    transactions.set_mock_transactions([])


@pytest.fixture
def mock_transactions_empty():
    """Provide empty mock transaction data."""
    transactions.set_mock_transactions(MOCK_TRANSACTIONS_EMPTY)
    yield MOCK_TRANSACTIONS_EMPTY
    transactions.set_mock_transactions([])


@pytest.fixture
def mock_transactions_edge_cases():
    """Provide mock transaction data with edge cases."""
    transactions.set_mock_transactions(MOCK_TRANSACTIONS_EDGE_CASES)
    yield MOCK_TRANSACTIONS_EDGE_CASES
    transactions.set_mock_transactions([])
