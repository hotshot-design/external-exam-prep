<script setup lang="ts">
import { computed } from 'vue'
import { withBase } from 'vitepress'
import { exams } from '../../data/exams'
import { focusFor, isoOf, isFinished, lastExamDate } from '../../data/examUtils'
import { useNow } from '../composables/useNow'

const now = useNow()

interface Day { date: string; label: string; today: boolean; exams: typeof exams; focus: ReturnType<typeof focusFor> }

const days = computed<Day[]>(() => {
  if (!now.value) return []
  const [ly, lm, ld] = lastExamDate().split('-').map(Number)
  const last = new Date(ly, lm - 1, ld)
  const start = new Date(now.value.getFullYear(), now.value.getMonth(), now.value.getDate())
  const todayIso = isoOf(start)
  const out: Day[] = []
  for (let d = new Date(start); d <= last; d.setDate(d.getDate() + 1)) {
    const date = isoOf(d)
    out.push({
      date,
      today: date === todayIso,
      label: d.toLocaleDateString('en-AU', { weekday: 'short', day: 'numeric', month: 'short' }),
      exams: exams.filter(e => e.date === date),
      focus: focusFor(date),
    })
  }
  return out
})

const allDone = computed(() => !!now.value && exams.every(e => isFinished(e, now.value!)))
</script>

<template>
  <ClientOnly>
    <p v-if="allDone" class="done">All exams are complete. Well done! 🎉</p>
    <div
      v-for="d in days" :key="d.date" class="day"
      :class="{ exam: d.exams.length, today: d.today }"
    >
      <div class="head">
        <strong>{{ d.label }}</strong>
        <span v-if="d.today" class="today-tag">Today</span>
        <span v-for="e in d.exams" :key="e.id" class="badge">EXAM {{ e.session }}: {{ e.subject }}</span>
      </div>
      <ul>
        <li v-for="f in d.focus" :key="f.subject + f.kind">
          <a :href="withBase(`/${f.slug}/`)">{{ f.subject }}</a> — {{ f.note }}
        </li>
      </ul>
    </div>
    <p class="tip">
      Generated automatically from today's date and the exam timetable. Adjust to your weak areas, and keep an hour of rest each day.
    </p>
  </ClientOnly>
</template>

<style scoped>
.day { border: 1px solid var(--vp-c-divider); border-radius: 8px; padding: 10px 14px; margin: 10px 0; }
.day.exam { border-left: 4px solid var(--vp-c-brand-1); background: var(--vp-c-bg-soft); }
.day.today { outline: 2px solid var(--vp-c-brand-1); }
.badge, .today-tag { margin-left: 8px; font-size: 12px; padding: 2px 8px; border-radius: 10px; background: var(--vp-c-brand-3); color: #fff; }
.today-tag { background: var(--vp-c-text-1); color: var(--vp-c-bg); }
ul { margin: 6px 0 0; padding-left: 18px; }
.tip, .done { font-size: 13px; color: var(--vp-c-text-2); }
.done { font-size: 16px; }
</style>
