import math, itertools
from svgkit import SVG

def earth():
    s = SVG('earth', 760, 352)
    s.title(380, 26, "Earth geometry: latitude, longitude and distance")
    cx, cy, r = 170, 185, 120
    s.circle(cx, cy, r, 'box')
    s.line(cx - r, cy, cx + r, cy, 'ln'); s.text(cx + r + 6, cy + 4, "equator", 't2', anchor='start', size=11)
    s.text(cx, cy - r - 10, "N", 't2'); s.text(cx, cy + r + 17, "S", 't2')
    for lat, lab in [(-27, "27° S"), (-37, "37° S")]:
        a = math.radians(-lat)  # south = below equator
        x, y = cx + r * math.cos(a), cy + r * math.sin(a)
        s.line(cx, cy, x, y, 'lnb'); s.circle(x, y, 5, 'dot'); s.text(x + 8, y + (4 if lat == -27 else 16), lab, 'tb', anchor='start', size=12)
    s.path(f"M {cx+60} {cy} A 60 60 0 0 1 {cx+60*math.cos(math.radians(27))} {cy+60*math.sin(math.radians(27))}", 'lng')
    s.path(f"M {cx+90*math.cos(math.radians(27))} {cy+90*math.sin(math.radians(27))} A 90 90 0 0 1 {cx+90*math.cos(math.radians(37))} {cy+90*math.sin(math.radians(37))}", 'lnr')
    s.text(cx + 40, cy + 70, "10°", 'tr', size=13); s.text(cx + 68, cy + 22, "27°", 'tg', size=12)
    s.text(170, 344, "side view along one meridian", 't2', size=11)
    s.box(360, 55, 370, 80, '', 'boxb'); s.text(545, 78, "Same meridian (north–south)", 'tb', size=14)
    s.text(545, 104, "D = 111.2 × angular distance", 't', size=14); s.text(545, 124, "27° S to 37° S: 10° → 1112 km", 't2', size=12)
    s.box(360, 145, 370, 80, '', 'boxg'); s.text(545, 168, "Same parallel (east–west)", 'tg', size=14)
    s.text(545, 194, "D = 111.2 × cos(latitude) × angular distance", 't', size=14); s.text(545, 214, "cos only for east–west distances", 't2', size=12)
    s.box(360, 235, 370, 80, '', 'boxy'); s.text(545, 258, "Opposite hemispheres: ADD the angles", 'ty', size=14)
    s.text(545, 284, "18.7° N and 12.4° S → 31.1°", 't', size=14); s.text(545, 304, "same hemisphere: subtract", 't2', size=12)
    return s.render("Side view of a meridian with latitudes and distance formulas"), "Distance along a meridian or parallel and when to add or subtract angles"

def time_zones():
    s = SVG('time-zones', 760, 300)
    s.title(380, 26, "Time zones: east is ahead")
    x0, x1, y = 40, 720, 130
    s.arrow(x0, y, x1, y, 'ar')
    for h in range(-12, 13, 4):
        x = x0 + (h + 12) / 24 * (x1 - x0)
        s.line(x, y - 6, x, y + 6, 'ln'); s.text(x, y + 24, f"UTC{h:+d}" if h else "UTC", 't2', size=11)
    def X(h): return x0 + (h + 12) / 24 * (x1 - x0)
    s.circle(X(-8), y, 7, 'dot'); s.text(X(-8), y - 48, "Santa Cruz\nUTC−8", 'tb', size=13)
    s.circle(X(9), y, 7, 'dotg'); s.text(X(9), y - 48, "Nagano\nUTC+9", 'tg', size=13)
    s.path(f"M {X(-8)} {y+45} L {X(9)} {y+45}", 'arb', arrow=True)
    s.text((X(-8) + X(9)) / 2, y + 65, "17 hours apart (9 − (−8))", 'tb', size=13)
    s.text(380, 230, "2:00 pm Monday in Nagano → 9:00 pm Sunday in Santa Cruz", 't', size=14)
    s.text(380, 252, "15° of longitude = 1 hour. Add 1 hour for daylight saving. Watch the date.", 't2', size=12)
    s.text(380, 272, "Distance and time together: convert time zones, then use the fraction of the journey (2024 Q7).", 't2', size=12)
    return s.render("Timeline of UTC offsets showing Nagano 17 hours ahead of Santa Cruz"), "Calculating a time-zone difference"

