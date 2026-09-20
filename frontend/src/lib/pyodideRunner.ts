// Loads Pyodide (Python compiled to WebAssembly) from the self-hosted
// assets in /public/pyodide and runs code entirely client-side — no
// server-side code execution, so nothing here can affect the backend.
import type { PyodideInterface } from 'pyodide'

let pyodidePromise: Promise<PyodideInterface> | null = null

export function getPyodide(): Promise<PyodideInterface> {
  if (!pyodidePromise) {
    pyodidePromise = import('pyodide').then(({ loadPyodide }) =>
      loadPyodide({ indexURL: '/pyodide/' }),
    )
  }
  return pyodidePromise
}

export interface RunResult {
  output: string
  error: string | null
}

export async function runPython(code: string): Promise<RunResult> {
  const pyodide = await getPyodide()
  const lines: string[] = []
  pyodide.setStdout({ batched: (msg: string) => lines.push(msg) })
  pyodide.setStderr({ batched: (msg: string) => lines.push(msg) })

  try {
    await pyodide.runPythonAsync(code)
    return { output: lines.join('\n'), error: null }
  } catch (e) {
    const message = e instanceof Error ? e.message : String(e)
    // Pyodide errors include a full Python traceback; keep only the last
    // line (the actual exception) plus what was already printed.
    const short = message.split('\n').filter(Boolean).pop() || message
    return { output: lines.join('\n'), error: short }
  }
}
