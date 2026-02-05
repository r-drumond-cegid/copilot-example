// Global test setup for Vitest + RTL + MSW
import '@testing-library/jest-dom'
import { afterAll, afterEach, beforeAll, vi } from 'vitest'
import { server } from './mocks/server'

// Start MSW
beforeAll(() => server.listen({ onUnhandledRequest: 'bypass' }))
afterEach(() => server.resetHandlers())
afterAll(() => server.close())

// Prevent hanging intervals/timeouts from app code (e.g., Dashboard cut-off updater)
if (!global.setTimeout || !global.clearTimeout) {
  // jsdom provides these, guard just in case
}
// Stub setInterval/clearInterval to no-op to avoid open handles
if (!global.__INTERVAL_STUBBED__) {
  const noop = () => {}
  vi.stubGlobal('setInterval', noop)
  vi.stubGlobal('clearInterval', noop)
  global.__INTERVAL_STUBBED__ = true
}

// Stub ResizeObserver for MUI/layout code
class ResizeObserverStub {
  observe() {}
  unobserve() {}
  disconnect() {}
}
if (!global.ResizeObserver) {
  global.ResizeObserver = ResizeObserverStub
}

// Stub matchMedia for MUI useMediaQuery
if (!window.matchMedia) {
  window.matchMedia = () => ({
    matches: false,
    addListener: () => {},
    removeListener: () => {},
    addEventListener: () => {},
    removeEventListener: () => {},
    dispatchEvent: () => false,
    media: '',
  })
}

// Mock heavy Plotly component to a lightweight stub
vi.mock('react-plotly.js', () => {
  return {
    default: (props) => {
      return {
        $$typeof: Symbol.for('react.element'),
        type: 'div',
        key: null,
        ref: null,
        props: { 'data-testid': 'plotly-stub', ...props },
        _owner: null,
      }
    },
  }
})

// Mock MUI icons to avoid loading many files
vi.mock('@mui/icons-material', () => {
  const Stub = (props) => ({
    $$typeof: Symbol.for('react.element'),
    type: 'span',
    key: null,
    ref: null,
    props: { 'data-testid': 'mui-icon-stub', ...props },
    _owner: null,
  })
  return new Proxy({}, {
    get() { return Stub }
  })
})
