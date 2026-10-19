"""Question-specific diagrams for the worked-solutions pages."""
import math
from svgkit import SVG

def _node(s, x, y, k, cls='node', r=17, size=13):
    s.circle(x, y, r, 'node')
    if cls != 'node': s.circle(x, y, r, cls)
    s.text(x, y + 5, k, 't', size=size, weight=600)

def _ewt(s, x, y, t):
    w = 10 + 8 * len(str(t))
    s.box(x - w / 2, y - 10, w, 20, str(t), 'box', rx=4, size=12)

def _edge(s, a, b, P, wt=None, hl=False, dash=False, off=(0, 0), r=17, arrow=False, cls=None, t=0.5):
    (x1, y1), (x2, y2) = P[a], P[b]
    d = math.hypot(x2 - x1, y2 - y1) or 1; ux, uy = (x2 - x1) / d, (y2 - y1) / d
    c = cls or ('arb' if (hl and arrow) else 'lnb' if hl else ('ar' if arrow else 'ln'))
    if arrow: s.arrow(x1 + ux * r, y1 + uy * r, x2 - ux * (r + 3), y2 - uy * (r + 3), c, dash=dash)
    else: s.line(x1, y1, x2, y2, c, dash=dash)
    if wt is not None: _ewt(s, x1 + (x2 - x1) * t + off[0], y1 + (y2 - y1) * t + off[1], wt)

# ---------------------------------------------------------------- maths 2025
def m25_flow():
    s = SVG('sol-2025-p2q3-flow', 760, 300)
    s.title(380, 24, "2025 Paper 2 Q3: flow network and minimum cut")
    P = {'A': (70, 150), 'B': (230, 70), 'C': (390, 150), 'D': (540, 70), 'E': (690, 150)}
    for a, b, c in [('A', 'B', 32), ('A', 'C', 38), ('B', 'C', 12), ('C', 'D', 20), ('C', 'E', 24), ('D', 'E', 20)]:
        _edge(s, a, b, P, c, arrow=True, hl=(a, b) in [('C', 'D'), ('C', 'E')])
    for k, (x, y) in P.items(): _node(s, x, y, k, 'nodeb' if k in 'AE' else 'node')
    s.text(70, 188, "source", 't2', size=11); s.text(690, 188, "river", 't2', size=11)
    s.line(432, 40, 432, 250, 'lnr', dash=True)
    s.text(432, 268, "min cut {A, B, C} | {D, E} = 20 + 24 = 44", 'tr', size=12)
    s.text(380, 290, "Upgrade C→E to 25: both 44-cuts become 45.", 'tg', size=12)
    return s.render("Flow network A to E with the minimum cut marked"), ""

def m25_road():
    s = SVG('sol-2025-p2q4-road', 760, 320)
    s.title(380, 24, "2025 Paper 2 Q4: shortest round trip from S")
    P = {'S': (380, 70), 'T': (560, 130), 'W': (500, 250), 'V': (260, 250), 'U': (200, 130)}
    E = [('S', 'T', 3), ('S', 'U', 12), ('S', 'V', 10), ('S', 'W', 9), ('T', 'U', 4), ('T', 'V', 7), ('T', 'W', 5), ('U', 'V', 8), ('U', 'W', 2), ('V', 'W', 6)]
    cyc = {('S', 'T'), ('T', 'U'), ('U', 'W'), ('W', 'V'), ('V', 'S')}
    offs = {('S', 'U'): (-12, -8), ('S', 'V'): (-26, 0), ('S', 'W'): (18, 6), ('T', 'V'): (0, -20), ('U', 'W'): (0, 16), ('T', 'U'): (0, -14), ('V', 'W'): (0, 14), ('U', 'V'): (-14, 0), ('T', 'W'): (14, 0), ('S', 'T'): (0, -12)}
    for a, b, w in E: _edge(s, a, b, P, w, hl=((a, b) in cyc or (b, a) in cyc), off=offs.get((a, b), (0, 0)))
    for k, (x, y) in P.items(): _node(s, x, y, k, 'nodeb' if k == 'S' else 'node')
    s.text(660, 60, "S–T–U–W–V–S", 'tb', anchor='middle', size=14)
    s.text(660, 82, "3 + 4 + 2 + 6 + 10 = 25 km", 't', size=13)
    s.text(660, 110, "12 machines × $25 = $300", 't2', size=12); s.text(660, 128, "25 km × $0.80 = $20", 't2', size=12); s.text(660, 150, "total $320", 'tg', size=13)
    return s.render("Weighted graph of five locations with the shortest round trip highlighted"), ""

