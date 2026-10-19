#!/usr/bin/env python3
"""Builds .vitepress/theme/diagrams/sources.json: for each diagram, links to the syllabus page that defines the
concept and to past-paper questions / marking guides that test it (with #page= anchors).
Needs macOS PDFKit via the helper binary /tmp/xp (see scripts/xp.swift: swiftc -O scripts/xp.swift -o /tmp/xp)."""
import json, os, re, subprocess, functools
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
KEY = {'business': 'business', 'digital-solutions': 'digital_solutions', 'maths': 'maths_general', 'film': 'ftvnm', 'english': 'english', 'spanish': 'spanish'}
SYL = {'business': 'business', 'digital-solutions': 'digital_solutions', 'maths': 'maths_general', 'film': 'film_tv', 'english': 'english', 'spanish': 'spanish'}

@functools.lru_cache(None)
def pages(path):
    out = subprocess.run(['/tmp/xp', path], capture_output=True, text=True).stdout
    parts = re.split(r'=====PAGE (\d+)\n', out)
    return {int(parts[i]): parts[i + 1] for i in range(1, len(parts), 2)}

def syl_page(sub, terms):
    path = f'{ROOT}/{sub}/syllabus/snr_{SYL[sub]}_25_syll.pdf'
    pg = pages(path)
    best, score = None, 0
    for k, t in pg.items():
        if k <= 4: continue            # skip cover and contents
        sc = sum(t.lower().count(x.lower()) for x in terms)
        if sc > score: best, score = k, sc
    return best

def paper_file(sub, yy, kind):
    mid = {'maths': {'mc': 'p1_mc_question', 'p1': 'p1_question_response', 'p2': 'p2_question_response'},
           'digital-solutions': {'mc': 'mc_question', 'q': 'question_response'}, 'business': {'q': 'question_response'},
           'film': {'q': 'question'}, 'english': {'q': 'question'}, 'spanish': {'q': 'question_response'}}[sub][kind]
    f = f'snr_{KEY[sub]}_{yy}_ea_{mid}.pdf'
    if not os.path.exists(f'{ROOT}/{sub}/papers/{f}') and sub == 'film': f = f'snr_{KEY[sub]}_{yy}_ea_question_response.pdf'
    return f

def guide_file(sub, yy):
    return f'snr_english_eal_{yy}_ea_mark_guide_pub.pdf' if sub == 'english' else f'snr_{KEY[sub]}_{yy}_ea_mark_guide_pub.pdf'

def find_q(path, n, mc):
    pat = re.compile(r'QUESTION\s+%d\b' % n if mc else r'QUESTION\s+%d\s*\(' % n)
    for k, t in sorted(pages(path).items()):
        if pat.search(t): return k


def _guide_map(pg, first, last_n=30):
    """Sequential page lookup: question n starts on the first page (>= the previous question's page) whose
    text has a line starting 'n •' / 'n word' or 'Sample response n'."""
    keys = sorted(pg); out = {}; cur = keys[0]
    for n in range(first, last_n + 1):
        pat1 = re.compile((r'(?m)^%d[a-z]?\)?[ \t]+(?:•|[^\W\d_]|\d{3,})' if n < 10 else r'(?m)^%d[a-z]?\)?[ \t]+\S') % n); pat2 = re.compile(r'Sample response\s*%d[a-z]?\b' % n)
        hit = next((k for k in keys if k >= cur and (pat1.search(pg[k]) or pat2.search(pg[k]))), None)
        if hit is None: continue
        out[n] = hit; cur = hit
    return out

def find_guide(sub, path, n, mc, paper):
    pg = pages(path); keys = sorted(pg)
    if mc:
        return next((k for k in keys if 'Multiple choice' in pg[k] and re.search(r'\bResponse\b', pg[k])), next((k for k in keys if 'Multiple choice' in pg[k]), None))
    if sub == 'maths':
        p1 = next((k for k in keys if re.search(r'Paper 1:? Short', pg[k])), None); p2 = next((k for k in keys if re.search(r'Paper 2:? Short', pg[k])), None)
        sec = {k: pg[k] for k in keys if (p1 and k >= p1 and (not p2 or k < p2))} if paper == 'p1' else {k: pg[k] for k in keys if p2 and k >= p2}
        return _guide_map(sec, 16 if paper == 'p1' else 1).get(n) if sec else None
    start = next((k for k in keys if 'Short response' in pg[k]), 1)
    sec = {k: pg[k] for k in keys if k >= start}
    return _guide_map(sec, 11 if sub == 'digital-solutions' else 1).get(n)

