<script setup lang="ts">
import { computed, onMounted, ref } from 'vue'
import { hashText } from '../../data/examUtils'

interface Card { q: string; a: string }
const props = defineProps<{ id: string; cards: Card[] }>()
const key = `flashcards:${props.id}`
const metaKey = `progress-cards:${props.id}`

// Progress is keyed by a hash of each question, so edits or reordering don't misassign it.
const hashes = props.cards.map(c => hashText(c.q))

const order = ref<number[]>(props.cards.map((_, i) => i))
const idx = ref(0)
const flipped = ref(false)
const known = ref<Record<string, boolean>>({})
const onlyUnknown = ref(false)

onMounted(() => {
  try {
    const saved = JSON.parse(localStorage.getItem(key) || '{}') as Record<string, boolean>
    const migrated: Record<string, boolean> = {}
    for (const [k, v] of Object.entries(saved)) {
      // Older versions saved progress by card position.
      if (/^\d+$/.test(k) && hashes[Number(k)] !== undefined) migrated[hashes[Number(k)]] = v
      else migrated[k] = v
    }
    known.value = migrated
    save()
  } catch {}
})

const deck = computed(() => order.value.filter(i => !onlyUnknown.value || !known.value[hashes[i]]))
const current = computed(() => (deck.value.length ? props.cards[deck.value[idx.value % deck.value.length]] : undefined))
const knownCount = computed(() => hashes.filter(h => known.value[h]).length)

function save() {
  try {
    localStorage.setItem(key, JSON.stringify(known.value))
    localStorage.setItem(metaKey, JSON.stringify({ known: knownCount.value, total: props.cards.length }))
  } catch {}
}
function next() { flipped.value = false; idx.value = (idx.value + 1) % Math.max(deck.value.length, 1) }
function prev() { flipped.value = false; idx.value = (idx.value - 1 + Math.max(deck.value.length, 1)) % Math.max(deck.value.length, 1) }
function mark(v: boolean) {
  if (!current.value) return
  const h = hashes[deck.value[idx.value % deck.value.length]]
  known.value = { ...known.value, [h]: v }
  save()
  flipped.value = false
  if (onlyUnknown.value && v) {
    // The known card leaves the deck, so the next card has taken its place: don't skip it.
    if (idx.value >= deck.value.length) idx.value = 0
  } else {
    next()
  }
}
function shuffle() {
  const a = [...order.value]
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]]
  }
  order.value = a; idx.value = 0; flipped.value = false
}
function reset() { known.value = {}; save(); idx.value = 0; flipped.value = false }
function onKey(e: KeyboardEvent) {
  if (e.key === 'ArrowRight') { e.preventDefault(); next() }
  else if (e.key === 'ArrowLeft') { e.preventDefault(); prev() }
}
</script>

<template>
  <ClientOnly>
    <div class="fc" @keydown="onKey">
      <div class="meta">
        Known {{ knownCount }} / {{ cards.length }}
        <label><input type="checkbox" v-model="onlyUnknown" @change="idx = 0" /> unknown only</label>
        <button type="button" @click="shuffle">Shuffle</button>
        <button type="button" @click="reset">Reset</button>
      </div>
      <button v-if="current" type="button" class="card" @click="flipped = !flipped" :aria-label="flipped ? 'Answer. Press to show question' : 'Question. Press to show answer'">
        <span class="side">{{ flipped ? 'Answer' : 'Question' }}</span>
        <span class="text" aria-live="polite">{{ flipped ? current.a : current.q }}</span>
        <span class="hint">click or press Enter to flip · ← → to move</span>
      </button>
      <div v-else class="card empty">Nothing left in this deck 🎉</div>
      <div class="actions" v-if="current">
        <button type="button" @click="mark(false)">Still learning</button>
        <button type="button" @click="mark(true)" class="primary">Got it</button>
      </div>
    </div>
  </ClientOnly>
</template>

<style scoped>
.meta { display: flex; gap: 12px; align-items: center; flex-wrap: wrap; font-size: 13px; color: var(--vp-c-text-2); }
button { border: 1px solid var(--vp-c-divider); border-radius: 6px; padding: 4px 12px; background: var(--vp-c-bg-soft); color: var(--vp-c-text-1); cursor: pointer; }
button.primary { background: var(--vp-c-brand-3); color: #fff; border-color: var(--vp-c-brand-3); }
button:focus-visible { outline: 2px solid var(--vp-c-brand-1); outline-offset: 2px; }
.card {
  width: 100%; margin: 12px 0; min-height: 160px; padding: 20px; border-radius: 10px; cursor: pointer;
  border: 1px solid var(--vp-c-divider); background: var(--vp-c-bg-soft); color: var(--vp-c-text-1);
  display: flex; flex-direction: column; justify-content: center; text-align: center;
}
.card.empty { cursor: default; align-items: center; }
.side { font-size: 11px; text-transform: uppercase; letter-spacing: .06em; color: var(--vp-c-text-3); }
.text { font-size: 18px; margin: 8px 0; white-space: pre-line; }
.hint { font-size: 11px; color: var(--vp-c-text-3); }
.actions { display: flex; gap: 8px; justify-content: center; }
</style>
