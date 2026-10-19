"""Diagrams for maths/worked-examples.md (numbers match the worked examples)."""
import math
from svgkit import SVG
from diagrams_solutions import _node, _edge, _project, _ewt

def _ax(s, x0, y0, w, h, xl, yl):
    s.arrow(x0, y0, x0, y0 - h, 'ar'); s.arrow(x0, y0, x0 + w, y0, 'ar'); s.text(x0 + w, y0 + 18, xl, 't2', size=11); s.text(x0 - 6, y0 - h - 8, yl, 't2', size=11, anchor='start')

def ex1():
    s = SVG('ex-1-lsl', 760, 320)
    s.title(380, 24, "Example 1: least-squares line y = 2x + 20")
    x0, y0, w, h = 60, 275, 430, 220
    _ax(s, x0, y0, w, h, "x", "y")
    X = lambda x: x0 + (x - 4) * 28; Y = lambda y: y0 - (y - 20) * 2.6
    pts = [(6, 33), (8, 35), (9, 39), (11, 41), (12, 45), (13, 44), (14, 50)]
    s.line(X(5), Y(30), X(15), Y(50), 'lnb')
    for x, y in pts: s.circle(X(x), Y(y), 4, 'dot')
    s.circle(X(10), Y(40), 7, 'dotg'); s.text(X(10) + 10, Y(40) + 22, "(x̄, ȳ) = (10, 40)", 'tg', size=12, anchor='start')
    s.text(X(14.5), Y(45), "slope 2: +1 in x, +2 in y", 'tb', size=11, anchor='start')
    s.box(520, 55, 225, 200, '', 'box', rx=8)
    for i, (t, c) in enumerate([("r = 0.8, sₓ = 2, s_y = 5", 't'), ("m = r × s_y ÷ sₓ = 2", 'tb'), ("c = ȳ − m·x̄ = 40 − 20 = 20", 'tb'), ("y = 2x + 20", 'tg'), ("R² = 0.8² = 0.64", 't'), ("64% of the variation in y", 't2'), ("is explained by x", 't2')]):
        s.text(535, 82 + i * 26, t, c, anchor='start', size=12)
    s.text(380, 308, "The line always passes through the point of means (x̄, ȳ). Dots are illustrative.", 't2', size=11)
    return s.render("Scatterplot with the least-squares line through the point of means"), ""

def ex2():
    s = SVG('ex-2-moving', 760, 320)
    s.title(380, 24, "Example 2: 3-point moving average")
    data = [12, 15, 14, 18, 20, 19, 23]
    sm = [(data[i - 1] + data[i] + data[i + 1]) / 3 for i in range(1, 6)]
    x0, y0, w, h = 60, 270, 440, 210
    _ax(s, x0, y0, w, h, "time", "value")
    X = lambda i: x0 + 35 + i * 62; Y = lambda v: y0 - (v - 8) * 12
    s.poly([(X(i), Y(v)) for i, v in enumerate(data)], 'lnl')
    for i, v in enumerate(data):
        s.circle(X(i), Y(v), 5, 'dot')
        below = 0 < i < 6 and v < sm[i - 1]
        s.text(X(i) - 12, Y(v) + (18 if below else -10), str(v), 't2', size=11)
    s.poly([(X(i + 1), Y(v)) for i, v in enumerate(sm)], 'lng')
    for i, v in enumerate(sm): s.circle(X(i + 1), Y(v), 5, 'dotg'); s.text(X(i + 1) + 14, Y(v) - 10 if data[i + 1] < v else Y(v) + 18, f"{v:.1f}", 'tg', size=11)
    s.box(520, 55, 225, 175, '', 'box', rx=8)
    s.text(535, 80, "Smoothed value i =", 't', anchor='start', size=12); s.text(535, 100, "mean of values i−1, i, i+1", 't', anchor='start', size=12)
    s.text(535, 130, "(12 + 15 + 14) ÷ 3 = 13.7", 'tg', anchor='start', size=12); s.text(535, 150, "(15 + 14 + 18) ÷ 3 = 15.7", 'tg', anchor='start', size=12)
    s.text(535, 180, "first and last points", 't2', anchor='start', size=12); s.text(535, 198, "have no smoothed value", 't2', anchor='start', size=12)
    s.text(380, 308, "Grey line: data. Green line: smoothed series.", 't2', size=11)
    return s.render("Data points with the 3-point moving average line"), ""