def _axes(s, x0, y0, w, h, xl='x', yl='y'):
    s.arrow(x0, y0, x0, y0 - h, 'ar'); s.arrow(x0, y0, x0 + w, y0, 'ar')
    s.text(x0 + w, y0 + 18, xl, 't2', size=12); s.text(x0 - 10, y0 - h - 6, yl, 't2', size=12)

def scatter_lsl():
    s = SVG('scatter-lsl', 760, 380)
    s.title(380, 26, "Bivariate data: least-squares line, interpolation and extrapolation")
    x0, y0, w, h = 60, 320, 480, 250
    _axes(s, x0, y0, w, h, "explanatory x", "response y")
    pts = [(1, 2.4), (2, 3.9), (3, 4.2), (4, 6.1), (5, 6.6), (6, 8.3)]
    sx = lambda x: x0 + 20 + x * 55
    sy = lambda y: y0 - 15 - y * 21
    m, c = 1.1, 1.4
    s.raw(f'<rect x="{sx(0.6)}" y="{y0-h+8}" width="{sx(6.4)-sx(0.6)}" height="{h-8}" class="areag"/>')
    s.raw(f'<rect x="{sx(6.4)}" y="{y0-h+8}" width="{x0+w-sx(6.4)-8}" height="{h-8}" class="arear"/>')
    s.text((sx(0.6) + sx(6.4)) / 2, y0 - h + 30, "interpolation: inside the data (reliable)", 'tg', size=12)
    s.text((sx(6.4) + x0 + w - 8) / 2, y0 - 40, "extrapolation:\noutside (risky)", 'tr', size=12)
    s.line(sx(0.6), sy(m * 0.6 + c), sx(8.2), sy(m * 8.2 + c), 'lnb')
    for x, y in pts:
        s.line(sx(x), sy(y), sx(x), sy(m * x + c), 'lnr', dash=True); s.circle(sx(x), sy(y), 5, 'dot')
    s.text(sx(2.2), sy(m * 2.2 + c) - 40, "y = mx + c", 'tb', size=13)
    s.box(560, 60, 190, 250, '', 'box', rx=8)
    items = [("slope m", "change in y for each\n1 unit increase in x", 'tb'), ("intercept c", "value of y when x = 0\n(if meaningful)", 'tb'),
             ("residual", "actual − predicted\n(the dashed segments)", 'tr'), ("R²", "% of the variation in y\nexplained by x", 'tb')]
    for i, (t, d, cls) in enumerate(items):
        y = 88 + i * 58
        s.text(575, y, t, cls, anchor='start', size=13)
        a, b = d.split('\n')
        s.text(575, y + 17, a, 't2', anchor='start', size=11); s.text(575, y + 31, b, 't2', anchor='start', size=11)
    s.text(380, 366, "m = r × s_y ÷ s_x and c = ȳ − m·x̄. Association is not causation.", 't2', size=12)
    return s.render("Scatterplot with least-squares line, residuals and interpolation and extrapolation regions"), "The parts of a least-squares model and why extrapolation is risky"

def residuals():
    s = SVG('residuals', 760, 300)
    s.title(380, 26, "Residual plots: is a linear model suitable?")
    for k, (x0, good) in enumerate([(50, True), (410, False)]):
        y0 = 150
        s.box(x0 - 10, 45, 330, 200, '', 'boxg' if good else 'boxr', rx=8)
        s.line(x0, y0, x0 + 300, y0, 'ln')
        xs = [i for i in range(1, 11)]
        if good: ys = [8, -12, 5, -6, 14, -9, 4, -14, 10, -3]
        else: ys = [-30, -14, 2, 14, 24, 28, 22, 8, -10, -32]
        for x, y in zip(xs, ys): s.circle(x0 + 20 + x * 26, y0 - y * 1.3, 5, 'dot' if good else 'dotr')
        s.text(x0 + 150, 66, "random scatter about 0" if good else "curved pattern", 'tg' if good else 'tr', size=13)
        s.text(x0 + 150, 230, "linear model is supported" if good else "a non-linear model is needed", 't', size=13)
        s.text(x0 - 4, y0 - 4, "0", 't2', anchor='end', size=11)
    s.text(380, 275, "Residual = actual − predicted. Plot residuals against x and look for a pattern.", 't2', size=12)
    return s.render("Two residual plots: random scatter versus a curved pattern"), "How residual plots show whether a linear model fits"