def ref(sub, year, n, kind='q'):
    yy = str(year)[2:]
    q = paper_file(sub, yy, kind); g = guide_file(sub, yy)
    mc = kind == 'mc'
    out = []
    if os.path.exists(f'{ROOT}/{sub}/papers/{q}'):
        if sub in ('film', 'english', 'spanish') or n is None:
            out.append({'text': f'{year} question paper', 'href': f'/{sub}/papers/{q}'})
        else:
            p = find_q(f'{ROOT}/{sub}/papers/{q}', n, mc)
            tag = {'p1': 'P1 ', 'p2': 'P2 '}.get(kind, '') if sub == 'maths' else ''
            label = f'{year} {tag}Q{n}' if not mc else f'{year} {tag or ""}MC Q{n}'
            out.append({'text': f'{label} (paper{f", p.{p}" if p else ""})', 'href': f'/{sub}/papers/{q}' + (f'#page={p}' if p else '')})
    if os.path.exists(f'{ROOT}/{sub}/papers/{g}'):
        if sub in ('film', 'english', 'spanish') or n is None:
            out.append({'text': f'{year} marking guide', 'href': f'/{sub}/papers/{g}'})
        else:
            p = find_guide(sub, f'{ROOT}/{sub}/papers/{g}', n, mc, 'p2' if kind == 'p2' else 'p1')
            out.append({'text': f'guide{f", p.{p}" if p else ""}', 'href': f'/{sub}/papers/{g}' + (f'#page={p}' if p else '')})
    return out

