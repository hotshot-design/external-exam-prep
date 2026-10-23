import { ref } from 'vue'

/**
 * Study progress saved in this browser (localStorage).
 * Pages are keyed by their route without base or extension, e.g. "/english/notes" or "/maths/".
 */

/** Bumped on every write so components showing progress can re-read it. */
export const progressVersion = ref(0)

export function pageKey(path: string, base = '/'): string {
  let p = path.split(/[?#]/)[0]
  if (base !== '/' && p.startsWith(base)) p = '/' + p.slice(base.length)
  return p.replace(/\.html$/, '').replace(/\/index$/, '/') || '/'
}

function read<T>(key: string, fallback: T): T {
  try { return JSON.parse(localStorage.getItem(key) || 'null') ?? fallback } catch { return fallback }
}
function write(key: string, value: unknown) {
  try {
    if (value === null) localStorage.removeItem(key)
    else localStorage.setItem(key, JSON.stringify(value))
  } catch {}
  progressVersion.value++
}

// ---- Pages: visited and marked done ----

export interface LastPage { path: string; title: string; ts: number }

export function recordVisit(path: string, title: string) {
  write(`visited:${path}`, Date.now())
  if (path !== '/' && path !== '/progress') write('last-page', { path, title, ts: Date.now() } satisfies LastPage)
}
export const lastVisited = (path: string) => read<number | null>(`visited:${path}`, null)
export const lastPage = () => read<LastPage | null>('last-page', null)

export const isDone = (path: string) => read<number | null>(`done:${path}`, null) !== null
export const setDone = (path: string, v: boolean) => write(`done:${path}`, v ? Date.now() : null)

// ---- Quizzes: saved answers and marks per question ----

export interface QuizResult { correct: number; checked: number; total: number; ts: number }

export const quizAnswer = (path: string, q: string) => read<unknown>(`quiz:${path}:${q}`, null)
export const saveQuizAnswer = (path: string, q: string, a: unknown) => write(`quiz:${path}:${q}`, a)

/** Marks: question hash → answered correctly when checked. */
export const quizMarks = (path: string) => read<Record<string, boolean>>(`quiz-marks:${path}`, {})

export function markQuiz(path: string, q: string, correct: boolean | null, total: number) {
  const marks = quizMarks(path)
  if (correct === null) delete marks[q]
  else marks[q] = correct
  const vals = Object.values(marks)
  write(`quiz-marks:${path}`, marks)
  write(`quiz-result:${path}`, vals.length
    ? { correct: vals.filter(Boolean).length, checked: vals.length, total, ts: Date.now() } satisfies QuizResult
    : null)
}
/** Forget every saved answer and mark on a quiz page. */
export function clearQuiz(path: string) {
  const keys: string[] = []
  for (let i = 0; i < localStorage.length; i++) {
    const k = localStorage.key(i)
    if (k && (k.startsWith(`quiz:${path}:`) || k === `quiz-marks:${path}` || k === `quiz-result:${path}`)) keys.push(k)
  }
  keys.forEach(k => localStorage.removeItem(k))
  progressVersion.value++
}
export const quizResult = (path: string) => read<QuizResult | null>(`quiz-result:${path}`, null)

// ---- Checklists and flashcards (saved by ProgressChecklist and Flashcards) ----

export const checklistProgress = (id: string) => read<{ done: number; total: number } | null>(`progress-checklist:${id}`, null)
export const cardProgress = (id: string) => read<{ known: number; total: number } | null>(`progress-cards:${id}`, null)

// ---- Backup: move progress to another device ----

const PREFIXES = ['visited:', 'last-page', 'done:', 'quiz:', 'quiz-marks:', 'quiz-result:', 'checklist:', 'progress-checklist:', 'flashcards:', 'progress-cards:']
const ours = (k: string) => PREFIXES.some(p => k.startsWith(p))

export function exportProgress(): string {
  const data: Record<string, string> = {}
  for (let i = 0; i < localStorage.length; i++) {
    const k = localStorage.key(i)
    if (k && ours(k)) data[k] = localStorage.getItem(k)!
  }
  return JSON.stringify({ app: 'exam-hub-progress', version: 1, saved: new Date().toISOString(), data }, null, 1)
}

/** Returns the number of entries restored. Throws if the file isn't a progress backup. */
export function importProgress(text: string): number {
  const parsed = JSON.parse(text)
  if (parsed?.app !== 'exam-hub-progress' || typeof parsed.data !== 'object') throw new Error('Not a progress backup file')
  let n = 0
  for (const [k, v] of Object.entries(parsed.data)) {
    if (ours(k) && typeof v === 'string') { localStorage.setItem(k, v); n++ }
  }
  progressVersion.value++
  return n
}

export function clearProgress() {
  const keys: string[] = []
  for (let i = 0; i < localStorage.length; i++) {
    const k = localStorage.key(i)
    if (k && ours(k)) keys.push(k)
  }
  keys.forEach(k => localStorage.removeItem(k))
  progressVersion.value++
}
