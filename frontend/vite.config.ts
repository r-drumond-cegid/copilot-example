import { defineConfig, loadEnv } from 'vite'
import react from '@vitejs/plugin-react'
import path from 'node:path'

// https://vite.dev/config/
export default defineConfig(({ mode }) => {
  const env = loadEnv(mode, process.cwd(), '')
  const base = env.VITE_BASE || '/'
  return {
    base,
    plugins: [react()],
    resolve: {
      alias: {
        '@cegid/cds-react': path.resolve(__dirname, 'src/cds-react-shim.js'),
        '@cegid/forms': path.resolve(__dirname, 'src/forms-shim.js'),
      },
    },
  }
})
