# Digital Solutions – worked solutions, 2025 paper

::: tip Source and how to use
Built from the QCAA **2025 Digital Solutions** question and response book, MC book, stimulus book and marking guide (`snr_digital_solutions_25_ea_*` in the [paper files](/digital-solutions/papers); CC BY 4.0, © State of Queensland (QCAA)). Marks and criteria come from the guide. The guide says to *"accept other suitable responses consistent with a reasonable understanding"*, so my wording is a model, not the only right answer. Diagrams (Q11, Q13) and the mock-up (Q16e) are in the question book. **Attempt first, then compare.**
:::

## Section 1: multiple choice (10 marks)
| Q | Ans | Reasoning |
|---|---|---|
| 1 | D | RSA is **asymmetric**: one (public) key encrypts, a second (private) key decrypts |
| 2 | A | **Hashing** is one-way and turns any-length input into a fixed-length output |
| 3 | D | Splitting code into blocks to cut complexity is **modularisation** |
| 4 | A | Unauthorised access to stored recordings breaches the **security of personal information** principle (APP 11) |
| 5 | B | **FTP** transfers files between computers |
| 6 | B | Properties are `song`, `duration`, `band` = **3** |
| 7 | C | Brute force: Caesar has only 25 useful keys, Gronsfeld with a 6-digit key has 10⁶, Vigenère with a 6-letter keyword has 26⁶ ≈ 309 million. Least to most secure: **Caesar, Gronsfeld, Vigenère** |
| 8 | A | XOR of each plaintext character with the key character produces the ciphertext, so line 10 **encrypts** |
| 9 | D | Efficient data processing needs **scalable database design** |
| 10 | B | Accidentally changing data compromises **integrity** |

## Section 2: short response (36 marks)

### Q11 (7 marks) Interpret a data flow diagram

<Diagram name="digital-dfd-example" />
Each mark is one relationship between the external entity **Student** and a process or data store, so write one clear sentence for each:
1. **Student → Book delivery:** the student inputs a book ID, and receives the book back.
2. **Student ↔ Search process:** the student enters keywords (title, author, topic) and receives matching book IDs and statuses.
3. **Student and Bookshelves:** the student has no direct data flow, but gets books from the Bookshelves via Book delivery (a **manual** data store).
4–6. **Student and Authors / Titles / Topics:** the student only reaches these **indirectly**, because the Search process uses them to find matches to the keywords.
7. **Recognise the manual nature** of the link between Bookshelves and Book delivery (a physical book is moved, not digital data).

**Marks (guide):** one each for the relationship with Book delivery, Search, Bookshelves, Authors, Titles and Topics (6), plus recognising the manual relationship (1). Name every process and store.

### Q12 (9 marks) Constraints and CIA risks
**a) Three constraints and their impact (3 marks, 1 each)**
- **Time (four weeks):** less testing time, fewer features, risk of bugs at launch.
- **Data stored on the school server:** limited storage, so compress images and limit data.
- **Mobile platform:** the app must work on iOS and Android, which increases development and testing work.

Each answer must **name** the constraint and **state its impact**.

**b) One risk each to confidentiality, integrity, availability, with justification (6 marks, 2 each)**
- **Confidentiality:** no user authentication, so student and staff details and balances could be viewed by anyone.
- **Integrity:** inventory updated manually during the event could be wrong, leading to overselling.
- **Availability:** manual processing of balances delays access to account data during a busy event.

Guide wording: "determines and justifies" a risk for each, so give the risk (1) and the reason it affects C, I or A (1). This question asks you to justify each risk, not to fix it, so don't spend time on recommendations.

### Q13 (4 marks) Data exchange vulnerabilities
Identify two vulnerable points and recommend a strategy for each (1 mark each for the vulnerability, 1 for the strategy):
1. **Payment details sent from the app to the app server:** vulnerable to **man-in-the-middle** attacks and interception. *Strategy:* **strong encryption (SSL/TLS)** or use a VPN, and avoid public Wi-Fi.
2. **Confirmation and gift-card emails to the user's account:** at risk if the email account or device is compromised (keylogger, weak password). *Strategy:* **strong password and multi-factor authentication**, and keep the device free of malware.

