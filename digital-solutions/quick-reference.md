# Digital Solutions – exam-day quick reference

::: tip Paper (2024–25): 66–67 marks
10 MC + 36 short response + one multi-part extended response (parts a–e, 20–21 marks). 5 min perusal + 120 min, about 1.8 min per mark. Non-programmable scientific calculator.
:::

## Useability and visual communication (syllabus)
**Useability principles:** accessibility, effectiveness, safety, utility, learnability. **Elements:** space, line, colour, shape, texture, tone, form, proportion, scale. **Principles:** balance, contrast, proximity, harmony, alignment, repetition, hierarchy.

## DFD (Gane-Sarson)
Entity (outside system) · process (numbered, verb-object name) · data store (numbered, **D** disk, **M** manual, **T** temporary) · data flow (labelled noun). Entities may not send data directly to entities or stores, or receive directly from stores.

## Australian Privacy Principles
1 open and transparent management · 2 anonymity and pseudonymity · 3 collection of solicited information · 4 unsolicited information · 5 notification of collection · 6 use or disclosure · 7 direct marketing · 8 cross-border disclosure · 9 government related identifiers · 10 quality · 11 security · 12 access · 13 correction.

## CIA risk and fix
Confidentiality (interception, weak passwords) → TLS, VPN, MFA, access control · Integrity (manual entry, shared IDs) → validation, cross-checks, audit logs · Availability (DDoS, failure) → backups, redundancy, firewalls.

## Algorithms and data
Pseudocode: BEGIN/END, SET, IF/ELSE/ENDIF, FOR/WHILE, comments for each criterion. **Desk check** = trace table per variable. JSON: `{"title": …, "reviews": [{"rating": 5}]}` read into objects/arrays. Percentage = part ÷ whole × 100. Data dictionary: field, data type (VARCHAR, INT, BOOLEAN, DATE), rule.

## Ciphers
Caesar (25 keys) < Gronsfeld (digit key) < Vigenère (keyword). XOR bits differ → 1. One-time pad: random key, at least as long as the message, used once. RSA: public key encrypts, private key decrypts. Hashing: one-way, fixed length.

## Answer verbs
**Identify and explain** (name + reason) · **Analyse the scenario** (use details) · **Evaluate** (judge against criteria) · **Recommend and justify** · **Symbolise** (draw or write) · **Desk check** (trace).

## Diagrams

<Diagram name="digital-cia" caption="CIA triad" />

<Diagram name="digital-dfd-symbols" caption="DFD symbols" />

<Diagram name="digital-useability" caption="Useability principles" />

<Diagram name="digital-sym-asym" caption="Symmetric vs asymmetric" />

More: [past papers analysis](/digital-solutions/past-papers) · [solutions 2025](/digital-solutions/solutions-2025) · [notes](/digital-solutions/notes)