def m25_euler():
    s = SVG('sol-2025-p2q5-euler', 760, 330)
    s.title(380, 24, "2025 Paper 2 Q5: Eulerian trails (not to scale)")
    P = {'A': (120, 230), 'B': (120, 80), 'C': (300, 80), 'D': (480, 150), 'E': (300, 230)}
    E = [('A', 'B', 208, (-26, 0)), ('B', 'C', 105, (0, -16)), ('C', 'D', 140, (10, -12)), ('D', 'E', 140, (10, 14)), ('E', 'C', 208, (-24, 0)), ('C', 'A', 233, (-18, -16))]
    for a, b, w, o in E: _edge(s, a, b, P, w, off=o)
    _edge(s, 'A', 'E', P, 105, hl=False, dash=True, off=(0, 16), cls='lnr')
    for k, (x, y) in P.items(): _node(s, x, y, k, 'nodeb' if k in 'AE' else 'node')
    s.box(540, 55, 205, 230, '', 'box', rx=8)
    for i, (t, c) in enumerate([("Degrees", 'tb'), ("A 3 · B 2 · C 4 · D 2 · E 3", 't2'), ("Odd vertices A and E:", 't'), ("open Eulerian trail A → E", 'tb'), ("A–B–C–D–E–C–A–E", 't2'), ("Tuesday: A–E closed (dashed)", 'tr'), ("closed trail A–B–C–D–E–C–A", 't2'), ("1139 m → 1034 m", 't'), ("1034 ÷ 67 = 15.4 min > 15", 'tg')]):
        s.text(552, 82 + i * 24, t, c, anchor='start', size=12)
    s.text(300, 305, "CA = √(208² + 105²) = 233 m (right angle at B)", 't2', size=12)
    return s.render("Walkway graph with odd-degree vertices A and E"), ""

def m25_hike():
    s = SVG('sol-2025-p2q6-hike', 760, 320)
    s.title(380, 24, "2025 Paper 2 Q6: Fiore and Goran meet")
    x0, y0, w, h = 70, 270, 440, 210
    s.arrow(x0, y0, x0, y0 - h, 'ar'); s.arrow(x0, y0, x0 + w, y0, 'ar')
    s.text(x0 + w - 10, y0 + 20, "hours n", 't2', size=12); s.text(x0 - 10, y0 - h - 8, "km from car park", 't2', size=12)
    X = lambda n: x0 + n * 80; Y = lambda d: y0 - d * 12
    s.line(X(0), Y(0), X(5), Y(10), 'lnb'); s.line(X(0), Y(15), X(5), Y(0), 'lnr')
    s.text(X(4.3), Y(9.6) - 8, "Fiore F(n) = 2n", 'tb', size=12); s.text(X(0.2), Y(15) - 10, "Goran G(n) = 15 − 3n", 'tr', size=12, anchor='start')
    s.circle(X(3), Y(6), 7, 'dotg'); s.text(X(3) + 14, Y(6) - 36, "meet: n = 3, 6 km", 'tg', size=13, anchor='start')
    for n in range(6): s.line(X(n), y0, X(n), y0 + 5, 'ln'); s.text(X(n), y0 + 18, str(n), 't2', size=11)
    s.box(540, 60, 200, 190, '', 'box', rx=8)
    for i, (t, c) in enumerate([("Meet at 1 pm, rest 30 min", 't'), ("resume 1:30 pm", 't'), ("arrive 4 pm → 2.5 h", 't'), ("6 km ÷ 2.5 h", 'tb'), ("= 2.4 km/h", 'tg')]):
        s.text(555, 90 + i * 30, t, c, anchor='start', size=13)
    return s.render("Two lines of distance against time crossing at three hours"), ""

# ---------------------------------------------------------------- maths 2024
def _project(s, acts, links, y0=0, crit=()):
    for a, b in links:
        xa, ya = acts[a][3] + 56, acts[a][4] + 25 + y0; xb, yb = acts[b][3] - 4, acts[b][4] + 25 + y0
        s.arrow(xa, ya, xb, yb, 'arg' if (a in crit and b in crit) else 'ar')
    for k, (d, est, lst, x, y) in acts.items():
        c = est == lst
        s.box(x, y + y0, 52, 50, '', 'boxg' if c else 'box', rx=6)
        s.text(x + 26, y + y0 + 20, k, 't', size=14, weight=700); s.text(x + 26, y + y0 + 38, str(d), 't2', size=11)
        s.text(x + 2, y + y0 - 5, f"EST {est}", 'tb', anchor='start', size=10); s.text(x + 50, y + y0 + 64, f"LST {lst}", 'tr', anchor='end', size=10)

