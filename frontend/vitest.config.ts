import { defineConfig } from 'vitest/config'
import react from '@vitejs/plugin-react'
import path from 'node:path'

export default defineConfig({
  plugins: [react()],
  resolve: {
    alias: {
      '@cegid/cds-react': path.resolve(__dirname, 'src/cds-react-shim.js'),
      '@cegid/forms': path.resolve(__dirname, 'src/forms-shim.js'),
    },
  },
  test: {
    environment: 'jsdom',
    setupFiles: 'src/tests/setup.js',
    globals: true,
    css: true,
    include: [
      'src/**/*.test.{js,jsx,ts,tsx}',
      'src/**/*.spec.{js,jsx,ts,tsx}',
    ],
    poolOptions: {
      threads: { singleThread: true },
    },
    coverage: { provider: 'v8' },
  },
})
