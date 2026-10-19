from svgkit import SVG

def kotter():
    s = SVG('kotter', 760, 330)
    s.title(380, 28, "Kotter's 8-step change model")
    steps = [("1", "Create\nurgency"), ("2", "Build a guiding\ncoalition"), ("3", "Form a strategic\nvision"), ("4", "Communicate\nthe vision"),
             ("5", "Empower\naction"), ("6", "Create\nquick wins"), ("7", "Build on\nthe change"), ("8", "Make it stick\n(anchor in culture)")]
    phases = [(0, 2, "Create the climate", "boxb"), (3, 5, "Engage and enable", "boxy"), (6, 7, "Implement and sustain", "boxg")]
    # two rows of four
    for i, (n, t) in enumerate(steps):
        row, col = divmod(i, 4)
        x, y = 30 + col * 180, 55 + row * 130
        cls = 'boxy' if 3 <= i <= 5 else ('boxb' if i < 3 else 'boxg')
        s.box(x, y, 150, 86, t, cls, size=14)
        s.circle(x + 18, y + 16, 12, 'nodeb')
        s.text(x + 18, y + 21, n, 'tb', size=13)
        if col < 3: s.arrow(x + 150, y + 43, x + 180, y + 43)
    s.path("M 480 141 L 480 150 L 105 150 L 105 168", 'ar', arrow=True)
    s.text(380, 312, "Steps 4–6 use the wording the 2025 exam marked: communicate the vision · empower action · create quick wins", 't2', size=12)
    s.box(30, 280, 12, 12, '', 'boxb', rx=3); s.text(52, 291, "climate", 't2', anchor='start', size=12)
    s.box(120, 280, 12, 12, '', 'boxy', rx=3); s.text(142, 291, "engage", 't2', anchor='start', size=12)
    s.box(210, 280, 12, 12, '', 'boxg', rx=3); s.text(232, 291, "sustain", 't2', anchor='start', size=12)
    return s.render("Kotter's eight steps in three phases"), "Kotter's eight steps grouped into three phases"

