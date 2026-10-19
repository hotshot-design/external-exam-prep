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

export default {
  extends: DefaultTheme,
  enhanceApp({ app }) {
    app.component('ExamCountdown', ExamCountdown)
    app.component('ExamCalendar', ExamCalendar)
    app.component('StudyPlanner', StudyPlanner)
    app.component('ProgressChecklist', ProgressChecklist)
    app.component('Flashcards', Flashcards)
    app.component('GlossaryBank', GlossaryBank)
    app.component('TodayPanel', TodayPanel)
    app.component('Diagram', Diagram)
    enhanceAppWithQuiz(app)
    enableLiveQuizFeedback(app)
  },
} satisfies Theme
