"""Tests for account API endpoints."""

import pytest
from fastapi.testclient import TestClient


class TestAccountBalances:
    """Test cases for account balance endpoints."""

    def test_get_accounts_single_date(self, client: TestClient, mock_accounts_single_day):
        """Test retrieving accounts for a single date."""
        response = client.get("/api/v1/bank-account-balances?date=2026-01-15")
        
        assert response.status_code == 200
        data = response.json()
        
        assert len(data) == 3
        assert all(acc["date"] == "2026-01-15" for acc in data)
        
        # Verify field transformations
        first_account = data[0]
        assert "account" in first_account
        assert "company" in first_account
        assert "balance" in first_account
        assert "account_description" not in first_account
        assert "holder_company_name" not in first_account
        assert "value_balance" not in first_account

    def test_get_accounts_date_range(self, client: TestClient, mock_accounts_range):
        """Test retrieving accounts for a date range."""
        response = client.get(
            "/api/v1/bank-account-balances?start_date=2026-01-01&end_date=2026-01-10"
        )
        
        assert response.status_code == 200
        data = response.json()
        
        # Should have 3 accounts × 10 days = 30 records
        assert len(data) == 30
        
        # Verify all dates are within range
        for acc in data:
            assert "2026-01-01" <= acc["date"] <= "2026-01-10"

    def test_get_accounts_empty_result(self, client: TestClient, mock_accounts_single_day):
        """Test retrieving accounts for a date with no data."""
        response = client.get("/api/v1/bank-account-balances?date=2025-12-01")
        
        assert response.status_code == 200
        data = response.json()
        assert len(data) == 0

    def test_get_accounts_missing_parameters(self, client: TestClient, mock_accounts_single_day):
        """Test error handling when required parameters are missing."""
        response = client.get("/api/v1/bank-account-balances")
        
        assert response.status_code == 400
        assert "must be provided" in response.json()["detail"]

    def test_get_accounts_invalid_date_format(self, client: TestClient, mock_accounts_single_day):
        """Test error handling for invalid date format."""
        response = client.get("/api/v1/bank-account-balances?date=15-01-2026")
        
        assert response.status_code == 200  # Will return empty list for non-matching date
        data = response.json()
        assert len(data) == 0

    def test_get_accounts_partial_date_range(self, client: TestClient, mock_accounts_single_day):
        """Test error handling when only one date parameter is provided."""
        response = client.get("/api/v1/bank-account-balances?start_date=2026-01-01")
        
        assert response.status_code == 400

    def test_get_accounts_field_values(self, client: TestClient, mock_accounts_single_day):
        """Test that account field values are correctly returned."""
        response = client.get("/api/v1/bank-account-balances?date=2026-01-15")
        
        assert response.status_code == 200
        data = response.json()
        
        # Find the main business account
        main_account = next(
            (acc for acc in data if acc["account"] == "Main Business Account"),
            None,
        )
        
        assert main_account is not None
        assert main_account["iban"] == "FR7612345678901234567890123"
        assert main_account["company"] == "ACME Corporation"
        assert main_account["balance"] == 150000.50
        assert main_account["currency"] == "EUR"
        assert main_account["allowed_overdraft"] == 10000.0

    def test_get_accounts_edge_cases(self, client: TestClient, mock_accounts_edge_cases):
        """Test accounts with edge case values."""
        response = client.get("/api/v1/bank-account-balances?date=2026-01-15")
        
        assert response.status_code == 200
        data = response.json()
        
        assert len(data) == 3
        
        # Verify zero balance
        zero_balance = next(acc for acc in data if acc["balance"] == 0.0)
        assert zero_balance is not None
        
        # Verify negative balance
        negative_balance = next(acc for acc in data if acc["balance"] < 0)
        assert negative_balance["balance"] == -5000.00
        
        # Verify large balance
        large_balance = next(acc for acc in data if acc["balance"] > 1000000)
        assert large_balance["balance"] == 9999999.99

    def test_get_accounts_multiple_companies(self, client: TestClient, mock_accounts_single_day):
        """Test that accounts from multiple companies are returned."""
        response = client.get("/api/v1/bank-account-balances?date=2026-01-15")
        
        assert response.status_code == 200
        data = response.json()
        
        companies = {acc["company"] for acc in data}
        assert "ACME Corporation" in companies
        assert "ACME USA Inc" in companies

    def test_get_accounts_multiple_currencies(self, client: TestClient, mock_accounts_single_day):
        """Test that accounts with multiple currencies are returned."""
        response = client.get("/api/v1/bank-account-balances?date=2026-01-15")
        
        assert response.status_code == 200
        data = response.json()
        
        currencies = {acc["currency"] for acc in data}
        assert "EUR" in currencies
        assert "USD" in currencies
