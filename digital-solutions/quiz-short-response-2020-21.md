# Digital Solutions quiz: short responses 2020–2021

Questions adapted from the QCAA short-response and extended-response questions, based on the marking guide's sample answers. These years were set under the earlier syllabus but the content is still examined. Each explanation links to the question paper and the marking guide (there are no worked solutions for these years). Source: QCAA external assessments (CC BY 4.0, © State of Queensland (QCAA)).

## 2021 paper

:::quiz
question: Match each item in the online sales platform to its data flow diagram role.
pair: Customer => External entity
pair: Shopping cart => Data store
pair: Confirm order => Process
pair: Product price updates sent from business owner to Update products => Data flow
explanation: The guide rewards external entities for customer and business owner, data stores for customer data, products, cart and orders, and processes such as payments and confirm order. (QCAA 2021 Q11 — [Question paper, p.4](/digital-solutions/papers/snr_digital_solutions_21_ea_question_response.pdf#page=4) · [Marking guide, p.4](/digital-solutions/papers/snr_digital_solutions_21_ea_mark_guide_pub.pdf#page=4))
:::

:::quiz
question: The online sales platform has data stores for customer data, products, shopping cart and orders. How many data stores must the data flow diagram show?
answer-input: 4
explanation: The guide awards one mark each for the customer data, shopping cart, orders and products data stores. (QCAA 2021 Q11 — [Question paper, p.4](/digital-solutions/papers/snr_digital_solutions_21_ea_question_response.pdf#page=4) · [Marking guide, p.4](/digital-solutions/papers/snr_digital_solutions_21_ea_mark_guide_pub.pdf#page=4))
:::

:::quiz
question: Match each CIA aspect to the risk example for the remote car unlock app.
pair: Confidentiality => An unauthorised person observes a password in transit
pair: Integrity => Data is corrupted or manipulated so the wrong car is unlocked
pair: Availability => Interference stops data packets reaching their destination
explanation: These are the risks and examples in the 2021 sample response to Question 12a. (QCAA 2021 Q12 — [Question paper, p.6](/digital-solutions/papers/snr_digital_solutions_21_ea_question_response.pdf#page=6) · [Marking guide, p.5](/digital-solutions/papers/snr_digital_solutions_21_ea_mark_guide_pub.pdf#page=5))
:::

:::quiz
question: Which action best reduces the confidentiality risk of a password being stolen in transit in the car unlock app?
answer-correct: Encrypt the data so it cannot be read if intercepted
answer: Compress the data to reduce its size
answer: Store a backup copy of the password
answer: Add a longer username
explanation: The guide says data would need to be encrypted so it cannot be stolen. (QCAA 2021 Q12 — [Question paper, p.6](/digital-solutions/papers/snr_digital_solutions_21_ea_question_response.pdf#page=6) · [Marking guide, p.5](/digital-solutions/papers/snr_digital_solutions_21_ea_mark_guide_pub.pdf#page=5))
shuffle: true
:::

:::quiz
question: Which Australian Privacy Principle does the guide give for an app that should de-identify or destroy personal information once it is no longer in use?
answer-correct: Security of personal information
answer: Openness and transparency
answer: Direct marketing
answer: Anonymity and pseudonymity
explanation: The guide names Security of personal information and says an administrator should de-identify or destroy data no longer in use. (QCAA 2021 Q12 — [Question paper, p.6](/digital-solutions/papers/snr_digital_solutions_21_ea_question_response.pdf#page=6) · [Marking guide, p.5](/digital-solutions/papers/snr_digital_solutions_21_ea_mark_guide_pub.pdf#page=5))
shuffle: true
:::

:::quiz
question: A Caesar cipher with shift 4 was used (each letter moved 4 places forward). Decrypt the password KYIWW by shifting each letter back 4 places.
answer-input: GUESS
explanation: K-4=G, Y-4=U, I-4=E, W-4=S, W-4=S; the guide requires a five-iteration desk check. The shift of 4 is assumed since the paper does not state it. (QCAA 2021 Q12 — [Question paper, p.6](/digital-solutions/papers/snr_digital_solutions_21_ea_question_response.pdf#page=6) · [Marking guide, p.5](/digital-solutions/papers/snr_digital_solutions_21_ea_mark_guide_pub.pdf#page=5))
:::

:::quiz
question: Using a Caesar cipher with shift 3 on the alphabet A to Z with wrap-around, encrypt XYZ.
answer-input: ABC
explanation: X, Y, Z move 3 places forward and wrap to A, B, C; this is the SHIFT step in the guide's FOR loop. (QCAA 2021 Q12 — [Question paper, p.6](/digital-solutions/papers/snr_digital_solutions_21_ea_question_response.pdf#page=6) · [Marking guide, p.5](/digital-solutions/papers/snr_digital_solutions_21_ea_mark_guide_pub.pdf#page=5))
:::

:::quiz
question: Match each line of the guide's Caesar cipher pseudocode to its purpose.
pair: SET alphabet = ABCDEFGHIJKLMNOPQRSTUVWXYZ => Declares the letters used to shift characters
pair: FOR each character in plainText => Iterates over the password one character at a time
pair: SHIFT character by keyShift => Encrypts a character using the key
pair: RETURN encryptedText => Gives back the encrypted password
explanation: The guide rewards an alphabet declaration, a FOR loop, a shift function using the key and a RETURN. (QCAA 2021 Q12 — [Question paper, p.6](/digital-solutions/papers/snr_digital_solutions_21_ea_question_response.pdf#page=6) · [Marking guide, p.5](/digital-solutions/papers/snr_digital_solutions_21_ea_mark_guide_pub.pdf#page=5))
:::

:::quiz
question: Match each security measure for the online silent auction to what it does.
pair: Checksum => Detects if data was corrupted or manipulated when the values differ
pair: Encryption => Scrambles data so it is unreadable in transit, decrypted with a secret key
pair: Authentication => Verifies bidder identity using a digital signature or authentication code
explanation: From the 2021 sample answer to Question 13a. (QCAA 2021 Q13 — [Question paper, p.10](/digital-solutions/papers/snr_digital_solutions_21_ea_question_response.pdf#page=10) · [Marking guide, p.7](/digital-solutions/papers/snr_digital_solutions_21_ea_mark_guide_pub.pdf#page=7))
:::

:::quiz
question: In the guide, AES supersedes DES and 3DES. What block size in bits does AES use?
answer-input: 128
explanation: The guide says AES uses 128-bit blocks (keys of 128, 192 or 256 bits), whereas DES and 3DES use 64-bit blocks. (QCAA 2021 Q13 — [Question paper, p.10](/digital-solutions/papers/snr_digital_solutions_21_ea_question_response.pdf#page=10) · [Marking guide, p.7](/digital-solutions/papers/snr_digital_solutions_21_ea_mark_guide_pub.pdf#page=7))
:::

:::quiz
question: On the match manager login view, the current view is white and other views are grey in the navigation. Which element is used to create visual hierarchy here?
answer-correct: Tone
answer: Line
answer: Space
answer: Repetition
explanation: The guide says visual hierarchy in the navigation is achieved with tone, active view white and inactive views greyed out. (QCAA 2021 Q14 — [Question paper, p.12](/digital-solutions/papers/snr_digital_solutions_21_ea_question_response.pdf#page=12) · [Marking guide, p.8](/digital-solutions/papers/snr_digital_solutions_21_ea_mark_guide_pub.pdf#page=8))
shuffle: true
:::

:::quiz
question: Match each data exchange component of the match manager app to its role.
pair: User interface => User's device, browser and the HTML, CSS and JavaScript website
pair: Server interface => Web server handling requests, with server-side code such as PHP or Node.js
pair: Data interface => DBMS that retrieves and stores data, e.g. via SQL queries
explanation: From the 2021 sample response to Question 14b. (QCAA 2021 Q14 — [Question paper, p.12](/digital-solutions/papers/snr_digital_solutions_21_ea_question_response.pdf#page=12) · [Marking guide, p.8](/digital-solutions/papers/snr_digital_solutions_21_ea_mark_guide_pub.pdf#page=8))
:::

:::quiz
question: Match each user survey finding to the guide's recommendation.
pair: Password is visible when logging in => Add a show/hide option for the password field
pair: 401 Unauthorised errors when clicking input or confirm => Add user-level access separating administrators and users
pair: No way of resetting or changing a password => Add a forgot/reset password link
pair: Closing the login window leaves the user stuck => Remove the close button on the login window
explanation: Recommendations are drawn from the 2021 sample responses to Questions 14c and 14d. (QCAA 2021 Q14 — [Question paper, p.12](/digital-solutions/papers/snr_digital_solutions_21_ea_question_response.pdf#page=12) · [Marking guide, p.8](/digital-solutions/papers/snr_digital_solutions_21_ea_mark_guide_pub.pdf#page=8))
:::

## 2020 paper

:::quiz
question: Match each visual communication idea to how the 2020 drone control panel used it.
pair: Spacing => Even, generous clear space between elements avoids clutter
pair: Contrast => Dial needles and distance values stand out against the background
pair: Alignment => Readings are aligned on both sides and mirrored
pair: Repetition => Shapes, spacing and alignment are repeated throughout the panel
pair: Proximity => Camera views are placed close to the actual camera locations on the drone
explanation: Taken from the 2020 marking guide sample answers for Questions 11a and 11c. (QCAA 2020 Q11 — [Question paper, p.4](/digital-solutions/papers/snr_digital_solutions_20_ea_question_response.pdf#page=4) · [Marking guide, p.4](/digital-solutions/papers/snr_digital_solutions_20_ea_mark_guide_pub.pdf#page=4))
:::

:::quiz
question: Marine markers send a JSON record with an ID, a fault flag and a date/time, but the central table is MarineMarkerStatus [MarkerID, MarkerType, AreaDescription, Latitude, Longitude, Fault_Detected]. Why is the solution unreliable for a quarterly summary of faults?
answer-correct: It has no date and time field, so historical fault events are not stored
answer: The JSON format cannot be sent over a satellite link
answer: Latitude and longitude cannot be stored in a table
answer: The fault flag must be stored as text rather than True/False
explanation: The guide says the structure does not allow date and time, so history is not kept and no ongoing summary or quarterly report is possible. (QCAA 2020 Q12 — [Question paper, p.6](/digital-solutions/papers/snr_digital_solutions_20_ea_question_response.pdf#page=6) · [Marking guide, p.7](/digital-solutions/papers/snr_digital_solutions_20_ea_mark_guide_pub.pdf#page=7))
shuffle: true
:::

:::quiz
question: The IoT device broadcasts the JSON fields QldMarineMarkerId, QldMarineMarkerFault and QldMarineMarkerDateTime. Which one of these has no matching column in the central MarineMarkerStatus table, threatening accuracy? Give the field name.
answer-input: QldMarineMarkerDateTime
answer-input: MarkerDateTime
answer-input: date and time
explanation: The guide states the only threat to accuracy is the absence of date and time data, which breaks the quarterly report. (QCAA 2020 Q12 — [Question paper, p.6](/digital-solutions/papers/snr_digital_solutions_20_ea_question_response.pdf#page=6) · [Marking guide, p.7](/digital-solutions/papers/snr_digital_solutions_20_ea_mark_guide_pub.pdf#page=7))
:::

:::quiz
question: Match each criterion to how the marine marker proposal was evaluated against it in the guide.
pair: Reliability => No date/time stored, so no historical log of fault events
pair: Accuracy => Missing date and time means the quarterly report request cannot be met
pair: Maintainability => Needs human intervention to update fault status once a marker is repaired
pair: Security => No mention of encryption of broadcast data, secure storage or user authentication
explanation: These evaluations are from the 2020 sample answers for Questions 12a and 12b. (QCAA 2020 Q12 — [Question paper, p.6](/digital-solutions/papers/snr_digital_solutions_20_ea_question_response.pdf#page=6) · [Marking guide, p.7](/digital-solutions/papers/snr_digital_solutions_20_ea_mark_guide_pub.pdf#page=7))
:::

:::quiz
question: Which is a valid reason JSON is an effective way to exchange data between the marine markers and the central database?
answer-correct: It is efficient and human readable, so it is easy to interpret even by non-coders
answer: It automatically encrypts the data in transit
answer: It is a compiled binary format that cannot be altered
answer: It enforces a fixed relational schema on every device
explanation: The guide justifies JSON as efficient and retaining human readability. (QCAA 2020 Q12 — [Question paper, p.6](/digital-solutions/papers/snr_digital_solutions_20_ea_question_response.pdf#page=6) · [Marking guide, p.7](/digital-solutions/papers/snr_digital_solutions_20_ea_mark_guide_pub.pdf#page=7))
shuffle: true
:::

:::quiz
question: Members table: members(id, given_name, last_name, email, phone). Complete the SQL to list all members by name sorted alphabetically by last name: SELECT given_name, last_name FROM members ORDER BY ____ ASC; Give the column name.
answer-input: last_name
explanation: The guide's SQL answer is SELECT given_name, last_name FROM members ORDER BY last_name ASC. (QCAA 2020 Q13 — [Question paper, p.8](/digital-solutions/papers/snr_digital_solutions_20_ea_question_response.pdf#page=8) · [Marking guide, p.8](/digital-solutions/papers/snr_digital_solutions_20_ea_mark_guide_pub.pdf#page=8))
:::

:::quiz
question: In the pseudocode for listing members who have been members for 10 or more years, which condition is correct (membershipYears = current date minus joinDate)?
answer-correct: IF membershipYears >= 10
answer: IF membershipYears > 10
answer: IF membershipYears <= 10
answer: IF membershipYears = 10
explanation: The guide uses membershipYears >= 10 so exactly 10 years is included; results are ordered by joinDate ascending. (QCAA 2020 Q13 — [Question paper, p.8](/digital-solutions/papers/snr_digital_solutions_20_ea_question_response.pdf#page=8) · [Marking guide, p.8](/digital-solutions/papers/snr_digital_solutions_20_ea_mark_guide_pub.pdf#page=8))
shuffle: true
:::

:::quiz
question: Contact details are in members and points_balance is in members_activity (both have an id column). Complete: SELECT ... FROM members JOIN members_activity ON members.id = members_activity.____ WHERE points_balance > 3000; Give the column name.
answer-input: id
explanation: The guide's SQL joins the two tables on id so contact details can be filtered by points_balance > 3000. (QCAA 2020 Q13 — [Question paper, p.8](/digital-solutions/papers/snr_digital_solutions_20_ea_question_response.pdf#page=8) · [Marking guide, p.8](/digital-solutions/papers/snr_digital_solutions_20_ea_mark_guide_pub.pdf#page=8))
:::

:::quiz
question: The Blowfish function accepts 64-bit text blocks and UTF-8 characters are 8 bits each. How many characters is one block (and the key) required to be?
answer-input: 8
explanation: 64 bits divided by 8 bits per UTF-8 character is 8; the guide checks Length of key = 8 and splits text into 8-character BlockSets. (QCAA 2020 Q14 — [Question paper, p.12](/digital-solutions/papers/snr_digital_solutions_20_ea_question_response.pdf#page=12) · [Marking guide, p.11](/digital-solutions/papers/snr_digital_solutions_20_ea_mark_guide_pub.pdf#page=11))
:::

:::quiz
question: Following the guide's approach of padding text with spaces and splitting it into 8-character blocks, how many blocks are needed to encrypt a 19-character message?
answer-input: 3
explanation: 19 characters padded to 24 gives three 8-character blocks, each passed to Blowfish(BlockSet, MyKeySet, 1). (QCAA 2020 Q14 — [Question paper, p.12](/digital-solutions/papers/snr_digital_solutions_20_ea_question_response.pdf#page=12) · [Marking guide, p.11](/digital-solutions/papers/snr_digital_solutions_20_ea_mark_guide_pub.pdf#page=11))
:::

:::quiz
question: Which implementation describes the useability principle of responsiveness (utility) for the programmers' web app?
answer-correct: Using breakpoints and a grid layout so the interface adjusts to all viewport sizes
answer: Encrypting every page with Blowfish
answer: Using a single fixed-width layout for desktop only
answer: Requiring users to re-enter the key on every page
explanation: The guide describes responsiveness as adjusting to all display devices, implemented with breakpoints and a grid. (QCAA 2020 Q14 — [Question paper, p.12](/digital-solutions/papers/snr_digital_solutions_20_ea_question_response.pdf#page=12) · [Marking guide, p.11](/digital-solutions/papers/snr_digital_solutions_20_ea_mark_guide_pub.pdf#page=11))
shuffle: true
:::

:::quiz
question: One strength of the programmers using different programming languages for their programs is that:
answer-correct: if one program is breached the damage is contained, as the same attack may not work on another language
answer: the encrypted text becomes shorter
answer: Blowfish keys no longer need to be 64 bits
answer: the emails no longer need to be copied and pasted
explanation: The guide gives containment of a breach as the strength; a weakness is that some languages have more vulnerabilities. (QCAA 2020 Q14 — [Question paper, p.12](/digital-solutions/papers/snr_digital_solutions_20_ea_question_response.pdf#page=12) · [Marking guide, p.11](/digital-solutions/papers/snr_digital_solutions_20_ea_mark_guide_pub.pdf#page=11))
shuffle: true
:::