Other valid vulnerabilities from the diagram include the payment gateway link and the email server.

### Q14 (8 marks) Desk check
Stimulus 1 has two movies. Create a table that follows the algorithm line by line and record each variable. 1 mark for each of `totalRating`, `numberOfReviews` and `review["rating"]` for **each** movie (6), plus the average for each (2).

**The Legends List** (ratings 5, 4, 3)
| review | review["rating"] | totalRating | numberOfReviews |
|---|---|---|---|
| start | | 0 | 0 |
| 1 | 5 | 5 | 1 |
| 2 | 4 | 9 | 2 |
| 3 | 3 | 12 | 3 |

averageRating = 12 ÷ 3 = **4**.

**The Sequel** (ratings 2, 1, 2)
| review | review["rating"] | totalRating | numberOfReviews |
|---|---|---|---|
| start | | 0 | 0 |
| 1 | 2 | 2 | 1 |
| 2 | 1 | 3 | 2 |
| 3 | 2 | 5 | 3 |

averageRating = 5 ÷ 3 = **1.67** (1.6666…).
Remember the variables reset to 0 at the start of each movie (lines 5–6). Output lines are "Average Rating for The Legends List is: 4" and "… The Sequel is: 1.67".

### Q15 (8 marks) Data dictionary
**a) Data types (6 marks, 1 each)**
| # | Field | Valid type |
|---|---|---|
| 1 | region | VARCHAR (text) |
| 2 | valid_licence | BOOLEAN (true/false) |
| 3 | licence_type | VARCHAR (learner, provisional, open) |
| 4 | registration_period | INT (a number of years) |
| 5 | date_of_birth | DATETIME / DATE |
| 6 | registration_date | DATETIME / DATE |

Pick types that fit the article's use of the data (average age needs a date of birth, "five years" needs a number, "10–20 December" needs a date).

**b) Recommend and justify one change (2 marks)**
- *If (i) average age by postcode or licence type:* add a `postcode` field (INT or VARCHAR) so ages can be compared in smaller areas than regions.
- *If (ii) learner licences expiring before conversion:* add `licence_number` (to track a licence over time) and replace `valid_licence` with a `licence_status` (VARCHAR: "active", "expired") to see status changes.

**Marks (guide):** a valid change (1) and a justification linked to the chosen question (1).

## Section 3: extended response (21 marks)

### Q16a (4 marks) Components working together

<Diagram name="sol-2025-q16-traffic" />
Explain **each component's role** and **the emergency priority**:
1. **Sensors** detect the emergency vehicle's speed and position, plus traffic flow, and send the data in real time.
2. **Data processing units** analyse the data, recognise patterns and **predict the vehicle's path and arrival time**.
3. **Adaptive traffic signals** receive the instruction and change timing: green along the predicted path, red or stop on intersecting roads and pedestrian crossings, so other traffic stops safely.
4. **Prioritising passage:** the system continues to update from real-time data, adjusts as conditions change, and returns to normal once the vehicle has passed.

### Q16b (8 marks) Pseudocode with library functions
Available functions (Stimulus 2): `getAdaptiveSignal(name)`, `setAdaptiveSignal(name, signal)`, `evaluateCongestion(name)`, `getVehicleCount(lane)`.
The guide gives 1 mark each for: control structures that form a **coherent solution**; **detects hazard locations**; **prioritises emergency vehicles**; **keeps pedestrians safe**; **three different library functions** (3 marks); and **comments** showing where each criterion is addressed (1).

