import { http, HttpResponse } from 'msw'

const API_BASE = 'http://localhost:8000/api/v1'

export const handlers = [
  // Balance summary
  http.get(`${API_BASE}/balance-summary`, ({ request }) => {
    const url = new URL(request.url)
    const date = url.searchParams.get('date') || '2026-02-01'
    return HttpResponse.json({
      date,
      total_balance: 123456.78,
      accounts: [],
    })
  }),

  // Alerts
  http.get(`${API_BASE}/alerts`, () => {
    return HttpResponse.json({ alerts: [] })
  }),

  // Enriched transactions
  http.get(`${API_BASE}/transactions/enriched`, () => {
    return HttpResponse.json([
      { id: 't1', amount: -100, category: 'Food', date: '2026-01-10' },
      { id: 't2', amount: 2000, category: 'Salary', date: '2026-01-15' },
    ])
  }),

  // Trends
  http.get(`${API_BASE}/transactions/trends`, () => {
    return HttpResponse.json({
      total_income: 2000,
      total_expenses: 100,
      net_flow: 1900,
      transaction_count: 2,
    })
  }),
]
