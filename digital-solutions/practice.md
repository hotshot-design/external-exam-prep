# Digital Solutions – worked examples and practice

::: warning Study aid
Examples are written for revision. The exam uses unseen stimulus, so practise the **methods** (trace tables, DFDs, SQL, evaluation).
:::

## 1. Ciphers

### Caesar cipher (shift 3)
`HELLO` → shift each letter 3 places forward → **KHOOR**. Decrypt by shifting back 3.
**Weakness:** only 25 possible shifts (brute force), and letter frequency is preserved.

### Vigenère cipher (key `KEY`)
Plaintext `ATTACK`, key repeats as `KEYKEY`. Add letter positions (A=0) mod 26:
| Plain | A | T | T | A | C | K |
|---|---|---|---|---|---|---|
| Key | K | E | Y | K | E | Y |
| Cipher | K | X | R | K | G | I |

**Ciphertext: KXRKGI.** Stronger than Caesar because the same plaintext letter maps to different cipher letters, but a short repeating key can still be broken.

### One-time pad
Random key as long as the message, used once and kept secret → unbreakable in theory. **Problem:** securely sharing and never reusing keys.

---

## 2. Trace table (desk check)
```
total = 0
FOR i = 1 TO 5
  IF i MOD 2 = 0 THEN
    total = total + i * 2
  ELSE
    total = total + i
  ENDIF
ENDFOR
OUTPUT total
```
| i | i MOD 2 | total after |
|---|---|---|
| 1 | 1 | 1 |
| 2 | 0 | 5 |
| 3 | 1 | 8 |
| 4 | 0 | 16 |
| 5 | 1 | 21 |

**Output: 21.**

**Operators:** `17 DIV 5 = 3`, `17 MOD 5 = 2`, real division `17 / 5 = 3.4`.

---

## 3. Data flow diagram: online library loans (described)
**External entities:** Member, Librarian.
**Processes:** 1 Validate login; 2 Process loan; 3 Update catalogue.
**Data stores:** D1 Member records; D2 Book catalogue; D3 Loan records.

| From | Data flow | To |
|---|---|---|
| Member | login details | 1 Validate login |
| 1 Validate login | member details lookup | D1 Member records |
| Member | book request | 2 Process loan |
| 2 Process loan | availability query | D2 Book catalogue |
| 2 Process loan | loan record | D3 Loan records |
| 2 Process loan | loan confirmation | Member |
| Librarian | new book details | 3 Update catalogue |
| 3 Update catalogue | catalogue update | D2 Book catalogue |

**Rules to remember (Gane-Sarson, as in the syllabus):** every flow is labelled with a **noun**; processes have **verb or verb-object names** and are **numbered**; data stores are numbered and typed **D** (data on disk), **M** (manual: paper or manually processed data) or **T** (temporary or transient, e.g. RAM or cache); entities may **not** send data directly to other entities or data stores, or get data directly from stores; each process has at least one input and one output.

---

## 4. SQL practice
**Tables:** `Student(id, name, year)`, `Enrolment(student_id, course, mark)`.

1. List all students in Year 12 ordered by name.
```sql
SELECT name FROM Student WHERE year = 12 ORDER BY name;
```
2. Show each course with its average mark, only where average is above 70.
```sql
SELECT course, AVG(mark) AS average
FROM Enrolment
GROUP BY course
HAVING AVG(mark) > 70;
```
3. Show student names with their marks for 'Maths'.
```sql
SELECT Student.name, Enrolment.mark
FROM Student
INNER JOIN Enrolment ON Enrolment.student_id = Student.id
WHERE Enrolment.course = 'Maths';
```
4. Add a student and update a mark.
```sql
INSERT INTO Student (id, name, year) VALUES (101, 'Sam', 12);
UPDATE Enrolment SET mark = 85 WHERE student_id = 101 AND course = 'Maths';
```
**Reminders:** `WHERE` filters rows before grouping; `HAVING` filters groups afterwards.

---

## 5. Australian Privacy Principles (APPs 1–13)
| # | Principle |
|---|---|
| 1 | Open and transparent management of personal information |
| 2 | Anonymity and pseudonymity |
| 3 | Collection of solicited personal information |
| 4 | Dealing with unsolicited personal information |
| 5 | Notification of the collection |
| 6 | Use or disclosure |
| 7 | Direct marketing |
| 8 | Cross-border disclosure |
| 9 | Government related identifiers |
| 10 | Quality of personal information |
| 11 | Security of personal information |
| 12 | Access to personal information |
| 13 | Correction of personal information |

Link examples to a scenario: encryption at rest and in transit supports **APP 11**; asking users to correct data supports **APP 13**; sending data overseas triggers **APP 8**.

---

## 6. Evaluation model answer
**Question:** *Evaluate the security of a system that sends customer details to a payment API using HTTP and stores passwords in plain text. Recommend improvements. (6)*

