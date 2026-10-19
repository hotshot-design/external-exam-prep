import { cpSync, existsSync } from 'node:fs'
import { join } from 'node:path'
import { defineConfig } from 'vitepress'
import { quizMarkdownPlugin } from '@matinfo/vitepress-plugin-quiz'

type Item = { text: string; link: string }

/** Each subject is grouped into Learn / Past papers / Practise so the sidebar stays short. */
const subject = (
  base: string,
  title: string,
  g: { learn?: Item[]; papers?: Item[]; practise?: Item[]; quizzes?: Item[] },
) => ({
  text: title,
  collapsed: true,
  items: [
    { text: 'Overview & exam format', link: `/${base}/` },
    { text: 'Quick reference (exam day)', link: `/${base}/quick-reference` },
    ...(g.quizzes?.length === 1
      ? [{ text: 'Quiz', link: g.quizzes[0].link }]
      : g.quizzes?.length ? [{ text: 'Quizzes', collapsed: false, items: g.quizzes }] : []),
    {
      text: 'Learn',
      collapsed: true,
      items: [{ text: 'Revision notes', link: `/${base}/notes` }, ...(g.learn ?? [])],
    },
    { text: 'Past papers', collapsed: true, items: g.papers ?? [] },
    {
      text: 'Practise',
      collapsed: true,
      items: [
        ...(g.practise ?? []),
        { text: 'Checklist', link: `/${base}/checklist` },
        { text: 'Flashcards', link: `/${base}/flashcards` },
      ],
    },
  ],
})

const subjectNav = [
  { text: 'English – Othello', link: '/english/' },
  { text: 'Spanish', link: '/spanish/' },
  { text: 'Business', link: '/business/' },
  { text: 'Film, TV & New Media', link: '/film/' },
  { text: 'General Maths', link: '/maths/' },
  { text: 'Digital Solutions', link: '/digital-solutions/' },
]

const siteBase = process.env.GITHUB_ACTIONS ? '/external-exam-prep' : ''