D = {  # diagram: (subject, syllabus search terms, [(year, question, kind), ...])
 'sol-2025-p2q3-flow': ('maths', None, [(2025, 3, 'p2')]), 'sol-2025-p2q4-road': ('maths', None, [(2025, 4, 'p2')]), 'sol-2025-p2q5-euler': ('maths', None, [(2025, 5, 'p2')]), 'sol-2025-p2q6-hike': ('maths', None, [(2025, 6, 'p2')]),
 'sol-2024-p2q4-bread': ('maths', None, [(2024, 4, 'p2')]), 'sol-2022-p1q21-graph': ('maths', None, [(2022, 21, 'p1')]), 'sol-2022-p2q4-shortest': ('maths', None, [(2022, 4, 'p2')]), 'sol-2022-p2q5-mst': ('maths', None, [(2022, 5, 'p2')]),
 'sol-2021-p1q19-project': ('maths', None, [(2021, 19, 'p1')]), 'sol-2021-p2q2-mst': ('maths', None, [(2021, 2, 'p2')]), 'sol-2020-p1q21-flow': ('maths', None, [(2020, 21, 'p1')]), 'sol-2020-p2q6-tasks': ('maths', None, [(2020, 6, 'p2')]),
 'sol-2024-q14-otp': ('digital-solutions', None, [(2024, 14, 'q')]), 'sol-2025-q16-traffic': ('digital-solutions', None, [(2025, 16, 'q')]), 'sol-2024-q15-nav': ('digital-solutions', None, [(2024, 15, 'q')]), 'sol-2025-q16e-pothole': ('digital-solutions', None, [(2025, 16, 'q')]),
 'sol-2025-swot': ('business', None, [(2025, 4, 'q')]), 'sol-2024-swot': ('business', None, [(2024, 5, 'q')]), 'sol-2024-costbenefit': ('business', None, [(2024, 5, 'q')]),
 'business-kotter': ('business', ['Kotter'], [(2025, 2, 'q'), (2024, 2, 'q'), (2022, 2, 'q')]),
 'business-lewin': ('business', ['Lewin'], [(2023, 1, 'q'), (2020, 3, 'q')]),
 'business-force-field': ('business', ['force field'], [(2025, 3, 'q'), (2022, 5, 'q'), (2021, 4, 'q')]),
 'business-power-interest': ('business', ['stakeholder'], [(2024, 4, 'q'), (2020, 4, 'q')]),
 'business-swot': ('business', ['SWOT'], [(2025, 4, 'q'), (2024, 5, 'q'), (2021, 5, 'q')]),
 'business-life-cycle': ('business', ['Seed', 'Start-up', 'Post-maturity'], []),
 'business-report': ('business', ['business report', 'report'], [(2025, 4, 'q'), (2024, 5, 'q')]),
 'business-criteria': ('business', ['competitiveness', 'stakeholder satisfaction'], [(2025, 4, 'q'), (2024, 5, 'q')]),
 'digital-cia': ('digital-solutions', ['confidentiality', 'integrity'], [(2025, 12, 'q'), (2024, 11, 'q')]),
 'digital-data-exchange': ('digital-solutions', ['data exchange'], [(2025, 13, 'q')]),
 'digital-sym-asym': ('digital-solutions', ['asymmetric', 'symmetric'], [(2025, 1, 'mc'), (2022, 2, 'mc')]),
 'digital-hashing': ('digital-solutions', ['hashing', 'hash'], [(2025, 2, 'mc'), (2021, 1, 'mc')]),
 'digital-caesar': ('digital-solutions', ['Caesar'], [(2023, 5, 'mc'), (2022, 6, 'mc')]),
 'digital-xor': ('digital-solutions', ['one-time pad', 'XOR'], [(2025, 8, 'mc'), (2024, 14, 'q'), (2023, 13, 'q')]),
 'digital-useability': ('digital-solutions', ['useability principles', 'visual communication'], [(2025, 16, 'q'), (2024, 15, 'q')]),
 'digital-dfd-symbols': ('digital-solutions', ['Gane-Sarson', 'data flow diagram'], [(2024, 14, 'q'), (2025, 11, 'q')]),
 'digital-dfd-example': ('digital-solutions', ['data flow diagram', 'data store'], [(2025, 11, 'q'), (2022, 15, 'q')]),
 'maths-scatter-lsl': ('maths', ['least-squares'], [(2025, 24, 'p1'), (2024, 3, 'p2')]),
 'maths-residuals': ('maths', ['residual'], [(2024, 15, 'mc'), (2020, 1, 'mc')]),
 'maths-correlation': ('maths', ['correlation coefficient', 'Pearson'], [(2025, 7, 'mc'), (2020, 2, 'p2')]),
 'maths-time-series': ('maths', ['seasonal index', 'seasonal'], [(2025, 19, 'p1'), (2024, 25, 'p1')]),
 'maths-sequences': ('maths', ['geometric sequence', 'arithmetic sequence'], [(2025, 2, 'p2'), (2024, 6, 'p2')]),
 'maths-earth': ('maths', ['great circle', 'latitude'], [(2025, 18, 'p1'), (2025, 12, 'mc')]),
 'maths-time-zones': ('maths', ['time zone', 'UTC'], [(2025, 16, 'p1'), (2024, 7, 'p2')]),
 'maths-reducing-balance': ('maths', ['reducing balance'], [(2025, 20, 'p1'), (2024, 22, 'p1')]),
 'maths-mst': ('maths', ['spanning tree'], [(2025, 23, 'p1'), (2024, 23, 'p1')]),
 'maths-flow': ('maths', ['flow'], [(2025, 3, 'p2'), (2021, 23, 'p1')]),
 'maths-critical-path': ('maths', ['critical path', 'earliest starting time'], [(2025, 25, 'p1'), (2024, 4, 'p2')]),
 'maths-euler': ('maths', ['Euler'], [(2025, 5, 'p2'), (2024, 17, 'p1')]),
 'maths-hungarian': ('maths', ['Hungarian', 'assignment'], [(2024, 5, 'p2'), (2022, 20, 'p1')]),
 'film-contexts': ('film', ['contexts of production'], [(2025, None, 'q')]),
 'film-marking': ('film', ['external assessment', 'objectives'], [(2025, None, 'q')]),
 'english-relationships': ('english', ['literary text'], [(2025, None, 'q'), (2024, None, 'q')]),
 'english-essay': ('english', ['analytical essay'], [(2025, None, 'q'), (2024, None, 'q')]),
 'spanish-email': ('spanish', ['extended response', 'email'], [(2025, None, 'q'), (2024, None, 'q')]),
 'spanish-subjunctive': ('spanish', ['subjunctive', 'grammar'], [(2025, None, 'q')]),
 'film-five-concepts': ('film', ['key concepts', 'institutions'], [(2025, None, 'q'), (2024, None, 'q')]),
 'film-essay': ('film', ['unseen stimulus', 'analytical essay'], [(2025, None, 'q')]),
 'english-arc': ('english', ['literary text', 'tragedy', 'analytical essay'], [(2025, None, 'q'), (2024, None, 'q')]),
 'english-paragraph': ('english', ['analytical essay', 'essay'], [(2025, None, 'q')]),
 'spanish-tenses': ('spanish', ['tense', 'grammar'], [(2025, None, 'q')]),
 'spanish-exam': ('spanish', ['external assessment', 'Unit 4'], [(2025, None, 'q'), (2024, None, 'q')]),
}
out = {}
for name, (sub, terms, refs) in D.items():
    items = []
    p = syl_page(sub, terms) if terms else None
    if name == 'business-life-cycle': p = 10   # page with the life-cycle stage table
    sylf = f'snr_{SYL[sub]}_25_syll.pdf'
    if terms: items.append({'text': f'Syllabus{f", p.{p}" if p else ""}', 'href': f'/{sub}/syllabus/{sylf}' + (f'#page={p}' if p else '')})
    for y, n, k in refs: items += ref(sub, y, n, k)
    out[name] = items
    print(name, [i['text'] for i in items])
json.dump(out, open(f'{ROOT}/.vitepress/theme/diagrams/sources.json', 'w'), indent=1, ensure_ascii=False)
