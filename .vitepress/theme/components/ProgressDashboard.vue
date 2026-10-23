<script setup lang="ts">
import { computed, onMounted, ref } from 'vue'
import { useData, withBase } from 'vitepress'
import { exams } from '../../data/exams'
import {
  cardProgress, checklistProgress, clearProgress, exportProgress, importProgress, isDone,
  lastPage, lastVisited, quizResult, type LastPage, type QuizResult,
} from '../progress'

interface Page { text: string; link: string; done: boolean; visited: number | null; quiz: QuizResult | null }
interface Subject {
  slug: string; title: string; exam: string; pages: Page[]
  checklist: { done: number; total: number } | null
  cards: { known: number; total: number } | null
}

const { theme } = useData()
const mounted = ref(false)
const subjects = ref<Subject[]>([])
const last = ref<LastPage | null>(null)
const message = ref('')

/** Leaf links under a sidebar group, in sidebar order. */
function leaves(items: any[]): { text: string; link: string }[] {
  return items.flatMap(i => (i.items ? leaves(i.items) : i.link ? [{ text: i.text, link: i.link }] : []))
}

function load() {
  const groups = (theme.value.sidebar as any[]).filter(g => g.text !== 'Plan')
  subjects.value = groups.map(g => {
    // Sidebar links match the keys progress.ts saves under ("/slug/" or "/slug/page").
    const pages = leaves(g.items).map(p => ({ ...p, done: isDone(p.link), visited: lastVisited(p.link), quiz: quizResult(p.link) }))
    const slug = pages[0].link.split('/')[1]
    const first = exams.filter(e => e.slug === slug).map(e => e.date).sort()[0]
    return {
      slug, title: g.text, pages,
      exam: first ? new Date(first + 'T00:00').toLocaleDateString('en-AU', { weekday: 'short', day: 'numeric', month: 'short' }) : '',
      checklist: checklistProgress(slug),
      cards: cardProgress(slug),
    }
  })
  last.value = lastPage()
}
onMounted(() => { mounted.value = true; load() })

const overall = computed(() => {
  const all = subjects.value.flatMap(s => s.pages)
  return { done: all.filter(p => p.done).length, total: all.length }
})
const doneCount = (s: Subject) => s.pages.filter(p => p.done).length
const quizzes = (s: Subject) => s.pages.filter(p => p.link.includes('/quiz'))
const quizSummary = (s: Subject) => {
  const r = quizzes(s).map(p => p.quiz).filter(Boolean) as QuizResult[]
  const checked = r.reduce((n, q) => n + q.checked, 0)
  const correct = r.reduce((n, q) => n + q.correct, 0)
  return checked ? `${correct}/${checked} correct (${Math.round((correct / checked) * 100)}%)` : 'none checked yet'
}
const pct = (a: number, b: number) => (b ? Math.round((a / b) * 100) : 0)
const ago = (ts: number | null) => {
  if (!ts) return ''
  const d = Math.floor((Date.now() - ts) / 86400000)
  return d === 0 ? 'today' : d === 1 ? 'yesterday' : `${d} days ago`
}

function download() {
  const blob = new Blob([exportProgress()], { type: 'application/json' })
  const a = document.createElement('a')
  a.href = URL.createObjectURL(blob)
  a.download = `exam-hub-progress-${new Date().toISOString().slice(0, 10)}.json`
  a.click()
  URL.revokeObjectURL(a.href)
  message.value = 'Backup saved. Open this page on another device and use “Restore from backup”.'
}
async function restore(e: Event) {
  const file = (e.target as HTMLInputElement).files?.[0]
  if (!file) return
  try {
    const n = importProgress(await file.text())
    load()
    message.value = `Restored ${n} saved items.`
  } catch {
    message.value = 'That file is not a progress backup from this site.'
  }
  ;(e.target as HTMLInputElement).value = ''
}
const confirming = ref(false)
function clearAll() {
  if (!confirming.value) { confirming.value = true; return }
  clearProgress(); load(); confirming.value = false
  message.value = 'All progress cleared.'
}
</script>

