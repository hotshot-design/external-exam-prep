#!/usr/bin/env python3
"""Automated accuracy checks for the study site. Run from anywhere:  python3 scripts/verify/check.py [--build] [--json]

Mechanical checks only (things a script can prove). Judgement checks against the PDFs are in VERIFY.md.
Exit code 1 if any ERROR is found; WARN items need a human or agent look.
Needs macOS + swiftc for the PDF page counts (compiled automatically to /tmp/xp)."""
import re, subprocess, sys, os, json, datetime, functools, glob

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
SUBJECTS = ['english', 'spanish', 'business', 'film', 'maths', 'digital-solutions']
issues = []

def add(level, where, msg): issues.append((level, where, msg))
def md_files(): return [f for f in glob.glob(f'{ROOT}/**/*.md', recursive=True) if '/node_modules/' not in f and '/.vitepress/' not in f and not f.endswith(('AGENTS.md', 'VERIFY.md', 'README.md', 'SUBJECTS.md'))]
def rel(f): return os.path.relpath(f, ROOT)

# ---- PDF page counts -----------------------------------------------------------------------
XP = '/tmp/xp'
def ensure_xp():
    if not os.path.exists(XP): subprocess.run(['swiftc', '-O', f'{ROOT}/scripts/xp.swift', '-o', XP], check=True)

@functools.lru_cache(None)
def pdf_pages(path):
    out = subprocess.run([XP, path], capture_output=True, text=True).stdout
    return len(re.findall(r'^=====PAGE \d+$', out, re.M))

# ---- 1. links: files exist, #page anchors are in range --------------------------------------
def check_links():
    pat = re.compile(r'\]\((/[^)\s]+?\.(?:pdf|mp3))(?:#page=(\d+))?\)')
    for f in md_files():
        for m in pat.finditer(open(f).read()):
            path, page = m.group(1), m.group(2)
            full = ROOT + path
            if not os.path.exists(full): add('ERROR', rel(f), f'linked file missing: {path}'); continue
            if page and path.endswith('.pdf'):
                n = pdf_pages(full)
                if int(page) > n or int(page) < 1: add('ERROR', rel(f), f'{path}#page={page} but the PDF has {n} pages')
    # the visible "p.N" must equal the #page=N it links to
    for f in md_files():
        for m in re.finditer(r'\[[^\]]*?, p\.(\d+)\]\([^)#]+\.pdf#page=(\d+)\)', open(f).read()):
            if m.group(1) != m.group(2): add('ERROR', rel(f), f'link text says p.{m.group(1)} but opens #page={m.group(2)}')


# ---- 2. quiz structure ----------------------------------------------------------------------
def check_quizzes():
    for f in md_files():
        t = open(f).read()
        if ':::quiz' not in t: continue
        opens = len(re.findall(r'^:::quiz', t, re.M)); closes = len(re.findall(r'^:::\s*$', t, re.M))
        other = len(re.findall(r'^:::\s*(?:tip|warning|info|danger|details)', t, re.M))
        if opens != closes - 0 and closes < opens: add('ERROR', rel(f), f'{opens} :::quiz blocks but only {closes} closing ::: lines (unclosed block breaks the page)')
        for i, b in enumerate(re.findall(r'^:::quiz\n(.*?)^:::\s*$', t, re.M | re.S), 1):
            q = re.search(r'^question:\s*(.+)$', b, re.M); name = (q.group(1)[:60] if q else f'block {i}')
            if not q: add('ERROR', rel(f), f'block {i}: no question:')
            has_ans = re.search(r'^(answer-correct|answer-input|pair):', b, re.M)
            if not has_ans: add('ERROR', rel(f), f'"{name}": no answer-correct / answer-input / pair line')
            if re.search(r'^answer:', b, re.M) and not re.search(r'^answer-correct:', b, re.M): add('ERROR', rel(f), f'"{name}": has answer: options but no answer-correct:')
            if not re.search(r'^explanation:', b, re.M) and not re.search(r'^pair:', b, re.M): add('WARN', rel(f), f'"{name}": no explanation:')
            if re.search(r'^answer-correct:\s*$', b, re.M): add('ERROR', rel(f), f'"{name}": empty answer-correct')
        # duplicate questions
        qs = re.findall(r'^question:\s*(.+)$', t, re.M)
        for d in {x for x in qs if qs.count(x) > 1 and not re.search(r'match', x)}: add('WARN', rel(f), f'duplicate question text: "{d[:60]}"')


