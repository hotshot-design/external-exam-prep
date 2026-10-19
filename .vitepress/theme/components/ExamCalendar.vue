<script setup lang="ts">
import { computed } from 'vue'
import { withBase } from 'vitepress'
import { exams } from '../../data/exams'
import { isFinished, isoOf } from '../../data/examUtils'
import { useNow } from '../composables/useNow'

const now = useNow()
const dows = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

const months = computed(() => {
  const dates = exams.map(e => e.date).sort()
  const [fy, fm] = dates[0].split('-').map(Number)
  const [ly, lm] = dates[dates.length - 1].split('-').map(Number)
  const out: { label: string; cells: { iso: string; day: number }[] }[] = []
  for (let y = fy, m = fm; y < ly || (y === ly && m <= lm); m === 12 ? (y++, (m = 1)) : m++) {
    const first = new Date(y, m - 1, 1)
    const lead = (first.getDay() + 6) % 7
    const days = new Date(y, m, 0).getDate()
    const cells: { iso: string; day: number }[] = Array.from({ length: lead }, () => ({ iso: '', day: 0 }))
    for (let d = 1; d <= days; d++) cells.push({ iso: isoOf(new Date(y, m - 1, d)), day: d })
    out.push({ label: first.toLocaleDateString('en-AU', { month: 'long', year: 'numeric' }), cells })
  }
  return out
})

const byDate = computed(() => {
  const map: Record<string, (typeof exams[number] & { done: boolean })[]> = {}
  for (const e of exams) (map[e.date] ??= []).push({ ...e, done: now.value ? isFinished(e, now.value) : false })
  return map
})
const today = computed(() => (now.value ? isoOf(now.value) : ''))
const short = (s: string) => s.replace(' (Othello)', '').replace('General ', '').replace(', TV & New Media', '').replace(' – Paper ', ' P')
</script>

<template>
  <ClientOnly>
    <div class="cal">
      <div v-for="m in months" :key="m.label" class="month">
        <div class="mname">{{ m.label }}</div>
        <div class="grid">
          <div v-for="d in dows" :key="d" class="dow">{{ d }}</div>
          <div v-for="(c, i) in m.cells" :key="i" class="cell"
            :class="{ empty: !c.iso, today: c.iso === today, exam: byDate[c.iso] }">
            <template v-if="c.iso">
              <span class="num">{{ c.day }}</span>
              <a v-for="e in byDate[c.iso] ?? []" :key="e.id" class="chip" :class="{ done: e.done }"
                :href="withBase(`/${e.slug}/`)" :title="`${e.subject}: ${e.session}, ${e.duration} + ${e.perusal} perusal`">
                {{ short(e.subject) }} <small>{{ e.session }}</small>
              </a>
            </template>
          </div>
        </div>
      </div>
      <p class="note">AM/PM sessions from the QCAA 2026 timetable. Select an exam to open its subject. Today is outlined; finished exams are struck through.</p>
    </div>
  </ClientOnly>
</template>

<style scoped>
.cal { margin: 16px 0; display: grid; gap: 16px; }
.month { border: 1px solid var(--vp-c-divider); border-radius: 8px; padding: 12px; background: var(--vp-c-bg-soft); }
.mname { font-weight: 600; margin-bottom: 8px; }
.grid { display: grid; grid-template-columns: repeat(7, minmax(0, 1fr)); gap: 4px; }
.dow { font-size: 11px; text-transform: uppercase; color: var(--vp-c-text-2); text-align: center; }
.cell { min-height: 62px; border-radius: 6px; padding: 3px 4px; background: var(--vp-c-bg); font-size: 12px; display: flex; flex-direction: column; gap: 2px; }
.cell.empty { background: transparent; }
.cell.today { outline: 2px solid var(--vp-c-brand-1); }
.num { color: var(--vp-c-text-2); font-size: 11px; }
.chip { display: block; background: var(--vp-c-brand-soft); color: var(--vp-c-brand-1); border-radius: 4px; padding: 1px 4px; font-size: 11px; line-height: 1.3; font-weight: 600; text-decoration: none; overflow-wrap: anywhere; }
.chip small { font-weight: 400; opacity: .8; }
.chip.done { text-decoration: line-through; opacity: .5; }
.note { font-size: 12px; color: var(--vp-c-text-2); margin: 0; }
@media (max-width: 640px) { .cell { min-height: 48px; padding: 2px; } .chip { font-size: 8px; padding: 1px; overflow-wrap: normal; letter-spacing: -.2px; } .chip small { display: none; } }
</style>
