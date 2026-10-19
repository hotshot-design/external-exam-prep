# VERIFY.md: checking the site against the source material

The QCAA PDFs in each `<subject>/papers/` and `<subject>/syllabus/` (plus the 2026 timetable PDF in the repo root) are the source of truth. This process lets you, or another agent, check the site against them and record what was checked. Run it after any large content change and before each exam.

## The three levels

| Level | What | Who | Command |
|---|---|---|---|
| 0. Mechanical | Links and `#page=` anchors resolve, quiz blocks are well formed, exam dates agree everywhere, diagrams and their sources exist, money `$` won't be read as maths, Maths worked-example numbers recompute | a script | `python3 scripts/verify/check.py --build` and `python3 scripts/verify/maths_examples.py` |
| 1. Page review | A reviewer reads one page against its source PDFs and checks every claim | an agent or person | `python3 scripts/verify/ledger.py next` |
| 2. Second review | A different reviewer re-checks the highest-risk pages (worked solutions, quiz answer keys) without seeing the first review | a different agent | same, using `--by` with a different name |

Level 0 must pass (0 errors) before Level 1 results mean anything. Warnings need a look but are not all defects (for example, 📐 marks Maths 2020–24 answers that depend on a diagram and are documented as such).

## Running a page review (Level 1)

1. `python3 scripts/verify/ledger.py next 5` lists the pages to review, highest risk first, with the source PDFs for each. `ledger.py sources <page>` lists the PDFs for one page. `ledger.py status` shows what is verified, stale (edited since checked) or never checked.
2. Get the text of the PDFs. There is no poppler. Compile the Swift tools once: `swiftc -O scripts/xp.swift -o /tmp/xp`, then `/tmp/xp file.pdf` prints each page's text after an `=====PAGE n` marker (matches the viewer's page numbers used in `#page=` links). Some PDFs have no text layer at all (the 2026 timetable prints nothing from `/tmp/xp`), and tables and diagrams lose their layout in text anyway. For those, render the page to an image and look at it (PDFKit via Swift, or Playwright with Chrome), because text extraction loses them.
3. Check the page against the checklist for its type (below). Read the whole page; don't sample.
4. Fix what you can prove from the sources (see "Fixing"). Anything you can't resolve goes in the report, not into the page.
5. Rebuild (`npx vitepress build`), run Level 0 again, then record the result:
   `python3 scripts/verify/ledger.py record <page> --by <your name> --result pass|fixed|issues --notes "what you checked, what changed"`.
   `pass` = nothing wrong, `fixed` = defects found and corrected, `issues` = defects remain (list them in the notes). The ledger stores a hash of the page, so any later edit makes it stale again.

## What to check, by page type

**Worked solutions (`solutions-*.md`)**
- Each question: does the stated question, mark allocation and command word match the question book? Are the marks for each part right?
- Is the answer the same as the marking guide's? Recompute every number yourself (script, not mental arithmetic). Check units, rounding (round only at the end) and the guide's accepted alternatives.
- Do the marking-criteria statements match the guide's wording (for example "draws a valid conclusion", "provides a relevant example")? No invented criteria.
- For years with no guide (Maths 2023) the page must say the working is the author's own. For audio, video or diagram-dependent questions it must not describe content that wasn't checked; it should say what is unverified.
- Quotes from the stimulus or from the guide's sample answers must be verbatim.

**Quizzes (`quiz-*.md`)**
- The question text matches the paper, and the keyed answer matches the guide (read the guide, don't trust the explanation). Check at least that the wrong options are wrong.
- Numeric answers: recompute by script, including the rounding the guide expects.
- The `QCAA <year> Q<n>` tag and the paper and guide links: open the `#page=` target and confirm the question or answer is on that page.
- Explanations agree with the keyed answer and add no new claims. Fill-in answers list every acceptable form (the plugin ignores case and accents).
- Vocabulary and grammar quizzes: translations, genders and conjugations are correct Spanish. No exam-skills quizzes (standing rule).

**Notes, quick reference, overview, checklist (`notes.md`, `quick-reference.md`, `index.md`)**
- Exam format facts (marks, timings, sections, question types, criteria and their weights) match the syllabus and the latest paper and guide. The overview page cites the syllabus page numbers; check them.
- Definitions use the syllabus's own terms. Formulae match the QCAA formula book (Maths); algorithm steps match the guides.
- Anything not in the sources (study advice, mnemonics) is fine but must not contradict them and should not be presented as QCAA's.

**Past-paper analysis and frameworks (`past-papers.md`, `past-prompts.md`, `past-questions.md`)**
- Question wording, years, topics and mark splits match the papers. Statistics (for example "appears in N of M years") must be recounted.
- English quotes from *Othello*: the folder holds no copy of the play, so verify against the student's class text and mark the page "quotes not checked against source" if you can't.

**Diagrams (`scripts/diagrams*.py`, embedded `<Diagram>`)**
- Question-specific diagrams use the paper's real numbers; recompute any derived values (critical paths, minimum cuts, spanning trees).
- Concept diagrams agree with the syllabus. Check legibility in light and dark and at phone width. Fix the Python source, regenerate (`python3 scripts/diagrams.py && python3 scripts/diagram_sources.py`), never hand-edit an SVG.

**Timetable and exam facts (`timetable.md`, `.vitepress/data/exams.ts`)**
- Dates, sessions and perusal against the supporting PDF in the repo root. `check.py` already confirms every page agrees with `exams.ts`; the review confirms `exams.ts` agrees with the PDF.

## Fixing

- Fix only what the sources prove. Quote the source (file and page) in your notes and commit message.
- A fix to a number or answer must be recomputed, and any other place that repeats it (quiz explanation, quick reference, diagram, flashcard) updated too. Search the repo for the old value.
- Don't rewrite style, restructure pages or change navigation during verification.
- If the source is ambiguous or unreadable (garbled extraction, an image-only table), record it as an open issue rather than guessing.

## Severity (use in reports)

- **S1 wrong:** a wrong answer, mark, date, formula or fact. Fix now.
- **S2 misleading:** true but ambiguous, outdated or attributed to the wrong source or page. Fix soon.
- **S3 minor:** wording, formatting, unreachable-anchor precision.

## Reviewing in parallel (agents)

Give each agent exactly one page (or one quiz file) and no more than five at a time. Prompt template:

> Verify `<page>` in `/path/to/repo` against its source PDFs, following `VERIFY.md` ("What to check" for this page type). Sources: `<output of ledger.py sources <page>>`. Compile `/tmp/xp` from `scripts/xp.swift` if missing. Recompute every number by script. Fix only what the sources prove, rebuild, run `python3 scripts/verify/check.py`, then run `ledger.py record` for this page. Reply with: pages checked, defects found (severity, location, source file and page, old → new), anything you could not verify and why, and what you changed.

For Level 2, use a different agent and don't show it the first review's notes.

## Completion

The site is "verified" when `check.py --build` shows 0 errors, `maths_examples.py` passes, and `ledger.py status` shows no `stale` or `never` pages except those you have recorded as `issues` with a reason. Re-run `status` before each exam: edits since the last review show as stale.
