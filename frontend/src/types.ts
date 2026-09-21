export interface User {
  id: number
  username: string
  displayName: string
  avatar: string
}

export interface ModuleSummary {
  id: string
  title: string
  week: number
  icon: string
  exam: 'exam1' | 'exam2' | null
  hasContent: boolean
  percentComplete: number
  quizPassed: boolean
}

export interface Example {
  code: string
  output: string
  note: string
}

export interface PracticeQuestion {
  id: string
  question: string
  choices: string[]
  answer: number
  explanation: string
}

export interface LessonComponent {
  id: string
  title: string
  explanation: string
  examples: Example[]
  practice: PracticeQuestion[]
  completed: boolean
}

export interface QuizQuestionPublic {
  id: string
  question: string
  choices: string[]
}

export interface ModuleDetail {
  id: string
  title: string
  intro: string
  components: LessonComponent[]
  quiz: QuizQuestionPublic[]
  quizPassed: boolean
  quizBest: number
  percentComplete: number
}

export interface AttemptQuestion {
  id: string
  question: string
  choices: string[]
}

export interface AttemptPayload {
  attemptId: number
  kind: string
  questions: AttemptQuestion[]
}

export interface AttemptResultItem {
  id: string
  question?: string
  choices?: string[]
  chosen?: number | null
  correct: boolean
  correctAnswer: number
  explanation: string
}

export interface AttemptResult {
  score: number
  correct: number
  total: number
  results: AttemptResultItem[]
}

export interface ProgressSummary {
  modules: { id: string; title: string; percentComplete: number; quizPassed: boolean }[]
  weakModules: { moduleId: string; timesMissed: number }[]
  overallPercent: number
}

export interface SandboxPrompt {
  id: string
  module_id: string
  title: string
  prompt: string
  starter_code: string
  expected_output: string | null
  mode: 'match_output' | 'freeform'
  series?: string
  part?: number
  series_total?: number
}
