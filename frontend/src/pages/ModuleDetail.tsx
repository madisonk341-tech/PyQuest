import { useEffect, useMemo, useState } from 'react'
import { useNavigate, useParams } from 'react-router-dom'
import { api } from '../api/client'
import ChoiceList from '../components/ChoiceList'
import CodeBlock from '../components/CodeBlock'
import type { AttemptResult, LessonComponent, ModuleDetail as ModuleDetailT, PracticeQuestion } from '../types'

type Step =
  | { type: 'lesson'; component: LessonComponent }
  | { type: 'practice'; component: LessonComponent; question: PracticeQuestion }
  | { type: 'quiz' }

export default function ModuleDetailPage() {
  const { moduleId } = useParams<{ moduleId: string }>()
  const navigate = useNavigate()
  const [module, setModule] = useState<ModuleDetailT | null>(null)
  const [stepIndex, setStepIndex] = useState(0)
  const [error, setError] = useState('')

  // per-practice-question answer state, keyed by question id
  const [answered, setAnswered] = useState<Record<string, number>>({})
  // quiz answers (only used on the quiz step)
  const [quizAnswers, setQuizAnswers] = useState<Record<string, number>>({})
  const [quizResult, setQuizResult] = useState<AttemptResult | null>(null)
  const [quizSubmitting, setQuizSubmitting] = useState(false)

  useEffect(() => {
    if (!moduleId) return
    setModule(null)
    setStepIndex(0)
    setAnswered({})
    setQuizAnswers({})
    setQuizResult(null)
    setError('')
    api
      .get<ModuleDetailT>(`/modules/${moduleId}`)
      .then(setModule)
      .catch((e) => setError(e.message || 'This module is not available yet.'))
  }, [moduleId])

  const steps: Step[] = useMemo(() => {
    if (!module) return []
    const s: Step[] = []
    for (const c of module.components) {
      s.push({ type: 'lesson', component: c })
      for (const q of c.practice) s.push({ type: 'practice', component: c, question: q })
    }
    s.push({ type: 'quiz' })
    return s
  }, [module])

  if (error) {
    return (
      <div className="min-h-screen flex flex-col items-center justify-center gap-4 px-6 text-center">
        <span className="text-5xl">🚧</span>
        <p className="font-bold text-gray-600">{error}</p>
        <button onClick={() => navigate('/learning')} className="pq-btn pq-btn-blue px-6 py-2 text-sm">
          Back to Learning
        </button>
      </div>
    )
  }

  if (!module) {
    return <div className="min-h-screen flex items-center justify-center text-gray-400">Loading…</div>
  }

  const step = steps[stepIndex]
  const progressPct = Math.round(((stepIndex + 1) / steps.length) * 100)

  function goNext() {
    if (stepIndex < steps.length - 1) setStepIndex(stepIndex + 1)
    else navigate('/learning')
  }

  async function onFinishLesson(component: LessonComponent) {
    try {
      await api.post(`/modules/${moduleId}/components/${component.id}/complete`)
    } catch {
      /* non-fatal: still let the user continue */
    }
    goNext()
  }

  async function onAnswerPractice(question: PracticeQuestion, choiceIndex: number) {
    setAnswered((prev) => ({ ...prev, [question.id]: choiceIndex }))
  }

  async function onSubmitQuiz() {
    setQuizSubmitting(true)
    try {
      const result = await api.post<AttemptResult & { passed: boolean }>(`/modules/${moduleId}/quiz/submit`, {
        answers: quizAnswers,
      })
      setQuizResult(result)
    } catch (e) {
      setError(e instanceof Error ? e.message : 'Could not submit quiz.')
    } finally {
      setQuizSubmitting(false)
    }
  }

  return (
    <div className="min-h-screen bg-[#f7f7f7] pb-10">
      <header className="sticky top-0 z-20 bg-white border-b border-gray-200 px-4 py-3 flex items-center gap-3">
        <button onClick={() => navigate('/learning')} className="text-xl text-gray-400" aria-label="Close">
          ✕
        </button>
        <div className="flex-1 bg-gray-100 rounded-full h-3">
          <div className="h-3 rounded-full bg-[#58cc02] transition-all" style={{ width: `${progressPct}%` }} />
        </div>
      </header>

      <div className="max-w-md mx-auto px-5 pt-6">
        {step.type === 'lesson' && (
          <LessonStep key={step.component.id} component={step.component} onContinue={() => onFinishLesson(step.component)} />
        )}

        {step.type === 'practice' && (
          <PracticeStep
            key={step.question.id}
            moduleId={moduleId!}
            question={step.question}
            selected={answered[step.question.id] ?? null}
            onSelect={(i) => onAnswerPractice(step.question, i)}
            onContinue={goNext}
          />
        )}

        {step.type === 'quiz' && (
          <QuizStep
            module={module}
            answers={quizAnswers}
            setAnswers={setQuizAnswers}
            result={quizResult}
            submitting={quizSubmitting}
            onSubmit={onSubmitQuiz}
            onFinish={() => navigate('/learning')}
            onRetry={() => {
              setQuizAnswers({})
              setQuizResult(null)
            }}
          />
        )}
      </div>
    </div>
  )
}