def m24_bread():
    s = SVG('sol-2024-p2q4-bread', 760, 330)
    s.title(380, 24, "2024 Paper 2 Q4: bread project network")
    acts = {'A': (3, 0, 0, 25, 130), 'B': (5, 3, 3, 135, 130), 'C': (20, 8, 8, 255, 60), 'E': (7, 28, 28, 385, 60), 'D': (15, 8, 20, 255, 205), 'F': (30, 35, 35, 520, 130)}
    _project(s, acts, [('A', 'B'), ('B', 'C'), ('B', 'D'), ('C', 'E'), ('E', 'F'), ('D', 'F')], crit=set('ABCEF'))
    s.text(380, 30, "", 't2')
    s.text(380, 308, "Critical path A–B–C–E–F = 65 min. D is non-critical: float = 20 − 8 = 12 min.", 't', size=13)
    return s.render("Activity network with earliest and latest start times for the bread-making project"), ""

# ---------------------------------------------------------------- maths 2022
def m22_graph():
    s = SVG('sol-2022-p1q21-graph', 760, 330)
    s.title(380, 24, "2022 Paper 1 Q21: semi-Eulerian graph")
    P = {'B': (130, 250), 'C': (300, 250), 'P': (130, 110), 'D': (300, 60), 'W': (300, 150), 'R': (470, 130)}
    for a, b in [('D', 'W'), ('D', 'R'), ('W', 'P'), ('W', 'C'), ('W', 'B'), ('P', 'C'), ('B', 'C')]:
        _edge(s, a, b, P)
    for (a, b, o) in [('D', 'P', 10), ('W', 'R', 10)]:
        (x1, y1), (x2, y2) = P[a], P[b]
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2; dx, dy = -(y2 - y1), (x2 - x1); d = math.hypot(dx, dy)
        for sgn in (1, -1):
            s.path(f"M {x1} {y1} Q {mx + sgn * dx / d * 22} {my + sgn * dy / d * 22} {x2} {y2}", 'ln')
    for k, (x, y) in P.items(): _node(s, x, y, k, 'nodeb' if k in 'RC' else 'node')
    s.box(540, 50, 205, 230, '', 'box', rx=8)
    for i, (t, c) in enumerate([("Degrees", 'tb'), ("D 4 · P 4 · W 6", 't2'), ("R 3 · C 3 · B 2", 't2'), ("Odd vertices: R and C", 'tr'), ("→ semi-Eulerian", 'tr'), ("Cycle: R–W–P–D–R", 't'), ("Double edges: D–P and W–R", 't2'), ("count 2 in the matrix", 't2')]):
        s.text(552, 76 + i * 26, t, c, anchor='start', size=12)
    return s.render("Graph with double edges and two odd-degree vertices"), ""

def m22_shortest():
    s = SVG('sol-2022-p2q4-shortest', 760, 320)
    s.title(380, 24, "2022 Paper 2 Q4: shortest path Manon to Farra")
    P = {'M': (80, 160), 'V': (230, 80), 'B': (230, 240), 'A': (400, 110), 'R': (420, 250), 'F': (620, 170)}
    E = [('M', 'V', 16, (0, -14)), ('M', 'B', 34, (-14, 14)), ('M', 'A', 33, (0, 0)), ('V', 'B', 12, (-16, 0)), ('V', 'A', 15, (0, -14)), ('B', 'R', 10, (0, 16)), ('F', 'R', 15, (0, 16)), ('F', 'A', 23, (14, -8)), ('R', 'A', 15, (14, 0))]
    best = {('M', 'V'), ('V', 'B'), ('B', 'R'), ('R', 'F'), ('F', 'R')}
    for a, b, w, o in E: _edge(s, a, b, P, w, hl=((a, b) in best or (b, a) in best), off=o, t=(0.72 if (a, b) == ('M', 'A') else 0.5))
    for k, (x, y) in P.items(): _node(s, x, y, k, 'nodeb' if k in 'MF' else 'node')
    s.text(380, 290, "M–V–B–R–F = 16 + 12 + 10 + 15 = 53 km (M–V–A–F = 54, M–A–F = 56). New road = 53 − 4 = 49 km.", 't', size=12)
    return s.render("Weighted graph of six towns with the shortest path highlighted"), ""

