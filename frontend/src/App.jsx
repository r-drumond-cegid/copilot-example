import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import { ThemeProvider, CssBaseline } from '@mui/material'
import Dashboard from './pages/Dashboard'
import Header from './components/layout/Header'
import cegidTheme from './theme/cegidTheme'
import './App.css'

function App() {
  return (
    <ThemeProvider theme={cegidTheme}>
      <CssBaseline />
      <Router>
        <div className="app">
          <Header />
          <main className="main-content" style={{ padding: 0, margin: 0 }}>
            <Routes>
              <Route path="/" element={<Dashboard />} />
            </Routes>
          </main>
        </div>
      </Router>
    </ThemeProvider>
  )
}

export default App