# ---- 2b. "QCAA <year> Q<n>" links land on the right page of the paper and the guide --------------
@functools.lru_cache(None)
def pdf_text_pages(path):
    out = subprocess.run([XP, path], capture_output=True, text=True).stdout
    parts = re.split(r'=====PAGE (\d+)\n', out)
    return {int(parts[i]): parts[i + 1] for i in range(1, len(parts), 2)}

def check_question_anchors():
    paper = re.compile(r'QCAA (20\d\d) ((?:P[12] )?)Q(\d+) \u2014 \[Question paper, p\.(\d+)\]\((/[^)#]+)#page=\d+\)')
    guide = re.compile(r'QCAA (20\d\d) ((?:P[12] )?)Q(\d+) \u2014 \[[^\]]*\]\([^)]*\) \u00b7 \[Marking guide, p\.(\d+)\]\((/[^)#]+)#page=\d+\)')
    for f in md_files():
        t = open(f).read()
        for m in paper.finditer(t):
            y, pp, q, pg, path = m.groups(); q, pg = int(q), int(pg)
            txt = pdf_text_pages(ROOT + path).get(pg, '')
            if not txt.strip(): continue  # image-only page: cannot check by text
            if not (re.search(r'QUESTION\s+%d\b' % q, txt, re.I) or re.search(r'(?m)^%d[ab]?\s*$' % q, txt)):
                add('ERROR', rel(f), f'QCAA {y} {pp}Q{q}: question paper p.{pg} does not contain that question')
        for m in guide.finditer(t):
            y, pp, q, pg, path = m.groups(); q, pg = int(q), int(pg)
            txt = pdf_text_pages(ROOT + path).get(pg, '')
            if not txt.strip(): continue
            if not (re.search(r'(?m)^(Q\s)?%d[a-z]?\)?[ \t]' % q, txt) or re.search(r'Sample response\s*%d\b' % q, txt) or re.search(r'(?m)^%d$' % q, txt)):
                add('WARN', rel(f), f'QCAA {y} {pp}Q{q}: marking guide p.{pg} may not contain that question (check by eye)')

# ---- 3. exam dates and sessions agree everywhere -------------------------------------------
def check_exam_facts():
    ts = open(f'{ROOT}/.vitepress/data/exams.ts').read()
    exams = re.findall(r"id: '(\w+)', subject: '([^']+)', slug: '([^']+)', date: '([\d-]+)', session: '(AM|PM)', duration: '(\w+)', perusal: '(\w+)'", ts)
    tt = open(f'{ROOT}/timetable.md').read()
    for id_, subj, slug, date, sess, dur, per in exams:
        d = datetime.date.fromisoformat(date); label = f'{d.strftime("%a")} {d.day} {d.strftime("%b")}'
        row = next((l for l in tt.splitlines() if l.startswith('|') and subj.split(' (')[0].split(' –')[0] in l and ('Paper' not in subj or subj[-1] in l)), None)
        if not row: add('ERROR', 'timetable.md', f'no row for {subj}'); continue
        if label not in row: add('ERROR', 'timetable.md', f'{subj}: expected date "{label}" in "{row[:60]}"')
        if f'| {sess} |' not in row: add('ERROR', 'timetable.md', f'{subj}: expected session {sess}')
        if (per.replace('m', ' min')) not in row: add('ERROR', 'timetable.md', f'{subj}: expected perusal {per}')
    for sub in SUBJECTS:
        idx = open(f'{ROOT}/{sub}/index.md').read()
        for id_, subj, slug, date, sess, *_ in exams:
            if slug != sub: continue
            d = datetime.date.fromisoformat(date); label = f'{d.strftime("%a")} {d.day} {d.strftime("%b")}'
            if label not in idx: add('ERROR', f'{sub}/index.md', f'exam date "{label}" not found on the overview page')

# ---- 4. every "QCAA <year>" reference has a paper behind it ---------------------------------
def check_year_refs():
    for f in md_files():
        sub = rel(f).split('/')[0]
        if sub not in SUBJECTS: continue
        for m in set(re.findall(r'QCAA (20\d\d)', open(f).read())):
            yy = m[2:]
            if not glob.glob(f'{ROOT}/{sub}/papers/snr_*_{yy}_ea_*'): add('WARN', rel(f), f'cites QCAA {m} but no {m} papers are in {sub}/papers/')

