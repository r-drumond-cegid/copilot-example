import { render, screen } from '@testing-library/react'
import App from './App.jsx'

describe('App', () => {
  it('renders the dashboard title', async () => {
    render(<App />)
    const heading = await screen.findByRole('heading', { name: /dashboard financier/i })
    expect(heading).toBeInTheDocument()
  })
})
