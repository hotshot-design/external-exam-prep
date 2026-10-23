import { defineComponent, h, inject, nextTick, onBeforeUnmount, onMounted, provide, ref, watch } from 'vue'
import type { App } from 'vue'
import { useData, useRoute, withBase } from 'vitepress'
import { hashText } from '../data/examUtils'
import { markQuiz, pageKey, quizAnswer, quizMarks, saveQuizAnswer } from './progress'

/**
 * The quiz plugin only reveals answers when the page-level "Validate" is pressed.
 * Wrap its <QuizQuestion> so each question can be checked on its own:
 *  - single-choice questions are checked as soon as an option is clicked
 *  - other questions (multiple choice, fill-in, matching) get a "Check answer" button
 * The page-level Validate and Reset still work for every question.
 * Answers and marks are kept in localStorage (see progress.ts), keyed by a hash of the
 * question, so they survive closing the tab and feed the Progress page.
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

        // Replace the plugin's per-tab (sessionStorage) answers with saved ones.
        const path = pageKey(useRoute().path, useData().site.value.base)
        const qid = hashText(props.dataQuiz)
        provide('quiz-question-id', () => qid)
        provide('quiz-save-answer', (_: unknown, a: unknown) => saveQuizAnswer(path, qid, a))
        provide('quiz-get-answer', () => quizAnswer(path, qid))
        // Capture the question's isCorrect so a check can be recorded.
        const register = inject<any>('quiz-register', null)
        let state: { isCorrect: { value: boolean } } | undefined
        provide('quiz-register', (s: any) => { state = s; return register ? register(s) : () => {} })
        const total = () => document.querySelectorAll('.quiz-live').length

        let restoring = false
        watch(checked, v => { if (v && state && !restoring) markQuiz(path, qid, state.isCorrect.value, total()) }, { flush: 'sync' })
        watch(pageValidated, v => { if (v) checked.value = true })
        watch(pageReset, () => {
          checked.value = false
          saveQuizAnswer(path, qid, null)
          markQuiz(path, qid, null, total())
        })

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
              a.href = m[2].startsWith('/') ? withBase(m[2]) : m[2]
              if (/\.(pdf|mp3)(#.*)?$/i.test(m[2]) || /^https?:/i.test(m[2])) { a.target = '_blank'; a.rel = 'noopener noreferrer' }
              frag.append(a)
              rest = rest.slice(m.index + m[0].length)
            }
            if (rest) frag.append(rest)
            node.replaceWith(frag)
          }
        }
        onMounted(() => {
          if (qid in quizMarks(path)) {
            restoring = true
            checked.value = true
            restoring = false
          }
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
