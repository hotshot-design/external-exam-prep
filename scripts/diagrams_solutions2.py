"""Question-specific diagrams for the Digital Solutions and Business solutions pages."""
from svgkit import SVG

def _store(s, x, y, w, label, tag):
    s.raw(f'<path d="M {x} {y} L {x+w} {y} M {x} {y+40} L {x+w} {y+40} M {x} {y} L {x} {y+40}" class="ln" fill="none"/>')
    s.text(x + 22, y + 25, tag, 'tb', size=12); s.line(x + 42, y, x + 42, y + 40, 'ln'); s.text(x + 42 + (w - 42) / 2, y + 25, label, 't', size=13)

def d24_otp():
    s = SVG('sol-2024-q14-otp', 760, 330)
    s.title(380, 24, "2024 Q14: DFD for a one-time pad message")
    s.box(15, 70, 110, 50, "Friend A", 'box', rx=2, weight=600)
    s.box(215, 70, 150, 50, "Encrypt message", 'boxb', rx=10, weight=600); s.text(237, 86, "1.0", 'tb', size=12)
    s.box(425, 70, 150, 50, "Decrypt message", 'boxb', rx=10, weight=600); s.text(447, 86, "2.0", 'tb', size=12)
    s.box(635, 70, 110, 50, "Friend B", 'box', rx=2, weight=600)
    s.arrow(125, 95, 215, 95, 'arb'); s.text(170, 62, "unencrypted\nmessage", 't2', size=11)
    s.arrow(365, 95, 425, 95, 'arb'); s.text(395, 62, "encrypted\nmessage", 't2', size=11)
    s.arrow(575, 95, 635, 95, 'arb'); s.text(605, 62, "unencrypted\nmessage", 't2', size=11)
    _store(s, 265, 205, 260, "One-time pad (key)", "D1")
    s.arrow(320, 205, 290, 120, 'ar'); s.text(285, 170, "key", 't2', size=11)
    s.arrow(470, 205, 500, 120, 'ar'); s.text(500, 170, "key", 't2', size=11)
    s.text(380, 280, "Two external entities, encrypt and decrypt processes (numbered, verb names), labelled flows,", 't2', size=11)
    s.text(380, 298, "a key data store, and no direct entity-to-store flows.", 't2', size=11)
    return s.render("Data flow diagram for sending a one-time-pad encrypted message between two friends"), ""

def d25_traffic():
    s = SVG('sol-2025-q16-traffic', 760, 370)
    s.title(380, 26, "2025 Q16a: smart traffic system with an emergency vehicle")
    s.box(20, 150, 150, 70, "Sensors", 'boxb', size=15, weight=700, sub="position and speed")
    s.box(305, 150, 170, 70, "Data processing units", 'boxy', size=14, weight=700, sub="analyse, predict path")
    s.box(590, 150, 150, 70, "Adaptive signals", 'boxg', size=15, weight=700, sub="change timing")
    s.arrow(170, 185, 305, 185, 'arb'); s.text(238, 175, "real-time data", 't2', size=11)
    s.arrow(475, 185, 590, 185, 'arb'); s.text(532, 175, "instructions", 't2', size=11)
    s.box(20, 55, 150, 40, "Emergency vehicle", 'boxr', size=13); s.arrow(95, 95, 95, 150, 'arr')
    s.box(590, 265, 150, 70, "", 'box', rx=8)
    s.text(665, 288, "path signals green", 'tg', size=12); s.text(665, 308, "others stop", 'tr', size=12); s.text(665, 326, "crossings: danger", 'tr', size=12)
    s.arrow(665, 220, 665, 265, 'arg')
    s.text(240, 310, "System adapts as conditions change, then returns to normal", 't2', size=12)
    s.text(240, 330, "operation once the vehicle has passed.", 't2', size=12)
    return s.render("Sensors send data to processing units which instruct adaptive signals"), ""

