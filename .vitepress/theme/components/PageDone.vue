<script setup lang="ts">
import { computed, onMounted, ref, watch } from 'vue'
import { useData, useRoute, withBase } from 'vitepress'
import { clearQuiz, isDone, pageKey, quizResult, progressVersion, recordVisit, setDone } from '../progress'

// Shown under every page: records the visit (for "continue where you left off")
// and lets the student mark the page as done.
const route = useRoute()
const { page, site } = useData()
const path = computed(() => pageKey(route.path, site.value.base))
const show = computed(() => path.value !== '/' && path.value !== '/progress')
const done = ref(false)
const hasAnswers = ref(false)

function refresh() { done.value = isDone(path.value); hasAnswers.value = !!quizResult(path.value) }
onMounted(() => {
  watch(path, p => { recordVisit(p, page.value.title); refresh() }, { immediate: true })
  watch(progressVersion, refresh)
})
function toggle() { setDone(path.value, !done.value); refresh() }
function clearAnswers() {
  clearQuiz(path.value)
  // The quiz plugin also keeps a "validated" flag for this tab.
  try { Object.keys(sessionStorage).filter(k => k.startsWith('quiz-state:')).forEach(k => sessionStorage.removeItem(k)) } catch {}
  location.reload()
}
</script>

<template>
  <ClientOnly>
    <div v-if="show" class="page-done" :class="{ done }">
      <button type="button" class="mark" :aria-pressed="done" @click="toggle">
        {{ done ? '✓ Done' : 'Mark this page as done' }}
      </button>
      <button v-if="hasAnswers" type="button" class="clear" @click="clearAnswers">Clear my answers</button>
      <a :href="withBase('/progress')">My progress</a>
    </div>
  </ClientOnly>
</template>

<style scoped>
.page-done { display: flex; flex-wrap: wrap; align-items: center; gap: 14px; margin: 32px 0 8px; padding: 12px 16px; border: 1px solid var(--vp-c-divider); border-radius: 8px; background: var(--vp-c-bg-soft); font-size: 14px; }
.page-done button { border: 1px solid var(--vp-c-brand-1); border-radius: 6px; padding: 5px 14px; background: var(--vp-c-bg); color: var(--vp-c-brand-1); font-weight: 600; cursor: pointer; }
.page-done.done button.mark { background: var(--vp-c-green-soft); border-color: var(--vp-c-green-1); color: var(--vp-c-green-1); }
.page-done button:focus-visible { outline: 2px solid var(--vp-c-brand-1); outline-offset: 2px; }
.page-done button.clear { border-color: var(--vp-c-divider); background: var(--vp-c-bg); color: var(--vp-c-text-1); font-weight: 400; }
.page-done a { color: var(--vp-c-text-2); }
@media print { .page-done { display: none; } }
</style>
