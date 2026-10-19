<script setup lang="ts">
import { computed, onMounted, reactive } from 'vue'
import { hashText } from '../../data/examUtils'

const props = defineProps<{ id: string; items: string[] }>()
const key = `checklist:${props.id}`
const metaKey = `progress-checklist:${props.id}`

// Keyed by a hash of each item's text so edits to the list don't misassign ticks.
const hashes = props.items.map(hashText)
const done = reactive<Record<string, boolean>>({})

const count = computed(() => hashes.filter(h => done[h]).length)
const pct = computed(() => Math.round((count.value / props.items.length) * 100) || 0)

function save() {
  try {
    localStorage.setItem(key, JSON.stringify(done))
    localStorage.setItem(metaKey, JSON.stringify({ done: count.value, total: props.items.length }))
  } catch {}
}

onMounted(() => {
  try {
    const saved = JSON.parse(localStorage.getItem(key) || '{}') as Record<string, boolean>
    for (const [k, v] of Object.entries(saved)) {
      // Older versions saved ticks by item position.
      if (/^\d+$/.test(k) && hashes[Number(k)] !== undefined) done[hashes[Number(k)]] = v
      else done[k] = v
    }
    save()
  } catch {}
})

function toggle(h: string) { done[h] = !done[h]; save() }
function reset() { for (const h of Object.keys(done)) delete done[h]; save() }
</script>

<template>
  <ClientOnly>
    <div class="checklist">
      <div class="bar" role="progressbar" :aria-valuenow="pct" aria-valuemin="0" aria-valuemax="100"><div class="fill" :style="{ width: pct + '%' }" /></div>
      <div class="summary">
        {{ count }} / {{ items.length }} done ({{ pct }}%)
        <button type="button" class="reset" @click="reset">Reset</button>
      </div>
      <label v-for="(item, i) in items" :key="hashes[i]" class="row" :class="{ checked: done[hashes[i]] }">
        <input type="checkbox" :checked="!!done[hashes[i]]" @change="toggle(hashes[i])" />
        <span>{{ item }}</span>
      </label>
    </div>
  </ClientOnly>
</template>

<style scoped>
.bar { height: 8px; background: var(--vp-c-divider); border-radius: 4px; overflow: hidden; }
.fill { height: 100%; background: var(--vp-c-brand-1); transition: width .2s; }
.summary { font-size: 13px; color: var(--vp-c-text-2); margin: 6px 0 12px; }
.reset { margin-left: 10px; font-size: 12px; border: 1px solid var(--vp-c-divider); border-radius: 6px; padding: 2px 8px; background: var(--vp-c-bg-soft); color: var(--vp-c-text-1); cursor: pointer; }
.row { display: flex; gap: 10px; align-items: flex-start; padding: 6px 0; cursor: pointer; }
.row.checked span { text-decoration: line-through; color: var(--vp-c-text-3); }
.row input { margin-top: 5px; }
</style>
