import { useEffect, useState, type ReactNode } from 'react'
import { api, ApiError } from '../api/client'
import BottomNav from '../components/BottomNav'
import ChoiceList from '../components/ChoiceList'
import TopBar from '../components/TopBar'
import type { AttemptPayload, AttemptResult, ModuleSummary } from '../types'

export default function Practice() {
  const [modules, setModules] = useState<ModuleSummary[]>([])
  const [selected, setSelected] = useState<string[]>([])
  const [count, setCount] = useState(10)
  const [attempt, setAttempt] = useState<AttemptPayload | null>(null)
  const [answers, setAnswers] = useState<Record<string, number>>({})
  const [result, setResult] = useState<AttemptResult | null>(null)
  const [busy, setBusy] = useState(false)
  const [error, setError] = useState('')

  useEffect(() => {
    api.get<{ modules: ModuleSummary[] }>('/modules').then((r) => setModules(r.modules))
  }, [])

  function toggle(id: string) {
    setSelected((s) => (s.includes(id) ? s.filter((x) => x !== id) : [...s, id]))
  }

  async function startCustom() {
    if (!selected.length) return
    await start(() => api.get<AttemptPayload>(`/practice/quiz?modules=${selected.join(',')}&count=${count}`))
  }

  async function startExam(id: 'exam1' | 'exam2') {
    await start(() => api.get<AttemptPayload>(`/practice/exam/${id}?count=20`))
  }

  async function startWeak() {
    await start(() => api.get<AttemptPayload>('/practice/weak?count=10'))
  }

  async function start(fetcher: () => Promise<AttemptPayload>) {
    setError('')
    setBusy(true)
    try {
      const payload = await fetcher()
      setAttempt(payload)
      setAnswers({})
      setResult(null)
    } catch (e) {
      setError(e instanceof ApiError ? e.message : 'Could not start that quiz.')
    } finally {
      setBusy(false)
    }
  }

  async function submit() {
    if (!attempt) return
    setBusy(true)
    try {
      const r = await api.post<AttemptResult>(`/practice/attempts/${attempt.attemptId}/submit`, { answers })
      setResult(r)
    } catch (e) {
      setError(e instanceof ApiError ? e.message : 'Could not submit.')
    } finally {
      setBusy(false)
    }
  }

  function reset() {
    setAttempt(null)
    setAnswers({})
    setResult(null)
    setError('')
  }

  const contentModules = modules.filter((m) => m.hasContent)

  return (
    <div className="min-h-screen bg-[#f7f7f7] pb-24">
      <TopBar title="Practice" />

      <div className="max-w-md mx-auto px-4 pt-4">
        {error && (
          <div className="bg-[#fff1f1] border-2 border-[#ff4b4b] text-[#b91c1c] rounded-xl p-3 mb-4 text-sm font-semibold">
            {error}
          </div>
        )}

        {!attempt && (
          <>
            <Section title="Full Practice Exams">
              <div className="flex gap-3">
                <button onClick={() => startExam('exam1')} disabled={busy} className="pq-btn pq-btn-blue flex-1 py-3 text-xs">
                  Exam 1
                </button>
                <button onClick={() => startExam('exam2')} disabled={busy} className="pq-btn pq-btn-blue flex-1 py-3 text-xs">
                  Exam 2
                </button>
              </div>
            </Section>

            <Section title="Struggling Topics">
              <p className="text-xs text-gray-500 mb-2">
                A quiz built from questions like the ones you've missed in Learning.
              </p>
              <button onClick={startWeak} disabled={busy} className="pq-btn pq-btn-outline w-full py-3 text-xs">
                🎯 Practice My Weak Areas
              </button>
            </Section>

            <Section title="Custom Quiz">
              <p className="text-xs text-gray-500 mb-2">Pick one or more modules to mix questions from.</p>
              <div className="flex flex-col gap-2 mb-3">
                {contentModules.map((m) => (
                  <label
                    key={m.id}
                    className={`flex items-center gap-2 px-3 py-2 rounded-xl border-2 text-sm font-semibold cursor-pointer ${
                      selected.includes(m.id) ? 'border-[#1cb0f6] bg-[#ddf4ff]' : 'border-gray-200 bg-white'
                    }`}
                  >
                    <input
                      type="checkbox"
                      checked={selected.includes(m.id)}
                      onChange={() => toggle(m.id)}
                      className="accent-[#1cb0f6]"
                    />
                    <span>{m.icon}</span>
                    {m.title}
                  </label>
                ))}
                {!contentModules.length && <p className="text-xs text-gray-400">Loading modules…</p>}
              </div>
              <label className="text-xs font-bold text-gray-500 uppercase flex items-center gap-2 mb-3">
                Questions:
                <select
                  value={count}
                  onChange={(e) => setCount(Number(e.target.value))}
                  className="border-2 border-gray-200 rounded-lg px-2 py-1 font-semibold text-gray-700"
                >
                  {[5, 10, 15, 20].map((n) => (
                    <option key={n} value={n}>
                      {n}
                    </option>
                  ))}
                </select>
              </label>
              <button
                onClick={startCustom}
                disabled={!selected.length || busy}
                className="pq-btn pq-btn-green w-full py-3 text-sm"
              >
                Start Quiz
              </button>
            </Section>
          </>
        )}

        {attempt && !result && (
          <div>
            <h2 className="text-xl font-black text-gray-800 mb-4">
              {attempt.kind === 'exam1' ? 'Exam 1' : attempt.kind === 'exam2' ? 'Exam 2' : attempt.kind === 'weak' ? 'Weak Areas Quiz' : 'Practice Quiz'}
            </h2>
            <div className="flex flex-col gap-6">
              {attempt.questions.map((q, i) => (
                <div key={q.id}>
                  <p className="font-bold text-gray-800 mb-2">
                    {i + 1}. {q.question}
                  </p>
                  <ChoiceList
                    choices={q.choices}
                    selected={answers[q.id] ?? null}
                    onSelect={(idx) => setAnswers({ ...answers, [q.id]: idx })}
                  />
                </div>
              ))}
            </div>
            <div className="flex gap-2 mt-6">
              <button onClick={reset} className="pq-btn pq-btn-outline flex-1 py-3 text-sm">
                Cancel
              </button>
              <button
                onClick={submit}
                disabled={busy || Object.keys(answers).length !== attempt.questions.length}
                className="pq-btn pq-btn-green flex-1 py-3 text-sm"
              >
                {busy ? 'Grading…' : 'Submit'}
              </button>
            </div>
          </div>
        )}

        {result && (
          <div className="text-center">
            <span className="text-6xl">{result.correct / result.total >= 0.7 ? '🎉' : '💪'}</span>
            <h2 className="text-2xl font-black text-gray-800 mt-2">
              {result.correct} / {result.total} correct ({result.score}%)
            </h2>
            <div className="text-left mt-6 flex flex-col gap-3">
              {result.results.map((r) => (
                <div key={r.id} className={`rounded-xl border-2 p-3 ${r.correct ? 'border-[#58cc02] bg-[#f2ffe6]' : 'border-[#ff4b4b] bg-[#fff1f1]'}`}>
                  <p className="font-bold text-sm text-gray-700">{r.question}</p>
                  {!r.correct && r.choices && (
                    <p className="text-xs font-bold text-[#58cc02] mt-1">Correct answer: {r.choices[r.correctAnswer]}</p>
                  )}
                  <p className="text-xs text-gray-500 mt-1">{r.explanation}</p>
                </div>
              ))}
            </div>
            <button onClick={reset} className="pq-btn pq-btn-green w-full py-3 text-sm mt-6">
              Done
            </button>
          </div>
        )}
      </div>

      <BottomNav />
    </div>
  )
}

function Section({ title, children }: { title: string; children: ReactNode }) {
  return (
    <div className="bg-white rounded-2xl border border-gray-200 p-4 mb-4">
      <h3 className="font-black text-gray-800 mb-2">{title}</h3>
      {children}
    </div>
  )
}