export default defineConfig({
  // GitHub Pages serves the site from /external-exam-prep/; local dev stays at /
  base: siteBase ? `${siteBase}/` : '/',
  title: 'Year 12 Exam Hub',
  description: 'QCAA external assessment revision – 2026',
  lang: 'en-AU',
  srcExclude: ['SUBJECTS.md'],
  // Non-markdown files in the source folders are not copied by `vitepress build`,
  // so copy each subject's papers/ and syllabus/ folders (PDFs, audio) into the built site.
  buildEnd(siteConfig) {
    for (const sub of ['english', 'spanish', 'business', 'film', 'maths', 'digital-solutions']) {
      for (const dir of ['papers', 'syllabus']) {
        const from = join(siteConfig.srcDir, sub, dir)
        if (existsSync(from)) cpSync(from, join(siteConfig.outDir, sub, dir), { recursive: true })
      }
    }
  },
  markdown: {
    math: true,
    config(md) {
      md.use(quizMarkdownPlugin)
      // Open PDFs, audio and external links in a new tab.
      const defaultRender = md.renderer.rules.link_open ||
        ((tokens, idx, options, _env, self) => self.renderToken(tokens, idx, options))
      md.renderer.rules.link_open = (tokens, idx, options, env, self) => {
        const href = tokens[idx].attrGet('href') || ''
        if (/\.(pdf|mp3)(#.*)?$/i.test(href) && href.startsWith('/')) tokens[idx].attrSet('href', siteBase + href.slice(1 - 1))
        if (/\.(pdf|mp3)(#.*)?$/i.test(href) || /^https?:\/\//i.test(href)) {
          tokens[idx].attrSet('target', '_blank')
          tokens[idx].attrSet('rel', 'noopener noreferrer')
        }
        return defaultRender(tokens, idx, options, env, self)
      }
    },
  },
  themeConfig: {
    search: { provider: 'local' },
    nav: [
      { text: 'Timetable', link: '/timetable' },
      { text: 'Planner', link: '/planner' },
      { text: 'Strategy', link: '/strategy' },
      { text: 'Subjects', items: subjectNav },
      { text: 'Past papers', link: '/past-papers' },
      { text: 'Quizzes', link: '/quizzes' },
    ],
    sidebar: [
      {
        text: 'Plan',
        items: [
          { text: 'Home', link: '/' },
          { text: 'Timetable', link: '/timetable' },
          { text: 'Study planner', link: '/planner' },
          { text: 'Exam strategy', link: '/strategy' },
          { text: 'All past papers', link: '/past-papers' },
          { text: 'All quizzes', link: '/quizzes' },
          { text: 'Concept diagrams', link: '/diagrams' },
          { text: 'Syllabuses (PDFs)', link: '/syllabuses' },
        ],
      },
      subject('english', 'English – Othello', {
        learn: [
          { text: 'Quote analysis', link: '/english/quotes' },
        ],
        papers: [
          { text: 'Past papers analysis', link: '/english/past-papers' },
          { text: 'Paper files (PDFs)', link: '/english/papers' },
          { text: 'Past Othello prompts', link: '/english/past-prompts' },
        ],
        practise: [
          { text: 'Essay plans', link: '/english/essay-plans' },
          { text: 'Model essay & self-marking', link: '/english/model-essay' },
        ],
        quizzes: [
          { text: 'Quotes and techniques', link: '/english/quiz-quotes' },
        ],
      }),
      subject('spanish', 'Spanish', {
        learn: [
          { text: 'Vocabulary bank', link: '/spanish/vocabulary' },
          { text: 'Verbs & tenses', link: '/spanish/verbs' },
        ],
        papers: [
          { text: 'Past papers analysis', link: '/spanish/past-papers' },
          { text: 'Paper files (PDFs)', link: '/spanish/papers' },
          { text: '2025 worked solutions', link: '/spanish/solutions-2025' },
          { text: '2024 worked solutions', link: '/spanish/solutions-2024' },
        ],
        practise: [{ text: 'Model responses & emails', link: '/spanish/practice' }],
        quizzes: [
          { text: 'Tenses and grammar', link: '/spanish/quiz-grammar' },
          { text: 'Vocabulary matching', link: '/spanish/quiz-vocab' },
        ],
      }),
      subject('business', 'Business', {
        learn: [{ text: 'Glossary bank', link: '/business/glossary' }],
        papers: [
          { text: 'Past papers analysis', link: '/business/past-papers' },
          { text: 'Paper files (PDFs)', link: '/business/papers' },
          { text: '2025 worked solutions', link: '/business/solutions-2025' },
          { text: '2024 worked solutions', link: '/business/solutions-2024' },
        ],
        practise: [{ text: 'Worked case & practice', link: '/business/practice' }],
        quizzes: [
          { text: 'Theories, criteria, report', link: '/business/quiz-theory' },
          { text: 'Reading a case', link: '/business/quiz-case' },
          { text: 'Short responses 2024–25', link: '/business/quiz-short-response-2024-25' },
          { text: 'Short responses 2022–23', link: '/business/quiz-short-response-2022-23' },
          { text: 'Short responses 2020–21', link: '/business/quiz-short-response-2020-21' },
        ],
      }),
      subject('film', 'Film, TV & New Media', {
        learn: [{ text: 'Glossary bank', link: '/film/glossary' }],
        papers: [
          { text: 'Past papers analysis', link: '/film/past-papers' },
          { text: 'Paper files (PDFs)', link: '/film/papers' },
          { text: 'Past questions frameworks', link: '/film/past-questions' },
        ],
        practise: [{ text: 'Essay plans', link: '/film/essay-plans' }],
        quizzes: [
          { text: 'Key concepts and exam', link: '/film/quiz-concepts' },
          { text: 'Terminology', link: '/film/quiz-terms' },
        ],
      }),
      subject('maths', 'General Maths', {
        learn: [{ text: 'Glossary bank', link: '/maths/glossary' }],
        papers: [
          { text: 'Past papers analysis', link: '/maths/past-papers' },
          { text: 'Paper files (PDFs)', link: '/maths/papers' },
          { text: '2025 worked solutions', link: '/maths/solutions-2025' },
          { text: '2024 worked solutions', link: '/maths/solutions-2024' },
          { text: '2023 worked solutions', link: '/maths/solutions-2023' },
          { text: '2022 worked solutions', link: '/maths/solutions-2022' },
          { text: '2021 worked solutions', link: '/maths/solutions-2021' },
          { text: '2020 worked solutions', link: '/maths/solutions-2020' },
        ],
        practise: [{ text: 'Worked examples', link: '/maths/worked-examples' }],
        quizzes: [
          { text: 'Past-paper multiple choice', link: '/maths/quiz-past-mc' },
          { text: 'Short responses 2024–25', link: '/maths/quiz-sr-2024-25' },
          { text: 'Short responses 2021–22', link: '/maths/quiz-sr-2021-22' },
          { text: 'Short responses 2020', link: '/maths/quiz-sr-2020' },
          { text: 'Calculation drills', link: '/maths/quiz-methods' },
        ],
      }),
      subject('digital-solutions', 'Digital Solutions', {
        learn: [{ text: 'Glossary bank', link: '/digital-solutions/glossary' }],
        papers: [
          { text: 'Past papers analysis', link: '/digital-solutions/past-papers' },
          { text: 'Paper files (PDFs)', link: '/digital-solutions/papers' },
          { text: '2025 worked solutions', link: '/digital-solutions/solutions-2025' },
          { text: '2024 worked solutions', link: '/digital-solutions/solutions-2024' },
        ],
        practise: [{ text: 'Worked examples', link: '/digital-solutions/practice' }],
        quizzes: [
          { text: 'Past-paper multiple choice', link: '/digital-solutions/quiz-past-mc' },
          { text: 'Short responses 2024–25', link: '/digital-solutions/quiz-short-response' },
          { text: 'Short responses 2022–23', link: '/digital-solutions/quiz-short-response-2022-23' },
          { text: 'Short responses 2020–21', link: '/digital-solutions/quiz-short-response-2020-21' },
          { text: 'Concepts and drills', link: '/digital-solutions/quiz-concepts' },
        ],
      }),
    ],
  },
})
