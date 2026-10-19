<script setup lang="ts">
import { computed, ref } from 'vue'
import Flashcards from './Flashcards.vue'

interface Theme { id: string; title: string; note?: string; words: [string, string][] }
const props = defineProps<{ id: string; themes: Theme[] }>()

const theme = ref('all')
const query = ref('')
const total = computed(() => props.themes.reduce((n, t) => n + t.words.length, 0))

const cards = computed(() => {
  const pairs = theme.value === 'all'
    ? props.themes.flatMap(t => t.words)
    : props.themes.find(t => t.id === theme.value)?.words ?? []
  return pairs.map(([q, a]) => ({ q, a }))
})

const filtered = computed(() => {
  const s = query.value.trim().toLowerCase()
  if (!s) return props.themes
  return props.themes
    .map(t => ({ ...t, words: t.words.filter(([a, b]) => (a + ' ' + b).toLowerCase().includes(s)) }))
    .filter(t => t.words.length)
})
</script>

<template>
  <div class="glossary">
    <p><strong>{{ total }} terms across {{ themes.length }} themes.</strong> Search, read by theme, then drill with the flashcards below.</p>

    <input v-model="query" class="search" type="search" placeholder="Search terms or definitions…" />

    <ul class="jump" v-if="!query">
      <li v-for="t in themes" :key="t.id"><a :href="'#' + id + '-' + t.id">{{ t.title }}</a></li>
    </ul>

    <section v-for="t in filtered" :key="t.id">
      <h2 :id="id + '-' + t.id">{{ t.title }}</h2>
      <p v-if="t.note"><em>{{ t.note }}</em></p>
      <table>
        <thead><tr><th>Term</th><th>Meaning</th></tr></thead>
        <tbody>
          <tr v-for="w in t.words" :key="w[0]"><td><strong>{{ w[0] }}</strong></td><td>{{ w[1] }}</td></tr>
        </tbody>
      </table>
    </section>
    <p v-if="!filtered.length">No matches.</p>

    <h2 :id="id + '-drill'">Drill with flashcards</h2>
    <div class="picker">
      <label :for="id + '-theme'">Theme: </label>
      <select :id="id + '-theme'" v-model="theme">
        <option value="all">All themes ({{ total }})</option>
        <option v-for="t in themes" :key="t.id" :value="t.id">{{ t.title }}</option>
      </select>
    </div>
    <ClientOnly>
      <Flashcards :key="theme" :id="id + '-glossary-' + theme" :cards="cards" />
    </ClientOnly>
  </div>
</template>

<style scoped>
.search { width: 100%; max-width: 420px; padding: 8px 12px; border: 1px solid var(--vp-c-divider); border-radius: 6px; background: var(--vp-c-bg-soft); color: var(--vp-c-text-1); margin: 8px 0; }
.jump { columns: 2; }
.picker { margin: 12px 0; }
.picker select { padding: 4px 8px; border: 1px solid var(--vp-c-divider); border-radius: 6px; background: var(--vp-c-bg-soft); color: var(--vp-c-text-1); }
table { display: block; overflow-x: auto; width: 100%; }
@media (max-width: 640px) { .jump { columns: 1; } }
</style>