def ex3():
    s = SVG('ex-3-seasonal', 760, 340)
    s.title(380, 24, "Example 3: seasonal index and deseasonalising")
    y1 = [40, 60, 80, 20]; y2 = [44, 66, 88, 22]
    x0, y0 = 60, 260
    _ax(s, x0, y0, 400, 210, "quarter", "sales")
    for q in range(4):
        bx = x0 + 30 + q * 95
        s.box(bx, y0 - y1[q] * 2.2, 36, y1[q] * 2.2, '', 'boxb', rx=2); s.box(bx + 38, y0 - y2[q] * 2.2, 36, y2[q] * 2.2, '', 'boxg', rx=2)
        s.text(bx + 18, y0 - y1[q] * 2.2 - 6, str(y1[q]), 't2', size=10); s.text(bx + 56, y0 - y2[q] * 2.2 - 6, str(y2[q]), 't2', size=10)
        s.text(bx + 37, y0 + 16, f"Q{q+1}", 't', size=12)
    s.box(75, 295, 12, 12, '', 'boxb', rx=2); s.text(92, 305, "Year 1 (average 50)", 't2', anchor='start', size=11); s.box(235, 295, 12, 12, '', 'boxg', rx=2); s.text(252, 305, "Year 2 (average 55)", 't2', anchor='start', size=11)
    s.box(490, 55, 255, 215, '', 'box', rx=8)
    for i, (t, c) in enumerate([("Value ÷ year average", 'tb'), ("Q1: 40÷50 = 0.8 · 44÷55 = 0.8", 't'), ("Q2: 1.2 · Q3: 1.6 · Q4: 0.4", 't'), ("Seasonal indices (sum = 4):", 'tb'), ("0.80  1.20  1.60  0.40", 'tg'), ("Deseasonalise Year 2 Q3:", 'tb'), ("88 ÷ 1.60 = 55", 'tg')]):
        s.text(503, 82 + i * 28, t, c, anchor='start', size=12)
    return s.render("Bar chart of two years of quarterly sales with seasonal indices"), ""

def ex4():
    s = SVG('ex-4-depreciation', 760, 330)
    s.title(380, 24, "Example 4: diminishing-value depreciation, $10 000 at 15% a year")
    x0, y0, w, h = 70, 275, 420, 215
    _ax(s, x0, y0, w, h, "years n", "value ($)")
    X = lambda n: x0 + 20 + n * 62; Y = lambda v: y0 - v / 10000 * 195
    vals = [10000 * 0.85 ** n for n in range(6)]
    s.poly([(X(n), Y(v)) for n, v in enumerate(vals)], 'lnr')
    for n, v in enumerate(vals):
        s.circle(X(n), Y(v), 5, 'dotr'); s.text(X(n) + 6, Y(v) - 10, f"{v:,.2f}".replace(',', ' '), 't2', size=10, anchor='start'); s.text(X(n), y0 + 16, str(n), 't2', size=11)
    s.circle(X(3), Y(vals[3]), 8, 'dotg')
    s.box(520, 55, 225, 190, '', 'box', rx=8)
    for i, (t, c) in enumerate([("Geometric decay", 'tr'), ("t₁ = 10 000, r = 0.85", 't'), ("value = 10 000 × 0.85ⁿ", 'tb'), ("n = 3: 10 000 × 0.85³", 't'), (f"= ${vals[3]:,.2f}".replace(',', ' '), 'tg'), ("r < 1 means decay", 't2')]):
        s.text(535, 82 + i * 28, t, c, anchor='start', size=13)
    s.text(380, 312, "Arithmetic example: t₁ = 12, d = 5 → t₂₀ = 12 + 19 × 5 = 107. Geometric: t₁ = 3, r = 2 → t₆ = 3 × 2⁵ = 96.", 't2', size=11)
    return s.render("Declining curve of a $10 000 asset losing 15% of its value each year"), ""

