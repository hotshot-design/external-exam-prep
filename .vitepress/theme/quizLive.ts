import { defineComponent, h, inject, nextTick, onBeforeUnmount, onMounted, provide, ref, watch } from 'vue'
import type { App } from 'vue'

/**
 * The quiz plugin only reveals answers when the page-level "Validate" is pressed.
 * Wrap its <QuizQuestion> so each question can be checked on its own:
 *  - single-choice questions are checked as soon as an option is clicked
 *  - other questions (multiple choice, fill-in, matching) get a "Check answer" button
 * The page-level Validate and Reset still work for every question.
 */
export function enableLiveQuizFeedback(app: App) {
  const Orig = app.component('QuizQuestion') as any
  if (!Orig) return

  app.component(
    'QuizQuestion',
    defineComponent({
      name: 'QuizQuestion',
      props: Orig.props,
      setup(props: any) {
        let single = false
        try {
          const q = JSON.parse(props.dataQuiz)
          single = q.type === 'choice' && (q.answers || []).filter((a: any) => a.correct).length === 1
        } catch { /* fall back to the Check button */ }

        const checked = ref(false)
        const pageValidated = inject<any>('quiz-validated', ref(false))
        const pageReset = inject<any>('quiz-reset', ref(0))
        provide('quiz-validated', checked)

        watch(pageValidated, v => { if (v) checked.value = true })
        watch(pageReset, () => { checked.value = false })

        // The plugin shows explanations as plain text (bold/italic/code only), so turn
        // [text](url) markdown links inside the explanation into real links.
        const root = ref<HTMLElement | null>(null)
        let observer: MutationObserver | undefined
        const LINK = /\[([^\]]+)\]\(([^)\s]+)\)/
        const linkify = () => {
          const box = root.value?.querySelector('.quiz-explanation')
          if (!box) return
          const walker = document.createTreeWalker(box, NodeFilter.SHOW_TEXT)
          const nodes: Text[] = []
          while (walker.nextNode()) if (LINK.test((walker.currentNode as Text).data)) nodes.push(walker.currentNode as Text)
          for (const node of nodes) {
            const frag = document.createDocumentFragment()
            let rest = node.data
            let m: RegExpExecArray | null
            while ((m = LINK.exec(rest))) {
              if (m.index) frag.append(rest.slice(0, m.index))
              const a = document.createElement('a')
              a.textContent = m[1]
              a.href = m[2]
              if (/\.(pdf|mp3)(#.*)?$/i.test(m[2]) || /^https?:/i.test(m[2])) { a.target = '_blank'; a.rel = 'noopener noreferrer' }
              frag.append(a)
              rest = rest.slice(m.index + m[0].length)
            }
            if (rest) frag.append(rest)
            node.replaceWith(frag)
          }
        }
        onMounted(() => {
          if (!root.value) return
          observer = new MutationObserver(linkify)
          observer.observe(root.value, { childList: true, subtree: true, characterData: true })
        })
        onBeforeUnmount(() => observer?.disconnect())

        const onClick = (e: MouseEvent) => {
          if (!single || checked.value) return
          if ((e.target as HTMLElement).closest('.quiz-answer')) nextTick(() => { checked.value = true })
        }

        return () =>
          h('div', { class: 'quiz-live', ref: root, onClick }, [
            h(Orig, props),
            !single && !checked.value
              ? h('button', { type: 'button', class: 'quiz-check-btn', onClick: () => { checked.value = true } }, 'Check answer')
              : null,
          ])
      },
    }),
  )
}