def correlation():
    s = SVG('correlation', 760, 260)
    s.title(380, 26, "Strength and direction of correlation")
    import random
    random.seed(3)
    for k, (cx, lab, f) in enumerate([(130, "strong positive\nr ≈ 0.95", lambda x: x * 0.9), (380, "weak\nr ≈ 0.3", lambda x: x * 0.3), (630, "strong negative\nr ≈ −0.9", lambda x: -x * 0.9)]):
        x0, y0 = cx - 100, 190
        _axes(s, x0, y0, 200, 120, "", "")
        for i in range(12):
            x = i / 11 * 2 - 1
            noise = random.uniform(-0.12, 0.12) if k != 1 else random.uniform(-0.9, 0.9)
            y = f(x) + noise
            s.circle(x0 + 100 + x * 80, y0 - 60 - y * 45, 4, 'dot')
        s.text(cx, 225, lab, 't', size=12)
    return s.render("Three scatterplots showing strong positive, weak and strong negative correlation"), "Describing correlation by direction and strength"

def time_series():
    s = SVG('time-series', 760, 400)
    s.title(380, 26, "Time series: trend, seasonality and the seasonal index")
    x0, y0, w, h = 60, 290, 640, 230
    _axes(s, x0, y0, w, h, "time (quarters)", "value")
    season = [0.7, 1.0, 1.3, 1.0]
    pts = []
    for i in range(12):
        trend = 70 + i * 6
        v = trend * season[i % 4]
        pts.append((x0 + 30 + i * 52, y0 - 10 - v * 1.1))
    s.line(x0 + 30, y0 - 10 - 70 * 1.1, x0 + 30 + 11 * 52, y0 - 10 - (70 + 66) * 1.1, 'lnb', dash=True)
    s.poly(pts, 'lnr')
    for (x, y) in pts: s.circle(x, y, 4, 'dotr')
    s.text(x0 + 500, y0 - 40, "dashed line: trend (long-term direction)", 'tb', size=12)
    s.text(x0 + 215, y0 - 215, "seasonality: the pattern repeats\nevery year (4 quarters)", 'tr', size=12)
    s.box(110, 318, 540, 56, '', 'box', rx=6)
    s.text(380, 340, "seasonal index = season ÷ that year's average (averaged over years)", 't', size=12)
    s.text(380, 360, "deseasonalised = actual ÷ index. The indices sum to the number of seasons.", 't2', size=11)
    s.text(380, 392, "Moving averages smooth the data; irregular (random) fluctuations remain.", 't2', size=12)
    return s.render("Quarterly time series with a rising trend and a repeating seasonal pattern"), "Trend and seasonality, with the seasonal index formulas"

def sequences():
    s = SVG('sequences', 760, 340)
    s.title(380, 26, "Arithmetic vs geometric sequences")
    x0, y0, w, h = 60, 290, 360, 230
    _axes(s, x0, y0, w, h, "n", "t(n)")
    for n in range(0, 8):
        x = x0 + 30 + n * 45
        ya = y0 - 20 - (15 + 6 * n) * 2.6
        yg = y0 - 20 - (4 * 1.5 ** n) * 2.6
        s.circle(x, ya, 5, 'dot'); s.circle(x, yg, 5, 'dotr')
    s.poly([(x0 + 30 + n * 45, y0 - 20 - (15 + 6 * n) * 2.6) for n in range(8)], 'lnb')
    s.poly([(x0 + 30 + n * 45, y0 - 20 - (4 * 1.5 ** n) * 2.6) for n in range(8)], 'lnr')
    s.box(450, 60, 290, 110, '', 'boxb'); s.text(595, 82, "Arithmetic (linear)", 'tb', size=14)
    s.text(595, 108, "constant difference d", 't', size=13); s.text(595, 130, "t(n) = t₁ + (n − 1)d", 't', size=14); s.text(595, 152, "flat-rate depreciation", 't2', size=12)
    s.box(450, 185, 290, 110, '', 'boxr'); s.text(595, 207, "Geometric (exponential)", 'tr', size=14)
    s.text(595, 233, "constant ratio r", 't', size=13); s.text(595, 255, "t(n) = t₁ · r^(n−1)", 't', size=14); s.text(595, 277, "r > 1 growth, r < 1 decay", 't2', size=12)
    s.text(380, 325, "Define n carefully: if 2012 is term 1, the start of 2021 is term 10.", 't2', size=12)
    return s.render("Straight-line arithmetic growth compared with curved geometric growth"), "Arithmetic and geometric sequences compared"