function LessonStep({ component, onContinue }: { component: LessonComponent; onContinue: () => void }) {
  return (
    <div>
      <h2 className="text-2xl font-black text-gray-800 mb-3">{component.title}</h2>
      {component.explanation.split('\n\n').map((para, i) => (
        <p key={i} className="text-gray-600 leading-relaxed mb-3 whitespace-pre-line">
          {para}
        </p>
      ))}
      {component.examples.map((ex, i) => (
        <CodeBlock key={i} example={ex} />
      ))}
      <button onClick={onContinue} className="pq-btn pq-btn-green w-full py-3 text-sm mt-4">
        Continue
      </button>
    </div>
  )
}

function PracticeStep({
  moduleId,
  question,
  selected,
  onSelect,
  onContinue,
}: {
  moduleId: string
  question: PracticeQuestion
  selected: number | null
  onSelect: (i: number) => void
  onContinue: () => void
}) {
  const [revealed, setRevealed] = useState(false)
  const isCorrect = selected === question.answer

  async function check() {
    if (selected === null) return
    setRevealed(true)
    try {
      await api.post(`/modules/${moduleId}/practice-answer`, { correct: selected === question.answer })
    } catch {
      /* non-fatal: local feedback still works even if logging fails */
    }
  }

  return (
    <div>
      <p className="text-xs font-bold text-[#1cb0f6] uppercase tracking-wide mb-2">Quick check</p>
      <h2 className="text-xl font-black text-gray-800 mb-4">{question.question}</h2>
      <ChoiceList
        choices={question.choices}
        selected={selected}
        correctIndex={question.answer}
        revealed={revealed}
        onSelect={onSelect}
      />
      {revealed && (
        <p className={`mt-3 text-sm font-semibold ${isCorrect ? 'text-[#58cc02]' : 'text-[#ff4b4b]'}`}>
          {isCorrect ? 'Correct! ' : 'Not quite. '}
          {question.explanation}
        </p>
      )}
      {!revealed ? (
        <button
          onClick={check}
          disabled={selected === null}
          className="pq-btn pq-btn-green w-full py-3 text-sm mt-4"
        >
          Check
        </button>
      ) : (
        <button onClick={onContinue} className="pq-btn pq-btn-blue w-full py-3 text-sm mt-4">
          Continue
        </button>
      )}
    </div>
  )
}

function QuizStep({
  module,
  answers,
  setAnswers,
  result,
  submitting,
  onSubmit,
  onFinish,
  onRetry,
}: {
  module: ModuleDetailT
  answers: Record<string, number>
  setAnswers: (a: Record<string, number>) => void
  result: (AttemptResult & { passed?: boolean }) | null
  submitting: boolean
  onSubmit: () => void
  onFinish: () => void
  onRetry: () => void
}) {
  if (result) {
    const passed = result.correct / result.total >= 0.7
    return (
      <div className="text-center">
        <span className="text-6xl">{passed ? '🎉' : '💪'}</span>
        <h2 className="text-2xl font-black text-gray-800 mt-2">
          {result.correct} / {result.total} correct
        </h2>
        <p className={`font-bold mt-1 ${passed ? 'text-[#58cc02]' : 'text-[#ff9600]'}`}>
          {passed ? 'Module complete!' : 'Keep practicing — 70% needed to pass.'}
        </p>

        <div className="text-left mt-6 flex flex-col gap-3">
          {result.results.map((r, i) => (
            <div key={r.id} className={`rounded-xl border-2 p-3 ${r.correct ? 'border-[#58cc02] bg-[#f2ffe6]' : 'border-[#ff4b4b] bg-[#fff1f1]'}`}>
              <p className="font-bold text-sm text-gray-700">{module.quiz[i]?.question}</p>
              {!r.correct && module.quiz[i] && (
                <p className="text-xs font-bold text-[#58cc02] mt-1">
                  Correct answer: {module.quiz[i].choices[r.correctAnswer]}
                </p>
              )}
              <p className="text-xs text-gray-500 mt-1">{r.explanation}</p>
            </div>
          ))}
        </div>

        <div className="flex gap-2 mt-6">
          {!passed && (
            <button onClick={onRetry} className="pq-btn pq-btn-outline flex-1 py-3 text-sm">
              Try Again
            </button>
          )}
          <button onClick={onFinish} className="pq-btn pq-btn-green flex-1 py-3 text-sm">
            Done
          </button>
        </div>
      </div>
    )
  }

  const allAnswered = module.quiz.every((q) => answers[q.id] !== undefined)

  return (
    <div>
      <h2 className="text-2xl font-black text-gray-800 mb-1">Module Quiz</h2>
      <p className="text-gray-500 text-sm mb-4">Answer all questions, then submit. 70% or higher passes.</p>
      <div className="flex flex-col gap-6">
        {module.quiz.map((q, qi) => (
          <div key={q.id}>
            <p className="font-bold text-gray-800 mb-2">
              {qi + 1}. {q.question}
            </p>
            <ChoiceList
              choices={q.choices}
              selected={answers[q.id] ?? null}
              onSelect={(i) => setAnswers({ ...answers, [q.id]: i })}
            />
          </div>
        ))}
      </div>
      <button
        onClick={onSubmit}
        disabled={!allAnswered || submitting}
        className="pq-btn pq-btn-green w-full py-3 text-sm mt-6"
      >
        {submitting ? 'Grading…' : 'Submit Quiz'}
      </button>
    </div>
  )
}
