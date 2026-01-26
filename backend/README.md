# Finance Dashboard Backend

Backend API for the Finance Dashboard application built with FastAPI.

## Features

- **Account Management**: Retrieve bank account balances for single dates or date ranges
- **Transaction Management**: Fetch bank transactions with date filtering
- **Mock Data Support**: Comprehensive test fixtures for development and testing
- **RESTful API**: Clean, well-documented API endpoints
- **Type Safety**: Pydantic models for data validation

## Project Structure

```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI application entry point
│   ├── models/              # Pydantic models
│   │   ├── account.py
│   │   └── transaction.py
│   └── routes/              # API endpoints
│       ├── accounts.py
│       └── transactions.py
├── tests/
│   ├── conftest.py          # Pytest fixtures
│   ├── fixtures/            # Mock data
│   │   ├── mock_accounts.py
│   │   └── mock_transactions.py
│   ├── test_accounts.py
│   └── test_transactions.py
├── requirements.txt
└── pyproject.toml
```

## Setup

### Prerequisites

- Python 3.10+
- pip

### Installation

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

Start the development server:

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

### API Documentation

Once running, access the interactive API documentation:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## API Endpoints

### Accounts

**GET** `/api/v1/bank-account-balances`

Query parameters:
- `date` (optional): Single date query (YYYY-MM-DD)
- `start_date` & `end_date` (optional): Date range query

Examples:
```bash
# Single date
curl "http://localhost:8000/api/v1/bank-account-balances?date=2026-01-15"

# Date range
curl "http://localhost:8000/api/v1/bank-account-balances?start_date=2026-01-01&end_date=2026-01-31"
```

### Transactions

**GET** `/api/v1/bank-transactions`

Query parameters:
- `from_date` (required): Start date (YYYY-MM-DD)
- `to_date` (required): End date (YYYY-MM-DD)

Example:
```bash
curl "http://localhost:8000/api/v1/bank-transactions?from_date=2026-01-01&to_date=2026-01-31"
```

## Testing

Run all tests:

```bash
pytest
```

Run with coverage:

```bash
pytest --cov=app --cov-report=html
```

Run specific test file:

```bash
pytest tests/test_accounts.py
pytest tests/test_transactions.py
```

### Test Fixtures

The project includes comprehensive mock data:

- **Mock Accounts**: Single day, date ranges, edge cases (zero balance, negative balance, large amounts)
- **Mock Transactions**: Sample data, date ranges, edge cases (minimal amounts, large amounts, date differences)

## Mock Data

### Using Mock Data in Tests

```python
def test_example(client, mock_accounts_single_day):
    response = client.get("/api/v1/bank-account-balances?date=2026-01-15")
    assert response.status_code == 200
```

### Generating Custom Mock Data

```python
from tests.fixtures.mock_accounts import generate_mock_accounts
from tests.fixtures.mock_transactions import generate_mock_transactions

# Generate 60 days of account data
accounts = generate_mock_accounts(start_date="2026-01-01", days=60)

# Generate 100 transactions
transactions = generate_mock_transactions(
    start_date="2026-01-01",
    end_date="2026-03-31",
    num_transactions=100
)
```

## Development

### Code Style

Follow the coding guidelines in `.github/instructions/chatbot-finance.instructions.md`:

- PascalCase for components, interfaces, types
- camelCase for variables and functions
- Clear, explicit naming
- Comprehensive error handling
- Modular code structure

### Adding New Endpoints

1. Create/update model in `app/models/`
2. Create/update route in `app/routes/`
3. Register router in `app/main.py`
4. Create mock fixtures in `tests/fixtures/`
5. Add tests in `tests/`

## Production Considerations

- Replace in-memory storage with actual database
- Implement authentication and authorization
- Add rate limiting
- Configure CORS appropriately
- Enable HTTPS
- Add logging and monitoring
- Implement data encryption for sensitive information

## License

MIT