def d24_nav():
    s = SVG('sol-2024-q15-nav', 760, 420)
    s.title(380, 24, "2024 Q15a: navigation app prototype (tablet)")
    s.box(30, 45, 480, 355, '', 'box', rx=14)
    s.box(45, 60, 450, 36, "🔍  Search buildings and classrooms…", 'boxy', size=12, rx=18)
    s.box(45, 106, 450, 250, '', 'boxg', rx=8)
    for (x, y, w, h, t) in [(70, 130, 110, 60, "A Block"), (230, 130, 120, 60, "Library"), (390, 130, 85, 60, "Hall"), (70, 250, 110, 60, "B Block"), (260, 260, 100, 70, "Canteen")]:
        s.box(x, y, w, h, t, 'box', size=12, rx=4)
    s.circle(215, 225, 9, 'dot'); s.text(215, 245, "You are here", 'tb', size=11)
    s.path("M 215 225 L 215 215 L 150 215 L 125 250", 'lnb', arrow=True)
    s.box(45, 364, 215, 28, "Directions to: B Block, Room 4", 'boxb', size=11, rx=14)
    s.box(280, 364, 215, 28, "Set a start location (off campus)", 'boxy', size=11, rx=14)
    notes = [("UI criteria", 'tb', ["map of the school only", "current location marker", "labelled buildings, rooms", "search feature", "navigation feature"]),
             ("Functionality (annotate)", 'tg', ["GPS updates the dot as you walk", "custom start off campus", "search lists matching rooms", "Go shows the route"])]
    y = 70
    for h, c, items in notes:
        s.text(530, y, h, c, anchor='start', size=13)
        for i, t in enumerate(items): s.text(530, y + 20 + i * 18, "• " + t, 't', anchor='start', size=11)
        y += 30 + len(items) * 18 + 20
    return s.render("Tablet wireframe of the school navigation app with annotations"), ""

def d25_pothole():
    s = SVG('sol-2025-q16e-pothole', 760, 400)
    s.title(380, 24, "2025 Q16e: improved Road Maintenance app mock-up")
    s.box(30, 45, 430, 340, '', 'box', rx=14)
    s.box(45, 58, 280, 30, "Search or filter: suburb · postcode · date", 'boxy', size=11, rx=15)
    s.box(335, 58, 110, 30, "Sort: nearest", 'boxy', size=11, rx=15)
    for i, (a, st) in enumerate([("Smith St, Brisbane", "to do"), ("Ann St, Brisbane", "to do"), ("High St, Ipswich", "done")]):
        y = 100 + i * 70
        s.box(45, y, 400, 58, '', 'box', rx=8)
        s.text(60, y + 24, a, 't', anchor='start', size=13, weight=600); s.text(60, y + 44, "0.8 km away · logged 12 Oct", 't2', anchor='start', size=11)
        s.box(325, y + 12, 108, 32, "Mark complete" if st == "to do" else "Done ✓", 'boxg' if st == "done" else 'boxb', size=10, rx=16)
    s.box(45, 318, 195, 52, "Offline map", 'boxb', size=12, rx=8); s.box(250, 318, 195, 52, "Confirm before saving", 'boxr', size=12, rx=8)
    s.text(480, 75, "Effectiveness", 'tb', size=13, anchor='start')
    for i, t in enumerate(["addresses instead of raw coordinates", "filter by suburb, postcode, date", "sort by distance from the worker", "offline map for directions"]): s.text(480, 96 + i * 18, "• " + t, 't', anchor='start', size=11)
    s.text(480, 190, "Safety (error prevention)", 'tr', size=13, anchor='start')
    for i, t in enumerate(["meaningful job names, not filenames", "status shown on each row", "confirm dialog before saving", "mark-complete button per job"]): s.text(480, 211 + i * 18, "• " + t, 't', anchor='start', size=11)
    return s.render("Mock-up of the pothole app with address list, filter, sort and offline map"), ""

