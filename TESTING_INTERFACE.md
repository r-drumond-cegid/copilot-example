# Testing Enriched Mock Data on Interface

## Quick Start Guide

### 1. Start Backend Server

Open a terminal in the `backend` directory and run:

```powershell
cd backend
C:/WORKSPACE_PULSE/copilot-example/.venv/Scripts/python.exe -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

You should see:
```
✓ Loaded enriched mock data:
  - 19 enriched transactions
  - 93 account balance records (30-day timeline)
INFO:     Uvicorn running on http://127.0.0.1:8000
```

### 2. Start Frontend Server

Open another terminal in the `frontend` directory and run:

```powershell
cd frontend
npm run dev
```

You should see:
```
VITE ready in XXX ms
➜  Local:   http://localhost:5173/
```

### 3. Open Browser

Navigate to: **http://localhost:5173**

---

## 🧪 Testing the Enriched Data

### Test 1: Balance Summary Card
**What to check:**
- ✅ Total balance displayed (should be ~728,501 EUR)
- ✅ 3 accounts shown
- ✅ Average, highest, lowest balances

### Test 2: Balance Chart (Timeline)
**What to check:**
- ✅ Chart shows 30-day timeline (Jan 1-31, 2026)
- ✅ Daily balance evolution visible
- ✅ Three account lines displayed:
  - Main Business Account (blue)
  - Savings Account (green)
  - USD Operating Account (yellow)
- ✅ Balance changes align with transaction dates

### Test 3: Transaction List
**What to check:**
- ✅ 19 transactions displayed
- ✅ Each transaction shows:
  - **Category badge with color** (NEW!)
  - **Merchant name** (NEW!)
  - **Tags** (income/expense, large, recurring, etc.) (NEW!)
  - Amount, date, account
- ✅ Filter by All/Income/Expense works
- ✅ Sort by date or amount works

### Test 4: Category Chart (Pie Chart)
**What to check:**
- ✅ Pie chart displays expense categories
- ✅ **Colors match category definitions** (NEW!)
- ✅ Top categories shown:
  - Équipement (purple) - 12,500 EUR
  - Fournitures (gray) - 5,300 EUR
  - Loyer (cyan) - 4,300 EUR
  - Taxes (red) - 3,200 EUR
  - Déplacements (orange) - 1,170 EUR
- ✅ Click on category to see breakdown

### Test 5: Date Range Picker
**What to test:**
- ✅ Change date range to Jan 1-15, 2026
- ✅ Data updates to show 15 days of balances
- ✅ Transactions filtered to first half of month
- ✅ Change to Jan 15-31, 2026
- ✅ Data updates to show second half

---

## 🔍 API Endpoint Testing

### Test Enriched Transactions API

Open browser to: **http://127.0.0.1:8000/api/v1/transactions/enriched?from_date=2026-01-01&to_date=2026-01-31**

**Expected response:**
```json
[
  {
    "account": "Main Business Account",
    "iban": "FR7612345678901234567890123",
    "company": "ACME Corporation",
    "operation_date": "2026-01-01",
    "value_date": "2026-01-01",
    "amount": 6500.0,
    "currency": "EUR",
    "is_debit": false,
    "category": {
      "id": "salary",
      "name": "Salaire",
      "icon": "money-bill-wave",
      "color": "#28a745",
      "description": "Revenus salariaux"
    },
    "merchant": "Payroll Department",
    "tags": ["income", "large", "recurring"]
  },
  ...
]
```

### Test Balance Summary API

Open browser to: **http://127.0.0.1:8000/api/v1/balance-summary?date=2026-01-26**

**Expected response:**
```json
{
  "total_balance": 728501.92,
  "account_count": 3,
  "average_balance": 242833.97,
  "highest_balance": 501583.32,
  "lowest_balance": 76500.0,
  "total_overdraft_allowed": 15000.0,
  "accounts": [...]
}
```

### Test Alerts API

Open browser to: **http://127.0.0.1:8000/api/v1/alerts?date=2026-01-26**

**Expected:** No alerts (all balances healthy)

### Test API Documentation

Open browser to: **http://127.0.0.1:8000/docs**

This opens the interactive Swagger UI where you can:
- ✅ See all available endpoints
- ✅ Try out API calls directly
- ✅ See request/response schemas

---

## 🎨 Visual Verification Checklist

### CategoryChart Component
- [ ] **Before**: Empty or "No category data" message
- [x] **After**: Colorful pie chart with 10 categories
- [ ] Category colors:
  - Salaire: Green (#28a745)
  - Équipement: Purple (#6610f2)
  - Loyer: Cyan (#17a2b8)
  - Taxes: Red (#dc3545)
  - Déplacements: Orange (#fd7e14)

### TransactionList Component
- [ ] **Before**: Plain transaction rows
- [x] **After**: Each row shows:
  - Colored category badge
  - Merchant name in subtitle
  - Tags as small chips
  - Amount and date

### BalanceChart Component
- [ ] **Before**: Single point or mock data
- [x] **After**: Smooth line chart showing 30 days
- [ ] Three lines for three accounts
- [ ] Tooltips show exact values on hover

---

## 🐛 Troubleshooting

### Backend won't start
**Error**: `ModuleNotFoundError: No module named 'tests'`

**Solution**: Run from backend directory:
```powershell
cd backend
python -m uvicorn app.main:app --reload
```

### Frontend shows "No data"
**Check**:
1. Backend is running (http://127.0.0.1:8000)
2. Check browser console for CORS errors
3. Check Network tab - API calls should return data

### Categories not showing colors
**Check**:
1. Open Network tab
2. Look for `/api/v1/transactions/enriched` call
3. Verify response includes `category.color` field
4. Check browser console for React errors

### Timeline chart shows only one day
**Check**:
1. Date range picker is set to Jan 1-31, 2026
2. API call: `/api/v1/bank-account-balances?start_date=2026-01-01&end_date=2026-01-31`
3. Response should have 93 records (3 accounts × 31 days)

---

## 📊 Expected Data Summary

### Accounts (Timeline 30 days)
- **Main Business**: 150,000 → 151,417.60 EUR (31 days)
- **Savings**: 500,000 → 501,583.32 EUR (31 days)
- **USD Operating**: 75,000 → 76,500 USD (31 days)

### Transactions (Enriched)
- **Total**: 19 transactions
- **Income**: 8 transactions, 35,730 EUR
- **Expenses**: 11 transactions, 28,644.65 EUR
- **Net Flow**: +7,085.35 EUR

### Categories Coverage
1. ✅ Salaire (2 transactions)
2. ✅ Fournitures (2 transactions)
3. ✅ Services publics (2 transactions)
4. ✅ Loyer (2 transactions)
5. ✅ Assurance (1 transaction)
6. ✅ Taxes (1 transaction)
7. ✅ Équipement (1 transaction)
8. ✅ Déplacements (2 transactions)
9. ✅ Autres revenus (4 transactions)
10. ✅ Autres dépenses (1 transaction)

---

## ✨ New Features Enabled

### 1. Category Filtering
In TransactionList, you can now:
- Filter by income/expense
- See category-specific breakdowns
- Click on category badge to filter

### 2. Merchant Tracking
- Each transaction shows detected merchant
- Can search by merchant name
- Merchant history tracking

### 3. Smart Tagging
Tags automatically added:
- `income` / `expense` - Transaction type
- `large` - Amounts > 10,000
- `recurring` - Monthly patterns (rent, salary)
- `business` - Business-related expenses
- `subscription` - Recurring software

### 4. Timeline Analysis
- 30-day balance evolution
- Visual trend identification
- Compare account performance

---

## 🚀 Next Steps

After verifying the interface:

1. **Test date range filtering** - Change dates, verify data updates
2. **Test sorting/filtering** - Sort transactions, filter by category
3. **Check responsive design** - Resize browser window
4. **Test chatbot** - Ask "Quel est mon solde?" (if implemented)
5. **Export reports** - Test any export functionality

---

## 📝 Notes

- All dates are in **January 2026** (current test data)
- Amounts are in **EUR** and **USD**
- Timezone is **UTC**
- Mock data loads automatically on backend startup
- Data persists in memory until server restart

**Last Updated**: January 26, 2026
