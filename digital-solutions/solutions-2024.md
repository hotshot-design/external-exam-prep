# Digital Solutions – worked solutions, 2024 paper

::: tip Source and how to use
Built from the QCAA **2024 Digital Solutions** question and response book, MC book, stimulus book and marking guide (`snr_digital_solutions_24_ea_*` in the [paper files](/digital-solutions/papers); CC BY 4.0, © State of Queensland (QCAA)). Marks and criteria are from the guide, whose sample responses I paraphrase. The guide accepts other reasonable answers. Question 14's diagram samples and Question 15a's prototype are drawings in the guide, so I describe them in words. Compare with the [2025 solutions](/digital-solutions/solutions-2025). **Attempt first, then compare.**
:::

## Section 1: multiple choice (10 marks)
| Q | Ans | Reasoning |
|---|---|---|
| 1 | C | **Scale** (size of elements, e.g. text too small) used badly makes content hard to see, which risks accessibility |
| 2 | D | Texting consenting customers about sales as they shop gives a **more personalised shopping experience** |
| 3 | C | **Renaming variables** (n, x, result) to descriptive names makes code easier to maintain. Comments on every line are clutter |
| 4 | D | Loop 1–100, add `i` if prime: **the sum of the primes from 1 to 100 inclusive** (not the first 100 primes) |
| 5 | A | **Buttons** show every fuel type at once and need one tap, so they are the most usable on a pump screen |
| 6 | C | DDoS stops legitimate requests, so it is a risk to **availability** |
| 7 | B | **Compression** reduces file size for faster loading while keeping quality |
| 8 | A | Line 2 sets x to a text string (JSON text), so the comment is "**assign a string to variable x**" |
| 9 | D | A timetable needs teacher, subject and student data. **Assessment** is not essential at first |
| 10 | A | Data flow 1 is the **hashed password**; flows 2 and 3 are the **encrypted username** going to the Users store and the **decrypted username** coming back |

## Section 2: short response (36 marks)

### Q11 (9 marks) Hospital boom gate (Stimulus 1: APPs)
**a) Three APPs and how to implement each (3 marks, 1 each)**
| APP | Implementation at the hospital |
|---|---|
| **APP 1: open and transparent management** | State why numberplates and ID swipes are collected, how they are used and shared, and who can see them. Give staff clear guidelines |
| **APP 2: anonymity and pseudonymity** | Consider letting staff use a pseudonym or ID number rather than a name. Otherwise handle data securely and use it only for its purpose |
| **APP 3: collection of solicited personal information** | Have a lawful reason to collect numberplates and ID data, and tell staff what it is for |

Other valid choices: APP 5 (notify staff at collection), APP 6 (use or disclose only for the purpose), APP 11 (security), APP 12 (access), APP 13 (correction).

**b) Analyse a risk and recommend a fix for each of C, I, A (6 marks, 1 + 1 each)**
| Property | Risk (analyse) | Recommendation |
|---|---|---|
| **Confidentiality** | Linking numberplates, names and times could reveal people's movements | Limit database access to one trusted role (e.g. IT manager) with an approval process |
| **Integrity** | Staff could lend ID cards or cover numberplates so wrong data is logged | Cross-check permitted numberplates against ID before opening the gate |
| **Availability** | Hacking, damage or an online outage could stop the gate working | Keep the database offline or on a secured, backed-up device, encrypt plate data, protect it physically |

### Q12 (8 marks) Pseudocode with JSON
Marks (guide): **retrieving the JSON data (1)**, **looping through the data (1)**, **calculating age (1)**, **calculating percentage won (1)**, **displaying gamer tag (1)**, **age (1)**, **percentage won (1)**, **effective use of pseudocode conventions (1)**. Statements must be free of logic errors.

```
BEGIN
GET currentDay, currentMonth, currentYear
READ the JSON file INTO playerArray
FOR each player IN playerArray
  DISPLAY player.gamerTag
  SPLIT player.dateOfBirth INTO birthDay, birthMonth, birthYear
  SET age = currentYear - birthYear
  IF currentMonth < birthMonth THEN
    age = age - 1
  ELSE IF currentMonth = birthMonth AND currentDay < birthDay THEN
    age = age - 1
  ENDIF
  DISPLAY age
  SET percentWon = player.gamesWon / player.gamesPlayed * 100
  DISPLAY percentWon
ENDFOR
END
```
Watch the age birthday check (the guide's solution subtracts 1 if the birthday hasn't occurred yet this year), and multiply by 100 for a percentage. The sample data has dates written as `dd/mm/yyyy`.

### Q13 (9 marks) Game design (Stimulus 2)
**a) Choose one code function (3 marks)**
Criteria: six unique grocery items displayed randomly; four unique shopping-list items chosen randomly; four grocery items match the list.
- **Choice:** `GetRandomFromList(List)`: it picks a random item (image or word) directly from a list of grocery items, which is what the interface shows.
- **Why not the others:** `GetRandomInt` would need each item mapped to a number (more code). `ShuffleList` randomises order but doesn't pick a subset.
- **Link to UI and criteria:** the six pictures shown and the four list words are items picked at random. Loop (6 and 4 times) and add a check so there are **no duplicates** (unique items).