> The system fails the **confidentiality** and **integrity** requirements. Sending details over HTTP exposes them to interception, and storing plain-text passwords means a breach reveals every credential. **Recommendation 1:** use **HTTPS/TLS** to encrypt data in transit, protecting confidentiality and reducing the risk of tampering. **Recommendation 2:** store passwords as **salted hashes**, so that stolen data cannot be reversed directly. **Recommendation 3:** add **multi-factor authentication** to reduce the impact of stolen passwords. These changes may add processing time and complexity (small cost to efficiency and usability) but significantly improve compliance with **APP 11 (security)** and customer trust, so the benefits outweigh the costs.

---

## 6b. Exam-pattern extras (2024–25)

### JSON and pseudocode: average, count and age
```
READ jsonData INTO players
FOR each player IN players DO
  SET totalRating = 0
  SET numberOfReviews = 0
  FOR each review IN player["reviews"] DO
    totalRating = totalRating + review["rating"]
    numberOfReviews = numberOfReviews + 1
  ENDFOR
  IF numberOfReviews > 0 THEN
    averageRating = totalRating / numberOfReviews
  ELSE
    averageRating = "No ratings"
  ENDIF
  OUTPUT player["title"], averageRating
ENDFOR
```
*Percentage:* `percentWon = gamesWon / gamesPlayed * 100`. *Age:* `age = currentYear - birthYear`, then subtract 1 if the birthday has not yet happened this year. **Desk check** = a table with one row per step and one column per variable.

### Data dictionary (2025 Q15)
| Field | Data type | Example / rule |
|---|---|---|
| region | VARCHAR | text such as "Wide Bay-Burnett" |
| valid_licence | BOOLEAN | true/false |
| licence_type | VARCHAR | learner, provisional, open |
| registration_period | INT | number of years |
| date_of_birth, registration_date | DATE / DATETIME | a date |

Choose the type from what the data **means and how it will be used** (calculate average age = date; compare = number; yes/no = boolean). A good "recommend a change" adds a field (e.g. `postcode`, `licence_number`) or a better type, and **justifies** it for the question being asked.

### Ciphers: Gronsfeld and XOR
- **Gronsfeld** uses a number key; each digit shifts a letter: key `123`, plaintext `CAT` → C+1 = D, A+2 = C, T+3 = W → **DCW**.
- **Brute-force ranking:** Caesar (25 keys) < Gronsfeld with a 6-digit key (10⁶ keys) < Vigenère with a 6-letter keyword (26⁶ ≈ 309 million keys).
- **XOR** (used in one-time pads): bits are 1 when they differ. `1010 XOR 0110 = 1100`. XOR with the same key again restores the plaintext. A one-time pad needs a **random key at least as long as the message, used once**.

### CIA risk-and-fix pairs (use in "analyse the scenario" answers)
| Risk | Property | Fix |
|---|---|---|
| Data intercepted in transit (man-in-the-middle, public Wi-Fi) | Confidentiality | **TLS/SSL encryption**, VPN, avoid public Wi-Fi |
| Stolen or weak passwords, no login | Confidentiality | **Multi-factor authentication**, strong passwords, role-based access control |
| Manual or unvalidated data entry, shared IDs | Integrity | Input validation, automatic updates, cross-checks, audit logs |
| DDoS, hardware failure, ransomware | Availability | Load balancing, backups, redundancy, firewalls |
| Unencrypted stored data | Confidentiality | Encrypt data at rest, hash passwords with salt |

## 7. Practice questions
1. Encrypt `CODE` using a Caesar shift of 2.
2. Complete a trace table for the loop below (the `OUTPUT` is **inside** the loop):
   ```
   SET x = 10
   WHILE x > 0 DO
     x = x - 3
     OUTPUT x
   ENDWHILE
   ```
   (Answer: outputs 7, 4, 1, −2. The loop stops when x is no longer greater than 0.)
3. Explain **latency** and **jitter** and why jitter matters for video calls.
4. Describe the difference between **symmetric** and **asymmetric** encryption and give one use for each.
5. Draw a DFD for a school canteen ordering app.
6. Write an SQL query returning the number of orders per customer, only for customers with more than 5 orders.
7. Evaluate the **personal, social and economic** impacts of an AI tool that analyses student data.
8. Explain how hashing and checksums differ.

### Answers (short)
1. `CODE` → **EQFG**.
2. Outputs 7, 4, 1, −2 (the final −2 is output before the condition `x > 0` is tested again).
3. Latency = delay; jitter = variation in delay. Jitter causes stuttering and out-of-sync video/audio.
4. Symmetric: one shared key (AES), good for bulk data. Asymmetric: key pair (RSA), good for key exchange and digital signatures.
5. Entities: Student, Canteen staff. Processes: place order, prepare order, take payment. Stores: menu, orders. Label all flows.
6. `SELECT customer_id, COUNT(*) FROM orders GROUP BY customer_id HAVING COUNT(*) > 5;`
7. Mention personal (privacy, bias), social (trust, equity), economic (efficiency, cost) with a judgement.
8. Hashing is a one-way fingerprint (integrity/passwords); a checksum detects accidental errors in transmission.
