---
title: Finance Dashboard Architecture & Interfaces Specification
version: 1.0
date_created: 2026-01-29
last_updated: 2026-01-29
owner: Finance Dashboard Team
tags: [architecture, app, backend, frontend, cds, plotly, fastapi, react]
---

# Introduction

This specification defines the architecture, requirements, interfaces, data contracts, and testing strategy for the Finance Dashboard project. It is structured for clear consumption by engineers and generative AIs, and is self-contained.

## 1. Purpose & Scope

The purpose of this specification is to formalize the end-to-end system design and integration points for a responsive, accessible finance dashboard that surfaces account balances, transactions, analytics, and a chatbot assistant. Scope covers:

- Backend service using FastAPI for accounts, transactions, analytics, and chat.
- Frontend web app using React + Vite, adhering to the Cegid Design System (CDS) and Plotly for charts.
- Data models for `Account`, `Transaction`, `BalanceSummary`, chat entities, and enrichment.
- Security, accessibility, and testing requirements.

Audience includes full-stack developers, QA engineers, and operations personnel. Assumptions: the system runs in a modern browser; backend runs in Python 3.11+; environment provides Azure OpenAI credentials server-side only.

## 2. Definitions

- CDS: Cegid Design System; UI components, tokens, and accessibility standards.
- Plotly: Plotly.js charting library used for interactive charts.
- FastAPI: Python framework for building REST APIs.
- Enrichment: Process of categorizing transactions and adding derived attributes.
- Azure OpenAI: Azure-hosted OpenAI service used for chatbot responses.
- APIRouter: FastAPI router instance for grouping endpoints.
- SLA: Service Level Agreement defining uptime and response characteristics.

## 3. Requirements, Constraints & Guidelines

- **REQ-001**: Provide endpoints for accounts, transactions, analytics, and chat with documented request/response schemas.
- **REQ-002**: Frontend must use CDS components via `cds-react` or local shim.
- **REQ-003**: Charts must use Plotly.js and be responsive.
- **REQ-004**: Use React Functional Components and hooks; ES6+ features in JavaScript/TypeScript.
- **REQ-005**: Implement data enrichment and categorization for transactions.
- **REQ-006**: Provide accessible UI (WCAG 2.1 AA), including keyboard navigation and ARIA roles on dialogs.
- **REQ-007**: Chatbot must support session creation, history retrieval, deletion, and listing sessions.
- **REQ-008**: Provide analytics: balance summary, low balance alerts, transaction trends, categories.
- **SEC-001**: Do not expose secrets or Azure OpenAI credentials in the frontend; all secrets must remain server-side.
- **SEC-002**: Validate and sanitize all user inputs for API requests; enforce parameter constraints.
- **SEC-003**: Encrypt sensitive data at rest and in transit; enforce HTTPS.
- **SEC-004**: Log security-relevant events (e.g., failed requests, unusual access patterns) without storing sensitive plaintext.
- **CON-001**: Maintain separation of concerns between frontend, backend, and AI services.
- **CON-002**: Use consistent naming conventions: PascalCase for components/types; camelCase for variables/functions; ALL_CAPS for constants.
- **CON-003**: Backend must return JSON; avoid breaking changes to API contracts without versioning.
- **GUD-001**: Prefer clear, explicit names and modular functions; comment complex logic (e.g., filters, enrichment).
- **GUD-002**: Use CDS accessibility patterns for forms, tables, and charts; provide descriptions and labels.
- **PAT-001**: Encapsulate charts in CDS `Card`/`Panel` components; keep dimensions reactive.
- **PAT-002**: Centralize API client and endpoints; manage querystring construction consistently.

## 4. Interfaces & Data Contracts

### 4.1 Backend Endpoints (FastAPI)

Base: `/` (served by FastAPI app). Endpoints and query parameters below are authoritative.

- Accounts
  - `GET /bank-account-balances`
    - Query: `date` (YYYY-MM-DD, optional), `start_date` (YYYY-MM-DD, optional), `end_date` (YYYY-MM-DD, optional)
    - Response: `List<AccountResponse>`
    - Implementation reference: [backend/app/routes/accounts.py](backend/app/routes/accounts.py)

- Transactions
  - `GET /bank-transactions`
    - Query: `from_date` (YYYY-MM-DD, required), `to_date` (YYYY-MM-DD, required)
    - Response: `List<TransactionResponse>`
    - Implementation reference: [backend/app/routes/transactions.py](backend/app/routes/transactions.py)
  - `GET /transactions/enriched`
    - Query: `from_date` (YYYY-MM-DD, required), `to_date` (YYYY-MM-DD, required), `category` (string, optional), `min_amount` (float, optional), `max_amount` (float, optional), `is_debit` (bool, optional)
    - Response: `List<EnrichedTransaction>`
    - Implementation reference: [backend/app/routes/analytics.py](backend/app/routes/analytics.py)
  - `GET /transactions/trends`
    - Query: `from_date` (YYYY-MM-DD, required), `to_date` (YYYY-MM-DD, required)
    - Response: `Record<string, any>` trends summary
    - Implementation reference: [backend/app/routes/analytics.py](backend/app/routes/analytics.py)