def ex6():
    s = SVG('ex-6-compound', 760, 320)
    s.title(380, 24, "Example 6: $5 000 at 6% p.a. compounded monthly for 3 years")
    x0, y0, w, h = 70, 270, 420, 210
    _ax(s, x0, y0, w, h, "months", "balance ($)")
    X = lambda n: x0 + 15 + n * 11; Y = lambda v: y0 - (v - 4800) / 1300 * 190
    pts = [(X(n), Y(5000 * 1.005 ** n)) for n in range(0, 37)]
    s.poly(pts, 'lnb'); s.circle(*pts[0], 5, 'dot'); s.circle(*pts[-1], 6, 'dotg')
    s.text(pts[0][0] + 12, pts[0][1] - 8, "$5 000", 't2', size=11, anchor='start'); s.text(pts[-1][0] - 6, pts[-1][1] - 12, "$5 983.40", 'tg', size=12, anchor='end')
    s.box(520, 55, 225, 195, '', 'box', rx=8)
    for i, (t, c) in enumerate([("i = 0.06 ÷ 12 = 0.005", 't'), ("n = 3 × 12 = 36", 't'), ("A = 5000 × 1.005³⁶", 'tb'), ("= $5 983.40", 'tg'), ("interest = $983.40", 't'), ("EAR = 1.005¹² − 1", 'tb'), ("= 6.17%", 'tg')]):
        s.text(535, 80 + i * 26, t, c, anchor='start', size=13)
    s.text(380, 305, "Interest is earned on interest already added, so the line curves slightly upward.", 't2', size=11)
    return s.render("Growth curve of a compound-interest investment"), ""

def ex7():
    s = SVG('ex-7-loan', 760, 320)
    s.title(380, 24, "Example 7: $20 000 loan, 7.2% p.a., monthly over 5 years")
    i = 0.072 / 12; d = 20000 * i / (1 - (1 + i) ** -60)
    bal = [20000]
    for _ in range(60): bal.append(bal[-1] * (1 + i) - d)
    x0, y0, w, h = 70, 270, 420, 210
    _ax(s, x0, y0, w, h, "months", "balance ($)")
    pts = [(x0 + 15 + n * 6.4, y0 - 10 - max(b, 0) / 20000 * 190) for n, b in enumerate(bal)]
    s.poly(pts, 'lnb'); s.circle(*pts[0], 5, 'dot'); s.circle(*pts[-1], 5, 'dotg')
    s.text(pts[0][0] + 12, pts[0][1] + 16, "$20 000", 't2', size=11, anchor='start'); s.text(pts[-1][0], pts[-1][1] - 12, "≈ $0", 'tg', size=12)
    s.box(520, 55, 225, 195, '', 'box', rx=8)
    for k, (t, c) in enumerate([("i = 0.006, n = 60", 't'), ("d = P·i ÷ (1 − (1+i)⁻ⁿ)", 'tb'), (f"≈ ${d:,.2f} per month", 'tg'), (f"repaid ≈ ${d*60:,.2f}", 't'), (f"interest ≈ ${d*60-20000:,.2f}", 't'), ("(from the unrounded payment)", 't2')]):
        s.text(535, 82 + k * 28, t, c, anchor='start', size=13)
    s.text(380, 305, "Each month the interest is added, then the repayment is taken off.", 't2', size=11)
    return s.render("Loan balance falling to zero over sixty months"), ""

def ex8():
    s = SVG('ex-8-annuity', 760, 320)
    s.title(380, 24, "Example 8: $200 a month at 4.8% p.a. for 10 years")
    i = 0.004; fv = [0]
    for _ in range(120): fv.append(fv[-1] * (1 + i) + 200)
    x0, y0, w, h = 70, 270, 420, 210
    _ax(s, x0, y0, w, h, "months", "balance ($)")
    X = lambda n: x0 + 15 + n * 3.3; Y = lambda v: y0 - v / 31000 * 195
    s.poly([(X(n), Y(200 * n)) for n in (0, 120)], 'ln'); s.text(X(120) - 10, Y(24000) + 22, "deposits only: $24 000", 't', size=11, anchor='end')
    s.poly([(X(n), Y(v)) for n, v in enumerate(fv)], 'lng'); s.circle(X(120), Y(fv[-1]), 6, 'dotg')
    s.text(X(120) - 8, Y(fv[-1]) - 12, f"${fv[-1]:,.2f}".replace(',', ' '), 'tg', size=12, anchor='end')
    s.box(520, 55, 225, 195, '', 'box', rx=8)
    for k, (t, c) in enumerate([("i = 0.004, n = 120", 't'), ("A = d × ((1+i)ⁿ − 1) ÷ i", 'tb'), (f"≈ ${fv[-1]:,.2f}".replace(',', ' '), 'tg'), ("deposits 200 × 120 = $24 000", 't'), (f"interest ≈ ${fv[-1]-24000:,.2f}".replace(',', ' '), 'tg')]):
        s.text(535, 82 + k * 30, t, c, anchor='start', size=13)
    s.text(380, 305, "Savings annuity: each deposit earns interest from the day it is made.", 't2', size=11)
    return s.render("Savings balance growing above the straight line of deposits"), ""

