from svgkit import SVG

def tenses():
    s = SVG('spanish-tenses', 760, 380)
    s.title(380, 26, "Which tense? A timeline")
    s.arrow(30, 140, 730, 140, 'ar')
    s.line(380, 120, 380, 160, 'lnb'); s.text(380, 176, "NOW", 'tb', size=13)
    cols = [(120, "PAST", "boxr", ["preterite: completed\n(trabajé)", "imperfect: habit or\nbackground (trabajaba)", "present perfect: recent,\nlinked to now (he trabajado)"]),
            (380, "PRESENT", "boxg", ["present: facts, habits,\nopinions (creo que es)", "estar + gerund: ongoing\n(estoy estudiando)", "llevar + time + gerund\n(llevo dos años estudiando)"]),
            (640, "FUTURE", "boxb", ["ir a + infinitive: plans\n(voy a viajar)", "future: predictions\n(estudiaré)", "conditional: wishes, advice\n(me gustaría)"])]
    for x, t, cls, ds in cols:
        s.box(x - 100, 55, 200, 36, t, cls, size=14, weight=700)
        for i, d in enumerate(ds): s.box(x - 112, 195 + i * 48, 224, 42, d, 'box', size=11, rx=6)
    s.text(380, 372, "Subjunctive (espero que…, cuando termine…) and si-clauses (si tuviera…, haría…) show range.", 't2', size=12)
    return s.render("Timeline of Spanish tenses for past, present and future"), "Choosing a Spanish tense by time and purpose"

def exam_structure():
    s = SVG('spanish-exam', 760, 300)
    s.title(380, 26, "Spanish exam: three sections (2024–25)")
    secs = [("Section 1", "audio · answer in SPANISH", "14–15 marks", "context, purpose, tone...\n'conclusion + N examples'", "boxb"),
            ("Section 2", "two texts · answer in ENGLISH", "17 marks", "audience, perspective,\npurpose, tone", "boxg"),
            ("Section 3", "email in SPANISH", "21 marks", "200–300 words, 3 bullets\ngreeting + sign-off", "boxy")]
    for i, (t, d, m, k, cls) in enumerate(secs):
        x = 20 + i * 245
        s.box(x, 55, 225, 40, t, cls, size=15, weight=700); s.box(x, 100, 225, 120, '', 'box', rx=8)
        s.text(x + 112, 125, d, 't', size=12, weight=600); s.text(x + 112, 150, m, 'tb', size=13); s.text(x + 112, 186, k, 't2', size=11)
    s.text(380, 250, "5 min perusal + 120 min. The audio can be replayed as often as you need.", 't2', size=12)
    s.text(380, 272, "Total 52–53 marks. Writing Section 3 in English scores 0.", 't2', size=12)
    return s.render("Three sections of the Spanish exam"), "Structure of the Spanish paper"

def email():
    s = SVG('spanish-email', 760, 400)
    s.title(380, 26, "Section 3 email: 200–300 words in Spanish")
    s.box(180, 45, 400, 335, '', 'box', rx=10)
    rows = [("Asunto: …", "boxy", 28), ("Estimado/a … / ¡Hola, …!", "boxy", 28), ("Purpose: Le escribo para …", "boxb", 30), ("Bullet 1: developed paragraph", "boxg", 44), ("Bullet 2: developed paragraph", "boxg", 44), ("Bullet 3: developed paragraph", "boxg", 44), ("Closing + Atentamente / Un saludo + name", "boxy", 30)]
    y = 58
    for t, cls, h in rows:
        s.box(195, y, 370, h, t, cls, size=13, rx=6); y += h + 8
    s.text(100, 120, "greeting +\nsign-off\n= 2 marks", 'ty', size=12); s.text(660, 200, "every bullet\naddressed AND\ndeveloped", 'tg', size=12)
    s.text(660, 290, "range of tenses\n+ one subjunctive", 'tb', size=12)
    return s.render("Layout of the Spanish extended-response email"), "How to lay out the Section 3 email"

def subjunctive():
    s = SVG('spanish-subjunctive', 760, 340)
    s.title(380, 26, "Present subjunctive: when to use it (WEIRDO)")
    items = [("W", "Wishes", "Quiero que me ayudes."), ("E", "Emotions", "Me alegra que tengas éxito."), ("I", "Impersonal", "Es importante que estudiemos."), ("R", "Recommendations", "Recomiendo que ahorres."), ("D", "Doubt, denial", "Dudo que sea fácil."), ("O", "Ojalá", "Ojalá que haga buen tiempo.")]
    for i, (l, t, ex) in enumerate(items):
        col, row = i % 3, i // 3
        x, y = 20 + col * 245, 50 + row * 105
        s.box(x, y, 225, 90, '', 'box', rx=8); s.circle(x + 28, y + 28, 18, 'nodeb'); s.text(x + 28, y + 34, l, 'tb', size=16)
        s.text(x + 130, y + 33, t, 't', size=14, weight=600); s.text(x + 112, y + 66, ex, 't2', size=12)
    s.text(380, 275, "Also: cuando + future meaning → Cuando termine el colegio, viajaré.", 't', size=13)
    s.text(380, 297, "creo que + indicative (es)   ·   no creo que + subjunctive (sea)", 't2', size=12)
    s.text(380, 320, "si + imperfect subjunctive → conditional: Si tuviera tiempo, haría voluntariado.", 't2', size=12)
    return s.render("The six triggers of the Spanish present subjunctive"), "WEIRDO triggers for the subjunctive"

ALL = {'spanish-email': email, 'spanish-subjunctive': subjunctive, 'spanish-tenses': tenses, 'spanish-exam': exam_structure}