def m22_mst():
    s = SVG('sol-2022-p2q5-mst', 760, 380)
    s.title(380, 24, "2022 Paper 2 Q5: minimum spanning tree (680 m)")
    P = {'RC': (60, 80), 'FW': (190, 80), 'T': (320, 140), 'SS': (200, 230), 'EA': (470, 140), 'CP': (330, 40), 'BC': (610, 70), 'LS': (640, 250), 'WS': (440, 300)}
    E = [('RC', 'FW', 70), ('RC', 'SS', 120), ('FW', 'T', 50), ('FW', 'CP', 170), ('SS', 'T', 110), ('T', 'EA', 95), ('EA', 'BC', 65), ('CP', 'BC', 60), ('BC', 'WS', 170), ('BC', 'LS', 165), ('SS', 'WS', 185), ('WS', 'LS', 65)]
    tree = {('FW', 'T'), ('CP', 'BC'), ('EA', 'BC'), ('WS', 'LS'), ('RC', 'FW'), ('T', 'EA'), ('SS', 'T'), ('BC', 'LS')}
    offs = {('RC', 'SS'): (-16, 0), ('FW', 'CP'): (0, -12), ('BC', 'WS'): (-14, 0), ('SS', 'WS'): (0, 14), ('CP', 'BC'): (0, -14)}
    for a, b, w in E: _edge(s, a, b, P, w, hl=(a, b) in tree, off=offs.get((a, b), (0, 0)), r=20)
    for k, (x, y) in P.items(): s.box(x - 20, y - 14, 40, 28, '', 'node', rx=14); s.box(x - 20, y - 14, 40, 28, k, 'nodeb', rx=14, size=12)
    s.text(380, 350, "Removed: 120 + 185 + 170 + 170 = 645 m. Saving 645 × $214 = $138 030 > $138 000, so reasonable (just).", 't', size=12)
    return s.render("Path network with the minimum spanning tree highlighted"), ""

# ---------------------------------------------------------------- maths 2021
def m21_project():
    s = SVG('sol-2021-p1q19-project', 760, 400)
    s.title(380, 24, "2021 Paper 1 Q19: project network (22 days)")
    acts = {'A': (2, 0, 9, 25, 70), 'C': (3, 2, 11, 150, 70), 'F': (4, 13, 14, 400, 70), 'B': (4, 0, 0, 25, 200), 'D': (6, 4, 4, 150, 200), 'E': (3, 10, 10, 275, 130), 'G': (8, 10, 10, 275, 250), 'H': (4, 18, 18, 540, 160)}
    # reposition for clarity
    acts = {'A': (2, 0, 9, 25, 55), 'C': (3, 2, 11, 150, 55), 'B': (4, 0, 0, 25, 200), 'D': (6, 4, 4, 150, 200), 'E': (3, 10, 11, 290, 130), 'G': (8, 10, 10, 290, 270), 'F': (4, 13, 14, 420, 90), 'H': (4, 18, 18, 560, 190)}
    links = [('A', 'C'), ('C', 'F'), ('B', 'D'), ('D', 'E'), ('D', 'G'), ('E', 'F'), ('F', 'H'), ('G', 'H')]
    _project(s, acts, links, crit=set('BDGH'))
    s.text(380, 385, "Critical path B–D–G–H = 4 + 6 + 8 + 4 = 22 days", 't', size=13)
    return s.render("Activity network for the 2021 project with earliest and latest start times"), ""

def m21_mst():
    s = SVG('sol-2021-p2q2-mst', 760, 380)
    s.title(380, 24, "2021 Paper 2 Q2: minimum spanning tree (135 m)")
    P = {'Admin': (90, 70), 'C1': (240, 130), 'C2': (400, 130), 'C3': (240, 260), 'C4': (400, 260), 'Tuck': (560, 195), 'Sports': (610, 60)}
    E = [('Admin', 'C1', 25, (-6, -10)), ('Admin', 'C2', 25, (0, -22)), ('Admin', 'Sports', 80, (0, -14)), ('C1', 'C2', 15, (0, -14)), ('C1', 'C3', 15, (-14, 0)), ('C1', 'C4', 60, (-20, 12)), ('C2', 'Sports', 60, (0, -12)),
         ('C2', 'C3', 25, (22, 14)), ('C2', 'C4', 15, (14, 0)), ('C2', 'Tuck', 20, (0, -10)), ('C3', 'C4', 15, (0, 14)), ('C4', 'Tuck', 20, (0, 12)), ('Tuck', 'Sports', 45, (14, 0))]
    tree = {('C1', 'C2'), ('C1', 'C3'), ('C2', 'C4'), ('C2', 'Tuck'), ('Admin', 'C1'), ('Tuck', 'Sports')}
    for a, b, w, o in E: _edge(s, a, b, P, w, hl=(a, b) in tree, off=o, r=22)
    for k, (x, y) in P.items(): s.box(x - 26, y - 14, 52, 28, '', 'node', rx=14); s.box(x - 26, y - 14, 52, 28, k, 'nodeb', rx=14, size=11)
    s.text(380, 345, "Tree: 15 + 15 + 15 + 20 + 25 + 45 = 135 m. Cost 135 × $1200 = $162 000 > $155 000.", 't', size=12)
    return s.render("Network of school buildings with the minimum spanning tree highlighted"), ""

