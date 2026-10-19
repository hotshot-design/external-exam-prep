import math
from svgkit import SVG

def five_concepts():
    s = SVG('five-concepts', 760, 440)
    s.title(380, 26, "The five key concepts in contexts of production and use")
    s.raw('<g transform="translate(0,36)">')
    s.circle(380, 205, 95, 'box')
    s.text(380, 175, "CONTEXTS OF", 'tb', size=13); s.text(380, 193, "PRODUCTION AND USE", 'tb', size=13); s.text(380, 222, "who, why, funding,\nplatform, audience", 't2', size=11)
    items = [("Technologies", "tools and processes", "boxb", -90), ("Representations", "people, places, ideas", "boxg", -18), ("Audiences", "who it is made for", "boxy", 54),
             ("Institutions", "organisations and rules", "boxr", 126), ("Languages", "codes and conventions", "boxi", 198)]
    for t, d, cls, ang in items:
        a = math.radians(ang)
        x, y = 380 + 270 * math.cos(a), 205 + 160 * math.sin(a)
        s.box(x - 85, y - 28, 170, 56, t, cls, size=14, weight=700, sub=d)
    s.raw('</g>')
    s.text(380, 428, "2024–25 questions each named one of technologies, representations, institutions or audiences.", 't2', size=12)
    return s.render("Five key concepts arranged around contexts of production and use"), "The five key concepts and contexts"

def essay_flow():
    s = SVG('film-essay', 760, 330)
    s.title(380, 26, "Film exam: 20 min plan + 120 min write (800–1000 words)")
    steps = [("1  Read the 3 questions\nand context boxes", "boxb"), ("2  Watch twice;\nlist elements", "boxb"), ("3  Viewpoint + 3\ninterrelationships", "boxy"),
             ("4  Production and\nuse contexts", "boxg"), ("5  Two to three\nanalysis paragraphs", "boxg"), ("6  Verdict:\nhow effective?", "boxr")]
    for i, (t, cls) in enumerate(steps):
        col, row = i % 3, i // 3
        x, y = 15 + col * 248, 50 + row * 80
        s.box(x, y, 235, 60, t, cls, size=13)
    s.line(15, 225, 255, 225, 'lnb'); s.text(135, 247, "steps 1–3: 20 minutes planning", 'tb', size=12)
    s.line(260, 225, 745, 225, 'lng'); s.text(500, 247, "steps 4–6: 120 minutes writing", 'tg', size=12)
    s.text(380, 285, "Marks (2025): explain contexts 6 · analyse 13 · appraise 10 · written literacy 3", 't', size=13)
    s.text(380, 307, "Every claim needs evidence from the clip, and every paragraph ends with an effectiveness judgment.", 't2', size=12)
    return s.render("Film exam steps and time split"), "Planning and writing steps for the film exam"

def contexts():
    s = SVG('film-contexts', 760, 360)
    s.title(380, 26, "Contexts of production and use (6 of 32 marks)")
    s.box(20, 55, 350, 36, "PRODUCTION: how it was made", 'boxb', size=14, weight=700)
    s.box(390, 55, 350, 36, "USE: how it reaches and is used by audiences", 'boxg', size=14, weight=700)
    for i, t in enumerate(["who made it, when, where, why", "public or commercial funding / commissioning", "technologies available (CGI, AR, animation)", "distribution and regulation"]):
        s.box(20, 100 + i * 48, 350, 40, t, 'box', size=12, rx=6)
    for i, t in enumerate(["who it is made for (target audience)", "platform and viewing context (e.g. YouTube)", "why and how audiences use it (share, buy, learn)", "outcome: views, awards, sales"]):
        s.box(390, 100 + i * 48, 350, 40, t, 'box', size=12, rx=6)
    s.text(380, 315, "The context box in the exam gives most of these facts. Write production and use SEPARATELY,", 't2', size=12)
    s.text(380, 335, "then link each to the key concept in the question.", 't2', size=12)
    return s.render("Production contexts and use contexts side by side"), "What counts as a context of production and a context of use"

def marking():
    s = SVG('film-marking', 760, 320)
    s.title(380, 26, "Film marking guide (2025, 32 marks)")
    rows = [("Explaining: production + use", 6, "boxb"), ("Analysing: elements, interrelationships, interpretation", 13, "boxg"), ("Appraising: viewpoint + evidence", 10, "boxy"), ("Applying written literacy skills", 3, "boxr")]
    for i, (t, m, cls) in enumerate(rows):
        y = 55 + i * 55
        s.text(20, y + 24, t, 't', anchor='start', size=13)
        s.box(380, y, 20 * m + 20, 38, f"{m}", cls, size=14, weight=700, rx=6)
    s.text(380, 290, "Analysing and appraising are 23 of the 32 marks: aim for interrelationships and a clear verdict.", 't2', size=12)
    return s.render("Bar chart of the marks for each Film marking criterion"), "Where the film marks sit"

ALL = {'film-contexts': contexts, 'film-marking': marking, 'film-five-concepts': five_concepts, 'film-essay': essay_flow}
