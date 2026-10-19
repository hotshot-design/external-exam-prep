#!/usr/bin/env python3
"""Verification ledger: which pages have been checked against the source PDFs, and which are stale.

  python3 scripts/verify/ledger.py status            # table of every page: verified / stale / never
  python3 scripts/verify/ledger.py next [N]          # the N highest-priority pages to review (default 5), with their source PDFs
  python3 scripts/verify/ledger.py sources <page>    # PDFs (and page hints) to check a page against
  python3 scripts/verify/ledger.py record <page> --by <name> --result pass|fixed|issues --notes "..."
A page goes stale when its text changes after it was recorded (the ledger stores a content hash)."""
import argparse, glob, hashlib, json, os, re, datetime, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
LEDGER = os.path.join(os.path.dirname(__file__), 'ledger.json')
SUBJECTS = ['english', 'spanish', 'business', 'film', 'maths', 'digital-solutions']
# review order: earliest exam first, and the highest-risk page types first
RISK = {'solutions': 0, 'quiz-past-mc': 0, 'quiz-sr': 0, 'quiz-short': 0, 'worked-examples': 1, 'quick-reference': 1, 'past-questions': 1, 'past-prompts': 1, 'past-papers': 2, 'index': 2, 'notes': 3, 'quiz': 3, 'checklist': 9, 'flashcards': 9}
EXAM_ORDER = {s: i for i, s in enumerate(SUBJECTS)}

def pages():
    out = []
    for sub in SUBJECTS:
        for f in sorted(glob.glob(f'{ROOT}/{sub}/*.md')):
            if os.path.basename(f) in ('papers.md',): continue
            out.append(os.path.relpath(f, ROOT))
    out += ['timetable.md', 'strategy.md', 'past-papers.md', 'syllabuses.md', 'index.md']
    return out

def digest(page): return hashlib.sha256(open(f'{ROOT}/{page}', 'rb').read()).hexdigest()[:12]
def load(): return json.load(open(LEDGER)) if os.path.exists(LEDGER) else {}
def risk(page):
    name = os.path.basename(page)[:-3]
    return min((v for k, v in RISK.items() if name.startswith(k)), default=3)

def sources(page):
    """Source PDFs a page must be checked against, derived from its name and subject."""
    parts = page.split('/')
    if len(parts) == 1: return ['2026 Supporting Year 12 Students leading up to and during the External Assessment.pdf'] if page == 'timetable.md' else []
    sub, name = parts[0], parts[1][:-3]
    papers = sorted(glob.glob(f'{ROOT}/{sub}/papers/*.pdf') + glob.glob(f'{ROOT}/{sub}/papers/*.mp3'))
    years = set()
    for m in re.finditer(r'(20\d\d)(?:[-–](\d\d))?', name):
        y = int(m.group(1)); years.add(y)
        if m.group(2): years.add(2000 + int(m.group(2)))
    wanted = [p for p in papers if (not years) or any(f'_{str(y)[2:]}_' in os.path.basename(p) for y in years)]
    if name in ('quiz-past-mc', 'past-papers', 'quick-reference', 'index', 'notes') and not years: wanted = papers
    syll = sorted(glob.glob(f'{ROOT}/{sub}/syllabus/*.pdf'))
    return [os.path.relpath(p, ROOT) for p in wanted + syll]

def status_of(page, led):
    e = led.get(page)
    if not e: return 'never'
    return 'verified' if e['hash'] == digest(page) else 'stale'

def cmd_status(a):
    led = load(); rows = [(p, status_of(p, led)) for p in pages()]
    for p, s in rows: print(f'{s:9} {p}' + (f'   ({led[p]["by"]}, {led[p]["date"]}, {led[p]["result"]})' if p in led else ''))
    n = {k: sum(1 for _, s in rows if s == k) for k in ('verified', 'stale', 'never')}
    print(f'\n{n["verified"]} verified · {n["stale"]} stale · {n["never"]} never checked (of {len(rows)} pages)')

def cmd_next(a):
    led = load()
    todo = [p for p in pages() if status_of(p, led) != 'verified']
    todo.sort(key=lambda p: (risk(p), EXAM_ORDER.get(p.split('/')[0], 99), p))
    for p in todo[:a.n]:
        print(f'\n{p}  [{status_of(p, led)}, risk {risk(p)}]')
        for s in sources(p)[:8]: print(f'    {s}')

def cmd_sources(a):
    for s in sources(a.page): print(s)

def cmd_record(a):
    led = load()
    if not os.path.exists(f'{ROOT}/{a.page}'): sys.exit(f'no such page: {a.page}')
    led[a.page] = {'hash': digest(a.page), 'by': a.by, 'date': datetime.date.today().isoformat(), 'result': a.result, 'notes': a.notes or ''}
    json.dump(led, open(LEDGER, 'w'), indent=1, sort_keys=True); print(f'recorded {a.page}: {a.result}')

ap = argparse.ArgumentParser(); sp = ap.add_subparsers(dest='cmd', required=True)
sp.add_parser('status').set_defaults(f=cmd_status)
n = sp.add_parser('next'); n.add_argument('n', nargs='?', type=int, default=5); n.set_defaults(f=cmd_next)
s = sp.add_parser('sources'); s.add_argument('page'); s.set_defaults(f=cmd_sources)
r = sp.add_parser('record'); r.add_argument('page'); r.add_argument('--by', required=True); r.add_argument('--result', required=True, choices=['pass', 'fixed', 'issues']); r.add_argument('--notes'); r.set_defaults(f=cmd_record)
a = ap.parse_args(); a.f(a)
