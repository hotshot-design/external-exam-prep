from svgkit import SVG

def dfd_symbols():
    s = SVG('dfd-symbols', 760, 340)
    s.title(380, 26, "Data flow diagram symbols (Gane-Sarson)")
    # external entity
    s.box(30, 55, 150, 54, "Student", 'box', rx=2, weight=600)
    s.text(105, 130, "External entity", 'tb', size=13); s.text(105, 158, "source or destination\noutside the system", 't2')
    # process (rounded top w/ number bar)
    s.box(215, 55, 150, 54, "Search catalogue", 'boxb', rx=10, weight=600)
    s.text(240, 71, "1.0", 'tb', size=12)
    s.text(290, 130, "Process", 'tb', size=13); s.text(290, 158, "numbered; verb or verb-object\nname; changes the data", 't2')
    # data store
    s.raw('<path d="M 400 55 L 550 55 M 400 109 L 550 109 M 400 55 L 400 109" class="ln" fill="none"/>')
    s.text(425, 87, "D1", 'tb', size=13); s.line(448, 55, 448, 109, 'ln'); s.text(500, 87, "Catalogue", 't', weight=600)
    s.text(475, 130, "Data store", 'tb', size=13); s.text(475, 158, "numbered; type D, M or T;\nnoun name", 't2')
    # data flow
    s.arrow(590, 82, 730, 82, 'arb'); s.text(660, 70, "book request", 't', size=13)
    s.text(660, 130, "Data flow", 'tb', size=13); s.text(660, 158, "labelled with a noun;\ndirection of the data", 't2')
    # store types + rules
    s.box(30, 195, 330, 125, '', 'box', rx=8)
    s.text(195, 217, "Data store types", 'tb', size=14)
    for i, t in enumerate(["D  data on disk (kept when switched off)", "M  manual data (paper or manually processed)", "T  temporary or transient (RAM, cache)"]):
        s.text(48, 245 + i * 25, t, 't', anchor='start', size=13)
    s.box(385, 195, 345, 125, '', 'boxr', rx=8)
    s.text(557, 217, "Not allowed", 'tr', size=14)
    for i, t in enumerate(["entity → entity", "entity → data store", "data store → entity", "(every flow must go through a process)"]):
        s.text(405, 242 + i * 22, t, 't', anchor='start', size=13)
    return s.render("Gane-Sarson DFD symbols: external entity, process, data store and data flow"), "The four Gane-Sarson symbols and the conventions the syllabus requires"

def dfd_example():
    s = SVG('dfd-example', 760, 330)
    s.title(380, 26, "Example DFD: library system (2025 Q11)")
    s.box(30, 125, 120, 54, "Student", 'box', rx=2, weight=600)
    s.box(250, 60, 170, 54, "Search", 'boxb', rx=10, weight=600); s.text(272, 76, "2.0", 'tb', size=12)
    s.box(250, 190, 170, 54, "Book delivery", 'boxb', rx=10, weight=600); s.text(272, 206, "1.0", 'tb', size=12)
    # stores
    def store(x, y, w, label, tag):
        s.raw(f'<path d="M {x} {y} L {x+w} {y} M {x} {y+40} L {x+w} {y+40} M {x} {y} L {x} {y+40}" class="ln" fill="none"/>')
        s.text(x + 22, y + 25, tag, 'tb', size=12); s.line(x + 42, y, x + 42, y + 40, 'ln'); s.text(x + 42 + (w - 42) / 2, y + 25, label, 't', size=13)
    store(560, 40, 160, "Authors", "D1"); store(560, 90, 160, "Titles", "D2"); store(560, 140, 160, "Topics", "D3")
    store(560, 215, 160, "Bookshelves", "M1")
    s.arrow(150, 135, 250, 85, 'arb'); s.text(170, 96, "keywords", 't2', size=11, anchor='middle')
    s.arrow(250, 100, 150, 150, 'arb'); s.text(250, 140, "book IDs, status", 't2', size=11, anchor='end')
    s.arrow(150, 160, 250, 205, 'arb'); s.text(150, 207, "book ID", 't2', size=11, anchor='middle')
    s.arrow(250, 222, 150, 172, 'arb'); s.text(250, 190, "book", 't2', size=11, anchor='end')
    for y in (60, 110, 160): s.arrow(560, y, 420, 87, 'ar')
    s.arrow(420, 225, 560, 225, 'ar'); s.text(490, 218, "book ID", 't2', size=11)
    s.arrow(560, 243, 420, 243, 'ar'); s.text(490, 258, "book", 't2', size=11)
    s.text(380, 290, "The Student never touches a data store directly: flows go through processes.", 't2', size=12)
    s.text(380, 310, "M1 is a manual store (physical bookshelves).", 't2', size=12)
    return s.render("Library system data flow diagram with Student, two processes and four data stores"), "A DFD where the student searches the catalogue and receives books (simplified from QCAA 2025 Q11)"

