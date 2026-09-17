import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// base relativa: el sitio funciona igual en Netlify, en subcarpetas o abierto local
export default defineConfig({
  plugins: [react()],
  base: './',
  build: { outDir: 'dist' }
})
