import { afterEach, describe, expect, it } from 'vitest'
import { server } from '../tests/mocks/server'
import { http, HttpResponse } from 'msw'
import apiClient from './client'

const API_BASE = 'http://localhost:8000/api/v1'

describe('apiClient', () => {
  afterEach(() => {
    // MSW reset is handled globally; this is just semantic here
  })

  it('unwraps response data on success', async () => {
    server.use(
      http.get(`${API_BASE}/hello`, () => HttpResponse.json({ ok: true, value: 42 }))
    )
    const res = await apiClient.get('/hello')
    expect(res).toEqual({ ok: true, value: 42 })
  })

  it('normalizes error message from backend detail', async () => {
    server.use(
      http.get(`${API_BASE}/boom`, () => HttpResponse.json({ detail: 'Oops' }, { status: 400 }))
    )
    await expect(apiClient.get('/boom')).rejects.toThrow('Oops')
  })
})
