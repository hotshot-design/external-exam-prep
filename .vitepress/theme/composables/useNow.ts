import { onBeforeUnmount, onMounted, ref } from 'vue'

/** Current time, set after mount (SSR-safe) and refreshed every minute. */
export function useNow() {
  const now = ref<Date | null>(null)
  let timer: ReturnType<typeof setInterval> | undefined
  onMounted(() => {
    now.value = new Date()
    timer = setInterval(() => { now.value = new Date() }, 60_000)
  })
  onBeforeUnmount(() => { if (timer) clearInterval(timer) })
  return now
}