def ex9():
    s = SVG('ex-9-perpetuity', 760, 270)
    s.title(380, 24, "Example 9: perpetuity, $500 a quarter at 4% p.a. (quarterly)")
    s.box(40, 95, 200, 80, "Principal\n$50 000", 'boxb', size=16, weight=700)
    s.box(330, 95, 190, 80, "Interest each quarter\n1% × 50 000 = $500", 'boxy', size=13)
    s.box(600, 95, 140, 80, "Payment\n$500", 'boxg', size=15, weight=700)
    s.arrow(240, 135, 330, 135, 'arb'); s.arrow(520, 135, 600, 135, 'arg')
    s.path("M 140 95 C 140 50 230 50 330 95", 'ar', arrow=True) if False else None
    s.text(380, 215, "The payment is only the interest, so the principal never shrinks and the payments continue forever.", 't', size=12)
    s.text(380, 237, "A = d ÷ i = 500 ÷ 0.01 = $50 000      (i = 0.04 ÷ 4 = 0.01 per quarter)", 'tb', size=13)
    return s.render("Principal earns interest which is paid out, leaving the principal unchanged"), ""

def ex10():
    s = SVG('ex-10-wheel', 760, 330)
    s.title(380, 24, "Example 10: planar graph with v = 6, e = 10, so f = 6")
    c = (200, 175); R = 105
    P = {'H': c}
    for k in range(5):
        a = math.radians(-90 + 72 * k); P[str(k + 1)] = (c[0] + R * math.cos(a), c[1] + R * math.sin(a))
    for k in range(5): _edge(s, str(k + 1), str((k + 1) % 5 + 1), P)
    for k in range(5): _edge(s, 'H', str(k + 1), P)
    for k, (x, y) in P.items(): _node(s, x, y, k, 'nodeb' if k == 'H' else 'node', r=14, size=12)
    s.box(380, 55, 365, 240, '', 'boxb', rx=8)
    for i, (t, cl) in enumerate([("v + f − e = 2", 'tb'), ("f = 2 + e − v = 2 + 10 − 6 = 6", 't'), ("5 triangles + the outside = 6 faces", 't2'), ("", 't'), ("Eulerian circuit: connected and every", 't'), ("vertex has an even degree", 't'), ("Eulerian trail: exactly two odd vertices", 't'), ("(this wheel has none, so neither exists)", 't2')]):
        s.text(395, 85 + i * 26, t, cl, anchor='start', size=13)
    return s.render("Wheel graph with six vertices, ten edges and six faces"), ""

def ex11():
    s = SVG('ex-11-critical', 760, 360)
    s.title(380, 24, "Example 11: critical path analysis")
    acts = {'A': (3, 0, 0, 40, 140), 'B': (4, 3, 3, 190, 70), 'C': (2, 3, 5, 190, 210), 'D': (5, 7, 7, 350, 140), 'E': (3, 12, 12, 510, 140)}
    _project(s, acts, [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('D', 'E')], crit=set('ABDE'))
    s.text(380, 315, "Path A→B→D→E = 3 + 4 + 5 + 3 = 15 (critical) · path A→C→D→E = 13", 't', size=13)
    s.text(380, 338, "Float for C = 15 − 13 = 2 (also LST − EST = 5 − 3).", 't2', size=12)
    return s.render("Activity network with earliest and latest start times and the critical path"), ""

def ex13():
    s = SVG('ex-13-hungarian', 760, 360)
    s.title(380, 24, "Example 13: Hungarian algorithm, minimum cost")
    mats = [("Original costs", [[9, 2, 7], [6, 4, 3], [5, 8, 1]], None), ("After row reduction", [[7, 0, 5], [3, 1, 0], [4, 7, 0]], None), ("After column reduction", [[4, 0, 5], [0, 1, 0], [1, 7, 0]], {(0, 1), (1, 0), (2, 2)})]
    for m, (t, M, hl) in enumerate(mats):
        x = 25 + m * 245
        s.text(x + 105, 58, t, 'tb', size=13)
        for r in range(3):
            for c in range(3):
                cls = 'boxg' if hl and (r, c) in hl else 'box'
                s.box(x + c * 70, 70 + r * 50, 64, 44, str(M[r][c]), cls, size=15, rx=6)
        if m < 2: s.arrow(x + 214, 140, x + 240, 140)
    for r, t in enumerate(["W1", "W2", "W3"]): s.text(16, 98 + r * 50, t, 't2', size=11, anchor='start')
    s.text(380, 250, "Cover the zeros with the fewest lines: 3 lines = n, so assign using the zeros.", 't', size=13)
    s.text(380, 275, "W1 → J2 (2) · W2 → J1 (6) · W3 → J3 (1)   →   minimum total cost = 9", 'tg', size=14)
    s.text(380, 305, "Row minima 2, 3, 1 are subtracted first; then column 1's minimum (3). Use ORIGINAL costs for the total.", 't2', size=11)
    s.text(380, 325, "Maximum problem: subtract every entry from the largest first.", 't2', size=11)
    return s.render("Cost matrix before and after row and column reduction with the assignment highlighted"), ""