def reducing_balance():
    s = SVG('reducing-balance', 760, 340)
    s.title(380, 26, "Reducing-balance loan: balance after each repayment")
    bal = [24000]
    for _ in range(4): bal.append(bal[-1] * 1.0045 - 557)
    x0, y0, w, h = 60, 285, 440, 215
    _axes(s, x0, y0, w, h, "month n", "balance ($)")
    pts = [(x0 + 40 + i * 100, y0 - 35 - (b - 22100) / 1600 * 148) for i, b in enumerate(bal)]
    s.poly(pts, 'lnb')
    for i, (x, y) in enumerate(pts):
        s.circle(x, y, 5, 'dot')
        if i < 4: s.text(x + 6, y - 12, f"A{'₀₁₂₃'[i]} = {bal[i]:,.2f}".replace(',', ' '), 't', size=11, anchor='start')
    s.text(x0 + 30, y0 + 16, "0", 't2', size=11)
    s.box(520, 60, 225, 200, '', 'box')
    s.text(632, 84, "Recurrence", 'tb', size=14)
    s.text(632, 112, "A(n+1) = r · A(n) − d", 't', size=14)
    s.text(632, 136, "r = 1 + monthly rate", 't2', size=12); s.text(632, 154, "d = repayment", 't2', size=12)
    s.text(632, 184, "Example (5.4% p.a., $557):", 't2', size=12); s.text(632, 204, "r = 1.0045, A₀ = 24 000", 't', size=13)
    s.text(632, 228, "interest = payments − reduction", 'tg', size=12); s.text(632, 246, "in balance", 'tg', size=12)
    s.text(380, 325, "Each month: add interest to the balance, then subtract the repayment.", 't2', size=12)
    return s.render("Loan balance falling over six months with the recurrence relation"), "Reducing-balance loan recurrence with the 2025 Q20 numbers"

def _graph(s, nodes, edges, hl=(), lab=True, r=17):
    for (a, b, wt) in edges:
        (x1, y1), (x2, y2) = nodes[a], nodes[b]
        cls = 'lnb' if (a, b) in hl or (b, a) in hl else 'ln'
        d = math.hypot(x2 - x1, y2 - y1) or 1; ux, uy = (x2 - x1) / d, (y2 - y1) / d
        s.line(x1 + ux * r, y1 + uy * r, x2 - ux * r, y2 - uy * r, cls)
        if lab:
            mx, my = (x1 + x2) / 2, (y1 + y2) / 2
            s.box(mx - 13, my - 10, 26, 20, str(wt), 'box', rx=4, size=12)
    for k, (x, y) in nodes.items():
        s.circle(x, y, r, 'nodeb' if any(k in e[:2] for e in hl) else 'node'); s.text(x, y + 5, k, 't', size=13, weight=600)

def mst():
    s = SVG('mst', 760, 340)
    s.title(380, 26, "Minimum spanning tree (Kruskal's algorithm)")
    nodes = {'A': (80, 120), 'B': (230, 70), 'C': (230, 190), 'D': (390, 120), 'E': (390, 250), 'F': (80, 250)}
    edges = [('A', 'B', 4), ('A', 'C', 6), ('B', 'C', 3), ('B', 'D', 7), ('C', 'D', 5), ('C', 'E', 8), ('D', 'E', 4), ('A', 'F', 9), ('C', 'F', 6), ('E', 'F', 10)]
    parent = {k: k for k in nodes}
    def find(x):
        while parent[x] != x: x = parent[x]
        return x
    tree = []
    for a, b, w in sorted(edges, key=lambda e: e[2]):
        if find(a) != find(b): parent[find(a)] = find(b); tree.append((a, b, w))
    _graph(s, nodes, edges, tree)
    total = sum(w for _, _, w in tree)
    s.box(480, 55, 260, 240, '', 'box', rx=8)
    s.text(610, 80, "Kruskal steps", 'tb', size=14)
    for i, t in enumerate(["1. List edges shortest first", "2. Add the next shortest edge", "3. Skip it if it makes a cycle", "4. Stop at (vertices − 1) edges"]):
        s.text(495, 112 + i * 26, t, 't', anchor='start', size=12)
    s.text(610, 235, f"Tree: {' + '.join(str(w) for _,_,w in sorted(tree,key=lambda e:e[2]))} = {total}", 'tg', size=13)
    s.text(610, 258, "Compare the total with the claim", 't2', size=12); s.text(610, 276, "(e.g. less than 25 m?)", 't2', size=12)
    s.text(380, 325, "Blue edges are in the tree: 6 vertices need 5 edges and no cycle.", 't2', size=12)
    return s.render("Weighted graph with the minimum spanning tree highlighted"), "Kruskal's algorithm on an example graph"

