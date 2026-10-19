<script setup lang="ts">
import { computed } from 'vue'
import { exams } from '../../data/exams'
import { daysUntil, isFinished } from '../../data/examUtils'
import { useNow } from '../composables/useNow'

const now = useNow()

const rows = computed(() => {
  if (!now.value) return []
  return exams.map(e => ({ ...e, days: daysUntil(e.date, now.value!), done: isFinished(e, now.value!) }))
})
const remaining = computed(() => rows.value.filter(r => !r.done))
const next = computed(() => remaining.value[0])
const later = computed(() => remaining.value.slice(1))
const fmt = (iso: string) =>
  new Date(iso + 'T00:00:00').toLocaleDateString('en-AU', { weekday: 'short', day: 'numeric', month: 'short' })
</script>

<template>
  <ClientOnly>
    <div v-if="next" class="countdown">
      <div class="label">Next exam</div>
      <div class="subject">{{ next.subject }}</div>
      <div class="when">
        {{ fmt(next.date) }} · {{ next.session }} · {{ next.duration }} + {{ next.perusal }} perusal
      </div>
      <div class="days">
        <template v-if="next.days === 0">Today</template>
        <template v-else-if="next.days === 1">Tomorrow</template>
        <template v-else>{{ next.days }} days to go</template>
      </div>
      <details v-if="later.length" class="later">
        <summary>{{ later.length }} more exam{{ later.length === 1 ? '' : 's' }}</summary>
        <ul>
          <li v-for="r in later" :key="r.id">{{ fmt(r.date) }} {{ r.session }}: {{ r.subject }}
            ({{ r.days }} day{{ r.days === 1 ? '' : 's' }})</li>
        </ul>
      </details>
    </div>
    <div v-else-if="rows.length" class="countdown">All exams complete 🎉</div>
  </ClientOnly>
</template>

<style scoped>
.countdown {
  border: 1px solid var(--vp-c-divider);
  border-left: 4px solid var(--vp-c-brand-1);
  border-radius: 8px;
  padding: 16px 20px;
  background: var(--vp-c-bg-soft);
  margin: 16px 0;
}
.label { font-size: 12px; text-transform: uppercase; letter-spacing: .06em; color: var(--vp-c-text-2); }
.subject { font-size: 22px; font-weight: 600; }
.when { color: var(--vp-c-text-2); font-size: 14px; }
.days { margin-top: 6px; font-size: 18px; color: var(--vp-c-brand-1); font-weight: 600; }
.later { margin-top: 10px; font-size: 13px; color: var(--vp-c-text-2); }
.later ul { margin: 6px 0 0; padding-left: 18px; }
</style>