**Marks (guide):** justifies the function (1), explains the relationship to the mock-up (1) and to the criteria (1).

**b) Two new programmed components with interface elements (6 marks)**
| Component | Related UI element | Justification (usability) |
|---|---|---|
| **User input to select items** | Large touch buttons or tappable pictures | Children can select easily, which makes the game usable and learnable |
| **Feedback on correct/incorrect** | Tick or colour change, sound, pop-up message | Immediate feedback helps children learn the word-picture link and keeps them engaged |

Other valid ideas: a **score/level counter** (progress), **text-to-speech** reading the word (accessibility), a **hint button**.
**Marks (guide):** two components (1 + 1), two UI elements (1 + 1), two justifications (1 + 1).

### Q14 (10 marks) Data flow diagram for a one-time pad

<Diagram name="sol-2024-q14-otp" />
Draw (the guide has two sample diagrams):
- **Two external entities:** Friend A (sender) and Friend B (receiver).
- **A process:** "Encrypt message" (1.0), and optionally "Decrypt message" (2.0).
- **Data flows (labelled):** *unencrypted message* from Friend A to 1.0, *key* (the one-time pad) into 1.0, and *encrypted message* from 1.0 to Friend B (then through 2.0 with the *key* to give the *unencrypted message* to Friend B).
- **Data store:** a "Key store" holding the shared pad (the guide accepts a solution that works without one).

Diagram conventions: external entities are squares or rectangles, processes are rounded rectangles with a number and a verb-object name, stores are open rectangles with an ID (D1), and every flow is a **labelled arrow** (nouns). Don't connect two entities, two stores, or an entity and a store directly.
**Marks (guide):** two external entities (1 + 1), an encrypt process (1), flows for unencrypted message, key and encrypted message (3), a data store or reasoned alternative (1), conventions with no errors (2) or one error (1), overall logic with no errors (1).

## Section 3: extended response (20 marks), Q15 navigation app

### Q15a (9 marks) User interface prototype

<Diagram name="sol-2024-q15-nav" />
Marks: **UI elements for all 5 UI criteria (5)** + **annotations explaining all 4 functionality criteria (4)**. One mark per criterion met.

| UI criterion | What to draw |
|---|---|
| Map of the school grounds only | A tablet screen with a map of the campus and no surrounding area |
| Current location on the map | A distinct marker (blue dot) labelled "You are here" |
| Labelled buildings and classrooms | Building shapes with names and room numbers |
| Search feature | A search bar at the top |
| Navigation feature | A "Directions" button and a highlighted route with arrows |

| Functionality criterion | Annotation |
|---|---|
| Locate and update location as users move | "GPS updates the dot every few seconds as the user walks" |
| Custom starting location when off campus | A "Set start location" button or drop-down so users can pick a start point manually |
| Search buildings and classrooms | "Typing a room number lists matches. Tapping one selects the destination" |
| Navigate to a desired location | "Select the destination, press Go, and the route displays step by step" |

### Q15b (4 marks) Two visual communication principles
Identify (1 each) and explain how it gives a good user experience (1 each). The guide's examples:
- **Contrast:** high-contrast colours make text and the map easy to read, which helps accessibility.
- **Harmony (consistency):** consistent icons, fonts and sizes give a uniform feel and make the app easier to learn.

Other valid principles: **alignment, proximity, hierarchy, emphasis, white space**.

### Q15c (3 marks) Social need and security impact
- **Social need (1):** students and staff want to **interact, share ideas and build community**, and the tour supports belonging.
- **Dissemination (1):** user content might be shared with unintended parties through third-party integrations, risking privacy violations, unauthorised access and identity theft.
- **Storage (1):** if data is not stored securely it could be hacked or leaked, destroying trust in the app and the community it supports.

### Q15d (2 marks) Data security strategy
**Access control** (role-based permissions). **Example:** administration staff, students and visitors see different data. Students cannot view other users' personal details, while administrators can manage content. *(Other valid strategies: encryption, multi-factor authentication, regular updates.)* Marks: strategy (1), example that justifies it (1).

### Q15e (2 marks) Two features that need authentication
- **Personalisation:** saved favourite locations and routes, language settings per user.
- **Communication:** notifications about school events or emergencies sent to the right users.

Marks: identify and explain each (1 + 1).

## What the guide rewards in 2024
| Wording | What to write |
|---|---|
| "identifies **and** explains the implementation of an APP" | Name the APP, say what the organisation does |
| "analyses a risk … makes a recommendation" for C, I and A | Six separate points; keep them distinct |
| "symbolises, without logic errors" | Code order must be correct (e.g. age calculation) |
| "conventions of the data flow diagram with no errors" | Labelled flows, numbered processes, no entity-to-entity arrows |
| "symbolises UI elements for all criteria" | Draw and label every criterion |
| "explains how the user interface addresses all the functionality criteria" | Annotate each functionality point |
| "evaluates the security impact of dissemination and storage" | Two separate effects, tied to the social need |

See also [past papers analysis](/digital-solutions/past-papers) and [worked examples](/digital-solutions/practice).
