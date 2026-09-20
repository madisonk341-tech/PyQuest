// Copies the Pyodide WASM runtime out of node_modules into public/pyodide
// so it's served as a static asset (no CDN dependency, works offline).
import { copyFileSync, existsSync, mkdirSync } from 'node:fs'
import { dirname, join } from 'node:path'
import { fileURLToPath } from 'node:url'

const __dirname = dirname(fileURLToPath(import.meta.url))
const src = join(__dirname, '..', 'node_modules', 'pyodide')
const dest = join(__dirname, '..', 'public', 'pyodide')

const files = ['pyodide.asm.wasm', 'pyodide.asm.mjs', 'pyodide.mjs', 'python_stdlib.zip', 'pyodide-lock.json']

if (!existsSync(src)) {
  console.warn('pyodide package not found in node_modules; skipping asset copy.')
  process.exit(0)
}

mkdirSync(dest, { recursive: true })
for (const f of files) {
  const from = join(src, f)
  if (existsSync(from)) {
    copyFileSync(from, join(dest, f))
  }
}
console.log('Pyodide runtime assets copied to public/pyodide')