- Analytics
  - `GET /balance-summary`
    - Query: `date` (YYYY-MM-DD, optional), `start_date` (YYYY-MM-DD, optional), `end_date` (YYYY-MM-DD, optional)
    - Response: `BalanceSummary`
    - Implementation reference: [backend/app/routes/analytics.py](backend/app/routes/analytics.py)
  - `GET /alerts`
    - Query: `threshold` (float, optional; default 0.1)
    - Response: `List<string>` or structured alert objects
    - Implementation reference: [backend/app/routes/analytics.py](backend/app/routes/analytics.py)
  - `GET /categories`
    - Response: `List<TransactionCategory>`
    - Implementation reference: [backend/app/routes/analytics.py](backend/app/routes/analytics.py)

- Chat
  - `POST /chat`
    - Body: `ChatRequest { message: string; session_id?: string }`
    - Response: `ChatResponse`
    - Implementation reference: [backend/app/routes/chat.py](backend/app/routes/chat.py)
  - `GET /chat/history/{session_id}`
    - Path: `session_id` (string)
    - Response: `ChatSession`
    - Implementation reference: [backend/app/routes/chat.py](backend/app/routes/chat.py)
  - `DELETE /chat/{session_id}`
    - Path: `session_id` (string)
    - Response: `{ success: boolean }`
    - Implementation reference: [backend/app/routes/chat.py](backend/app/routes/chat.py)
  - `GET /chat/sessions`
    - Response: `List<ChatSession>`
    - Implementation reference: [backend/app/routes/chat.py](backend/app/routes/chat.py)

### 4.2 Frontend API Client

Client functions are centralized in:
- [frontend/src/api/accounts.js](frontend/src/api/accounts.js)
- [frontend/src/api/transactions.js](frontend/src/api/transactions.js)
- [frontend/src/api/chat.js](frontend/src/api/chat.js)

### 4.3 Data Models (Schemas)

Representative fields (full schemas in backend models):

- `AccountResponse`
  - `account`: string
  - `iban`: string
  - `company`: string
  - `balance`: float
  - Reference: [backend/app/models/account.py](backend/app/models/account.py)

- `BalanceSummary`
  - `total_balance`: float (sum of all account balances)
  - `account_count`: int
  - `highest_balance`: float
  - `lowest_balance`: float
  - `average_balance`: float
  - `accounts`: `List<AccountResponse>`
  - Reference: [backend/app/models/account.py](backend/app/models/account.py)

- `TransactionResponse`
  - `account`: string
  - `iban`: string
  - `company`: string
  - `amount`: float
  - `is_debit`: bool
  - Reference: [backend/app/models/transaction.py](backend/app/models/transaction.py)

- `EnrichedTransaction`
  - `account`: string
  - `iban`: string
  - `company`: string
  - `amount`: float
  - `is_debit`: bool
  - `category`: `TransactionCategory | null`
  - Reference: [backend/app/models/transaction.py](backend/app/models/transaction.py)

- `TransactionCategory`
  - `id`: string | number
  - `name`: string
  - `type`: string (`income` | `expense` | `other`)
  - Reference: [backend/app/models/transaction.py](backend/app/models/transaction.py)

- Chat models
  - `ChatMessage { role: 'user'|'assistant'; content: string; timestamp: string }`
  - `ChatSession { session_id: string; messages: List<ChatMessage> }`
  - `ChatRequest { message: string; session_id?: string }`
  - `ChatResponse { message: ChatMessage }`
  - Reference: [backend/app/models/chat.py](backend/app/models/chat.py)

### 4.4 UI Components & Pages

- Pages: [frontend/src/pages/Dashboard.jsx](frontend/src/pages/Dashboard.jsx)
- Components: Balance summary card, transaction list, date picker, charts, header, chatbot UI
  - References: [frontend/src/components/dashboard/](frontend/src/components/dashboard/), [frontend/src/components/charts/](frontend/src/components/charts/), [frontend/src/components/chatbot/](frontend/src/components/chatbot/), [frontend/src/components/layout/](frontend/src/components/layout/)
- Theming: [frontend/src/theme/cegidTheme.js](frontend/src/theme/cegidTheme.js)
- CDS shim: [frontend/src/cds-react-shim.js](frontend/src/cds-react-shim.js), [frontend/src/types/cds-react.d.ts](frontend/src/types/cds-react.d.ts)

## 5. Acceptance Criteria

