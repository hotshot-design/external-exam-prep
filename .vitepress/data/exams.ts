export interface Exam {
  id: string
  subject: string
  slug: string
  date: string // ISO local date
  session: 'AM' | 'PM'
  duration: string
  perusal: string
}

// Source: QCAA external assessment timetable 2026 (pp. 3-4)
export const exams: Exam[] = [
  { id: 'english', subject: 'English (Othello)', slug: 'english', date: '2026-10-27', session: 'AM', duration: '2h', perusal: '15m' },
  { id: 'spanish', subject: 'Spanish', slug: 'spanish', date: '2026-10-28', session: 'PM', duration: '2h', perusal: '5m' },
  { id: 'business', subject: 'Business', slug: 'business', date: '2026-11-03', session: 'PM', duration: '2h', perusal: '15m' },
  { id: 'film', subject: 'Film, TV & New Media', slug: 'film', date: '2026-11-04', session: 'AM', duration: '2h', perusal: '20m' },
  { id: 'maths1', subject: 'General Maths – Paper 1', slug: 'maths', date: '2026-11-05', session: 'PM', duration: '90m', perusal: '5m' },
  { id: 'maths2', subject: 'General Maths – Paper 2', slug: 'maths', date: '2026-11-06', session: 'AM', duration: '90m', perusal: '5m' },
  { id: 'digital', subject: 'Digital Solutions', slug: 'digital-solutions', date: '2026-11-10', session: 'AM', duration: '2h', perusal: '5m' },
]
