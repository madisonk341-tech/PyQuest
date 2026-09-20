import { useEffect, useMemo, useState } from 'react'
import { api } from '../api/client'
import BottomNav from '../components/BottomNav'
import TopBar from '../components/TopBar'
import { runPython } from '../lib/pyodideRunner'
import type { ModuleSummary, SandboxPrompt } from '../types'

export default function Sandbox() {
  const [prompts, setPrompts] = useState<SandboxPrompt[]>([])
  const [modules, setModules] = useState<ModuleSummary[]>([])
  const [search, setSearch] = useState('')
  const [moduleFilter, setModuleFilter] = useState('')
  const [active, setActive] = useState<SandboxPrompt | null>(null)

  const [code, setCode] = useState('print("Hello, PyQuest!")')
  const [output, setOutput] = useState('')
  const [runError, setRunError] = useState<string | null>(null)
  const [status, setStatus] = useState<'idle' | 'loading-runtime' | 'running'>('idle')
  const [matchResult, setMatchResult] = useState<'pass' | 'fail' | null>(null)

  useEffect(() => {
    api.get<{ modules: ModuleSummary[] }>('/modules').then((r) => setModules(r.modules.filter((m) => m.hasContent)))
  }, [])

  useEffect(() => {
    const params = new URLSearchParams()
    if (search) params.set('search', search)
    if (moduleFilter) params.set('module', moduleFilter)
    api.get<{ prompts: SandboxPrompt[] }>(`/sandbox/prompts?${params}`).then((r) => setPrompts(r.prompts))
  }, [search, moduleFilter])

  const moduleTitle = useMemo(() => {
    const map: Record<string, string> = {}
    for (const m of modules) map[m.id] = `${m.icon} ${m.title}`
    return map
  }, [modules])

  function selectPrompt(p: SandboxPrompt) {
    setActive(p)
    setCode(p.starter_code || '')
    setOutput('')
    setRunError(null)
    setMatchResult(null)
  }

  function clearPrompt() {
    setActive(null)
    setOutput('')
    setRunError(null)
    setMatchResult(null)
  }

  async function run() {
    setStatus((s) => (s === 'idle' ? 'loading-runtime' : 'running'))
    setOutput('')
    setRunError(null)
    setMatchResult(null)
    const result = await runPython(code)
    setStatus('idle')
    setOutput(result.output)
    setRunError(result.error)
    if (active?.mode === 'match_output' && active.expected_output != null) {
      setMatchResult(!result.error && result.output.trim() === active.expected_output.trim() ? 'pass' : 'fail')
    }
  }

  return (
    <div className="min-h-screen bg-[#08090a] pb-24">
      <TopBar title="Sandbox" />

      <div className="max-w-2xl mx-auto px-4 pt-4 flex flex-col gap-4">
        <div className="bg-[#101113] rounded-2xl border border-[#2a2c2f] p-4">
          <h3 className="font-black text-[#eafff0] mb-3">Coding Prompts</h3>
          <input
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            placeholder="Search prompts..."
            className="w-full border-2 border-[#2a2c2f] bg-[#0c0d0f] text-[#d9f2d9] rounded-xl px-3 py-2 text-sm font-medium mb-2 focus:outline-none focus:border-[#39ff14]"
          />
          <div className="flex gap-2 overflow-x-auto pb-1 mb-3">
            <FilterChip active={moduleFilter === ''} onClick={() => setModuleFilter('')} label="All" />
            {modules.map((m) => (
              <FilterChip
                key={m.id}
                active={moduleFilter === m.id}
                onClick={() => setModuleFilter(m.id)}
                label={`${m.icon} ${m.title.split(',')[0]}`}
              />
            ))}
          </div>
          <div className="flex flex-col gap-2 max-h-56 overflow-y-auto">
            {prompts.map((p) => (
              <button
                key={p.id}
                onClick={() => selectPrompt(p)}
                className={`text-left px-3 py-2 rounded-xl border-2 text-sm font-semibold ${
                  active?.id === p.id ? 'border-[#39ff14] bg-[#0f2408]' : 'border-[#2a2c2f] bg-[#0c0d0f] hover:border-[#500000]'
                }`}
              >
                <span className="block text-[#eafff0]">{p.title}</span>
                <span className="block text-xs text-[#7d8a80] font-normal">{moduleTitle[p.module_id] || ''}</span>
              </button>
            ))}
            {!prompts.length && <p className="text-xs text-[#7d8a80] py-2">No prompts match your search.</p>}
          </div>
        </div>

        <div className="bg-[#101113] rounded-2xl border border-[#2a2c2f] p-4">
          {active ? (
            <div className="mb-3">
              <div className="flex items-start justify-between gap-2">
                <p className="font-bold text-[#eafff0]">{active.title}</p>
                <button onClick={clearPrompt} className="text-xs text-[#7d8a80] font-semibold shrink-0">
                  Clear X
                </button>
              </div>
              <p className="text-sm text-[#c9d9c9] mt-1">{active.prompt}</p>
              {active.mode === 'match_output' && (
                <p className="text-xs text-[#7d8a80] mt-1">
                  Write code so the output matches exactly, then hit Run.
                </p>
              )}
            </div>
          ) : (
            <p className="text-sm text-[#a0aca0] mb-3">
              Free sandbox -- write any Python and hit Run to see the output. Pick a prompt above for a guided
              exercise.
            </p>
          )}

          <textarea
            value={code}
            onChange={(e) => setCode(e.target.value)}
            spellCheck={false}
            className="w-full h-40 bg-[#0c0d0f] text-[#d9f2d9] border border-[#2a2c2f] rounded-xl p-3 font-mono text-sm resize-y focus:outline-none focus:border-[#39ff14]"
          />

          <button
            onClick={run}
            disabled={status !== 'idle'}
            className="pq-btn pq-btn-green w-full py-3 text-sm mt-3"
          >
            {status === 'loading-runtime' ? 'Starting Python...' : status === 'running' ? 'Running...' : '> Run'}
          </button>

          {(output || runError) && (
            <div className="mt-3 rounded-xl overflow-hidden border border-[#2a2c2f]">
              <div className="bg-[#0a0a0a] text-xs font-bold text-[#7d8a80] px-3 py-1.5">Output</div>
              <pre className="bg-[#050605] text-[#39ff14] text-sm p-3 overflow-x-auto whitespace-pre-wrap min-h-8">
                <code>{output || ' '}</code>
              </pre>
              {runError && (
                <pre className="bg-[#1a0e0e] text-[#ff8080] text-xs p-3 overflow-x-auto whitespace-pre-wrap border-t border-[#2a2c2f]">
                  {runError}
                </pre>
              )}
            </div>
          )}

          {matchResult && (
            <div
              className={`mt-3 rounded-xl p-3 text-sm font-bold text-center ${
                matchResult === 'pass' ? 'bg-[#0f2408] text-[#39ff14]' : 'bg-[#2a1010] text-[#ff8080]'
              }`}
            >
              {matchResult === 'pass' ? '✅ Output matches — nice work!' : '❌ Not quite — check your output above.'}
            </div>
          )}
        </div>
      </div>

      <BottomNav />
    </div>
  )
}

function FilterChip({ active, onClick, label }: { active: boolean; onClick: () => void; label: string }) {
  return (
    <button
      onClick={onClick}
      className={`shrink-0 px-3 py-1.5 rounded-full text-xs font-bold border-2 ${
        active ? 'bg-[#500000] border-[#500000] text-[#eafff0]' : 'bg-[#0c0d0f] border-[#2a2c2f] text-[#a0aca0]'
      }`}
    >
      {label}
    </button>
  )
}
