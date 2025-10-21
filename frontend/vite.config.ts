import { defineConfig } from 'vite'
import http from "http";
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig((configEnv) => { return {
  base: '/ui/',
  build: {
      sourcemap: configEnv.mode === 'development',
  },
  plugins: [react()],
  server: {
      proxy: {
          '/api': {
              target: 'http://localhost:8000',
              secure: false,
              agent: new http.Agent()
          }
      }
  }
};})