def flow():
    s = SVG('flow', 760, 340)
    s.title(380, 26, "Flow network: maximum flow = minimum cut")
    nodes = {'S': (80, 170), 'A': (260, 80), 'B': (260, 260), 'T': (440, 170)}
    edges = [('S', 'A', 10), ('S', 'B', 8), ('A', 'B', 3), ('A', 'T', 7), ('B', 'T', 9)]
    for a, b, c in edges:
        (x1, y1), (x2, y2) = nodes[a], nodes[b]
        d = math.hypot(x2 - x1, y2 - y1); ux, uy = (x2 - x1) / d, (y2 - y1) / d
        s.arrow(x1 + ux * 18, y1 + uy * 18, x2 - ux * 22, y2 - uy * 22, 'arb' if (a, b) in [('A', 'T'), ('B', 'T')] else 'ar')
        s.box((x1 + x2) / 2 - 13, (y1 + y2) / 2 - 10, 26, 20, str(c), 'box', rx=4, size=12)
    for k, (x, y) in nodes.items():
        s.circle(x, y, 17, 'nodeb' if k in 'ST' else 'node'); s.text(x, y + 5, k, 't', size=13, weight=600)
    s.line(310, 50, 310, 300, 'lnr', dash=True)
    s.text(310, 315, "cut {S, A, B} | {T}", 'tr', size=12)
    s.box(500, 55, 245, 240, '', 'box', rx=8); s.text(622, 80, "Capacity of a cut", 'tb', size=14)
    for i, t in enumerate(["Add only edges that go FROM", "the source side TO the sink side.", "", "Cut {S}: 10 + 8 = 18", "Cut {S, A}: 8 + 3 + 7 = 18", "Cut {S, B}: 10 + 9 = 19", "Cut {S, A, B}: 7 + 9 = 16"]):
        s.text(515, 108 + i * 22, t, 'tr' if 'A, B' in t else 't', anchor='start', size=12)
    s.text(622, 275, "Minimum cut 16 = maximum flow 16", 'tg', size=13)
    return s.render("Flow network with a minimum cut marked"), "Cut capacities and the maximum flow"

def critical_path():
    s = SVG('critical-path', 760, 400)
    s.title(380, 26, "Critical path analysis (forward and backward scan)")
    acts = {'A': (3, 0, 0, 90, 150), 'B': (4, 3, 3, 250, 90), 'C': (2, 3, 5, 250, 205), 'D': (5, 7, 7, 420, 150), 'E': (3, 12, 12, 590, 150)}
    # (duration, EST, LST, x, y)
    links = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('D', 'E')]
    for a, b in links:
        crit = a in 'ABDE' and b in 'ABDE'
        s.arrow(acts[a][3] + 55, acts[a][4] + 25, acts[b][3] - 5, acts[b][4] + 25, 'arg' if crit else 'ar')
    for k, (d, est, lst, x, y) in acts.items():
        crit = lst == est
        s.box(x, y, 50, 50, '', 'boxg' if crit else 'box', rx=6)
        s.text(x + 25, y + 20, k, 't', size=14, weight=700); s.text(x + 25, y + 38, f"{d} min", 't2', size=11)
        s.text(x + 3, y - 6, f"EST {est}", 'tb', anchor='start', size=11); s.text(x + 47, y + 66, f"LST {lst}", 'tr', anchor='end', size=11)
    s.text(380, 312, "Critical path A–B–D–E = 3 + 4 + 5 + 3 = 15 (float 0). C has float 2.", 't', size=13)
    s.text(380, 338, "Forward scan → EST. Backward scan → LST. Float = LST − EST.", 't2', size=12)
    s.text(380, 360, "Minimum completion time = the longest path.", 't2', size=12)
    return s.render("Activity network with earliest and latest start times and the critical path in green"), "Forward and backward scans with the critical path"

