# Film flashcards

<script setup>
const cards = [
  { q: "The five key concepts?", a: "Technologies, representations, audiences, institutions, languages." },
  { q: "Define Institutions.", a: "The organisations and people whose operational processes and practices enable or constrain production and use." },
  { q: "Define Audiences.", a: "Individuals and groups for whom products are made, and who make meanings when they use them." },
  { q: "Contexts of production include…", a: "How, when, where, why and by whom it was made; financing (public/commercial); available technologies; distribution; regulation." },
  { q: "Contexts of use include…", a: "Who it is made for, why it is used, how it is shaped for consumers/citizens, platform and viewing context." },
  { q: "The standard exam question?", a: "'How effectively…? Justify your viewpoint by analysing the stimulus and explaining the contexts of production and use (including the target audience).'" },
  { q: "What do top marks in Analysing need?", a: "Accurate and detailed elements, significant interrelationships between elements, and insightful, plausible interpretations of meaning." },
  { q: "What does Appraising reward?", a: "An insightful viewpoint with valid, convincing conclusions, backed by pertinent evidence from the stimulus." },
  { q: "Word limit and marks?", a: "800–1000 words; 35 marks (2024) and 32 marks (2025)." },
  { q: "B2B advertisement?", a: "Business-to-business: made for businesses rather than individual consumers." },
  { q: "Gamification?", a: "Adding game elements (scores, rewards) to engage users, as in an AR lens with high scores and coupons." },
  { q: "French New Wave – key techniques?", a: "Jump cuts, handheld camera, location shooting, direct address (Godard, Breathless)." },
  { q: "German Expressionism – key techniques?", a: "Distorted sets, stark shadows, chiaroscuro lighting, psychological mood (Murnau)." },
  { q: "Italian Neorealism – key techniques?", a: "Location shooting, non-professional actors, social realism (De Sica)." },
  { q: "Soviet Montage – key technique?", a: "Rapid, meaning-creating editing; juxtaposition of shots (Vertov)." },
  { q: "Surrealism in film?", a: "Dream logic and shocking juxtaposition to challenge reality (Buñuel)." },
  { q: "Diegetic vs non-diegetic sound?", a: "Diegetic comes from the story world; non-diegetic (score, voice-over) is added for the audience." },
  { q: "What is mise-en-scène?", a: "Everything in the frame: setting, lighting, costume, props, actor placement." },
  { q: "What is a jump cut?", a: "A cut within the same shot that skips time and draws attention to the edit." },
  { q: "What is a match cut?", a: "A cut linking two shots by similar action, shape or sound." },
  { q: "What is depth of field?", a: "The range of distance in focus; shallow isolates a subject, deep keeps all in focus." },
  { q: "What is an auteur?", a: "A filmmaker with a recognisable personal style and recurring themes across works." },
  { q: "Analyse vs evaluate?", a: "Analyse = break down and explain how/why. Evaluate = judge effectiveness and justify a viewpoint." },
  { q: "What is representation?", a: "How people, places, events and ideas are constructed and portrayed, shaping audience understanding." },
  { q: "Exam time: planning and working?", a: "20 minutes planning, 120 minutes working." },
  { q: "Exam objective 6 focus (syllabus)?", a: "Evaluate production practices of artists to communicate conceptual, technical or creative purpose." },
]
</script>

<Flashcards id="film" :cards="cards" />