# ---------------------------------------------------------------- maths 2020
def m20_flow():
    s = SVG('sol-2020-p1q21-flow', 760, 320)
    s.title(380, 24, "2020 Paper 1 Q21: maximum flow 90 tonnes per day")
    P = {'W': (70, 160), 'A': (280, 60), 'B': (280, 160), 'C': (280, 265), 'S': (490, 160)}
    for a, b, c in [('W', 'A', 50), ('A', 'S', 20), ('W', 'B', 30), ('B', 'S', 40), ('W', 'C', 40), ('C', 'B', 20), ('C', 'S', 30)]:
        _edge(s, a, b, P, c, arrow=True, hl=(a, b) in [('A', 'S'), ('B', 'S'), ('C', 'S')])
    for k, (x, y) in P.items(): _node(s, x, y, k, 'nodeb' if k in 'WS' else 'node')
    s.text(70, 195, "warehouse", 't2', size=11); s.text(490, 195, "shelter", 't2', size=11)
    s.line(400, 30, 400, 295, 'lnr', dash=True)
    s.text(400, 310, "cut {W, A, B, C} | {S} = 20 + 40 + 30 = 90", 'tr', size=12)
    s.box(560, 60, 185, 170, '', 'box', rx=8)
    for i, (t, c) in enumerate([("Minimum cut = 90", 'tg'), ("so maximum flow = 90", 'tg'), ("", 't'), ("With A unusable", 'tb'), ("min cut becomes 70", 't'), ("max flow = 70", 'tg')]):
        s.text(575, 90 + i * 26, t, c, anchor='start', size=13)
    return s.render("Flow network from warehouse to shelter with the minimum cut"), ""

def m20_tasks():
    s = SVG('sol-2020-p2q6-tasks', 760, 420)
    s.title(380, 24, "2020 Paper 2 Q6: project network (14 days)")
    acts = {'A': (3, 0, 0, 20, 160), 'C': (2, 3, 3, 130, 160), 'D': (8, 5, 6, 270, 50), 'E': (5, 5, 5, 270, 160), 'B': (4, 0, 2, 20, 290), 'F': (4, 4, 6, 130, 290), 'G': (3, 4, 7, 130, 230),
            'H': (1, 10, 10, 410, 200), 'I': (2, 7, 9, 270, 290), 'J': (3, 11, 11, 540, 200)}
    acts['G'] = (3, 4, 8, 20, 360)
    acts = {'A': (3, 0, 0, 20, 120), 'C': (2, 3, 3, 130, 120), 'D': (8, 5, 6, 270, 30), 'E': (5, 5, 5, 270, 120), 'B': (4, 0, 2, 20, 230), 'F': (4, 4, 6, 150, 215), 'G': (3, 4, 6, 150, 300), 'H': (1, 10, 10, 410, 170), 'I': (2, 7, 9, 290, 300), 'J': (3, 11, 11, 560, 170)}
    links = [('A', 'C'), ('C', 'D'), ('C', 'E'), ('B', 'F'), ('B', 'G'), ('E', 'H'), ('F', 'H'), ('G', 'I'), ('H', 'J'), ('I', 'J')]
    _project(s, acts, links, y0=25, crit=set('ACEHJ'))
    s.text(380, 410, "Critical path A–C–E–H–J = 3 + 2 + 5 + 1 + 3 = 14 days. At least 4 workers are needed.", 't', size=12)
    return s.render("Task network with earliest and latest start times and the critical path"), ""

ALL = {'sol-2025-p2q3-flow': m25_flow, 'sol-2025-p2q4-road': m25_road, 'sol-2025-p2q5-euler': m25_euler, 'sol-2025-p2q6-hike': m25_hike, 'sol-2024-p2q4-bread': m24_bread,
       'sol-2022-p1q21-graph': m22_graph, 'sol-2022-p2q4-shortest': m22_shortest, 'sol-2022-p2q5-mst': m22_mst, 'sol-2021-p1q19-project': m21_project, 'sol-2021-p2q2-mst': m21_mst,
       'sol-2020-p1q21-flow': m20_flow, 'sol-2020-p2q6-tasks': m20_tasks}