def ex14():
    s = SVG('ex-14-flight', 760, 300)
    s.title(380, 24, "Example 14: flight Sydney (UTC+10) to Los Angeles (UTC−8)")
    x0, x1, y = 60, 700, 120
    s.arrow(x0, y, x1, y, 'ar')
    def X(h): return x0 + h / 15 * (x1 - x0 - 40)
    for h, t in [(0, "9:50 pm Tue"), (6, "3:50 am Wed"), (15, "12:50 pm Wed")]:
        s.circle(X(h), y, 7, 'dotg' if h == 6 else 'dot'); s.text(X(h), y - 20, t, 'tg' if h == 6 else 't', size=13, weight=600)
    s.text(X(0), y + 24, "depart Sydney", 't2', size=11); s.text(X(15), y + 24, "arrive (Sydney time)", 't2', size=11); s.text(X(6), y + 24, "4828 km flown", 'tg', size=11)
    s.line(X(0), y + 50, X(15), y + 50, 'lnb'); s.text((X(0) + X(15)) / 2, y + 70, "15 h in the air", 'tb', size=13)
    s.text(380, 215, "LA arrival 6:50 pm Tue + 18 h (UTC+10 − (−8)) = 12:50 pm Wed Sydney time", 't', size=13)
    s.text(380, 240, "Fraction flown 4828 ÷ 12 070 = 0.4 → 0.4 × 15 h = 6 h → 9:50 pm Tue + 6 h = 3:50 am Wed", 't', size=13)
    s.text(380, 275, "Convert time zones first, then use the fraction of the total distance.", 't2', size=12)
    return s.render("Timeline of the flight showing departure, the 4828 km point and arrival in Sydney time"), ""

def ex16():
    s = SVG('ex-16-adjacency', 760, 300)
    s.title(380, 24, "Example 16: adjacency matrix and Eulerian trail")
    P = {'A': (90, 90), 'B': (90, 220), 'C': (230, 155), 'D': (370, 155)}
    for a, b in [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'D')]: _edge(s, a, b, P, hl=True)
    for k, (x, y) in P.items(): _node(s, x, y, k, 'nodeb' if k in 'CD' else 'node')
    s.text(300, 245, "C–A–B–C–D uses every edge once", 'tg', size=12)
    s.text(430, 62, "Adjacency matrix", 'tb', size=13, anchor='start')
    M = [[0, 1, 1, 0], [1, 0, 1, 0], [1, 1, 0, 1], [0, 0, 1, 0]]
    for r in range(4):
        s.text(450, 100 + r * 38, "ABCD"[r], 't2', size=12)
        s.text(488 + r * 44, 78, "ABCD"[r], 't2', size=12)
        for c in range(4): s.box(466 + c * 44, 82 + r * 38, 40, 32, str(M[r][c]), 'boxg' if M[r][c] else 'box', size=14, rx=4)
    s.text(430, 262, "Degrees A 2, B 2, C 3, D 1.", 't', size=12, anchor='start'); s.text(430, 282, "Odd vertices C, D → Eulerian trail C to D.", 't', size=12, anchor='start')
    return s.render("Four-vertex graph with its adjacency matrix and an Eulerian trail"), ""

ALL = {'ex-1-lsl': ex1, 'ex-2-moving': ex2, 'ex-3-seasonal': ex3, 'ex-4-depreciation': ex4, 'ex-6-compound': ex6, 'ex-7-loan': ex7, 'ex-8-annuity': ex8, 'ex-9-perpetuity': ex9,
       'ex-10-wheel': ex10, 'ex-11-critical': ex11, 'ex-13-hungarian': ex13, 'ex-14-flight': ex14, 'ex-16-adjacency': ex16}
