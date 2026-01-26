"""Tests for transaction API endpoints."""

import pytest
from fastapi.testclient import TestClient


class TestTransactions:
    """Test cases for transaction endpoints."""

    def test_get_transactions_date_range(self, client: TestClient, mock_transactions_sample):
        """Test retrieving transactions for a date range."""
        response = client.get(
            "/api/v1/bank-transactions?from_date=2026-01-01&to_date=2026-01-31"
        )
        
        assert response.status_code == 200
        data = response.json()
        
        assert len(data) == 5
        
        # Verify field transformations
        first_transaction = data[0]
        assert "account" in first_transaction
        assert "company" in first_transaction
        assert "operation_date" in first_transaction
        assert "value_date" in first_transaction
        assert "amount" in first_transaction
        assert "is_debit" in first_transaction
        assert "account_description" not in first_transaction
        assert "holder_company_name" not in first_transaction

    def test_get_transactions_filtered_by_date(self, client: TestClient, mock_transactions_sample):
        """Test filtering transactions by specific date range."""
        response = client.get(
            "/api/v1/bank-transactions?from_date=2026-01-05&to_date=2026-01-10"
        )
        
        assert response.status_code == 200
        data = response.json()
        
        # Should only return transactions within the specified range
        assert len(data) == 3
        
        for trans in data:
            assert "2026-01-05" <= trans["operation_date"] <= "2026-01-10"

    def test_get_transactions_empty_result(self, client: TestClient, mock_transactions_sample):
        """Test retrieving transactions for a date range with no data."""
        response = client.get(
            "/api/v1/bank-transactions?from_date=2025-12-01&to_date=2025-12-31"
        )
        
        assert response.status_code == 200
        data = response.json()
        assert len(data) == 0

    def test_get_transactions_missing_parameters(self, client: TestClient, mock_transactions_sample):
        """Test error handling when required parameters are missing."""
        response = client.get("/api/v1/bank-transactions")
        
        assert response.status_code == 422  # FastAPI validation error

    def test_get_transactions_invalid_date_format(self, client: TestClient, mock_transactions_sample):
        """Test error handling for invalid date format."""
        response = client.get(
            "/api/v1/bank-transactions?from_date=01-01-2026&to_date=31-01-2026"
        )
        
        assert response.status_code == 400
        assert "Invalid date format" in response.json()["detail"]

    def test_get_transactions_invalid_date_range(self, client: TestClient, mock_transactions_sample):
        """Test error handling when from_date is after to_date."""
        response = client.get(
            "/api/v1/bank-transactions?from_date=2026-01-31&to_date=2026-01-01"
        )
        
        assert response.status_code == 400
        assert "before or equal" in response.json()["detail"]

    def test_get_transactions_field_values(self, client: TestClient, mock_transactions_sample):
        """Test that transaction field values are correctly returned."""
        response = client.get(
            "/api/v1/bank-transactions?from_date=2026-01-01&to_date=2026-01-31"
        )
        
        assert response.status_code == 200
        data = response.json()
        
        # Find the first transaction
        first_trans = data[0]
        
        assert first_trans["account"] == "Main Business Account"
        assert first_trans["iban"] == "FR7612345678901234567890123"
        assert first_trans["company"] == "ACME Corporation"
        assert first_trans["operation_date"] == "2026-01-05"
        assert first_trans["value_date"] == "2026-01-05"
        assert first_trans["amount"] == 5000.00
        assert first_trans["currency"] == "EUR"
        assert first_trans["is_debit"] is False

    def test_get_transactions_debit_credit_mix(self, client: TestClient, mock_transactions_sample):
        """Test that both debit and credit transactions are returned."""
        response = client.get(
            "/api/v1/bank-transactions?from_date=2026-01-01&to_date=2026-01-31"
        )
        
        assert response.status_code == 200
        data = response.json()
        
        debits = [trans for trans in data if trans["is_debit"]]
        credits = [trans for trans in data if not trans["is_debit"]]
        
        assert len(debits) > 0
        assert len(credits) > 0

    def test_get_transactions_multiple_accounts(self, client: TestClient, mock_transactions_sample):
        """Test that transactions from multiple accounts are returned."""
        response = client.get(
            "/api/v1/bank-transactions?from_date=2026-01-01&to_date=2026-01-31"
        )
        
        assert response.status_code == 200
        data = response.json()
        
        accounts = {trans["account"] for trans in data}
        assert "Main Business Account" in accounts
        assert "Savings Account" in accounts
        assert "USD Operating Account" in accounts

    def test_get_transactions_multiple_currencies(self, client: TestClient, mock_transactions_sample):
        """Test that transactions with multiple currencies are returned."""
        response = client.get(
            "/api/v1/bank-transactions?from_date=2026-01-01&to_date=2026-01-31"
        )
        
        assert response.status_code == 200
        data = response.json()
        
        currencies = {trans["currency"] for trans in data}
        assert "EUR" in currencies
        assert "USD" in currencies

    def test_get_transactions_edge_cases(self, client: TestClient, mock_transactions_edge_cases):
        """Test transactions with edge case values."""
        response = client.get(
            "/api/v1/bank-transactions?from_date=2026-01-01&to_date=2026-01-31"
        )
        
        assert response.status_code == 200
        data = response.json()
        
        assert len(data) == 3
        
        # Verify minimal amount
        minimal = next(trans for trans in data if trans["amount"] == 0.01)
        assert minimal is not None
        
        # Verify large amount
        large = next(trans for trans in data if trans["amount"] > 100000)
        assert large["amount"] == 999999.99
        
        # Verify zero amount
        zero = next(trans for trans in data if trans["amount"] == 0.0)
        assert zero is not None

    def test_get_transactions_value_date_difference(self, client: TestClient, mock_transactions_edge_cases):
        """Test transactions where value_date differs from operation_date."""
        response = client.get(
            "/api/v1/bank-transactions?from_date=2026-01-01&to_date=2026-01-31"
        )
        
        assert response.status_code == 200
        data = response.json()
        
        # Find transaction with different value_date
        diff_dates = next(
            (trans for trans in data if trans["operation_date"] != trans["value_date"]),
            None,
        )
        
        assert diff_dates is not None
        assert diff_dates["operation_date"] == "2026-01-16"
        assert diff_dates["value_date"] == "2026-01-20"

    def test_get_transactions_large_dataset(self, client: TestClient, mock_transactions_range):
        """Test handling of larger transaction datasets."""
        response = client.get(
            "/api/v1/bank-transactions?from_date=2026-01-01&to_date=2026-01-31"
        )
        
        assert response.status_code == 200
        data = response.json()
        
        # Should return all 50 generated transactions
        assert len(data) == 50
        
        # Verify all transactions are within date range
        for trans in data:
            assert "2026-01-01" <= trans["operation_date"] <= "2026-01-31"