- **AC-001**: Given valid date inputs, When calling `GET /bank-account-balances`, Then the API returns `List<AccountResponse>` with HTTP 200 and correct aggregates.
- **AC-002**: Given valid range, When calling `GET /transactions/trends`, Then the response contains trend metrics for credits and debits.
- **AC-003**: Given message and optional `session_id`, When `POST /chat` is called, Then `ChatResponse` contains an assistant message and session is persisted.
- **AC-004**: Given `session_id`, When `GET /chat/history/{session_id}` is called, Then the full `ChatSession` is returned.
- **AC-005**: Given threshold, When `GET /alerts` is called, Then alert list matches balances below threshold.
- **AC-006**: UI components meet WCAG 2.1 AA: focus styles visible, keyboard navigation complete, proper labels and ARIA roles.
- **AC-007**: Plotly charts resize responsively and include accessible descriptions.
- **AC-008**: Frontend uses CDS components for forms, tables, notifications; no custom components where CDS exists.

## 6. Test Automation Strategy

- **Test Levels**: Unit (models, services), Integration (routes/endpoints), End-to-End (frontend-backend flows).
- **Backend Frameworks**: `pytest`, `requests` or FastAPI `TestClient`; data fixtures as in [backend/app/tests/fixtures](backend/app/tests/fixtures).
- **Frontend Frameworks**: `Vitest` and `@testing-library/react` for components; mock API via MSW.
- **Test Data Management**: Use mock data generators documented in [backend/MOCK_DATA_GENERATION.md](backend/MOCK_DATA_GENERATION.md); isolate test data per run and clean up in fixtures.
- **CI/CD Integration**: GitHub Actions pipeline to run linting, unit/integration tests, and build; fail on coverage below thresholds.
- **Coverage Requirements**: Backend ≥ 80% lines; Frontend ≥ 70% statements; critical paths ≥ 90%.
- **Performance Testing**: Light load tests for endpoints (e.g., `balance-summary`, `transactions/trends`) targeting p95 latency ≤ 300ms under moderate load.

## 7. Rationale & Context

The system prioritizes clarity, accessibility, and security. CDS ensures consistent UI/UX and accessibility. Plotly provides interactive, responsive charts. FastAPI offers fast development and type-safe APIs. Azure OpenAI is leveraged for contextual financial assistance, with a robust fallback when unavailable.

## 8. Dependencies & External Integrations

### External Systems
- **EXT-001**: Banking data source (mocked in this project) - Provides account balances and transactions.

### Third-Party Services
- **SVC-001**: Azure OpenAI - Text generation for chatbot. SLA requires graceful degradation; provide fallback responses.

### Infrastructure Dependencies
- **INF-001**: HTTPS termination and secret management (e.g., Azure Key Vault or environment variables) - Secure runtime configuration.

### Data Dependencies
- **DAT-001**: Transaction and account datasets - CSV or in-memory mocks; cadence configurable.

### Technology Platform Dependencies
- **PLT-001**: Python 3.11+ runtime for FastAPI; Node 18+ for Vite/React.

### Compliance Dependencies
- **COM-001**: GDPR/PII handling - Ensure no personal data exposure in logs; support data deletion requests.

Note: Dependencies specify capabilities (e.g., “OAuth 2.0 library” if authentication is added) rather than specific packages.

## 9. Examples & Edge Cases

```code
// Example: Balance summary equation
// total_balance = sum of account balances
// KaTeX: $total\\_balance = \\sum_{i=1}^{n} balance_i$

// Edge cases:
// - Empty accounts list → total_balance = 0, account_count = 0
// - Transactions outside date range → endpoints return empty lists
// - Chat with missing session_id → server creates new session
// - Invalid query params → 400 Bad Request with error details
```

## 10. Validation Criteria

- API contracts match schemas in Section 4.3.
- Endpoints satisfy acceptance criteria with positive and negative tests.
- UI complies with CDS and WCAG 2.1 AA checks (keyboard, focus, ARIA).
- Secrets are server-side only; no credentials in frontend bundles.
- Charts are responsive and provide descriptive text for accessibility.

## 11. Related Specifications / Further Reading

- Coding Guidelines: [.github/instructions/copilot-instructions.instructions.md](.github/instructions/copilot-instructions.instructions.md)
- CDS Documentation: [docs/cds/component-catalog.md](docs/cds/component-catalog.md), [docs/cds/conformity-report.md](docs/cds/conformity-report.md), [docs/cds/recommendations.md](docs/cds/recommendations.md)
- Backend Readme: [backend/README.md](backend/README.md)
- Frontend Readme: [frontend/README.md](frontend/README.md)
- Quickstarts: [QUICKSTART.md](QUICKSTART.md), [QUICKSTART_CHATBOT.md](QUICKSTART_CHATBOT.md)