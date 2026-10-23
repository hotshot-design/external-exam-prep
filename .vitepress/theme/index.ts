import { h } from 'vue'
import DefaultTheme from 'vitepress/theme'
import './custom.css'
import { enhanceAppWithQuiz } from '@matinfo/vitepress-plugin-quiz'
import { enableLiveQuizFeedback } from './quizLive'
import type { Theme } from 'vitepress'
import ExamCountdown from './components/ExamCountdown.vue'
import ExamCalendar from './components/ExamCalendar.vue'
import StudyPlanner from './components/StudyPlanner.vue'
import ProgressChecklist from './components/ProgressChecklist.vue'
import Flashcards from './components/Flashcards.vue'
import GlossaryBank from './components/GlossaryBank.vue'
import TodayPanel from './components/TodayPanel.vue'
import Diagram from './components/Diagram.vue'
import PageDone from './components/PageDone.vue'
import ProgressDashboard from './components/ProgressDashboard.vue'

export default {
  extends: DefaultTheme,
  Layout: () => h(DefaultTheme.Layout, null, { 'doc-footer-before': () => h(PageDone) }),
  enhanceApp({ app }) {
    app.component('ExamCountdown', ExamCountdown)
    app.component('ExamCalendar', ExamCalendar)
    app.component('StudyPlanner', StudyPlanner)
    app.component('ProgressChecklist', ProgressChecklist)
    app.component('Flashcards', Flashcards)
    app.component('GlossaryBank', GlossaryBank)
    app.component('TodayPanel', TodayPanel)
    app.component('Diagram', Diagram)
    app.component('ProgressDashboard', ProgressDashboard)
    enhanceAppWithQuiz(app)
    enableLiveQuizFeedback(app)
  },
} satisfies Theme
