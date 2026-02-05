import { render, screen, waitFor } from '@testing-library/react'
import App from '../App.jsx'
import { server } from '../tests/mocks/server'
import { http, HttpResponse } from 'msw'

const API_BASE = 'http://localhost:8000/api/v1'

describe('Dashboard', () => {
  it('shows loading then renders key sections on success', async () => {
    render(<App />)

    // Loading state
    expect(screen.getByText(/chargement des données/i)).toBeInTheDocument()

    // Content sections (from default handlers)
    expect(await screen.findByRole('heading', { name: /évolution du solde/i })).toBeInTheDocument()
    expect(screen.getByRole('heading', { name: /dépenses par catégorie/i })).toBeInTheDocument()
    expect(screen.getByRole('heading', { name: /résumé des transactions/i })).toBeInTheDocument()
  })

  it('shows error and allows retry when an endpoint fails', async () => {
    // Make one endpoint fail
    server.use(
      http.get(`${API_BASE}/balance-summary`, () => HttpResponse.json({ detail: 'Backend HS' }, { status: 500 }))
    )
    render(<App />)

    const alert = await screen.findByRole('alert')
    expect(alert).toBeInTheDocument()
    expect(screen.getByText(/erreur de chargement des données/i)).toBeInTheDocument()

    // Retry button should exist
    const retry = screen.getByRole('button', { name: /réessayer/i })
    expect(retry).toBeInTheDocument()

    // Switch to success for retry and click
    server.use(
      http.get(`${API_BASE}/balance-summary`, () => HttpResponse.json({
        date: '2026-02-02',
        total_balance: 1000,
        accounts: [],
      }))
    )
    retry.click()

    await waitFor(() => {
      expect(screen.queryByRole('alert')).not.toBeInTheDocument()
    })
  })
})
