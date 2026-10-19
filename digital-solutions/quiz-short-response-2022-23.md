# Digital Solutions quiz: short responses 2022–2023

Questions adapted from the QCAA short-response and extended-response questions, based on the marking guide's sample answers. These years were set under the earlier syllabus but the content is still examined. Each explanation links to the question paper and the marking guide (there are no worked solutions for these years). Source: QCAA external assessments (CC BY 4.0, © State of Queensland (QCAA)).

## 2023 paper

:::quiz
question: Match each criterion for the digital ticketing system to the technique in the guide.
pair: Keep data size in data stores to a minimum => Use data compression
pair: Transmit data securely => Use encryption
explanation: From the 2023 sample answer to Question 11a. (QCAA 2023 Q11 — [Question paper, p.4](/digital-solutions/papers/snr_digital_solutions_23_ea_question_response.pdf#page=4) · [Marking guide](/digital-solutions/papers/snr_digital_solutions_23_ea_mark_guide_pub.pdf))
:::

:::quiz
question: In the guide's login algorithm for the ticketing system, what happens to the password before it is compared with the data store?
answer-correct: It is hashed
answer: It is converted to upper case
answer: It is emailed to the user
answer: It is deleted
explanation: The sample answer includes HASH password, then verifies the username and hashed password against the data store. (QCAA 2023 Q11 — [Question paper, p.4](/digital-solutions/papers/snr_digital_solutions_23_ea_question_response.pdf#page=4) · [Marking guide](/digital-solutions/papers/snr_digital_solutions_23_ea_mark_guide_pub.pdf))
shuffle: true
:::

:::quiz
question: For safety, the guide's login algorithm handles an unsuccessful login by:
answer-correct: Outputting an error message such as 'Wrong password, try again' or 'Wrong username and/or password, try again'
answer: Ending the program without output
answer: Showing the stored password
answer: Creating a new account
explanation: The guide awards safety marks for handling an incorrect username and an incorrect password with error messages. (QCAA 2023 Q11 — [Question paper, p.4](/digital-solutions/papers/snr_digital_solutions_23_ea_question_response.pdf#page=4) · [Marking guide](/digital-solutions/papers/snr_digital_solutions_23_ea_mark_guide_pub.pdf))
shuffle: true
:::

:::quiz
question: The dentist's van system has no secure login and emails patient data. Which two personal data security needs does the guide identify? Select all that apply.
answer-correct: A secure log-in system to restrict access to the computer
answer-correct: Encryption of patient data when transferring to the central server
answer: Faster internet speed on the van
answer: A larger monitor for the dentist
answer: More frequent roster changes
explanation: The sample answer names a secure log-in system and encryption of patient data in transfer. (QCAA 2023 Q12 — [Question paper, p.6](/digital-solutions/papers/snr_digital_solutions_23_ea_question_response.pdf#page=6) · [Marking guide](/digital-solutions/papers/snr_digital_solutions_23_ea_mark_guide_pub.pdf))
shuffle: true
:::

:::quiz
question: How does a VPN improve data security for the dental van?
answer-correct: It sets up a private, encrypted connection that stops unauthorised interception between the van and the practice
answer: It removes the need to store patient data
answer: It speeds up the email service
answer: It lets all staff share one login
explanation: The guide describes a private connection between the van and practice and encryption protecting data if intercepted. (QCAA 2023 Q12 — [Question paper, p.6](/digital-solutions/papers/snr_digital_solutions_23_ea_question_response.pdf#page=6) · [Marking guide](/digital-solutions/papers/snr_digital_solutions_23_ea_mark_guide_pub.pdf))
shuffle: true
:::

:::quiz
question: One-time pad algorithm encrypts an 8-character word using array index 0 as the first index. The loop starts at FOR i = 0 to 9. What upper bound should replace 9?
answer-input: 7
explanation: Indexes 0 to 7 cover 8 characters; the guide's fix is FOR i = 0 to 7. (QCAA 2023 Q13 — [Question paper, p.8](/digital-solutions/papers/snr_digital_solutions_23_ea_question_response.pdf#page=8) · [Marking guide](/digital-solutions/papers/snr_digital_solutions_23_ea_mark_guide_pub.pdf))
:::

:::quiz
question: Match each faulty line of the one-time pad algorithm to its correction.
pair: Line 9: FOR i = 0 to 9 => FOR i = 0 to 7
pair: Line 12: IF plainText[j] = alphabet[i] => IF plainText[i] = alphabet[j]
pair: Line 18: alphabet(alphabetLocation + key[i]) mod 26 => alphabet[(alphabetLocation + key[i]) mod 26]
pair: Line 21: OUTPUT cipherText[i] => OUTPUT cipherText
explanation: From the 2023 sample answer: i indexes plainText, j indexes the alphabet, the mod belongs inside the brackets, and the output must not use an index. (QCAA 2023 Q13 — [Question paper, p.8](/digital-solutions/papers/snr_digital_solutions_23_ea_question_response.pdf#page=8) · [Marking guide](/digital-solutions/papers/snr_digital_solutions_23_ea_mark_guide_pub.pdf))
:::

:::quiz
question: Why is line 21, OUTPUT cipherText[i], wrong in the one-time pad algorithm?
answer-correct: The index would make it output only one character (or none, due to scope)
answer: It would output the key instead of the cipher text
answer: It would output the cipher text in upper case
answer: It would cause the loop to run forever
explanation: The guide says the index should be removed or only one character will be output. (QCAA 2023 Q13 — [Question paper, p.8](/digital-solutions/papers/snr_digital_solutions_23_ea_question_response.pdf#page=8) · [Marking guide](/digital-solutions/papers/snr_digital_solutions_23_ea_mark_guide_pub.pdf))
shuffle: true
:::

:::quiz
question: Which additional features does the guide suggest to improve accessibility of the smart home app? Select all that apply.
answer-correct: Voice recognition to check status, turn plugs on/off and set schedules
answer-correct: Changing UI colours to suit colour blindness
answer: Removing the back button
answer: Reducing the screen size
answer: Using only icons with no text
explanation: From the 2023 sample answer to Question 14b. (QCAA 2023 Q14 — [Question paper, p.10](/digital-solutions/papers/snr_digital_solutions_23_ea_question_response.pdf#page=10) · [Marking guide](/digital-solutions/papers/snr_digital_solutions_23_ea_mark_guide_pub.pdf))
shuffle: true
:::

:::quiz
question: Candidate X (Year 11, esports captain) is encoded in XML: <candidate><name>Candidate X</name><year>Year 11</year><position>Esports captain ... Give the closing tag that completes the position element.
answer-input: </position>
explanation: The guide uses child containers name, year and position inside a parent candidate container. (QCAA 2023 Q15 — [Question paper, p.13](/digital-solutions/papers/snr_digital_solutions_23_ea_question_response.pdf#page=13) · [Marking guide](/digital-solutions/papers/snr_digital_solutions_23_ea_mark_guide_pub.pdf))
:::

:::quiz
question: In the guide's XML for a nominated candidate, which is the parent container?
answer-correct: candidate
answer: name
answer: year
answer: position
explanation: The guide symbolises a parent candidate container with child name, year and position elements. (QCAA 2023 Q15 — [Question paper, p.13](/digital-solutions/papers/snr_digital_solutions_23_ea_question_response.pdf#page=13) · [Marking guide](/digital-solutions/papers/snr_digital_solutions_23_ea_mark_guide_pub.pdf))
shuffle: true
:::

:::quiz
question: Match each school voting rule to a system feature that enforces it.
pair: Only students and staff can vote => Verify the login email against an imported list of current students and staff
pair: Each user can vote only once => Check for existing votes under the login email; show an error and hide the candidate list
pair: Voting only on the nominated day, 8:30 am to 4:00 pm => Block login outside this time using a time parameter
explanation: From the 2023 sample answer to Question 15b. (QCAA 2023 Q15 — [Question paper, p.13](/digital-solutions/papers/snr_digital_solutions_23_ea_question_response.pdf#page=13) · [Marking guide](/digital-solutions/papers/snr_digital_solutions_23_ea_mark_guide_pub.pdf))
:::

:::quiz
question: Match each process in the guide's voting system data flow diagram to its job.
pair: 1.0 Check voting period and register/login => Checks time and verifies email/password against the school database
pair: 2.0 Check conflicts => Uses the verified email to find conflicts of interest in the school database
pair: 3.0 Check votes and display candidate list => Checks for an existing vote and shows candidates without conflicts
pair: 4.0 Cast votes => Records selected candidates and positions in the voting data store
pair: 5.0 Count votes => Aggregates votes for the admin after the voting period
explanation: From the 2023 sample DFD and the explanation for Question 15d. (QCAA 2023 Q15 — [Question paper, p.13](/digital-solutions/papers/snr_digital_solutions_23_ea_question_response.pdf#page=13) · [Marking guide](/digital-solutions/papers/snr_digital_solutions_23_ea_mark_guide_pub.pdf))
:::

## 2022 paper

:::quiz
question: Which statement correctly contrasts the network transmission protocols HTTP and HTTPS?
answer-correct: HTTPS uses encryption (e.g. TLS) and certificates to confirm server identity, whereas HTTP sends text with no encryption or authentication
answer: HTTP encrypts data with TLS but HTTPS does not
answer: HTTPS is used only between databases, HTTP only between websites
answer: Both protocols encrypt data but HTTP is slower
explanation: From the 2022 sample answer: HTTP offers no encryption or authentication; HTTPS uses TLS and certificates. (QCAA 2022 Q11 — [Question paper, p.4](/digital-solutions/papers/snr_digital_solutions_22_ea_question_response.pdf#page=4) · [Marking guide, p.4](/digital-solutions/papers/snr_digital_solutions_22_ea_mark_guide_pub.pdf#page=4))
shuffle: true
:::

:::quiz
question: Match each algorithm construct to its description.
pair: Assignment => A stated or calculated value stored in a variable
pair: Condition => A comparison that gives a true or false result
pair: Iteration => Statements repeated while a condition is met
pair: Modularisation => Breaking code into smaller reusable chunks that are easier to understand
explanation: These definitions are from the 2022 sample answers to Questions 12a and 12b. (QCAA 2022 Q12 — [Question paper, p.5](/digital-solutions/papers/snr_digital_solutions_22_ea_question_response.pdf#page=5) · [Marking guide, p.4](/digital-solutions/papers/snr_digital_solutions_22_ea_mark_guide_pub.pdf#page=4))
:::

:::quiz
question: Code: calculateInterestRate returns 0.04 if depositAmount <= 10000; 0.03 if depositAmount > 10000 and <= 50000; otherwise 0.02. What rate is returned for a deposit of 10000?
answer-input: 0.04
answer-input: .04
explanation: 10000 satisfies depositAmount <= 10000, so value = 0.04 (line 13 of the stimulus). (QCAA 2022 Q12 — [Question paper, p.5](/digital-solutions/papers/snr_digital_solutions_22_ea_question_response.pdf#page=5) · [Marking guide, p.4](/digital-solutions/papers/snr_digital_solutions_22_ea_mark_guide_pub.pdf#page=4))
:::

:::quiz
question: Using the same rules (0.04 up to 10000, 0.03 up to 50000, otherwise 0.02), what rate is returned for a deposit of 60000?
answer-input: 0.02
answer-input: .02
explanation: 60000 fails both conditions so the ELSE assigns 0.02. (QCAA 2022 Q12 — [Question paper, p.5](/digital-solutions/papers/snr_digital_solutions_22_ea_question_response.pdf#page=5) · [Marking guide, p.4](/digital-solutions/papers/snr_digital_solutions_22_ea_mark_guide_pub.pdf#page=4))
:::

:::quiz
question: What is the purpose of modularisation, e.g. calculateInterestRate being a separate module called at line 5?
answer-correct: It breaks code into smaller parts that are easier to understand and lets the same code be reused
answer: It makes the program run without a computer
answer: It encrypts the code so it cannot be read
answer: It removes the need for variables
explanation: The guide says modularisation breaks code into smaller chunks and allows the same code to be used in different parts of the application. (QCAA 2022 Q12 — [Question paper, p.5](/digital-solutions/papers/snr_digital_solutions_22_ea_question_response.pdf#page=5) · [Marking guide, p.4](/digital-solutions/papers/snr_digital_solutions_22_ea_mark_guide_pub.pdf#page=4))
shuffle: true
:::

:::quiz
question: One-time pad with a = 0 ... z = 25: encrypt plain text letter q with key letter r. Cipher index = (plain index + key index) mod 26. Give the cipher letter.
answer-input: h
explanation: q = 16 and r = 17, so 33 mod 26 = 7 which is h, the first letter of hsnanz in the guide's desk check. (QCAA 2022 Q13 — [Question paper, p.6](/digital-solutions/papers/snr_digital_solutions_22_ea_question_response.pdf#page=6) · [Marking guide, p.5](/digital-solutions/papers/snr_digital_solutions_22_ea_mark_guide_pub.pdf#page=5))
:::

:::quiz
question: One-time pad (a = 0 ... z = 25): plain letter s with key letter h. Give the cipher letter.
answer-input: z
explanation: s = 18 and h = 7 so 25 which is z, the last letter of the guide's output hsnanz. (QCAA 2022 Q13 — [Question paper, p.6](/digital-solutions/papers/snr_digital_solutions_22_ea_question_response.pdf#page=6) · [Marking guide, p.5](/digital-solutions/papers/snr_digital_solutions_22_ea_mark_guide_pub.pdf#page=5))
:::

:::quiz
question: Using the guide's one-time pad method, encrypt the plain text hello with key xmckl. Give the cipher text.
answer-input: eqnvz
explanation: h7+x23=30 mod 26=4 e; e4+m12=16 q; l11+c2=13 n; l11+k10=21 v; o14+l11=25 z. (QCAA 2022 Q13 — [Question paper, p.6](/digital-solutions/papers/snr_digital_solutions_22_ea_question_response.pdf#page=6) · [Marking guide, p.5](/digital-solutions/papers/snr_digital_solutions_22_ea_mark_guide_pub.pdf#page=5))
:::

:::quiz
question: In the student results algorithm, which order matches the guide's sample answer?
answer-correct: Hash the password and call checkLogin; if true getResults for the student ID and decryptData each line; otherwise display Access denied
answer: getResults, then checkLogin, then hashPassword
answer: decryptData every line first, then checkLogin
answer: checkLogin with the plain text password, then display results
explanation: The guide: IF checkLogin(studentID, hashPassword(password)) THEN getResults then decryptData for each line, ELSE Display Access denied. (QCAA 2022 Q14 — [Question paper, p.8](/digital-solutions/papers/snr_digital_solutions_22_ea_question_response.pdf#page=8) · [Marking guide, p.6](/digital-solutions/papers/snr_digital_solutions_22_ea_mark_guide_pub.pdf#page=6))
shuffle: true
:::

:::quiz
question: Match each code library function to its role in the student results system.
pair: hashPassword => Applies a hash function to the plain text password
pair: checkLogin => Checks student ID and hashed password against the database, returning True/False
pair: getResults => Retrieves the encrypted result lines for a student ID
pair: decryptData => Uses the supplied key to decrypt a line of results
explanation: Stimulus 3 function descriptions as used in the 2022 sample answer. (QCAA 2022 Q14 — [Question paper, p.8](/digital-solutions/papers/snr_digital_solutions_22_ea_question_response.pdf#page=8) · [Marking guide, p.6](/digital-solutions/papers/snr_digital_solutions_22_ea_mark_guide_pub.pdf#page=6))
:::

:::quiz
question: In the school fundraising app, which functions should be restricted to administration staff only? Select all that apply.
answer-correct: Adding item details
answer-correct: Viewing payment details
answer-correct: Viewing order history
answer: Logging in
answer: Viewing items
answer: Selecting items
explanation: The guide rewards admin-only access for adding item details, viewing payment details and viewing order history. (QCAA 2022 Q15 — [Question paper, p.10](/digital-solutions/papers/snr_digital_solutions_22_ea_question_response.pdf#page=10) · [Marking guide, p.7](/digital-solutions/papers/snr_digital_solutions_22_ea_mark_guide_pub.pdf#page=7))
shuffle: true
:::

:::quiz
question: Match each wireframe element of the fundraising app to the process or data flow it triggers.
pair: Item tiles => Request item details from the items data store
pair: Buy item button => Selects the item and pushes it to the shopping cart data store
pair: View cart => Displays the selected items and starts checkout
pair: Another user finalising an order => Item data is re-requested so stock availability is updated
explanation: From the 2022 sample answers to Questions 15b and 15c. (QCAA 2022 Q15 — [Question paper, p.10](/digital-solutions/papers/snr_digital_solutions_22_ea_question_response.pdf#page=10) · [Marking guide, p.7](/digital-solutions/papers/snr_digital_solutions_22_ea_mark_guide_pub.pdf#page=7))
:::

:::quiz
question: Match each type of impact of the fundraising app to the example in the guide.
pair: Personal => Users can create an account and purchase items for fundraising
pair: Social => Healthy competition among students to fundraise the most
pair: Economic => Money is raised for school activities or events
explanation: From the 2022 sample answer to Question 15d. (QCAA 2022 Q15 — [Question paper, p.10](/digital-solutions/papers/snr_digital_solutions_22_ea_question_response.pdf#page=10) · [Marking guide, p.7](/digital-solutions/papers/snr_digital_solutions_22_ea_mark_guide_pub.pdf#page=7))
:::