<template>
  <ClientOnly>
    <div v-if="mounted" class="pd">
      <div class="continue">
        <template v-if="last">
          <span class="lbl">Continue where you left off</span>
          <a :href="withBase(last.path)" class="big">{{ last.title || last.path }}</a>
          <span class="muted">{{ ago(last.ts) }}</span>
        </template>
        <span v-else class="muted">Nothing yet. Open any page and it will show up here.</span>
      </div>

      <p class="overall">
        <strong>{{ overall.done }} / {{ overall.total }}</strong> pages marked done
        <span class="bar"><span class="fill" :style="{ width: pct(overall.done, overall.total) + '%' }" /></span>
      </p>

      <details v-for="s in subjects" :key="s.slug" class="subj">
        <summary>
          <span class="name">{{ s.title }}</span>
          <span class="muted">exam {{ s.exam }}</span>
          <span class="bar"><span class="fill" :style="{ width: pct(doneCount(s), s.pages.length) + '%' }" /></span>
          <span class="muted">{{ doneCount(s) }}/{{ s.pages.length }}</span>
        </summary>
        <ul class="stats">
          <li>
            <a :href="withBase(`/${s.slug}/checklist`)">Checklist</a>:
            {{ s.checklist ? `${s.checklist.done}/${s.checklist.total} ticked` : 'not started' }}
          </li>
          <li>
            <a :href="withBase(`/${s.slug}/flashcards`)">Flashcards</a>:
            {{ s.cards ? `${s.cards.known}/${s.cards.total} known` : 'not started' }}
          </li>
          <li>Quizzes: {{ quizSummary(s) }}</li>
        </ul>
        <table>
          <thead><tr><th>Page</th><th>Status</th></tr></thead>
          <tbody>
            <tr v-for="p in s.pages" :key="p.link" :class="{ done: p.done }">
              <td><a :href="withBase(p.link)">{{ p.text }}</a></td>
              <td>
                <span v-if="p.done" class="ok">✓ done</span>
                <span v-else-if="p.visited" class="muted">opened {{ ago(p.visited) }}</span>
                <span v-else class="muted">not opened</span>
                <span v-if="p.quiz" class="score"> · {{ p.quiz.correct }}/{{ p.quiz.checked }} correct<template v-if="p.quiz.checked < p.quiz.total"> ({{ p.quiz.total - p.quiz.checked }} left)</template></span>
              </td>
            </tr>
          </tbody>
        </table>
      </details>

      <h2>Backup and other devices</h2>
      <p class="muted">
        Progress is saved in this browser only. To carry it to another device or browser, save a backup here and restore it there.
      </p>
      <div class="actions">
        <button type="button" @click="download">Save backup</button>
        <label class="file">Restore from backup<input type="file" accept="application/json,.json" @change="restore" /></label>
        <button type="button" class="danger" @click="clearAll">{{ confirming ? 'Click again to clear everything' : 'Clear all progress' }}</button>
      </div>
      <p v-if="message" class="msg" role="status">{{ message }}</p>
    </div>
  </ClientOnly>
</template>

<style scoped>
.continue { display: flex; flex-wrap: wrap; align-items: baseline; gap: 4px 12px; padding: 14px 18px; border: 1px solid var(--vp-c-brand-1); border-radius: 8px; background: var(--vp-c-bg-soft); }
.lbl { width: 100%; font-size: 12px; text-transform: uppercase; letter-spacing: .05em; color: var(--vp-c-text-2); }
.big { font-size: 18px; font-weight: 600; }
.muted { color: var(--vp-c-text-2); font-size: 13px; }
.overall { display: flex; flex-wrap: wrap; align-items: center; gap: 10px; }
.bar { flex: 1; min-width: 60px; height: 8px; background: var(--vp-c-divider); border-radius: 4px; overflow: hidden; display: inline-block; }
.fill { display: block; height: 100%; background: var(--vp-c-brand-1); }
.subj { border: 1px solid var(--vp-c-divider); border-radius: 8px; padding: 10px 14px; margin: 10px 0; }
.subj summary { display: flex; flex-wrap: wrap; align-items: center; gap: 6px 12px; cursor: pointer; }
.subj summary .name { font-weight: 600; }
.subj summary .bar { max-width: 200px; }
.stats { margin: 10px 0; padding-left: 18px; font-size: 14px; }
.vp-doc .subj table { display: table; width: 100%; font-size: 14px; margin: 8px 0 4px; }
.vp-doc .subj td, .vp-doc .subj th { padding: 6px 10px; }
tr.done td:first-child a { color: var(--vp-c-text-2); }
.ok { color: var(--vp-c-green-1); font-weight: 600; }
.score { color: var(--vp-c-text-2); font-size: 13px; }
.actions { display: flex; flex-wrap: wrap; gap: 10px; }
.actions button, .file { border: 1px solid var(--vp-c-divider); border-radius: 6px; padding: 5px 14px; background: var(--vp-c-bg-soft); color: var(--vp-c-text-1); cursor: pointer; font-size: 14px; }
.file input { position: absolute; opacity: 0; width: 1px; height: 1px; }
.file { position: relative; }
.file:focus-within { outline: 2px solid var(--vp-c-brand-1); }
.danger { color: var(--vp-c-red-1) !important; }
.msg { font-size: 14px; color: var(--vp-c-text-1); }
</style>