def euler():
    s = SVG('euler', 760, 320)
    s.title(380, 26, "Planar graphs and Euler's formula")
    nodes = {'1': (120, 200), '2': (260, 200), '3': (260, 90), '4': (120, 90), '5': (190, 50)}
    edges = [('1', '2'), ('2', '3'), ('3', '4'), ('4', '1'), ('4', '5'), ('5', '3'), ('1', '3')]
    for a, b in edges: s.line(*nodes[a], *nodes[b], 'ln')
    for k, (x, y) in nodes.items(): s.circle(x, y, 14, 'node'); s.text(x, y + 5, k, 't', size=12)
    s.text(150, 165, "f₁", 'tb', size=13); s.text(235, 125, "f₂", 'tb', size=13); s.text(190, 80, "f₃", 'tb', size=13); s.text(60, 250, "f₄ (outside)", 'tb', size=13, anchor='start')
    s.box(380, 60, 350, 200, '', 'boxb', rx=8)
    s.text(555, 90, "v + f − e = 2", 'tb', size=22)
    s.text(555, 125, "v vertices, e edges, f faces", 't2', size=13)
    s.text(555, 160, "This graph: v = 5, e = 7, f = 4", 't', size=14); s.text(555, 184, "5 + 4 − 7 = 2 ✓", 'tg', size=14)
    s.text(555, 220, "Count the outside region as a face.", 't2', size=12); s.text(555, 240, "Planar = can be drawn with no edges crossing.", 't2', size=12)
    s.text(380, 300, "Eulerian circuit: all vertices even. Eulerian trail: exactly two odd vertices.", 't2', size=12)
    return s.render("Planar graph with four faces and Euler's formula"), "Euler's formula and Eulerian trails"

def hungarian():
    s = SVG('hungarian', 760, 360)
    s.title(380, 26, "Hungarian algorithm (assignment, minimum cost)")
    steps = [("1  Reduce rows", "subtract each row's\nminimum", "boxb"), ("2  Reduce columns", "subtract each column's\nminimum", "boxb"), ("3  Cover the zeros", "use the fewest lines\nthat cover all zeros", "boxy")]
    for i, (t, d, cls) in enumerate(steps):
        x = 40 + i * 235
        s.box(x, 50, 200, 40, t, cls, size=14, weight=700); s.box(x, 94, 200, 50, d, 'box', size=12, rx=6)
        if i < 2: s.arrow(x + 200, 70, x + 235, 70)
    s.arrow(510, 144, 510, 185)
    s.box(400, 185, 220, 50, "Lines = n ?", 'boxy', size=15, weight=700)
    s.arrow(620, 210, 665, 210, 'arg'); s.box(665, 190, 85, 40, "YES: assign", 'boxg', size=12); s.text(707, 250, "using the zeros", 'tg', size=11)
    s.arrow(400, 210, 355, 210, 'arr'); s.box(40, 180, 315, 60, "NO: subtract the smallest uncovered\nvalue from uncovered cells, add it to\ndoubly covered cells, cover zeros again", 'boxr', size=11)
    s.path("M 197 180 L 197 162 L 450 162 L 450 146", 'ar', arrow=True)
    s.text(380, 300, "Total cost = add the ORIGINAL values of the assigned cells.", 't', size=12)
    s.text(380, 322, "Maximum problem: subtract every value from the largest first.", 't2', size=12)
    return s.render("Flowchart of the Hungarian algorithm steps"), "The Hungarian algorithm as a flowchart"

ALL = {'maths-earth': earth, 'maths-time-zones': time_zones, 'maths-scatter-lsl': scatter_lsl, 'maths-residuals': residuals, 'maths-correlation': correlation,
       'maths-time-series': time_series, 'maths-sequences': sequences, 'maths-reducing-balance': reducing_balance, 'maths-mst': mst, 'maths-flow': flow,
       'maths-critical-path': critical_path, 'maths-euler': euler, 'maths-hungarian': hungarian}