def cia():
    s = SVG('cia', 760, 380)
    s.title(380, 26, "The CIA triad: three properties of secure data")
    s.path("M 380 80 L 250 236 L 510 236 Z", 'ln')
    s.box(305, 42, 150, 38, "Confidentiality", 'boxb', size=14, weight=700)
    s.box(175, 236, 150, 38, "Integrity", 'boxg', size=14, weight=700)
    s.box(435, 236, 150, 38, "Availability", 'boxy', size=14, weight=700)
    s.text(470, 112, "only authorised people can see data", 't', anchor='start', size=12)
    s.text(470, 130, "risk: interception, weak passwords", 't2', anchor='start', size=12)
    s.text(470, 148, "fix: TLS, MFA, access control", 'tb', anchor='start', size=12)
    s.text(250, 300, "data is accurate and unchanged", 't', size=12); s.text(250, 318, "risk: manual entry, shared IDs", 't2', size=12); s.text(250, 336, "fix: validation, audit logs", 'tg', size=12)
    s.text(510, 300, "data and systems usable when needed", 't', size=12); s.text(510, 318, "risk: DDoS, hardware failure", 't2', size=12); s.text(510, 336, "fix: backups, redundancy", 'ty', size=12)
    s.text(380, 368, "Name the property, the risk from the scenario, then a fix that reduces it.", 't2', size=12)
    return s.render("CIA triad with risks and fixes"), "Confidentiality, integrity and availability, with a typical risk and fix for each"

def sym_asym():
    s = SVG('sym-asym', 760, 360)
    s.title(380, 26, "Symmetric vs asymmetric encryption")
    s.text(380, 56, "SYMMETRIC (one shared key): Caesar, AES, one-time pad", 'tb', size=14)
    s.box(30, 70, 130, 50, "Plaintext", 'box'); s.box(280, 70, 130, 50, "Ciphertext", 'boxb'); s.box(530, 70, 130, 50, "Plaintext", 'box')
    s.arrow(160, 95, 280, 95); s.arrow(410, 95, 530, 95)
    s.text(220, 85, "encrypt", 't2'); s.text(470, 85, "decrypt", 't2')
    s.box(185, 135, 80, 28, "same key", 'boxy', size=12); s.box(435, 135, 80, 28, "same key", 'boxy', size=12)
    s.line(225, 122, 225, 135, 'ln'); s.line(475, 122, 475, 135, 'ln')
    s.text(380, 205, "ASYMMETRIC (key pair): RSA", 'tg', size=14)
    s.box(30, 220, 130, 50, "Plaintext", 'box'); s.box(280, 220, 130, 50, "Ciphertext", 'boxg'); s.box(530, 220, 130, 50, "Plaintext", 'box')
    s.arrow(160, 245, 280, 245); s.arrow(410, 245, 530, 245)
    s.text(220, 235, "encrypt", 't2'); s.text(470, 235, "decrypt", 't2')
    s.box(165, 285, 120, 28, "public key", 'boxg', size=12); s.box(415, 285, 120, 28, "private key", 'boxr', size=12)
    s.line(225, 272, 225, 285, 'ln'); s.line(475, 272, 475, 285, 'ln')
    s.text(380, 345, "Symmetric is fast and good for bulk data; asymmetric solves key exchange and signatures.", 't2', size=12)
    return s.render("Symmetric encryption uses one key; asymmetric uses a public and private key"), "Symmetric and asymmetric encryption compared"

def hashing():
    s = SVG('hashing', 760, 300)
    s.title(380, 26, "Hashing: one-way, fixed-length output")
    ins = ["'hello'", "'a very long password…'"]
    for i, t in enumerate(ins):
        s.box(20, 60 + i * 70, 190, 44, t, 'box', size=13)
        s.arrow(210, 82 + i * 70, 300, 125)
    s.box(300, 100, 140, 50, "hash function", 'boxb', weight=600)
    s.arrow(440, 125, 530, 125)
    s.box(530, 100, 200, 50, "5d41402a… (fixed length)", 'boxg', size=12)
    s.path("M 530 175 L 440 175", 'arr', arrow=True); s.text(485, 195, "cannot be reversed", 'tr', size=12)
    s.text(380, 245, "Login: hash the typed password and compare it with the stored hash. Same input → same hash.", 't2', size=12)
    s.text(380, 265, "Used for storing passwords (security of data in storage) and for detecting changes (checksum).", 't2', size=12)
    return s.render("Hash function turning any input into a fixed-length output that cannot be reversed"), "Hashing is one-way and gives a fixed-length output"

