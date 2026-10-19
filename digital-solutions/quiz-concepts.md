# Digital Solutions quiz: concepts and drills

Privacy principles, useability and visual communication, DFD rules, CIA risks, ciphers and data. See the [quick reference](/digital-solutions/quick-reference) and [notes](/digital-solutions/notes).

:::quiz
question: Match each Australian Privacy Principle (1–7)
pair: APP 1 => Open and transparent management of personal information
pair: APP 2 => Anonymity and pseudonymity
pair: APP 3 => Collection of solicited personal information
pair: APP 4 => Dealing with unsolicited personal information
pair: APP 5 => Notification of the collection of personal information
pair: APP 6 => Use or disclosure of personal information
pair: APP 7 => Direct marketing
:::

:::quiz
question: Match each Australian Privacy Principle (8–13)
pair: APP 8 => Cross-border disclosure of personal information
pair: APP 9 => Adoption, use or disclosure of government related identifiers
pair: APP 10 => Quality of personal information
pair: APP 11 => Security of personal information
pair: APP 12 => Access to personal information
pair: APP 13 => Correction of personal information
:::

:::quiz
question: Match each useability principle (syllabus) to its meaning
pair: Accessibility => Usable by people with a range of abilities and needs
pair: Effectiveness => Users can complete tasks accurately and completely
pair: Safety => The design prevents errors and harm
pair: Utility => The system provides the functions users need and adapts to their devices
pair: Learnability => New users can learn the system quickly
:::

:::quiz
question: Which are elements of visual communication (syllabus)? Select all that apply.
answer-correct: Space
answer-correct: Line
answer-correct: Colour
answer-correct: Scale
answer: Hierarchy
answer: Harmony
answer: Alignment
explanation: Elements: space, line, colour, shape, texture, tone, form, proportion, scale. Principles: balance, contrast, proximity, harmony, alignment, repetition, hierarchy.
shuffle: true
:::

:::quiz
question: Which are principles of visual communication (syllabus)? Select all that apply.
answer-correct: Contrast
answer-correct: Harmony
answer-correct: Hierarchy
answer-correct: Proximity
answer: Texture
answer: Scale
answer: Tone
explanation: Principles: balance, contrast, proximity, harmony, alignment, repetition, hierarchy.
shuffle: true
:::

:::quiz
question: In a Gane-Sarson DFD, which flow is NOT allowed?
answer-correct: An external entity sending data directly to a data store
answer: A process sending data to a data store
answer: An entity sending data to a process
answer: A store sending data to a process
explanation: Data must pass through a process.
shuffle: true
:::

:::quiz
question: In a DFD, what does the data store type "M" mean?
answer-correct: Manual data (physical files or manually processed data)
answer: Memory
answer: Master data
answer: Mobile data
explanation: D = data on disk, M = manual, T = temporary/transient.
shuffle: true
:::

:::quiz
question: How should processes and data flows be named in a DFD?
answer-correct: Processes: verb or verb-object (e.g. check credentials); flows and stores: nouns
answer: All verbs
answer: All nouns
answer: No names are needed
explanation: Also number the processes and stores.
shuffle: true
:::

:::quiz
question: Match each risk to the best fix
pair: Data intercepted over public Wi-Fi => TLS/SSL encryption or a VPN
pair: Stolen or weak passwords => Multi-factor authentication
pair: Manual data entry errors cause overselling => Validation and automatic updates
pair: A DDoS attack takes the system offline => Redundancy, backups and firewalls
:::

:::quiz
question: Match each CIA property to the risk
pair: Confidentiality => Private data is viewed by unauthorised people
pair: Integrity => Data is changed, wrong or corrupted
pair: Availability => Authorised users cannot access the system or data
:::

:::quiz
question: Caesar cipher with shift 2: encrypt CODE.
answer-input: EQFG
explanation: C→E, O→Q, D→F, E→G. (Digital Solutions practice)
:::

:::quiz
question: Gronsfeld cipher with key 123: encrypt CAT (letters only).
answer-input: DCW
explanation: C+1=D, A+2=C, T+3=W.
:::

:::quiz
question: XOR the bits 1010 and 0110. What is the result?
answer-input: 1100
explanation: Bits that differ become 1.
:::

:::quiz
question: A one-time pad is secure only if the key is…
answer-correct: Random, at least as long as the message, and used once
answer: A short word
answer: Reused for each message
answer: Public
explanation: Reuse or short keys break the guarantee.
shuffle: true
:::

:::quiz
question: Which question asks you to "desk check" an algorithm?
answer-correct: Trace the values of every variable step by step in a table
answer: Write it in a new language
answer: Draw a DFD
answer: Explain the law
explanation: 2025 Q14 was a desk check of a JSON average-rating algorithm.
shuffle: true
:::

:::quiz
question: Percentage of games won in pseudocode?
answer-correct: percentWon = gamesWon / gamesPlayed * 100
answer: gamesWon * gamesPlayed
answer: gamesPlayed / gamesWon
answer: gamesWon + gamesPlayed
explanation: (QCAA 2024 Q12 — [Question paper, p.8](/digital-solutions/papers/snr_digital_solutions_24_ea_question_response.pdf#page=8) · [Marking guide, p.6](/digital-solutions/papers/snr_digital_solutions_24_ea_mark_guide_pub.pdf#page=6))
shuffle: true
:::

:::quiz
question: Which data type suits a field for yes/no (e.g. valid_licence)?
answer-correct: BOOLEAN
answer: VARCHAR
answer: INT
answer: DATETIME
explanation: (QCAA 2025 Q15 — [Question paper, p.12](/digital-solutions/papers/snr_digital_solutions_25_ea_question_response.pdf#page=12) · [Marking guide, p.8](/digital-solutions/papers/snr_digital_solutions_25_ea_mark_guide_pub.pdf#page=8))
shuffle: true
:::

:::quiz
question: Which is a good "recommend a change to the data dictionary" for comparing average age by postcode?
answer-correct: Add a postcode field and justify that it allows smaller areas to be compared
answer: Delete date_of_birth
answer: Change everything to text
answer: Remove region
explanation: (QCAA 2025 Q15 — [Question paper, p.12](/digital-solutions/papers/snr_digital_solutions_25_ea_question_response.pdf#page=12) · [Marking guide, p.8](/digital-solutions/papers/snr_digital_solutions_25_ea_mark_guide_pub.pdf#page=8)b)
shuffle: true
:::

:::quiz
question: HTTP vs HTTPS?
answer-correct: HTTPS encrypts traffic using TLS; HTTP sends plain text
answer: They are identical
answer: HTTP is encrypted
answer: HTTPS is only for images
explanation: (QCAA 2022 Q11 — [Question paper, p.4](/digital-solutions/papers/snr_digital_solutions_22_ea_question_response.pdf#page=4) · [Marking guide, p.4](/digital-solutions/papers/snr_digital_solutions_22_ea_mark_guide_pub.pdf#page=4))
shuffle: true
:::
