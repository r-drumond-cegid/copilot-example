import { describe, it, expect } from 'vitest'
import { server } from '../tests/mocks/server'
import { http, HttpResponse } from 'msw'
import { getBalanceSummary, getAccountBalances, getAlerts } from './accounts'

const API_BASE = 'http://localhost:8000/api/v1'

describe('accounts API', () => {
  it('passes date param to getBalanceSummary', async () => {
    const seen = { date: null }
    server.use(
      http.get(`${API_BASE}/balance-summary`, ({ request }) => {
        const url = new URL(request.url)
        seen.date = url.searchParams.get('date')
        return HttpResponse.json({ ok: true })
      })
    )
    const res = await getBalanceSummary({ date: '2026-02-01' })
    expect(res).toEqual({ ok: true })
    expect(seen.date).toBe('2026-02-01')
  })

  it('builds query for getAccountBalances', async () => {
    const seen = {}
    server.use(
      http.get(`${API_BASE}/bank-account-balances`, ({ request }) => {
        const url = new URL(request.url)
        seen.date = url.searchParams.get('date')
        seen.start_date = url.searchParams.get('start_date')
        seen.end_date = url.searchParams.get('end_date')
        return HttpResponse.json({ items: [] })
      })
    )
    const res = await getAccountBalances({ date: '2026-02-02', start_date: '2026-01-01', end_date: '2026-02-02' })
    expect(res).toEqual({ items: [] })
    expect(seen).toEqual({ date: '2026-02-02', start_date: '2026-01-01', end_date: '2026-02-02' })
  })

  it('calls alerts endpoint with threshold', async () => {
    const seen = { threshold: null }
    server.use(
      http.get(`${API_BASE}/alerts`, ({ request }) => {
        const url = new URL(request.url)
        seen.threshold = url.searchParams.get('threshold')
        return HttpResponse.json({ alerts: [{ message: 'Low balance' }] })
      })
    )
    const res = await getAlerts(0.2)
    expect(res).toEqual({ alerts: [{ message: 'Low balance' }] })
    expect(seen.threshold).toBe('0.2')
  })
})