def data_exchange():
    s = SVG('data-exchange', 760, 300)
    s.title(380, 26, "Data exchange components")
    boxes = [("User interface", "device, browser, app\n(what the user sees)", "boxb"), ("Server interface", "web server handling\nrequests and responses", "boxy"), ("Data interface", "database / DBMS\nstores and returns data", "boxg")]
    for i, (t, d, cls) in enumerate(boxes):
        x = 25 + i * 245
        s.box(x, 70, 210, 60, t, cls, size=15, weight=700)
        s.box(x, 135, 210, 60, d, 'box', size=12, rx=6)
    for i in range(2):
        x = 235 + i * 245
        s.arrow(x, 88, x + 35, 88, 'arb'); s.arrow(x + 35, 112, x, 112, 'arb')
    s.text(252, 62, "request", 't2', size=11); s.text(497, 62, "query", 't2', size=11)
    s.text(380, 230, "Data travels in a format (JSON, XML) over a protocol (HTTP, HTTPS, FTP).", 't2', size=12)
    s.text(380, 250, "Risks: interception in transit (use TLS/HTTPS), weak login, unvalidated input.", 't2', size=12)
    return s.render("User interface, server interface and data interface exchanging requests and data"), "The three data exchange components used in Digital Solutions answers"

def caesar():
    s = SVG('caesar', 760, 250)
    s.title(380, 26, "Caesar cipher, shift 2: CODE → EQFG")
    plain = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i, c in enumerate(plain):
        x = 30 + i * 26.5
        hl = c in "CODE"
        s.box(x, 60, 24, 30, c, 'boxb' if hl else 'box', size=13, rx=3)
        k = plain[(i + 2) % 26]
        s.box(x, 130, 24, 30, k, 'boxg' if hl else 'box', size=13, rx=3)
        if hl: s.arrow(x + 12, 90, x + 12, 130, 'arb')
    s.text(15, 80, "", 't2'); s.text(380, 50, "plaintext alphabet", 't2', size=12); s.text(380, 182, "shifted alphabet (each letter moves 2 places forward)", 't2', size=12)
    s.text(380, 215, "Decrypt by shifting back. Wrap round with MOD 26. Only 25 useful keys, so it is easy to brute force.", 't2', size=12)
    return s.render("Caesar cipher alphabet shifted by two places"), "Caesar cipher with a shift of 2"

def xor():
    s = SVG('xor', 760, 280)
    s.title(380, 26, "XOR and the one-time pad")
    rows = [("plaintext", "1 0 1 0"), ("key", "0 1 1 0"), ("ciphertext", "1 1 0 0")]
    for i, (n, b) in enumerate(rows):
        y = 60 + i * 55
        s.text(110, y + 26, n, 't', size=14, anchor='end')
        for j, ch in enumerate(b.split()):
            s.box(130 + j * 50, y, 42, 40, ch, 'boxg' if i == 2 else 'box', size=16, rx=4)
    s.line(125, 170, 335, 170, 'ln'); s.text(98, 98, "", 't2'); s.text(360, 130, "XOR: 1 when the bits differ", 'tb', anchor='start', size=14)
    s.text(360, 155, "same key again restores the plaintext", 't2', anchor='start', size=13)
    s.text(380, 230, "One-time pad: key is random, at least as long as the message, and used once.", 't2', size=12)
    s.text(380, 250, "Reusing or shortening the key breaks the security.", 't2', size=12)
    return s.render("XOR of plaintext and key bits giving ciphertext"), "XOR of bits for a one-time pad"

def useability():
    s = SVG('useability', 760, 340)
    s.title(380, 26, "Useability principles and visual communication (syllabus)")
    pr = [("Accessibility", "usable by people\nwith different abilities", "boxb"), ("Effectiveness", "tasks completed\naccurately, completely", "boxg"), ("Safety", "design prevents\nerrors and harm", "boxr"),
          ("Utility", "has the functions\nneeded; adapts to\ndifferent devices", "boxy"), ("Learnability", "new users learn\nit quickly", "boxi")]
    for i, (t, d, cls) in enumerate(pr):
        x = 10 + i * 148
        s.box(x, 50, 142, 40, t, cls, size=13, weight=700); s.box(x, 94, 142, 56, d, 'box', size=11, rx=6)
    s.box(20, 175, 340, 110, '', 'box'); s.text(190, 197, "Elements of visual communication", 'tb', size=13)
    s.text(190, 232, "space · line · colour · shape · texture\ntone · form · proportion · scale", 't', size=13)
    s.box(400, 175, 340, 110, '', 'box'); s.text(570, 197, "Principles of visual communication", 'tg', size=13)
    s.text(570, 232, "balance · contrast · proximity · harmony\nalignment · repetition · hierarchy", 't', size=13)
    s.text(380, 315, "Evaluate a UI with two useability principles: name each, then justify with evidence from the screen.", 't2', size=12)
    return s.render("Five useability principles and the visual communication elements and principles"), "The syllabus lists of useability principles and visual communication elements and principles"

ALL = {'digital-dfd-symbols': dfd_symbols, 'digital-dfd-example': dfd_example, 'digital-cia': cia, 'digital-sym-asym': sym_asym, 'digital-hashing': hashing,
       'digital-data-exchange': data_exchange, 'digital-caesar': caesar, 'digital-xor': xor, 'digital-useability': useability}
