# Spanish – vocabulary bank

<script setup>
import { ref, computed } from 'vue'
import { themes, allPairs } from '../.vitepress/data/spanishVocab'

const theme = ref('all')
const cards = computed(() => {
  const pairs = theme.value === 'all' ? allPairs : themes.find(t => t.id === theme.value).words
  return pairs.map(([es, en]) => ({ q: es, a: en }))
})
const total = allPairs.length
</script>

::: tip Vocabulary aligned to the 2024–25 papers
This vocabulary is aligned to **Unit 4: Mi presente; mi futuro** topics (graduation, volunteering, work and study, independence, technology, sustainability, global citizenship). Add anything your teacher stressed. Regional variants exist (Spain vs Latin America).
:::

**{{ total }} entries across {{ themes.length }} themes.** Use the tables to learn, then drill with the flashcards below (progress is saved in your browser).

## Jump to a theme
<ul>
  <li v-for="t in themes" :key="t.id"><a :href="'#' + t.id">{{ t.title }}</a></li>
</ul>

<div v-for="t in themes" :key="t.id" class="vocab-theme">
  <h2 :id="t.id">{{ t.title }}</h2>
  <p v-if="t.note"><em>{{ t.note }}</em></p>
  <table>
    <thead><tr><th>Español</th><th>English</th></tr></thead>
    <tbody>
      <tr v-for="w in t.words" :key="w[0]"><td>{{ w[0] }}</td><td>{{ w[1] }}</td></tr>
    </tbody>
  </table>
</div>

## Drill with flashcards

<div class="picker">
  <label for="theme">Theme: </label>
  <select id="theme" v-model="theme">
    <option value="all">All themes ({{ total }})</option>
    <option v-for="t in themes" :key="t.id" :value="t.id">{{ t.title }}</option>
  </select>
</div>

<Flashcards :key="theme" :id="'vocab-' + theme" :cards="cards" />

## Grammar tips for using the vocabulary

| Pattern | Example |
|---|---|
| `esperar que` + subjunctive | Espero que tenga éxito. |
| `cuando` + subjunctive (future) | Cuando termine el colegio, viajaré. |
| `es importante que` + subjunctive | Es importante que ayudemos a la comunidad. |
| `si` + imperfect subjunctive, conditional | Si tuviera más tiempo, haría voluntariado. |
| `para` + infinitive (purpose) | Estudio para conseguir una beca. |
| `acabar de` + infinitive | Acabo de terminar mi último examen. |
| `llevar` + time + gerund | Llevo dos años estudiando español. |

## Learning plan (7 days)
1. **Days 1–2:** schools, volunteering, work (about 65 words). Cover the English column, say the Spanish aloud.
2. **Days 3–4:** study, independence, technology, environment, global (about 95 words).
3. **Day 5:** issues, feelings, connectors, time, verbs (about 100 words).
4. **Day 6:** drill "All themes", with "Still learning" cards only.
5. **Day 7:** write a 200-word response using at least 20 words from your weakest themes.

::: tip Using vocabulary in the exam
Group words into **chunks** you can reuse: *"Creo que… es importante que…"*, *"Cuando termine…, me gustaría…"*. Chunks save time in the 200–300 word email.
:::

<style scoped>
.vocab-theme table { display: table; width: 100%; }
.picker { margin: 12px 0; }
.picker select { padding: 4px 8px; border: 1px solid var(--vp-c-divider); border-radius: 6px; background: var(--vp-c-bg-soft); color: var(--vp-c-text-1); }
</style>
