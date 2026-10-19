from svgkit import SVG

def paragraph():
    s = SVG('english-paragraph', 760, 380)
    s.title(380, 26, "Analytical paragraph: point to link")
    steps = [("1  Topic sentence", "uses the prompt's key word", "boxb"), ("2  Embedded quote", "6–10 words, accurate", "boxg"), ("3  Named technique", "soliloquy, imagery, irony…", "boxy"),
             ("4  Effect on reader", "how the audience is positioned", "boxi"), ("5  Context / value", "race, gender, honour", "boxr"), ("6  Link to thesis", "answer the question", "boxb")]
    for i, (t, d, cls) in enumerate(steps):
        col, row = i % 3, i // 3
        x, y = 15 + col * 248, 50 + row * 90
        s.box(x, y, 235, 40, t, cls, size=13, weight=700); s.box(x, y + 44, 235, 34, d, 'box', size=12, rx=6)
    s.text(380, 250, "Example (reputation): Cassio's \"I have lost the immortal part of myself\" (2.3) uses hyperbole,", 't', size=12)
    s.text(380, 270, "positioning the audience to see reputation as identity, in a society where honour is social currency.", 't', size=12)
    s.text(380, 315, "Marks: Knowledge application · Organisation and development · Textual features (45 total)", 't2', size=12)
    s.text(380, 335, "800–1000 words; 15 min planning + 120 min writing.", 't2', size=12)
    return s.render("Analytical paragraph steps from topic sentence to link"), "The steps of a strong analytical paragraph"

def arc():
    s = SVG('english-arc', 760, 390)
    s.title(380, 26, "Othello: the tragic arc by act")
    s.raw('<g transform="translate(0,40)">')
    pts = [(70, 220), (190, 190), (310, 120), (440, 70), (580, 190), (700, 270)]
    s.path("M 70 220 C 130 210 150 190 190 190 C 250 190 270 130 310 120 C 370 100 400 60 440 70 C 500 85 530 160 580 190 C 640 225 670 260 700 270", 'lnb')
    for (x, y), t in zip(pts, ["Act 1\nVenice: marriage,\nIago's plan", "Act 2\nCyprus: Cassio\ndisgraced", "Act 3\nTemptation scene\nhandkerchief", "Act 3\nturning point:\n'Chaos is come again'", "Act 4\nprose collapse (4.1)\nstrikes Desdemona", "Act 5\nmurder, truth,\n'loved not wisely'"]):
        s.circle(x, y, 6, 'dot'); s.text(x, y + (46 if x in (190, 70, 310) else (-62 if x in (580,) else -52)) if x != 440 else y - 56, t, 't2', size=11)
    s.text(380, 315, "Rise → complication → crisis (3.3) → fall. Verse becomes fragmented prose as Othello breaks down.", 't2', size=12)
    s.raw('</g>')
    return s.render("Line graph of Othello's rise and fall across five acts"), "Plot arc of Othello"

def relationships():
    s = SVG('english-relationships', 760, 380)
    s.title(380, 26, "Othello: who manipulates, loves and betrays whom")
    P = {'Iago': (380, 70), 'Othello': (380, 190), 'Desdemona': (290, 310), 'Cassio': (650, 300), 'Emilia': (80, 150), 'Roderigo': (680, 110), 'Brabantio': (80, 310)}
    cls = {'Iago': 'boxr', 'Othello': 'boxb', 'Desdemona': 'boxg', 'Cassio': 'boxy', 'Emilia': 'boxg', 'Roderigo': 'box', 'Brabantio': 'box'}
    E = [('Iago', 'Othello', 'manipulates', 'arr'), ('Iago', 'Cassio', 'frames', 'arr'), ('Iago', 'Roderigo', 'uses', 'arr'), ('Iago', 'Emilia', 'husband', 'ar'),
         ('Othello', 'Desdemona', 'loves, then kills', 'arb'), ('Emilia', 'Desdemona', 'serves; exposes Iago', 'arg'), ('Brabantio', 'Desdemona', 'father', 'ar')]
    import math
    for a, b, t, c in E:
        (x1, y1), (x2, y2) = P[a], P[b]
        d = math.hypot(x2 - x1, y2 - y1); ux, uy = (x2 - x1) / d, (y2 - y1) / d
        s.arrow(x1 + ux * 50, y1 + uy * 24, x2 - ux * 50, y2 - uy * 24, c)
        s.text(x1 + (x2 - x1) * 0.5 + (0 if abs(x2 - x1) > 40 else 36), y1 + (y2 - y1) * 0.5 - 6, t, 't2', size=11)
    for k, (x, y) in P.items(): s.box(x - 55, y - 20, 110, 40, k, cls[k], size=14, weight=700)
    s.text(380, 365, "Use relationships for 'significance of a character' questions: what does each link reveal?", 't2', size=12)
    return s.render("Network of character relationships in Othello"), "Main character relationships and what each reveals"

def essay_structure():
    s = SVG('english-essay', 760, 340)
    s.title(380, 26, "Essay structure (800–1000 words, 120 min writing)")
    blocks = [("Introduction", "thesis uses the\nprompt's key word", "about 120", "boxb"), ("Body 1", "idea + quotes +\ntechnique + context", "about 200", "boxg"), ("Body 2", "new angle that\ndevelops the thesis", "about 200", "boxg"),
              ("Body 3", "complication or\ncounter-view", "about 200", "boxy"), ("Conclusion", "synthesise, don't\nsummarise", "about 100", "boxb")]
    for i, (t, d, w, cls) in enumerate(blocks):
        x = 15 + i * 148
        s.box(x, 60, 138, 40, t, cls, size=14, weight=700); s.box(x, 104, 138, 60, d, 'box', size=12, rx=6); s.text(x + 69, 186, w + " words", 't2', size=11)
    s.line(15, 215, 745, 215, 'lnl')
    s.text(380, 240, "Before: 15 min plan (thesis, 3–4 ideas, 2–3 short quotes each)", 'tb', size=13)
    s.text(380, 264, "After: 10 min proofread (names, quotes, punctuation)", 'tb', size=13)
    s.text(380, 300, "Marked on: Knowledge application · Organisation and development · Textual features (45 marks)", 't2', size=12)
    return s.render("Five-part essay structure with approximate word counts"), "Essay structure and timing"

ALL = {'english-relationships': relationships, 'english-essay': essay_structure, 'english-paragraph': paragraph, 'english-arc': arc}
