# Digital Solutions – Unit 4: Digital impacts

::: warning Check against class notes
Structure follows Unit 4 subject matter (syllabus pp.30–33). Add your teacher's examples and any specific languages used.
:::

## Topic 1: Digital methods for exchanging data

### Securing data

<Diagram name="digital-xor" caption="XOR" />

<Diagram name="digital-caesar" caption="Caesar cipher" />

<Diagram name="digital-hashing" caption="Hashing" />

<Diagram name="digital-sym-asym" caption="Symmetric vs asymmetric" />

<Diagram name="digital-cia" caption="CIA triad" />
- **Authentication:** 2FA/MFA (verification codes vs biometrics).
- **Symmetric** encryption (one shared key): DES, Triple DES, **AES**, Blowfish, Twofish. Fast; key distribution is the problem.
- **Asymmetric** encryption (public/private key pair): **RSA**. Slower; solves key exchange.
- **Hashing** (one-way, integrity checks, password storage), **checksums** (detect corruption), **compression** (reduce size).
- **Classical ciphers to analyse and write in pseudocode:** Caesar (shift), polyalphabetic (Vigenère, Gronsfeld), **one-time pad** (theoretically unbreakable if key is truly random, as long as the message, used once).
- **CIA triad:** Confidentiality, Integrity, Availability.

### Networks and exchange

<Diagram name="digital-data-exchange" caption="Data exchange components" />
- **Performance metrics:** latency (delay), jitter (variation in delay), reliability/timeliness of delivery.
- **Principles:** protocols (TCP/IP, HTTP, FTP, VPN), packet switching, error detection and correction, routing/forwarding, flow and congestion control, quality of service (QoS).
- **Data exchange methods:** REST APIs; formats **JSON** and **XML**.
- **Sub-systems:** front end, back end; how they work together.

### Privacy and ethics
- **Australian Privacy Principles (APPs, 2014)** and ethics for personal and sensitive data.

### Emerging technologies
- Machine learning, deep learning, neural networks, NLP, reinforcement learning – basic definitions and how algorithms process data differently.

### Design

<Diagram name="digital-useability" caption="Useability principles" />
- **Useability principles (syllabus): accessibility, effectiveness, safety, utility and learnability.** Use these names in answers (e.g. 2025 Q16d used *effectiveness* and *safety*).
- **Elements of visual communication (limited to):** space, line, colour, shape, texture, tone, form, proportion and scale. **Principles (limited to):** balance, contrast, proximity, harmony, alignment, repetition and hierarchy.
- User interface skills: symbolise ideas with sketches, diagrams or mock-ups, then evaluate and recommend using the useability principles.
- **Naming conventions, data formats and structures.**

## Topic 2: Complex digital data exchange problems and solution requirements

<Diagram name="digital-dfd-example" caption="DFD example" />

<Diagram name="digital-dfd-symbols" caption="DFD symbols" />
- **Local vs global variables** (scope).
- Analyse problems: scope, constraints, limitations, requirements, modularity, risks to **confidentiality, integrity, availability and privacy**, existing library code, success criteria.
- Decomposition: constraints, risks, tools/libraries/frameworks, storage/output needs, interface.
- **Data flow diagrams (DFD, Gane-Sarson notation):** four symbols: **external entity/source** (outside the system), **process** (transforms input flows to output flows), **data store** (repository) and **data flow** (labelled arrow). Conventions: nouns for entities, flows and stores; verb or verb-object names for processes; **number** processes and stores; type each store **D** (disk), **M** (manual) or **T** (temporary/transient). Entities may not send data to, or get data from, other entities or stores directly; data must pass through a process.
- Data quality: completeness, consistency, integrity.
- **Pseudocode** and comments/annotations.

## Topic 3: Prototype digital data exchanges
### Algorithms and programming
- **Constructs:** assignment, sequence, selection, condition, iteration, modularisation.
- **Five features of programming:** variables, control structures, data structures, syntax, libraries/classes.
- **Good practice:** dependability, efficiency, testing, debugging, error correction, comments, consistent naming, simplicity, portability.
- **Operators:** arithmetic, comparison, logical, **real division, integer division, modulus**.
- **Data types and conversion**, error-checking functions, **1D arrays/lists**.
- **Desk checks** (trace tables) to predict output and find errors.

### SQL (syllabus list)
`CREATE`, `DROP`, `ALTER`; `INSERT`, `UPDATE`; `SELECT … WHERE … GROUP BY … HAVING … ORDER BY`; sub-selects; `INNER JOIN`.

Example:
```sql
SELECT customer.name, COUNT(orders.id) AS total
FROM customer
INNER JOIN orders ON orders.customer_id = customer.id
WHERE orders.status = 'shipped'
GROUP BY customer.name
HAVING COUNT(orders.id) > 2
ORDER BY total DESC;
```

### Pseudocode example (Caesar cipher)
```
BEGIN encrypt(text, shift)
  result = ""
  FOR each character c IN text
    IF c is a letter THEN
      shifted = ((ASCII(c) - base + shift) MOD 26) + base   // base = ASCII('A') or ASCII('a')
      result = result + CHAR(shifted)
    ELSE
      result = result + c
    ENDIF
  ENDFOR
  RETURN result
END
```

### Evaluating
- **Personal, social and economic impacts** of data exchange, storage, accuracy, ownership, emerging technologies (e.g. AI).
- Test solutions: accuracy, reliability, maintainability, efficiency, effectiveness, useability.
- Justified recommendations on **security impacts**.

## Exam technique
- Perusal: scan for diagrams/code that need desk-checking.
- For "evaluate/justify": give a judgement, evidence from the stimulus, and a recommendation.
- For DFDs: label every flow; processes need inputs and outputs; data stores connect only to processes.
- Show working for trace tables and calculations; use correct SQL syntax.
