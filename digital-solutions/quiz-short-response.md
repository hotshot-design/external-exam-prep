# Digital Solutions quiz: short responses 2024–2025

Questions adapted from the QCAA 2024 and 2025 short-response and extended-response questions. Desk checks and calculations are type-in; written answers become matching or multiple choice. Each explanation links to the question paper, the marking guide and the full **worked solution**. Source: QCAA external assessments (CC BY 4.0, © State of Queensland (QCAA)).

## 2025 paper

:::quiz
question: Desk check (2025 Q14): The Sequel has ratings 2, 1 and 2. What is totalRating after all three reviews?
answer-input: 5
explanation: 2 + 1 + 2 = 5, with numberOfReviews = 3. (QCAA 2025 Q14 — [Question paper, p.10](/digital-solutions/papers/snr_digital_solutions_25_ea_question_response.pdf#page=10) · [Marking guide, p.7](/digital-solutions/papers/snr_digital_solutions_25_ea_mark_guide_pub.pdf#page=7)) · [Worked solution](/digital-solutions/solutions-2025#q14-8-marks-desk-check)
:::

:::quiz
question: The Sequel's averageRating = totalRating ÷ numberOfReviews = 5 ÷ 3. Give the value to 2 decimal places.
answer-input: 1.67
answer-input: 1.6667
explanation: 5 ÷ 3 = 1.67. (QCAA 2025 Q14 — [Question paper, p.10](/digital-solutions/papers/snr_digital_solutions_25_ea_question_response.pdf#page=10) · [Marking guide, p.7](/digital-solutions/papers/snr_digital_solutions_25_ea_mark_guide_pub.pdf#page=7)) · [Worked solution](/digital-solutions/solutions-2025#q14-8-marks-desk-check)
:::

:::quiz
question: The Legends List has ratings 5, 4 and 3. What is its averageRating?
answer-input: 4
explanation: (5 + 4 + 3) ÷ 3 = 4. (QCAA 2025 Q14 — [Question paper, p.10](/digital-solutions/papers/snr_digital_solutions_25_ea_question_response.pdf#page=10) · [Marking guide, p.7](/digital-solutions/papers/snr_digital_solutions_25_ea_mark_guide_pub.pdf#page=7)) · [Worked solution](/digital-solutions/solutions-2025#q14-8-marks-desk-check)
:::

:::quiz
question: At the start of each movie's loop in the 2025 Q14 algorithm, what must happen to totalRating and numberOfReviews?
answer-correct: Both are reset to 0
answer: They carry over from the previous movie
answer: They are set to 1
answer: They are set to the first rating
explanation: Lines 5–6 reset the variables for each movie, which is why the second desk check starts from 0 again. (QCAA 2025 Q14 — [Question paper, p.10](/digital-solutions/papers/snr_digital_solutions_25_ea_question_response.pdf#page=10) · [Marking guide, p.7](/digital-solutions/papers/snr_digital_solutions_25_ea_mark_guide_pub.pdf#page=7)) · [Worked solution](/digital-solutions/solutions-2025#q14-8-marks-desk-check)
shuffle: true
:::

:::quiz
question: percentWon = gamesWon ÷ gamesPlayed × 100. Brandon Rioli won 4 of 10 games. What is percentWon?
answer-input: 40
answer-input: 40%
explanation: 4 ÷ 10 × 100 = 40. (QCAA 2024 Q12 — [Question paper, p.8](/digital-solutions/papers/snr_digital_solutions_24_ea_question_response.pdf#page=8) · [Marking guide, p.6](/digital-solutions/papers/snr_digital_solutions_24_ea_mark_guide_pub.pdf#page=6)) · [Worked solution](/digital-solutions/solutions-2024#q12-8-marks-pseudocode-with-json)
:::

:::quiz
question: Chloe Pezer won 55 of 58 games. What is percentWon to 1 decimal place?
answer-input: 94.8
answer-input: 94.8%
explanation: 55 ÷ 58 × 100 = 94.8. (QCAA 2024 Q12 — [Question paper, p.8](/digital-solutions/papers/snr_digital_solutions_24_ea_question_response.pdf#page=8) · [Marking guide, p.6](/digital-solutions/papers/snr_digital_solutions_24_ea_mark_guide_pub.pdf#page=6)) · [Worked solution](/digital-solutions/solutions-2024#q12-8-marks-pseudocode-with-json)
:::

:::quiz
question: Smart traffic system (2025 Q16a): match each component to its role in prioritising an emergency vehicle
pair: Sensors => Detect the vehicle's position and speed in real time
pair: Data processing units => Analyse the data, recognise patterns and predict the vehicle's path
pair: Adaptive traffic signals => Change timing to give green along the path and stop other traffic safely
explanation: The sensors detect, the processing units predict and the signals act. (QCAA 2025 Q16 — [Question paper, p.14](/digital-solutions/papers/snr_digital_solutions_25_ea_question_response.pdf#page=14) · [Marking guide, p.9](/digital-solutions/papers/snr_digital_solutions_25_ea_mark_guide_pub.pdf#page=9)) · [Worked solution](/digital-solutions/solutions-2025#q16a-4-marks-components-working-together)
:::

:::quiz
question: Fundraising app (2025 Q12b): match each risk to the property it affects
pair: No user authentication, so anyone could see balances => Confidentiality
pair: Inventory updated manually, risking overselling => Integrity
pair: Manual balance processing delays access during the event => Availability
explanation: Each risk breaks a different property of the CIA triad. (QCAA 2025 Q12 — [Question paper, p.6](/digital-solutions/papers/snr_digital_solutions_25_ea_question_response.pdf#page=6) · [Marking guide, p.5](/digital-solutions/papers/snr_digital_solutions_25_ea_mark_guide_pub.pdf#page=5)) · [Worked solution](/digital-solutions/solutions-2025#q12-9-marks-constraints-and-cia-risks)
:::

:::quiz
question: Fundraising app (2025 Q12a): match each constraint to its impact
pair: Four weeks to build the app => Less time to test thoroughly before launch
pair: Data must stay on the school server => Limited storage, so images need compressing
pair: Must run on iOS and Android => More development and testing across platforms
explanation: Name the constraint and state its impact. (QCAA 2025 Q12 — [Question paper, p.6](/digital-solutions/papers/snr_digital_solutions_25_ea_question_response.pdf#page=6) · [Marking guide, p.5](/digital-solutions/papers/snr_digital_solutions_25_ea_mark_guide_pub.pdf#page=5)) · [Worked solution](/digital-solutions/solutions-2025#q12-9-marks-constraints-and-cia-risks)
:::

:::quiz
question: 2025 Q13: payment details travel from the mobile app to the app server. Which vulnerability and security strategy fit best?
answer-correct: Interception (man-in-the-middle); use TLS/SSL encryption or a VPN
answer: Weak server RAM; add more memory
answer: Slow display; compress images
answer: Data loss; print a copy
explanation: The second vulnerability was the gift-card emails: an insecure email account, fixed with a strong password and multi-factor authentication. (QCAA 2025 Q13 — [Question paper, p.8](/digital-solutions/papers/snr_digital_solutions_25_ea_question_response.pdf#page=8) · [Marking guide, p.6](/digital-solutions/papers/snr_digital_solutions_25_ea_mark_guide_pub.pdf#page=6)) · [Worked solution](/digital-solutions/solutions-2025#q13-4-marks-data-exchange-vulnerabilities)
shuffle: true
:::

:::quiz
question: 2025 Q11: in the library DFD, how does the Student get the books they request?
answer-correct: The Search process returns matching book IDs; the Student then requests books through Book delivery from the manual Bookshelves store
answer: The Student reads the Bookshelves store directly
answer: The Student updates the Titles store
answer: The Authors store sends books to the Student
explanation: Entities may not access data stores directly; flows go through processes. The Bookshelves store is manual (M). (QCAA 2025 Q11 — [Question paper, p.4](/digital-solutions/papers/snr_digital_solutions_25_ea_question_response.pdf#page=4) · [Marking guide, p.4](/digital-solutions/papers/snr_digital_solutions_25_ea_mark_guide_pub.pdf#page=4)) · [Worked solution](/digital-solutions/solutions-2025#q11-7-marks-interpret-a-data-flow-diagram)
shuffle: true
:::

:::quiz
question: Pothole app (2025 Q16d): match each useability principle to the evidence
pair: Effectiveness => Locations are raw longitude/latitude with no way to filter, so jobs take longer
pair: Safety => Meaningless filenames make it easy to log the wrong job
explanation: Use the syllabus principles and justify each with evidence from the stimulus. (QCAA 2025 Q16 — [Question paper, p.14](/digital-solutions/papers/snr_digital_solutions_25_ea_question_response.pdf#page=14) · [Marking guide, p.9](/digital-solutions/papers/snr_digital_solutions_25_ea_mark_guide_pub.pdf#page=9)) · [Worked solution](/digital-solutions/solutions-2025#q16a-4-marks-components-working-together)
:::

## 2024 paper

:::quiz
question: Hospital boom gate (2024 Q11a): match each Australian Privacy Principle to how the hospital could implement it
pair: APP 1 (open and transparent management) => State why plate and ID data is collected, how it is used and who can see it
pair: APP 2 (anonymity and pseudonymity) => Let staff use a pseudonym or ID number where practical
pair: APP 3 (collection of solicited information) => Have a lawful reason to collect the data and tell staff its purpose
explanation: Identify the principle and explain how it is implemented. (QCAA 2024 Q11 — [Question paper, p.4](/digital-solutions/papers/snr_digital_solutions_24_ea_question_response.pdf#page=4) · [Marking guide, p.4](/digital-solutions/papers/snr_digital_solutions_24_ea_mark_guide_pub.pdf#page=4)) · [Worked solution](/digital-solutions/solutions-2024#q11-9-marks-hospital-boom-gate-stimulus-1-apps)
:::

:::quiz
question: Hospital boom gate (2024 Q11b): match each risk to the best recommendation
pair: Plate and name data could be linked to track movements => Restrict database access to one trusted role with an approval process
pair: Staff lend ID cards or hide plates => Cross-check permitted plates against IDs before opening
pair: Hacking or damage stops the gate working => Keep the database offline or backed up, encrypted and physically secured
explanation: Analyse the risk, then recommend a way to reduce it. (QCAA 2024 Q11 — [Question paper, p.4](/digital-solutions/papers/snr_digital_solutions_24_ea_question_response.pdf#page=4) · [Marking guide, p.4](/digital-solutions/papers/snr_digital_solutions_24_ea_mark_guide_pub.pdf#page=4)) · [Worked solution](/digital-solutions/solutions-2024#q11-9-marks-hospital-boom-gate-stimulus-1-apps)
:::

:::quiz
question: 2024 Q13a: a matching game must show six unique grocery items at random. Which library function is the best choice?
answer-correct: GetRandomFromList(List), looped six times with a duplicate check
answer: ShuffleList(List) only
answer: GetRandomInt(a, b) with no mapping
answer: None: it can't be done
explanation: It picks an item (image or word) directly from a list, so no integer mapping is needed; add a check so items are unique. (QCAA 2024 Q13 — [Question paper, p.10](/digital-solutions/papers/snr_digital_solutions_24_ea_question_response.pdf#page=10) · [Marking guide, p.8](/digital-solutions/papers/snr_digital_solutions_24_ea_mark_guide_pub.pdf#page=8)) · [Worked solution](/digital-solutions/solutions-2024#q13-9-marks-game-design-stimulus-2)
shuffle: true
:::

:::quiz
question: 2024 Q15d: which is a good data security strategy for a school navigation app, with an example?
answer-correct: Access control: administrators, students and visitors see different data
answer: Turn the app off at night
answer: Use only red buttons
answer: Delete all user data daily
explanation: Role-based permissions limit who can view personal data. (QCAA 2024 Q15 — [Question paper, p.14](/digital-solutions/papers/snr_digital_solutions_24_ea_question_response.pdf#page=14) · [Marking guide, p.12](/digital-solutions/papers/snr_digital_solutions_24_ea_mark_guide_pub.pdf#page=12)) · [Worked solution](/digital-solutions/solutions-2024#q15a-9-marks-user-interface-prototype)
shuffle: true
:::

:::quiz
question: 2024 Q15c: what is a possible social need for the interactive tour feature?
answer-correct: Students and staff want to interact, share ideas and build a sense of community
answer: Faster downloads
answer: Cheaper printing
answer: A bigger map
explanation: The security impact of dissemination and storage is then evaluated in relation to this need. (QCAA 2024 Q15 — [Question paper, p.14](/digital-solutions/papers/snr_digital_solutions_24_ea_question_response.pdf#page=14) · [Marking guide, p.12](/digital-solutions/papers/snr_digital_solutions_24_ea_mark_guide_pub.pdf#page=12)) · [Worked solution](/digital-solutions/solutions-2024#q15a-9-marks-user-interface-prototype)
shuffle: true
:::
