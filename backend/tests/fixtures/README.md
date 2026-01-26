# Test Fixtures Documentation

Comprehensive mock data for testing the Finance Dashboard application.

## 📋 Table of Contents

- [Account Fixtures](#account-fixtures)
- [Transaction Fixtures](#transaction-fixtures)
- [Chat Fixtures](#chat-fixtures)
- [Usage Examples](#usage-examples)

---

## 🏦 Account Fixtures

### `MOCK_ACCOUNTS_SINGLE_DAY`
**Purpose**: Basic 3-account snapshot for a single date.

**Contents**:
- Main Business Account: 150,000.50 EUR
- Savings Account: 500,000.00 EUR
- USD Operating Account: 75,000.00 USD

**Use case**: Testing single-date balance queries, basic balance summaries.

---

### `MOCK_ACCOUNTS_TIMELINE_30_DAYS`
**Purpose**: Historical balance progression over 30 days (Jan 1-31, 2026).

**Contents**: 90 records (3 accounts × 30 days)
- Shows realistic daily balance evolution
- Reflects transaction impacts (salaries, rent, purchases)
- Aligned with enriched transaction fixtures

**Use case**: 
- Testing `BalanceChart` component
- Historical balance analysis
- Trend detection

**Data highlights**:
- Main Business: 150,000 → 151,417.60 EUR
- Savings: 500,000 → 501,583.32 EUR (interest + investment return)
- USD Operating: 75,000 → 76,500 USD

---

### `MOCK_ACCOUNTS_DIVERSE_TYPES`
**Purpose**: Different account types for comprehensive testing.

**Contents**: 8 accounts
1. **Standard Business Account** (EUR)
2. **Savings Account** (EUR)
3. **Business Credit Card** (negative balance, 50K overdraft)
4. **Line of Credit** (-25,000 EUR, 100K limit)
5. **Investment Portfolio** (250,000 EUR)
6. **UK Operations** (45,000 GBP)
7. **Swiss Account** (80,000 CHF)
8. **Payroll Account** (120,000 EUR)

**Use case**: 
- Multi-currency testing
- Credit account handling
- Different account type scenarios

---

### `MOCK_ACCOUNTS_EDGE_CASES`
**Purpose**: Boundary and error conditions.

**Contents**:
- Zero balance account
- Negative balance account (within overdraft)
- Very large balance (9,999,999.99 EUR)

**Use case**: Edge case testing, validation logic.

---

### `MOCK_ACCOUNTS_EMPTY`
**Purpose**: Empty result set.

**Use case**: Testing no-data scenarios, empty state UI.

---

### `generate_mock_accounts(start_date, days)`
**Purpose**: Dynamic account data generator.

**Parameters**:
- `start_date`: Start date (YYYY-MM-DD)
- `days`: Number of days to generate

**Returns**: List of account dictionaries with daily balance evolution.

**Use case**: Custom date range testing, performance testing.

---

## 💸 Transaction Fixtures

### `MOCK_TRANSACTIONS_SAMPLE`
**Purpose**: Basic 5-transaction sample (no enrichment).

**Contents**: Simple transactions without category/merchant/tags.

**Use case**: Basic transaction API testing.

---

### `MOCK_TRANSACTIONS_ENRICHED` ⭐
**Purpose**: **CRITICAL for frontend** - Fully enriched transactions with categories, merchants, and tags.

**Contents**: 20 transactions covering all 10 category types:
1. ✅ **Salary** (2 transactions, 13,000 EUR total)
2. ✅ **Supplies** (4 transactions, various suppliers)
3. ✅ **Utilities** (2 transactions, electricity + water)
4. ✅ **Rent** (2 transactions, Paris + NYC)
5. ✅ **Insurance** (1 transaction, AXA)
6. ✅ **Tax** (1 transaction, 3,200 EUR)
7. ✅ **Equipment** (1 transaction, Dell 12,500 EUR)
8. ✅ **Travel** (2 transactions, flight + hotel)
9. ✅ **Other Income** (4 transactions, customers + investment)
10. ✅ **Other Expense** (1 transaction, bank fees)

**Data structure**:
```python
{
    "account_description": "Main Business Account",
    "iban": "FR76...",
    "holder_company_name": "ACME Corporation",
    "operation_date": "2026-01-05",
    "value_date": "2026-01-05",
    "amount": 2500.00,
    "currency": "EUR",
    "is_debit": True,
    "category": {
        "id": "rent",
        "name": "Loyer",
        "icon": "building",
        "color": "#17a2b8",
        "description": "Loyers et charges"
    },
    "merchant": "Paris Office Landlord",
    "tags": ["expense", "large", "recurring"]
}
```

**Use case**: 
- **CategoryChart** component (requires category with color)
- **TransactionList** component (requires merchant + tags)
- Enrichment service testing
- Analytics and reporting

**Financial summary**:
- Total Income: 35,730 EUR
- Total Expense: 28,644.65 EUR
- Net Flow: +7,085.35 EUR

---

### `MOCK_TRANSACTIONS_ADVANCED_EDGE_CASES`
**Purpose**: Complex scenarios and edge cases.

**Contents**: 15+ scenarios
- ✅ Refunds (negative expenses)
- ✅ Multiple transactions same day (3 on Jan 15)
- ✅ Duplicate transactions (same amount, date, merchant)
- ✅ Fractional cents (83.33 EUR interest)
- ✅ Very small amounts (2.50 EUR parking)
- ✅ Foreign currency (USD)
- ✅ Recurring subscriptions (Microsoft 365, Adobe)
- ✅ ATM withdrawals
- ✅ Weekend transactions (operation vs value date)
- ✅ Online purchases

**Use case**: 
- Duplicate detection
- Rounding/precision testing
- Recurring pattern detection
- Weekend date handling

---

### `MOCK_TRANSACTIONS_HIGH_VOLUME_DAY`
**Purpose**: Stress testing with 120 transactions on single day (Jan 15, 2026).

**Contents**: 120 generated transactions
- Mix of debits (66%) and credits (33%)
- Varying amounts (15.00 - 402.75 EUR)

**Use case**: 
- Performance testing
- UI scalability (scrolling, pagination)
- Database query optimization

---

### `MOCK_TRANSACTIONS_INACTIVE_PERIOD`
**Purpose**: Empty transaction list (no activity).

**Use case**: Testing periods without transactions, empty state UI.

---

### `MOCK_TRANSACTIONS_EDGE_CASES`
**Purpose**: Basic edge cases.

**Contents**:
- Minimal amount (0.01 EUR)
- Large amount (999,999.99 EUR)
- Zero amount (0.0 EUR)
- Large value date gap (4 days)

---

### `generate_mock_transactions(start_date, end_date, num_transactions)`
**Purpose**: Dynamic transaction generator with 24 transaction types.

**Transaction types** (expanded from 8 to 24):

**Income (6 types)**:
1. Salary Payment (3,000-8,000)
2. Customer Payment (1,000-10,000)
3. Investment Return (500-2,000)
4. Interest Income (50-300)
5. Refund (100-800)
6. Commission (200-1,500)

**Expenses (18 types)**:
1. Rent Payment (1,500-3,000)
2. Supplier Payment (500-5,000)
3. Utility Bill (100-500)
4. Bank Fees (10-50)
5. Tax Payment (1,000-5,000)
6. Insurance Premium (200-800)
7. Subscription Service (20-200)
8. ATM Withdrawal (50-500)
9. Card Payment (15-300)
10. Direct Debit (30-400)
11. Wire Transfer (1,000-15,000)
12. Check Payment (200-3,000)
13. Equipment Purchase (500-20,000)
14. Travel Expense (100-2,000)
15. Office Supplies (50-800)
16. Marketing Expense (300-5,000)
17. Legal Fees (500-3,000)
18. Accounting Services (300-1,500)

**Parameters**:
- `start_date`: Start date (default: "2026-01-01")
- `end_date`: End date (default: "2026-01-31")
- `num_transactions`: Number to generate (default: 50)

**Use case**: Custom scenarios, large dataset testing, date range testing.

---

## 💬 Chat Fixtures

### `MOCK_CHAT_SESSION_BALANCE_INQUIRY`
**Purpose**: Simple balance inquiry conversation.

**Messages**: 4 messages (2 user, 2 assistant)
- Question: "Quel est mon solde total ?"
- Answer: 728,501.92 EUR across 3 accounts
- Follow-up: List of all accounts

**Context data**:
```python
{
    "total_balance": 728501.92,
    "currency": "EUR",
    "account_count": 3,
    "recent_transactions_count": 20
}
```

**Use case**: Basic chatbot testing, balance queries.

---

### `MOCK_CHAT_SESSION_TRANSACTION_ANALYSIS`
**Purpose**: Detailed expense analysis conversation.

**Messages**: 6 messages
- Expense breakdown by category (top 5)
- Comparison to average spending
- Revenue summary with diversification analysis

**Context data**:
- Total income: 35,730 EUR
- Total expense: 28,644.65 EUR
- Net flow: +7,085.35 EUR
- Expense categories with amounts

**Use case**: Analytics chatbot, expense categorization, financial advice.

---

### `MOCK_CHAT_SESSION_ALERTS`
**Purpose**: Proactive alerts and recommendations.

**Messages**: 5 messages
- ⚠️ Low balance alert (15,000 EUR < 20,000 threshold)
- Recommendations: internal transfer, upcoming payments, expected income
- User confirmation

**Context data**:
```python
{
    "alerts": [{
        "severity": "warning",
        "type": "low_balance",
        "message": "Solde faible sur Main Account",
        "threshold": 20000.00
    }]
}
```

**Use case**: Alert system testing, recommendation engine, proactive chatbot.

---

### `MOCK_CHAT_SESSION_COMPLEX_QUERY`
**Purpose**: Year-over-year comparison analysis.

**Messages**: 6 messages
- Compare January 2025 vs 2026
- Category growth analysis
- Detailed breakdown

**Context data**: Multi-year comparison data

**Use case**: Complex analytics, historical comparisons, trend analysis.

---

### `MOCK_CHAT_SESSION_EMPTY`
**Purpose**: New conversation (no messages).

**Use case**: Testing new session creation, empty state UI.

---

### `MOCK_CHAT_SESSIONS`
**Purpose**: Collection of all chat sessions.

**Use case**: Testing session management, session listing.

---

### Helper Functions

#### `get_mock_session_by_id(session_id)`
Retrieve a specific mock chat session by ID.

#### `generate_mock_chat_message(role, content, timestamp)`
Create a new chat message dictionary.

---

## 📚 Usage Examples

### Basic Import
```python
from backend.tests.fixtures import (
    MOCK_ACCOUNTS_SINGLE_DAY,
    MOCK_TRANSACTIONS_ENRICHED,
    MOCK_CHAT_SESSION_BALANCE_INQUIRY,
)
```

### Testing BalanceChart Component
```python
# Use timeline data for historical chart
from backend.tests.fixtures import MOCK_ACCOUNTS_TIMELINE_30_DAYS

def test_balance_chart():
    accounts = MOCK_ACCOUNTS_TIMELINE_30_DAYS
    # Filter by specific account
    main_account = [a for a in accounts if a["iban"] == "FR7612345678901234567890123"]
    # main_account now has 30 days of balance data
```

### Testing CategoryChart Component
```python
# Use enriched transactions with categories
from backend.tests.fixtures import MOCK_TRANSACTIONS_ENRICHED

def test_category_chart():
    transactions = MOCK_TRANSACTIONS_ENRICHED
    # All transactions have category.color for chart
    expenses = [t for t in transactions if t["is_debit"]]
    # Group by category for pie chart
```

### Testing Chatbot
```python
from backend.tests.fixtures import (
    MOCK_CHAT_SESSION_TRANSACTION_ANALYSIS,
    get_mock_session_by_id,
)

def test_chatbot_context():
    session = MOCK_CHAT_SESSION_TRANSACTION_ANALYSIS
    assert session["context"]["total_expense"] == 28644.65
    assert len(session["messages"]) == 6
```

### Dynamic Data Generation
```python
from backend.tests.fixtures import generate_mock_transactions

def test_large_dataset():
    # Generate 500 transactions for Q1 2026
    transactions = generate_mock_transactions(
        start_date="2026-01-01",
        end_date="2026-03-31",
        num_transactions=500
    )
    assert len(transactions) == 500
```

---

## 🎯 Key Frontend Requirements Met

| Component | Required Data | Fixture |
|-----------|--------------|---------|
| **BalanceChart** | Daily balance history | `MOCK_ACCOUNTS_TIMELINE_30_DAYS` |
| **CategoryChart** | Transactions with `category.color` | `MOCK_TRANSACTIONS_ENRICHED` |
| **TransactionList** | Transactions with `merchant`, `tags` | `MOCK_TRANSACTIONS_ENRICHED` |
| **BalanceSummaryCard** | Balance summary object | `MOCK_ACCOUNTS_SINGLE_DAY` |
| **Chatbot** | Session with financial context | `MOCK_CHAT_SESSION_*` |

---

## 📊 Data Statistics

### Accounts
- **Basic fixtures**: 3 accounts (EUR, EUR, USD)
- **Diverse types**: 8 accounts (EUR, USD, GBP, CHF)
- **Timeline**: 90 records (3 accounts × 30 days)

### Transactions
- **Enriched**: 20 fully categorized transactions
- **Edge cases**: 15+ special scenarios
- **High volume**: 120 transactions (single day)
- **Generator**: 24 transaction types

### Chat Sessions
- **Sample sessions**: 4 complete conversations
- **Total messages**: 20+ messages
- **Context scenarios**: Balance inquiry, analytics, alerts, comparisons

---

## 🔄 Version History

**v2.0.0** (January 26, 2026)
- ✨ Added `MOCK_TRANSACTIONS_ENRICHED` (20 transactions with full categorization)
- ✨ Added `MOCK_ACCOUNTS_TIMELINE_30_DAYS` (30-day historical balances)
- ✨ Added `MOCK_ACCOUNTS_DIVERSE_TYPES` (8 account types, multi-currency)
- ✨ Added chat session fixtures (4 complete conversations)
- ✨ Expanded transaction generator from 8 to 24 types
- ✨ Added advanced edge cases (duplicates, refunds, high-volume)
- 🐛 Fixed frontend blocking issues (CategoryChart, TransactionList now testable)

**v1.0.0** (Initial)
- Basic account and transaction fixtures
- Edge case fixtures
- Dynamic data generators

---

## 🚀 Next Steps

1. **Update tests** to use new enriched fixtures
2. **Test frontend components** with enriched transaction data
3. **Validate CategoryChart** displays all 10 categories correctly
4. **Validate BalanceChart** shows 30-day timeline
5. **Test chatbot** with financial context scenarios

---

## 📞 Support

For questions or issues with test fixtures:
- Check this README first
- Review fixture source files in `backend/tests/fixtures/`
- Consult coding guidelines in `.github/instructions/copilot-instructions.md`