A compact model (my own, in the style of the guide's sample):
```
BEGIN
SET roads = ["LillyE","LillyW","FaberS","FaberN"]
SET crossings = ["LillyE_cross","LillyW_cross","FaberS_cross","FaberN_cross"]
SET hazard = False
SET emergencyVehicle = False

# CRITERION 1: detect hazard locations
FOR each road IN roads
  IF getVehicleCount(road) > 0 AND sensor reports vehicle speed = 0 AND evaluateCongestion(road) = "high" THEN   # stopped traffic = possible accident
    SET hazard = True
    SET hazardLocation = road
  ENDIF
ENDFOR

# detect emergency vehicle from sensor data
IF sensor reports emergency vehicle approaching THEN
  SET emergencyVehicle = True
  GET emergencyPath = predicted path from data processing unit
ENDIF

# CRITERION 2: keep pedestrians safe
IF hazard = True OR emergencyVehicle = True THEN
  FOR each crossing IN crossings
    IF getAdaptiveSignal(crossing) = "walking" THEN
      setAdaptiveSignal(crossing, "danger")
    ENDIF
  ENDFOR
ENDIF

# CRITERION 3: prioritise passage for emergency vehicles
IF emergencyVehicle = True THEN
  FOR each road IN emergencyPath
    setAdaptiveSignal(road, "yellow")
    WAIT 5 seconds        # avoid sudden changes
    setAdaptiveSignal(road, "green")
  ENDFOR
ELSE
  Run normal adaptive signal management
ENDIF
END
```
**Tips:** (1) comment each criterion, (2) use at least three *different* library functions with the correct parameters, (3) use IF/FOR/WHILE logically and finish with an ELSE or ENDIF, and (4) make the algorithm unambiguous (no vague lines like "do something safe").

### Q16c (3 marks) New feature and component
- **Feature:** enhanced object recognition to detect obstacles, animals, pedestrians outside crossings.
- **Component:** additional cameras at strategic locations (e.g. mid-block crossings).
- **Justification:** they improve the system's ability to identify hazards early and trigger signals that protect vehicles and pedestrians.

### Q16d (4 marks) Two usability principles
Stimulus 3 shows filenames like `Pothole_080503_E.MP4` and locations as longitude/latitude, with an internet connection needed for directions.
| Principle | Identify (1) | Justify (1) |
|---|---|---|
| **Effectiveness** | The app does not help workers do the task accurately and completely | Raw coordinates are not usable, there is no filter by suburb/date, and workers waste time converting to addresses or take poor routes |
| **Safety** (error prevention) | The design lets users make mistakes | Filenames carry no useful meaning, so workers must remember which job they finished and are likely to update the wrong record |

Other valid principles include **efficiency**, **learnability** and **accessibility** if justified by the stimulus.

### Q16e (2 marks) Interface mock-up

<Diagram name="sol-2025-q16e-pothole" />
Sketch the app screen with annotations. 1 mark for a feature that **improves each of your two principles**, with an explanation of how it prevents errors or delays.
- For **effectiveness:** a list showing **suburb or street address**, a **search/filter** (suburb, postcode, date logged), a **distance-from-me sort**, and **offline maps**.
- For **safety:** clear job names (e.g. "Pothole – Smith St"), a **status field** (to do/done), a **confirm dialog** before saving, and a "mark complete" button beside each row.
Annotate each feature: "Addresses replace coordinates so workers can plan a route without conversion".

## What the guide rewards
| Wording in the guide | What to write |
|---|---|
| "identifies **and** explains/justifies" | Two parts, with the second linked to the scenario |
| "determines and justifies a risk to C / I / A" | Name the risk and say why it breaks that property |
| "desk checks … values of …" | A full trace table per movie, with every variable |
| "uses pseudocode to symbolise an unambiguous algorithm" | Standard keywords, indentation, no vague English |
| "incorporates one / a second / a third code library function" | Use the functions in the stimulus and count three different ones |
| "includes code comments to identify where criteria are addressed" | A comment line for each criterion |
| "recommends … and justifies" | The suggestion plus the reason |
| "symbolises and explains features" | A drawing **and** an annotation |

See also [past papers analysis](/digital-solutions/past-papers) and [worked examples](/digital-solutions/practice).