def lewin():
    s = SVG('lewin', 760, 300)
    s.title(380, 28, "Lewin's 3-stage change model")
    cols = [("UNFREEZE", "boxr", "tr", ["Show why change is needed", "Reduce resistance", "Communicate and involve staff"]),
            ("CHANGE", "boxy", "ty", ["Implement new processes", "Train and support staff", "Monitor progress"]),
            ("REFREEZE", "boxg", "tg", ["KPIs and reward system", "New structure for new processes", "Feedback system (e.g. surveys)"])]
    for i, (h, cls, tcls, items) in enumerate(cols):
        x = 30 + i * 240
        s.box(x, 55, 200, 40, h, cls, tcls=tcls, weight=700)
        s.box(x, 105, 200, 130, '', 'box')
        for j, it in enumerate(items):
            s.text(x + 100, 132 + j * 38, (it.replace(' (', '\n(') if '(' in it else (it[:it.rfind(' ', 0, len(it) // 2 + 4)] + '\n' + it[it.rfind(' ', 0, len(it) // 2 + 4) + 1:] if len(it) > 24 else it)), 't', size=12)
        if i < 2: s.arrow(x + 200, 75, x + 240, 75)
    s.text(380, 270, "Refreeze embeds the change so it becomes normal operations; without it old behaviour can return (2023 guide).", 't2', size=12)
    return s.render("Lewin's unfreeze, change, refreeze stages with example actions"), "Lewin's stages with the actions the exam guides credit"

def force_field():
    s = SVG('force-field', 760, 340)
    s.title(380, 28, "Force field analysis (example: Music Co, 2025)")
    s.line(380, 50, 380, 300, 'lnb')
    s.box(300, 305, 160, 28, "THE CHANGE", 'boxb', tcls='tb', size=13)
    s.text(135, 62, "FORCES FOR change", 'tg', size=14)
    s.text(625, 62, "FORCES AGAINST change", 'tr', size=14)
    fo = [("2 600 searches a month for\n'where to upload music demo'", 5), ("Streaming forecast to grow\nto $4 billion by 2034", 4)]
    ag = [("R&D about $1 million;\nstreaming about $1.5 million", 5), ("Expenses rising for five years,\nagainst the 20% profit goal", 4)]
    for i, (t, w) in enumerate(fo):
        y = 100 + i * 90
        s.box(20, y - 22, 230, 56, t, 'boxg', size=12)
        s.arrow(252, y + 6, 372, y + 6, 'arg')
    for i, (t, w) in enumerate(ag):
        y = 100 + i * 90
        s.box(510, y - 22, 230, 56, t, 'boxr', size=12)
        s.arrow(508, y + 6, 388, y + 6, 'arr')
    s.text(380, 290, "", 't2')
    s.text(190, 292, "Weigh each force's strength, then decide", 't2', size=12)
    s.text(580, 292, "and propose ONE action (e.g. a cost-benefit analysis)", 't2', size=12)
    return s.render("Force field analysis with forces for and against change"), "Force field analysis: driving forces push for change, restraining forces push against"

def power_interest():
    s = SVG('power-interest', 760, 380)
    s.title(380, 26, "Stakeholder power-interest grid")
    x0, y0, w, h = 110, 50, 280, 130
    cells = [("Keep satisfied", "boxy", "high power\nlow interest", 0, 0), ("Manage closely", "boxr", "high power\nhigh interest", 1, 0),
             ("Monitor", "box", "low power\nlow interest", 0, 1), ("Keep informed", "boxb", "low power\nhigh interest", 1, 1)]
    for t, cls, sub, cx, cy in cells:
        s.box(x0 + cx * w, y0 + cy * h, w - 6, h - 6, t, cls, size=16, weight=700, sub=sub.replace('\n', ' · '))
    s.arrow(x0 - 30, y0 + 2 * h - 6, x0 - 30, y0, 'arb')
    s.raw(f'<text x="{x0-48}" y="{y0+h}" transform="rotate(-90 {x0-48} {y0+h})" text-anchor="middle" class="tb" font-size="13">POWER</text>')
    s.arrow(x0, y0 + 2 * h + 8, x0 + 2 * w - 6, y0 + 2 * h + 8, 'arb')
    s.text(x0 + w, y0 + 2 * h + 28, "INTEREST", 'tb', size=13)
    s.text(x0 + w, y0 + 2 * h + 52, "2024: Anton (positive) and the dissatisfied members (negative) were high power and high interest.", 't2', size=12)
    return s.render("Power-interest grid with the action for each quadrant"), "Power-interest grid: the action depends on the quadrant"

def swot():
    s = SVG('swot', 760, 340)
    s.title(380, 26, "SWOT: classify each case fact")
    s.text(260, 56, "HELPFUL", 'tg', size=13); s.text(520, 56, "HARMFUL", 'tr', size=13)
    s.text(60, 135, "INTERNAL", 'tb', size=13); s.text(60, 255, "EXTERNAL", 'tb', size=13)
    cells = [("Strengths", "boxg", "own resources: partnerships,\nbrand, new investment", 130, 66), ("Weaknesses", "boxr", "own limits: low brand awareness,\nno budget, falling profit", 395, 66),
             ("Opportunities", "boxg", "outside chances: market growth,\nnew demand, technology", 130, 190), ("Threats", "boxr", "outside risks: competitors,\ndeclining sales, regulation", 395, 190)]
    for t, cls, sub, x, y in cells:
        s.box(x, y, 255, 110, t, cls, size=16, weight=700, sub=sub.split('\n')[0])
        s.text(x + 127, y + 92, sub.split('\n')[1], 't2', size=12)
    s.text(380, 322, "Internal = S or W (inside the business). External = O or T (outside it). Quote data from the case.", 't2', size=12)
    return s.render("SWOT matrix of internal and external, helpful and harmful factors"), "SWOT: internal factors are strengths or weaknesses; external factors are opportunities or threats"

def life_cycle():
    s = SVG('life-cycle', 760, 360)
    s.title(380, 26, "Business life cycle and the post-maturity options")
    # axes
    s.arrow(60, 310, 60, 50, 'ar'); s.arrow(60, 310, 700, 310, 'ar')
    s.text(30, 180, "", 't2')
    s.raw('<text x="24" y="180" transform="rotate(-90 24 180)" text-anchor="middle" class="t2" font-size="12">sales / profit</text>')
    s.text(260, 336, "time", 't2', size=12)
    s.path("M 70 290 C 130 285 160 240 220 190 C 280 140 310 100 360 95 L 420 95", 'lnb')
    s.path("M 420 95 C 520 80 560 70 650 60", 'lng')
    s.path("M 420 95 L 650 100", 'lny')
    s.path("M 420 95 C 500 130 560 200 650 280", 'lnr')
    for x, t in [(120, "Introduction"), (260, "Growth"), (390, "Maturity")]:
        s.text(x, 335, "", 't2')
    s.text(95, 268, "Seed", 't', size=13); s.text(170, 232, "Start-up", 't', size=13); s.text(250, 150, "Growth", 't', size=13); s.text(380, 75, "Maturity", 't', size=13)
    s.line(420, 55, 420, 305, 'lnl', dash=True)
    s.text(535, 42, "Renewal (transformation)", 'tg', size=13, anchor='middle')
    s.text(570, 126, "Steady state", 'ty', size=13)
    s.text(570, 224, "Decline", 'tr', size=13)
    s.text(560, 336, "POST-MATURITY: this exam covers renewal", 'tb', size=12)
    return s.render("Business life-cycle curve with renewal, steady state or decline after maturity"), "Life cycle: after maturity a business renews, holds steady or declines"

def report():
    s = SVG('report', 760, 400)
    s.title(380, 26, "Business report: where the marks are (2025, 24 marks)")
    rows = [("1  Describe the situation", "2", "boxb", 0.25), ("2  SWOT with case data", "4", "boxb", 0.5), ("3  ONE relationship + ONE trend, effects, implications", "8", "boxg", 1.0),
            ("4  Evaluate ONE strategy with TWO criteria", "8", "boxg", 1.0), ("5  Decision, then recommendation", "(in 4)", "boxy", 0.5), ("6  Concise, logical report layout", "2", "boxb", 0.25)]
    y = 55
    for t, m, cls, f in rows:
        s.box(30, y, 470, 40, t, 'box', size=13, rx=6)
        s.box(510, y, 40 + 170 * f, 40, f"{m} marks" if m.isdigit() else m, cls, size=13, rx=6)
        y += 50
    s.text(380, 385, "16 of 24 marks are for synthesising (3) and evaluating (4). Keep the SWOT short. 400–600 words.", 't2', size=12)
    return s.render("Business report structure with marks per section"), "Where the marks sit in the business report"

def criteria():
    s = SVG('criteria', 760, 250)
    s.title(380, 26, "The four business criteria (syllabus)")
    items = [("Competitiveness", "meets or exceeds\nmarket standards\nvs rivals", "boxb"), ("Effectiveness", "goals achieved and\ntarget problems\nsolved", "boxg"),
             ("Efficiency", "best use of\nresources and\nprocesses", "boxy"), ("Stakeholder\nsatisfaction", "expectations\nconsidered\nand managed", "boxi")]
    for i, (t, d, cls) in enumerate(items):
        x = 20 + i * 185
        s.box(x, 55, 170, 60, t, cls, size=14, weight=700)
        s.box(x, 120, 170, 76, d, 'box', size=12, rx=6)
    s.text(380, 225, "Choose TWO. Judge the strategy against each: 'to what degree …?'", 't2', size=12)
    return s.render("Four business criteria with meanings"), "The four syllabus business criteria"

ALL = {'business-kotter': kotter, 'business-lewin': lewin, 'business-force-field': force_field, 'business-power-interest': power_interest,
       'business-swot': swot, 'business-life-cycle': life_cycle, 'business-report': report, 'business-criteria': criteria}