# ---- 5. generated assets in sync ------------------------------------------------------------
def check_diagrams():
    names = set(re.findall(r'<Diagram name="([^"]+)"', ''.join(open(f).read() for f in md_files())))
    for n in sorted(names):
        if not os.path.exists(f'{ROOT}/.vitepress/theme/diagrams/{n}.svg'): add('ERROR', 'diagrams', f'<Diagram name="{n}"> has no SVG')
    src = json.load(open(f'{ROOT}/.vitepress/theme/diagrams/sources.json'))
    for n in sorted(names):
        if n not in src: add('WARN', 'diagrams', f'{n}: no Sources entry (add to scripts/diagram_sources.py)')
        else:
            for it in src[n]:
                p = ROOT + it['href'].split('#')[0]
                if not os.path.exists(p): add('ERROR', 'diagrams', f'{n}: source link missing {it["href"]}')
    gallery = set(re.findall(r'<Diagram name="([^"]+)"', open(f'{ROOT}/diagrams.md').read()))
    for n in sorted(set(os.path.splitext(f)[0] for f in os.listdir(f'{ROOT}/.vitepress/theme/diagrams') if f.endswith('.svg')) - gallery): add('WARN', 'diagrams.md', f'{n}.svg is not in the gallery')

# ---- 6. page hygiene ------------------------------------------------------------------------
def check_pages():
    for f in md_files():
        t = re.sub(r'^:::quiz\n.*?^:::\s*$', lambda m: '\n' * m.group(0).count('\n'), open(f).read(), flags=re.M | re.S)  # quiz text is not maths-rendered
        if re.search(r'\bTODO\b|\bFIXME\b|\?\?\?', t): add('WARN', rel(f), 'contains TODO/FIXME/???')
        if '📐' in t and 'solutions-2023' not in f: add('WARN', rel(f), 'contains 📐 (diagram-dependent answer not verified)')
        # money with an unescaped $ followed by digit inside prose is ok only when $ is escaped
        for i, l in enumerate(t.splitlines(), 1):
            if l.startswith(('|', ':::', '#')) or '`' in l or '<' in l: continue
            for m in re.finditer(r'(?<!\\)\$(?=\S)([^$]*?\S)(?<!\\)\$(?!\d)', l):  # pandoc rule: closer not after space or before a digit
                inner = m.group(1)
                if len(re.findall(r'[A-Za-z]{3,}', inner)) >= 3 and '\\' not in inner: add('WARN', f'{rel(f)}:{i}', f'money $ may be read as maths: "${inner[:40]}..." (escape as \\$)')


# ---- 7. in-page anchors (#...) point at a heading that exists in the built site ---------------
def check_anchors():
    import html, urllib.parse
    dist = f'{ROOT}/.vitepress/dist'
    if not os.path.isdir(dist): add('WARN', 'anchors', 'no build found; run with --build to check #anchors'); return
    ids = {}
    def ids_of(page):
        if page not in ids:
            f = f'{dist}/{page}.html' if not page.endswith('/') else f'{dist}/{page}index.html'
            ids[page] = set(html.unescape(i) for i in re.findall(r'id="([^"]+)"', open(f).read())) if os.path.exists(f) else None
        return ids[page]
    for f in md_files():
        here = '/' + rel(f)[:-3]
        for m in re.finditer(r'\]\((/[^)#\s]*)?#([^)\s]+)\)', open(f).read()):
            target = (m.group(1) or here).rstrip('/') or '/index'
            if target.endswith('.pdf') or target.endswith('.mp3'): continue
            page = target.lstrip('/') or 'index'
            if page.endswith('.html'): page = page[:-5]
            found = ids_of(page) if os.path.exists(f'{dist}/{page}.html') else ids_of(page + '/')
            frag = urllib.parse.unquote(m.group(2))
            if found is not None and frag not in found:
                add('ERROR', rel(f), f'anchor #{frag} not found on {target}')

def main():
    if '--build' in sys.argv:
        r = subprocess.run(['npx', 'vitepress', 'build'], cwd=ROOT, capture_output=True, text=True)
        if r.returncode != 0 or 'build complete' not in r.stdout: add('ERROR', 'build', (r.stdout + r.stderr)[-400:])
    ensure_xp()
    for fn in (check_links, check_question_anchors, check_quizzes, check_exam_facts, check_year_refs, check_diagrams, check_pages, check_anchors): fn()
    if '--json' in sys.argv: print(json.dumps(issues, indent=1))
    else:
        for lvl in ('ERROR', 'WARN'):
            rows = [i for i in issues if i[0] == lvl]
            print(f'\n== {lvl} ({len(rows)})')
            for _, w, m in rows: print(f'  {w}: {m}')
        print(f'\n{sum(1 for i in issues if i[0]=="ERROR")} errors, {sum(1 for i in issues if i[0]=="WARN")} warnings')
    sys.exit(1 if any(i[0] == 'ERROR' for i in issues) else 0)

if __name__ == '__main__': main()
