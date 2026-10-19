<script setup lang="ts">
import { computed, onMounted, ref, watch } from 'vue'
import { withBase } from 'vitepress'
import { exams } from '../../data/exams'
import { daysUntil, focusFor, isFinished, isoOf } from '../../data/examUtils'
import { useNow } from '../composables/useNow'

const now = useNow()

const subjects = [
  { id: 'english', title: 'English' },
  { id: 'spanish', title: 'Spanish' },
  { id: 'business', title: 'Business' },
  { id: 'film', title: 'Film, TV & New Media' },
  { id: 'maths', title: 'General Maths' },
  { id: 'digital-solutions', title: 'Digital Solutions' },
]
// Checklist ids saved by ProgressChecklist (see each subject's checklist.md)
const checklistId: Record<string, string> = {
  english: 'english', spanish: 'spanish', business: 'business', film: 'film', maths: 'maths', 'digital-solutions': 'digital-solutions',
}

const progress = ref<Record<string, { done: number; total: number } | null>>({})
function load() {
  const out: Record<string, { done: number; total: number } | null> = {}
  for (const s of subjects) {
    try { out[s.id] = JSON.parse(localStorage.getItem(`progress-checklist:${checklistId[s.id]}`) || 'null') } catch { out[s.id] = null }
  }
  progress.value = out
}
onMounted(load)
watch(now, load)

const todayIso = computed(() => (now.value ? isoOf(now.value) : ''))
const focus = computed(() => (todayIso.value ? focusFor(todayIso.value) : []))
const tomorrowExams = computed(() => {
  if (!now.value) return []
  return exams.filter(e => daysUntil(e.date, now.value!) === 1)
})
const todaysExams = computed(() => (now.value ? exams.filter(e => daysUntil(e.date, now.value!) === 0 && !isFinished(e, now.value!)) : []))
const allDone = computed(() => !!now.value && exams.every(e => isFinished(e, now.value!)))
const link = (slug: string, page: string) => withBase(`/${slug}/${page}`)
</script>

<template>
  <ClientOnly>
    <div v-if="now && !allDone" class="today">
      <h2 class="h">Today</h2>
      <p v-if="todaysExams.length" class="alert">
        Exam today: <strong v-for="e in todaysExams" :key="e.id">{{ e.subject }} ({{ e.session }}) </strong>
      </p>
      <p v-else-if="tomorrowExams.length" class="alert">
        Exam tomorrow: <strong v-for="e in tomorrowExams" :key="e.id">{{ e.subject }} ({{ e.session }}) </strong>
        Do a light review, pack your equipment and sleep.
      </p>
      <ul>
        <li v-for="f in focus" :key="f.subject + f.kind">
          <strong>{{ f.subject }}</strong>: {{ f.note }}
          (<a :href="link(f.slug, 'checklist')">checklist</a> · <a :href="link(f.slug, 'flashcards')">flashcards</a> · <a :href="link(f.slug, 'past-papers')">past papers</a>)
        </li>
      </ul>
      <div class="prog">
        <span v-for="s in subjects" :key="s.id" class="chip">
          <a :href="link(s.id, 'checklist')">{{ s.title }}</a>
          {{ progress[s.id] ? `${progress[s.id]!.done}/${progress[s.id]!.total}` : 'not started' }}
        </span>
      </div>
    </div>
  </ClientOnly>
</template>

<style scoped>
.today { border: 1px solid var(--vp-c-divider); border-radius: 8px; padding: 14px 18px; background: var(--vp-c-bg-soft); margin: 16px 0; }
.h { border: none; margin: 0 0 6px; padding: 0; font-size: 18px; }
.alert { margin: 6px 0; padding: 6px 10px; border-left: 4px solid var(--vp-c-brand-1); background: var(--vp-c-bg); }
ul { margin: 6px 0; padding-left: 18px; }
.prog { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 10px; }
.chip { font-size: 12px; padding: 3px 10px; border-radius: 12px; border: 1px solid var(--vp-c-divider); background: var(--vp-c-bg); }
</style>
