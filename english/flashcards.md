# English flashcards

<script setup>
const cards = [
  { q: "Has Othello been set before 2024?", a: "No: it first appeared in 2024. Hamlet and Macbeth prompts from 2020–23 are the closest practice." },
  { q: "What did 2022 ask for five of the eight texts?", a: "How the ending invites the audience to view the protagonist (e.g. Hamlet, Jane Eyre). Be ready for Othello's final speech." },
  { q: "Othello concepts not yet asked?", a: "Race, trust, deception/appearance vs reality, love and violence, honour and revenge, gender and power, the ending and tragic hero." },
  { q: "Who says 'Give me the ocular proof' and when?", a: "Othello, demanding evidence from Iago in 3.3 (before accepting a handkerchief as proof)." },
  { q: "Who says 'Put out the light, and then put out the light'?", a: "Othello, before smothering Desdemona (5.2): light/dark imagery and ritual." },
  { q: "Who says 'Demand me nothing' and why does it matter?", a: "Iago (5.2): refuses to explain his motives, leaving evil unexplained." },
  { q: "Who says 'I will not charm my tongue; I am bound to speak'?", a: "Emilia (5.2): breaks her silence and exposes Iago." },
  { q: "'Moor, she was chaste. She loved thee, cruel Moor.' Who and why?", a: "Emilia (5.2): restores Desdemona's reputation after her death." },
  { q: "Exam format: words, time, marks?", a: "800–1000 words; 15 min planning + 120 min writing; 45 marks." },
  { q: "Othello prompts in 2024?", a: "(a) the concept of jealousy; (b) the significance of Desdemona's handkerchief." },
  { q: "Othello prompts in 2025?", a: "(a) the importance of reputation; (b) the significance of Emilia's character." },
  { q: "Who is Iago's rival that gets promoted instead of him?", a: "Michael Cassio" },
  { q: "What object becomes Iago's 'ocular proof'?", a: "Desdemona's handkerchief (Othello's first gift to her)" },
  { q: "Who steals the handkerchief?", a: "Emilia, Iago's wife, at his request" },
  { q: "Finish: 'O, beware, my lord, of jealousy; It is the green-eyed ___'", a: "monster, which doth mock the meat it feeds on (Iago, 3.3)" },
  { q: "'I am not what I am' – speaker and significance?", a: "Iago, 1.1. Inverts God's 'I am that I am'; announces deception." },
  { q: "What is dramatic irony in Othello?", a: "The audience knows Iago's plot while Othello and others trust 'honest Iago'." },
  { q: "What is hamartia?", a: "The tragic flaw leading to a hero's downfall (Othello: insecurity and credulity)." },
  { q: "Where is the play set in Acts 1 and 2–5?", a: "Act 1 Venice (order); Acts 2–5 Cyprus (disorder, war outpost)." },
  { q: "Who says 'Reputation, reputation, reputation!'?", a: "Cassio, 2.3, after being dismissed." },
  { q: "What does Emilia's speech in 4.3 argue?", a: "Husbands are as culpable as wives; women have the same senses and desires; critiques double standards." },
  { q: "Name three animal images used about Othello.", a: "Iago: 'old black ram', 'Barbary horse' and 'the beast with two backs' (1.1). Dehumanising racist imagery in Act 1. (Roderigo's 'thick-lips' is a racist insult, not an animal image.)" },
  { q: "Why does Othello's language change at 4.1?", a: "Verse collapses into fragmented prose and exclamations, reflecting his mental breakdown." },
  { q: "What's the structure of a strong body paragraph?", a: "Topic sentence → short embedded quote → analysis of technique and effect → link to values/context → link to thesis." },
  { q: "What does 'invite audiences to take up positions' mean?", a: "How the text shapes the audience's sympathies and judgments (e.g. complicity with Iago via soliloquy)." },
  { q: "'The Moor is of a free and open nature… led by th' nose as asses are' – what does it reveal?", a: "Iago (1.3): his contempt and his diagnosis of Othello's flaw: a trusting, credulous nature. Animal imagery dehumanises." },
  { q: "'So will I turn her virtue into pitch' – effect?", a: "Iago (2.3): Desdemona's goodness will become the net that traps her; shows intent and irony via soliloquy." },
  { q: "'Haply, for I am black' – what does it show?", a: "Othello (3.3): internalised prejudice and insecurity that Iago exploits; race as source of vulnerability." },
  { q: "'Chaos is come again' – technique and function?", a: "Othello (3.3): dramatic irony/foreshadowing; love is what holds his world in order." },
  { q: "'Handkerchief—confessions—handkerchief!' – what does the form show?", a: "Othello (4.1): fragmented prose and repetition mirror mental collapse; handkerchief as symbol of supposed guilt." },
  { q: "'Nobody; I myself' – significance?", a: "Desdemona (5.2): dying loyalty protects her murderer; self-erasure under patriarchal ideals of obedience." },
  { q: "'loved not wisely but too well' – why is it problematic?", a: "Othello (5.2) tries to author his own legacy and soften guilt; invites pity while the audience judges." },
  { q: "Name the final fate of Iago.", a: "Exposed by Emilia; he kills her, Othello wounds him, and he refuses to speak ('Demand me nothing'); taken for punishment/torture." },
]
</script>

<Flashcards id="english" :cards="cards" />