def b25_swot():
    s = SVG('sol-2025-swot', 760, 360)
    s.title(380, 24, "2025 report: SWOT for Music Co (case facts)")
    cells = [("Strengths", 'boxg', 'tg', 30, 45, ["Strongest industry partnerships (score 9, S6)", "Established retailer, 26% market share (S7)", "Streaming already offered to customers (S4)"]),
             ("Weaknesses", 'boxr', 'tr', 395, 45, ["Lowest brand awareness (4, S6)", "Total USP score 28 trails rivals (S6)", "Expenses rising, profit falling (S2)"]),
             ("Opportunities", 'boxg', 'tg', 30, 195, ["Streaming revenue forecast to grow (S9)", "2 600 searches a month to upload demos (S10)", "Content creation hubs growing (S8)"]),
             ("Threats", 'boxr', 'tr', 395, 195, ["Physical sales declining (S7, S9)", "Rivals score higher on USPs (S6)", "R&D ~$1 million, streaming ~$1.5 million (S7)"])]
    for t, cls, tc, x, y, items in cells:
        s.box(x, y, 335, 140, '', cls, rx=8); s.text(x + 167, y + 24, t, tc, size=15)
        for i, it in enumerate(items): s.text(x + 14, y + 55 + i * 26, "• " + it, 't', anchor='start', size=12)
    s.text(380, 350, "Internal = S/W (top). External = O/T (bottom). Cite stimulus numbers.", 't2', size=12)
    return s.render("SWOT matrix filled with Music Co case facts"), ""

def b24_swot():
    s = SVG('sol-2024-swot', 760, 360)
    s.title(380, 24, "2024 report: SWOT for the Gym Business (case facts)")
    cells = [("Strengths", 'boxg', 'tg', 30, 45, ["Passionate, visible owners (S4)", "Loyal foundation members (S2, S4)", "$900 000 investment on offer (S6)"]),
             ("Weaknesses", 'boxr', 'tr', 395, 45, ["Profit and membership falling since 2020", "Few services, lock-in contracts (S4)", "No budget or forecast (S6)"]),
             ("Opportunities", 'boxg', 'tg', 30, 195, ["Wellbeing demand: 70% want self-care (S11)", "Virtual fitness programs up 95% (S10)", "New services: dietitian, physio (S7)"]),
             ("Threats", 'boxr', 'tr', 395, 195, ["Traditional gyms down 15% (S10)", "Home gym equipment up 236% (S10)", "Rivals with the vibe, no contracts (S4)"])]
    for t, cls, tc, x, y, items in cells:
        s.box(x, y, 335, 140, '', cls, rx=8); s.text(x + 167, y + 24, t, tc, size=15)
        for i, it in enumerate(items): s.text(x + 14, y + 55 + i * 26, "• " + it, 't', anchor='start', size=12)
    s.text(380, 350, "Internal = S/W (top). External = O/T (bottom). Cite stimulus numbers.", 't2', size=12)
    return s.render("SWOT matrix filled with Gym Business case facts"), ""

def b24_costbenefit():
    s = SVG('sol-2024-costbenefit', 760, 330)
    s.title(380, 24, "2024: cost-benefit summary (Stimulus 8)")
    rows = [("Additional costs", 934470, 'boxr'), ("Anton's investment", 900000, 'boxy'), ("Benefits (year 1)", 1098700, 'boxg')]
    for i, (t, v, cls) in enumerate(rows):
        y = 60 + i * 62
        s.text(20, y + 26, t, 't', anchor='start', size=14)
        s.box(190, y, 450 * v / 1100000, 40, "", cls, rx=6); s.text(190 + 450 * v / 1100000 + 8, y + 26, f"${v:,.0f}".replace(',', ' '), 't', anchor='start', size=13, weight=600)
    s.text(380, 262, "Shortfall: 934 470 − 900 000 = $34 470", 'tr', size=14)
    s.text(380, 286, "Net benefit: 1 098 700 − 934 470 = $164 230.  Payback: 934 470 ÷ 1 098 700 = 0.85 years (10.2 months).", 't2', size=12)
    s.text(380, 308, "Costs: registration $15 000 · wages $342 000 · recruitment and training $2 470 · refurbishment $500 000 · marketing $75 000", 't2', size=11)
    return s.render("Bars comparing the additional costs, the investment and the benefits"), ""

ALL = {'sol-2024-q14-otp': d24_otp, 'sol-2025-q16-traffic': d25_traffic, 'sol-2024-q15-nav': d24_nav, 'sol-2025-q16e-pothole': d25_pothole,
       'sol-2025-swot': b25_swot, 'sol-2024-swot': b24_swot, 'sol-2024-costbenefit': b24_costbenefit}
