"""Per-question diagrams for the Film, English and Spanish solution/framework pages.
Only facts already on those pages are used (no invented shots, sounds or audio)."""
import textwrap
from svgkit import SVG

def wrap(s, x, y, w, text, cls='t', size=12, lh=16, anchor='start', maxlines=9):
    """wrap text into a box of width w px (approx 6.3 px per char at size 12)"""
    cpl = max(8, int(w / (size * 0.6)))
    lines = textwrap.wrap(text, cpl)[:maxlines]
    for i, ln in enumerate(lines): s.text(x, y + i * lh, ln, cls, anchor=anchor, size=size)
    return y + len(lines) * lh

def card(s, x, y, w, h, head, body, cls='box', hc='tb', size=12):
    s.box(x, y, w, h, '', cls, rx=8)
    s.text(x + 12, y + 22, head, hc, anchor='start', size=13, weight=700)
    wrap(s, x + 12, y + 42, w - 24, body, 't', size, 16, maxlines=(h - 44) // 16)

# ---------------------------------------------------------------- film
def film(name, title, concept, prod, use, analyse, viewpoint, alt):
    s = SVG(name, 760, 400)
    s.title(380, 24, title)
    s.box(190, 40, 380, 34, f"Key concept: {concept}", 'boxy', size=13, weight=700)
    card(s, 20, 90, 235, 190, "Context of production", prod, 'boxb')
    card(s, 262, 90, 235, 190, "Context of use", use, 'boxg', 'tg')
    card(s, 504, 90, 236, 190, "Analyse after watching", analyse, 'box', 'tr')
    s.arrow(137, 280, 137, 305, 'arb'); s.arrow(380, 280, 380, 305, 'arg'); s.arrow(622, 280, 622, 305, 'arr')
    s.box(20, 305, 720, 75, '', 'boxi', rx=10)
    s.text(36, 330, "Viewpoint (appraise)", 'ti', anchor='start', size=13, weight=700)
    wrap(s, 36, 352, 690, viewpoint, 't', 12, 16, maxlines=2)
    return s.render(alt), ""

def f25q1(): return film('sol-film-2025-q1', "2025 Q1 Technologies: Mitski, Love Me More", "technologies", "Mitski, fourth single from Laurel Hell (2022); second Mitski video directed by Christopher Good. Meaning: isolation as a singer-songwriter and longing for connection and validation; a romantic relationship as the “narrative vehicle”.", "Music video circulated online for streaming audiences. You must name and justify a target audience (age, interests).", "Technologies and how they work with other elements to build isolation and longing. Link each point to the target audience.", "How effectively have technologies been used to enhance meaning? Judge effectiveness for the target audience and name one limit.", "Mind map of context facts and what to analyse for the Mitski question")
def f25q2(): return film('sol-film-2025-q2', "2025 Q2 Representations: The Last Job on Earth", "representations", "Animation by Moth Collective, funded by the DOEN Foundation (green, socially inclusive, creative innovation). Idea: Paul Mason's “biggest enigma” of a post-work society.", "Published with a Guardian article on a post-work society, in its sustainable business section. Over two-thirds of readers are 35 or older.", "How ideas about the future are represented (identity beyond corporate identity, skill set, seniority). Tie every point to an older business-news audience.", "The animation represents the future as … effectively/ineffectively because … (link to the article's message: do not fear a post-work society).", "Mind map of context facts and what to analyse for the animation question")
def f25q3(): return film('sol-film-2025-q3', "2025 Q3 Audiences: The Underdogs (Apple)", "audiences", "Web film by Mark Molloy, commissioned by Apple Business for “Apple at Work”. A B2B (trade) advertisement: same four office workers in a mini-sitcom. Award-winning.", "On Apple's YouTube channel. The 4th instalment (8+ min) had 2 million views on day one and 78 million since.", "How the audience is positioned to see Apple products as useful at work: humour, narrative, sitcom format, and why B2B differs from consumer ads.", "The web film positions the audience effectively … because the sitcom format … while the brand appears …", "Mind map of context facts and what to analyse for the Apple web film question")
def f24q1(): return film('sol-film-2024-q1', "2024 Q1 Representations: Silent (Moonbot, Dolby)", "representations", "Moonbot Studios with Dolby; sound by Steve Boeddeker. Purpose: show the evolution of film technology and the emotional power of audio. Morris Lessmore and The Kid represent picture and sound.", "Debuted at the Scientific and Technical Academy Awards (15 Feb 2014): industry and technical experts. (Inferred: promotes Dolby sound.)", "How each character's design, movement and sound work together, and how the relationship between picture and sound is shown.", "The characters are an effective/ingenious/limited representation of picture and sound because …", "Mind map of context facts and what to analyse for the Silent question")
def f24q2(): return film('sol-film-2024-q2', "2024 Q2 Technologies: Jurassic World Dominion", "technologies", "Third Jurassic World film, sixth in the series (from 1993); director Colin Trevorrow; Universal Pictures. Scene: Claire evades a large blind dinosaur in the trees.", "(Inferred, not in the context box) a major franchise release for a broad audience; the clip is online.", "How sound design, CGI/animatronics, camera and editing build tension, and how the audience is positioned alongside Claire.", "Technologies such as … build tension effectively by … (a blind predator suggests sound and silence).", "Mind map of context facts and what to analyse for the Jurassic World question")
def f24q3(): return film('sol-film-2024-q3', "2024 Q3 Institutions: Goldfish Focus Faceoff Lens", "institutions", "Campbell's hired Zulu Alpha Kilo to market a new Goldfish flavour to teenagers (13–17) with an AR Snapchat lens using eye-tracking and facial mesh.", "Launched Nov 2021 on Snapchat for one month; paid promotion; high scores shared; a coupon reward. Success measured by playtime and sales (quadrupled revenue).", "Institutions (agency, brand, platform), audience targeting, gamification and rewards, and how success was measured.", "The campaign was highly effective because the institution matched the platform, technology and incentive to its teenage audience, shown by …", "Mind map of context facts and what to analyse for the Goldfish question")

# ---------------------------------------------------------------- english
def eng(name, title, prompt, thesis, rows, alt):
    s = SVG(name, 760, 420)
    s.title(380, 24, title)
    s.box(20, 40, 720, 38, '', 'boxy', rx=8); wrap(s, 34, 64, 690, prompt, 't', 12, 16, maxlines=1)
    s.box(20, 90, 720, 76, '', 'boxi', rx=10); s.text(34, 112, "Thesis", 'ti', anchor='start', size=13, weight=700); wrap(s, 34, 132, 690, thesis, 't', 12, 16, maxlines=2)
    for i, (idea, quote, ctx) in enumerate(rows):
        x = 20 + i * 245
        s.arrow(x + 112, 166, x + 112, 186, 'arb')
        s.box(x, 186, 230, 220, '', 'box', rx=8)
        s.text(x + 12, 208, f"Paragraph {i+1}", 'tb', anchor='start', size=12, weight=700)
        y = wrap(s, x + 12, 228, 206, idea, 'tb', 12, 16, maxlines=3)
        y = wrap(s, x + 12, y + 8, 206, quote, 't', 11, 15, maxlines=6)
        wrap(s, x + 12, y + 8, 206, "Context: " + ctx, 't2', 11, 15, maxlines=4)
    return s.render(alt), ""

def e24a(): return eng('sol-eng-2024a', "2024 (a): jealousy", "How is the reader invited to view the concept of jealousy in the play?", "Jealousy is a self-generating, destructive force that exploits insecurity: born in Iago's resentment, nourished by Othello's need for certainty, fatal to all it touches.",
  [("A manipulated “monster”", "“the green-eyed monster which doth mock / The meat it feeds on” (3.3): personification, dramatic irony", "Jacobean fear of cuckoldry; honour tied to chastity"),
   ("Jealousy needs no cause", "“jealous for they are jealous; 'tis a monster / Begot upon itself” (3.4); “Trifles light as air” (3.3)", "irrationality, not justice"),
   ("Destroys the jealous and the innocent", "Othello's fragmented prose (4.1); Desdemona's death; Iago: “'twixt my sheets / He's done my office” (1.3)", "pity and judgment of both men")], "Thesis and three paragraphs for the jealousy prompt")
def e24b(): return eng('sol-eng-2024b', "2024 (b): the handkerchief", "Analyse the significance of Desdemona's handkerchief in the play.", "The handkerchief is the central symbol: a love token Iago converts into “ocular proof”, showing objects replacing people as evidence and women treated as property.",
  [("Symbol of love and bond", "“That handkerchief / Did an Egyptian to my mother give” (3.4): exotic, sacred origins", "Othello treats the gift as a ritual guarantee of fidelity"),
   ("Iago's tool: trifle becomes proof", "Iago will “in Cassio's lodging lose this napkin” (3.3); “ocular proof”", "the more empty the sign, the more it controls"),
   ("Collapse of Othello's language", "“Handkerchief—confessions—handkerchief!” (4.1): fragmented prose; Bianca flings it", "stands in for Desdemona's chastity: objectification")], "Thesis and three paragraphs for the handkerchief prompt")
def e25a(): return eng('sol-eng-2025a', "2025 (a): reputation", "What comment does the play make about the importance of reputation?", "Reputation is a fragile social currency, easily stolen or counterfeited; those who value appearances over truth, from Cassio to Othello, are most vulnerable.",
  [("Reputation as identity", "Cassio: “I have lost the immortal part of myself” (2.3): repetition, hyperbole", "Venetian military honour culture"),
   ("Iago manipulates reputation", "“he that filches from me my good name / Robs me of that which not enriches him” (3.3); “honest Iago”", "appearance vs reality"),
   ("Othello and Desdemona's names", "“begrimed and black / As mine own face” (3.3); “Speak of me as I am” (5.2)", "an outsider needing approval writes his own legacy")], "Thesis and three paragraphs for the reputation prompt")
def e25b(): return eng('sol-eng-2025b', "2025 (b): Emilia", "Analyse the significance of Emilia's character in the play.", "Emilia is a foil to Desdemona, the unwitting agent of the handkerchief plot, and the voice that exposes patriarchal double standards and finally destroys Iago with the truth.",
  [("Foil and realist", "“They are all but stomachs, and we all but food” (3.4): metaphor of consumption", "marriage as appetite and power"),
   ("The handkerchief and complicity", "takes it “to please his fantasy” (3.3): victim and tool of Iago's control", "wifely obedience and its cost"),
   ("Voice of truth", "“I will not charm my tongue; I am bound to speak” (5.2); “Moor, she was chaste”", "defies her husband and dies for the truth")], "Thesis and three paragraphs for the Emilia prompt")

# ---------------------------------------------------------------- spanish
def tree(name, title, question, concl, ex, marks, alt, h=None):
    n = len(ex); h = h or 330
    s = SVG(name, 760, h)
    s.title(380, 24, title)
    s.box(20, 40, 720, 40, '', 'boxy', rx=8); wrap(s, 34, 64, 690, question, 't', 12, 16, maxlines=1)
    s.box(110, 100, 540, 60, '', 'boxb', rx=10); s.text(126, 122, f"Conclusion (1 mark)", 'tb', anchor='start', size=13, weight=700); wrap(s, 126, 142, 510, concl, 't', 12, 16, maxlines=1)
    w = (720 - 12 * (n - 1)) / n
    for i, e in enumerate(ex):
        x = 20 + i * (w + 12)
        s.arrow(x + w / 2, 160, x + w / 2, 186, 'arb')
        s.box(x, 186, w, 90, '', 'boxg', rx=8); s.text(x + 10, 206, f"Example {i+1} (1)", 'tg', anchor='start', size=12, weight=700)
        wrap(s, x + 10, 224, w - 20, e, 't', 11, 15, maxlines=4)
    s.text(380, 306, marks, 't2', size=11)
    return s.render(alt), ""

S_MARK = "+ 4 marks for your Spanish: 4 few errors · 3 some · 2 words/phrases · 1 fragmented."
def s25q1(): return tree('sol-es-2025-q1', "2025 Q1: context of the audio (7 marks)", "¿Cuál es el contexto? Justifica con dos ejemplos.", "A speech at a father's 50th birthday celebration, given by his son.", ["Welcomes the guests to the special occasion and asks for applause for his father.", "Thanks his father and wishes him a happy birthday."], S_MARK, "Conclusion and two examples for the 2025 Q1 audio answer")
def s25q2(): return tree('sol-es-2025-q2', "2025 Q2: tone and opinion (7 marks)", "¿Qué revela el tono sobre la opinión del hablante? Dos ejemplos.", "Tone: agradecido (grateful); his father was a positive influence.", ["Lists everything his father gave him, from inspiration to volunteering trips.", "Recalls the memorable trip to Bolivia, helping people, and expresses appreciation."], S_MARK, "Conclusion and two examples for the 2025 Q2 audio answer")
def s25q4(): return tree('sol-es-2025-q4', "2025 Q4: two perspectives in Stimulus 2 (6 marks)", "Two perspectives, each with two examples (3 marks each).", "P1 embracing change is beneficial; P2 keep learning.", ["P1: changed plans, worked and travelled in Mexico instead of university.", "P1: “¿a qué esperan?” challenges readers to start their next adventure.", "P2: promotes university and other courses.", "P2: dance class and volleyball team, enjoyed though not careers."], "Each perspective: 1 mark + 1 per example. Another valid one: value independence.", "Two perspectives with two examples each for the 2025 Q4 answer", 330)
def s24q1(): return tree('sol-es-2024-q1', "2024 Q1: who is Juliana contacting? (7 marks)", "¿A quién intenta contactar Juliana? Dos ejemplos.", "The restaurant staff who take the reservations.", ["Says she has a reservation for her graduation dinner.", "Says the reservation is in her name."], S_MARK, "Conclusion and two examples for the 2024 Q1 voicemail answer")
def s24q2(): return tree('sol-es-2024-q2', "2024 Q2: purpose of the call (8 marks)", "¿Cuál es el propósito de la llamada? Tres ejemplos.", "To change her reservation.", ["Change the time of the dinner.", "Sit in the garden.", "Add a high chair for her one-year-old cousin."], S_MARK, "Conclusion and three examples for the 2024 Q2 voicemail answer")
def s24q6(): return tree('sol-es-2024-q6', "2024 Q6: why is Spanish “el idioma del futuro”? (5 marks)", "Conclusion plus four relevant examples.", "Spanish is growing quickly and widely, with the potential to rank first.", ["Second most widely spoken language after English.", "Third most used on the internet; 65% rise in users (2010–2020).", "Cervantes Institute: rising as a native language relative to English.", "18 million students; valuable in international relations and politics."], "Count the examples: this question needs four.", "Conclusion and four examples for the 2024 Q6 answer", 330)

ALL = {f.__name__.replace('f25', 'f25'): f for f in []}
ALL.update({'sol-film-2025-q1': f25q1, 'sol-film-2025-q2': f25q2, 'sol-film-2025-q3': f25q3, 'sol-film-2024-q1': f24q1, 'sol-film-2024-q2': f24q2, 'sol-film-2024-q3': f24q3,
 'sol-eng-2024a': e24a, 'sol-eng-2024b': e24b, 'sol-eng-2025a': e25a, 'sol-eng-2025b': e25b,
 'sol-es-2025-q1': s25q1, 'sol-es-2025-q2': s25q2, 'sol-es-2025-q4': s25q4, 'sol-es-2024-q1': s24q1, 'sol-es-2024-q2': s24q2, 'sol-es-2024-q6': s24q6})
