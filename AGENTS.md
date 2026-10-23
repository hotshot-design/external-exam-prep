# AGENTS.md

Guidance for AI agents working on this repo.

## What this is
A VitePress 1.6 study site for a Queensland Year 12 student sitting the **QCAA 2026 external exams**: English (Othello) 27 Oct, Spanish 28 Oct, Business 3 Nov, Film, TV & New Media 4 Nov, General Maths P1 5 Nov / P2 6 Nov, Digital Solutions 10 Nov. Deployed to GitHub Pages at https://hotshot-design.github.io/external-exam-prep/ (repo `hotshot-design/external-exam-prep`, public).

**The QCAA PDFs are the source of truth** (past papers, marking guides, syllabuses in each `<subject>/papers/` and `<subject>/syllabus/`). Check facts, mark allocations and answers against them. Never invent what an unseen clip, audio file or missing diagram contains; say so instead (see `film/past-questions.md`, `maths/solutions-2023.md`).

## Commands
- `npm install`, `npm run docs:dev` (http://localhost:5173), `npm run docs:build`, `npm run docs:preview`.
- Always run `npx vitepress build` after content changes. It must finish with no errors or dead links.
- Pushing to `main` deploys via `.github/workflows/deploy.yml`. Only commit or push when the user asks.
- `base` is `/external-exam-prep/` only when `GITHUB_ACTIONS` is set. Local dev and preview use `/`. Use `withBase()` in components and root-relative links in markdown.

## Layout
- Root pages: `index.md` (countdown, today panel, exam calendar), `timetable.md`, `planner.md`, `progress.md`, `strategy.md`, `past-papers.md`, `quizzes.md`, `syllabuses.md`, `diagrams.md` (gallery of every diagram). `SUBJECTS.md` is excluded from the site.
- Per subject (`english`, `spanish`, `business`, `film`, `maths`, `digital-solutions`): `index.md`, `notes.md`, `quick-reference.md`, `checklist.md`, `flashcards.md`, `past-papers.md`, `papers.md` (link tables to the PDFs), `quiz-*.md`, plus subject extras (`solutions-<year>.md`, `worked-examples.md`, `glossary.md`, `essay-plans.md`, `past-prompts.md`, `past-questions.md`, `vocabulary.md`, `verbs.md`, `practice.md`, and so on).
- `.vitepress/config.ts`: nav, grouped sidebar (via `subject()`), markdown config, `buildEnd` hook that copies each `papers/` and `syllabus/` folder into the build (non-markdown files in the source tree are not copied otherwise).
- `.vitepress/theme/`: `index.ts` registers components and the quiz plugin; `components/` (ExamCountdown, ExamCalendar, TodayPanel, StudyPlanner, ProgressChecklist, Flashcards, GlossaryBank, Diagram); `quizLive.ts` (wrapper over the quiz plugin); `custom.css`; `diagrams/*.svg` (generated, do not hand-edit) and `diagrams/sources.json` (generated).
- `.vitepress/data/`: `exams.ts` (single source of exam dates and sessions), `examUtils.ts`, `spanishVocab.ts`, `glossary/*.ts`.

## Conventions and gotchas
- **Math** uses `markdown: { math: true }` (MathJax). Use `$...$`. **Escape money as `\$`**, or it pairs with maths delimiters and garbles the page.
- **Links** to `.pdf`, `.mp3` and `http(s)` open in a new tab (markdown-it `link_open` rule). Link past-paper PDFs with `#page=N` where useful (page numbers are the PDF viewer's).
- **Quizzes** use `@matinfo/vitepress-plugin-quiz` `:::quiz` blocks (`question:`, `answer:`, `answer-correct:`, `answer-input:`, `pair: A => B`, `explanation:`). Inside `explanation:` only bold, italic and code render; `[text](url)` is converted to a link by `quizLive.ts`. A block missing its closing `:::` breaks the rest of the page, so check blocks. Fill-in answers ignore accents, so test Spanish accents with multiple choice.
- **Do not add "exam skills" or technique quizzes.** The user asked for those to be removed. Quizzes cover past-paper questions, vocabulary and grammar, terms and concepts, and short-response questions only.
- Quiz pages are now maintained by hand. The one-off generator scripts that produced them are not in the repo; do not try to regenerate them.
- Progress (checklists, flashcards, planner) is in `localStorage`, keyed by a hash of the item text (`hashText`). Changing an item's wording resets its tick.
- `.vitepress/theme/progress.ts` holds the rest of the saved progress: pages visited and marked done (`PageDone.vue`, in the `doc-footer-before` slot), the last page opened, and quiz answers and marks (saved by `quizLive.ts`, keyed by a hash of the question, so editing a question resets it). `progress.md` (`ProgressDashboard.vue`) lists it per subject from the sidebar, with backup and restore for moving between devices. Add new storage prefixes to `PREFIXES` there.
- Exam finish cut-offs are approximate (AM 13:00, PM 18:00) because the QCAA timetable gives only AM or PM.
- Facts already established from the papers: English 45 marks, 800–1000 words, 15 + 120 min; Spanish 2024–25 has three sections (audio in Spanish, texts in English, 200–300 word email); Business report is 24–25 marks; Film uses five key concepts; Maths P1 57 marks and P2 38; Digital 66–67 marks. Digital papers print 15 min perusal but the 2026 timetable says 5, so the site uses 5.
- Model essays, reports, emails and plans are original revision aids, not QCAA samples. Questions and context text are © State of Queensland (QCAA), CC BY 4.0.
- Worked solutions cite marking-guide criteria. Answers must be recomputed and checked (use a script for numeric answers). If there is no guide (Maths 2023), say so.

## Diagrams
- Source is Python in `scripts/`: `svgkit.py` (the `SVG` helper and style classes), `diagrams_<subject>.py`, `diagrams_solutions*.py` (question-specific, embedded in solutions pages), `diagrams_examples.py` (Maths worked examples). Each module exposes an `ALL` dict; register new modules in `scripts/diagrams.py`.
- Regenerate with `python3 scripts/diagrams.py && python3 scripts/diagram_sources.py`. The second step writes `sources.json`, which drives the "Sources:" line under each diagram (question paper, marking guide page, syllabus page). Add an entry to `D` in `diagram_sources.py` for every new diagram. It needs macOS and a compiled `scripts/xp.swift` (`swiftc -O scripts/xp.swift -o /tmp/xp`) to read PDF text without poppler.
- Embed with `<Diagram name="x" caption="..." />` (the SVG is looked up in `.vitepress/theme/diagrams/`). List new diagrams in `diagrams.md`.
- Styles use VitePress CSS variables so light and dark both work. After changes, build, open the page and check **legibility, overlap and accuracy against the source PDF**, in light and dark, and at phone width. Question-specific diagrams must use the paper's real numbers.

## Verifying accuracy
The process for checking the site against the QCAA sources is in [VERIFY.md](VERIFY.md). Tools: `python3 scripts/verify/check.py --build` (mechanical checks, exit 1 on errors), `python3 scripts/verify/maths_examples.py` (recomputes the worked examples), `python3 scripts/verify/ledger.py status|next|record` (which pages have been reviewed against the PDFs, and which are stale). Run `check.py` after content edits.

## Verifying changes
- Build clean, then look at the changed pages in a browser (Playwright with system Chrome works; there is no poppler, and text and page images come from the Swift PDFKit tools).
- Check phone width (no horizontal scroll, 16px gutters) and dark mode for anything visual.
- Keep edits minimal and match the surrounding style. Do not reorganise the nav or sidebar unless asked (quizzes are grouped as a **Quizzes** group per subject, shown as a single **Quiz** link when a subject has only one).
