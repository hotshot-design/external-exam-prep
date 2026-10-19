import { exams, type Exam } from './exams'

const localDate = (iso: string, h = 0, m = 0) => {
  const [y, mo, d] = iso.split('-').map(Number)
  return new Date(y, mo - 1, d, h, m)
}

export const isoOf = (d: Date) =>
  `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, '0')}-${String(d.getDate()).padStart(2, '0')}`

/**
 * Approximate end of a session. The QCAA timetable gives AM/PM only, not clock times,
 * so an exam counts as finished after 1 pm (AM) or 6 pm (PM) on its date.
 */
export const examEnd = (e: Exam) => localDate(e.date, e.session === 'AM' ? 13 : 18)

export const isFinished = (e: Exam, now: Date) => now.getTime() > examEnd(e).getTime()

export const daysUntil = (iso: string, now: Date) => {
  const today = new Date(now.getFullYear(), now.getMonth(), now.getDate()).getTime()
  return Math.round((localDate(iso).getTime() - today) / 86400000)
}

export const lastExamDate = () => exams.map(e => e.date).sort().slice(-1)[0]

export interface Focus { subject: string; slug: string; note: string; kind: 'exam' | 'main' | 'secondary' }

/** What to do on a given ISO date: any exams that day, then the next two distinct subjects. */
export function focusFor(date: string): Focus[] {
  const out: Focus[] = []
  const todays = exams.filter(e => e.date === date)
  todays.forEach(e => out.push({
    subject: e.subject, slug: e.slug, kind: 'exam',
    note: e.session === 'AM' ? 'Exam this morning: light review only' : 'Exam this afternoon: light review in the morning',
  }))
  const todaySlugs = new Set(todays.map(e => e.slug))
  const seen = new Set<string>()
  const upcoming = exams
    .filter(e => e.date > date && !todaySlugs.has(e.slug))
    .filter(e => (seen.has(e.slug) ? false : (seen.add(e.slug), true)))
  if (upcoming[0]) out.push({ subject: upcoming[0].subject.replace(/ – Paper \d/, ''), slug: upcoming[0].slug, kind: 'main', note: 'Main study block (timed past questions + weak topics)' })
  if (upcoming[1]) out.push({ subject: upcoming[1].subject.replace(/ – Paper \d/, ''), slug: upcoming[1].slug, kind: 'secondary', note: 'Lighter block (flashcards + checklist)' })
  return out
}

/** Stable key for saved progress: survives reordering or inserting items. */
export function hashText(s: string): string {
  let h = 5381
  for (let i = 0; i < s.length; i++) h = ((h << 5) + h + s.charCodeAt(i)) | 0
  return (h >>> 0).toString(36)
}
