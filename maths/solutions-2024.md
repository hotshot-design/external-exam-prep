# General Maths – worked solutions, 2024 papers

::: tip Source and how to use
Built from the QCAA **2024 General Mathematics** Paper 1 and Paper 2 books and the 2024 marking guide (`snr_maths_general_24_ea_*` in the [paper files](/maths/papers); CC BY 4.0, © State of Queensland (QCAA)). Answers and mark allocations come from the guide and I re-checked the arithmetic. Questions that depend on a diagram (marked 📐) are described from the guide's working. Open the question book to see the drawing. Compare with the [2025 solutions](/maths/solutions-2025). **Attempt first, then compare.**
:::

## Paper 1 (57 marks)

### Section 1: multiple choice (15 marks)
| Q | Ans | Reasoning |
|---|---|---|
| 1 | B | Latitude comes first (N/S of the equator), longitude second (E/W of the prime meridian): 28° N, 16° W |
| 2 | D | An open walk with repeated vertices but **no repeated edges** is a **trail** |
| 3 | B | $R^{2} = 0.36$ means **36% of the total variation (in y) is explained by the linear association** |
| 4 | D | Seasonal (repeating pattern each year) **and** increasing (peaks and troughs rise) 📐 |
| 5 | C | Uluru is south of the equator and east of the prime meridian: **25° S 131° E** |
| 6 | A | Friday's 5 points are Wed–Sun: (24.6 + 25.2 + 25.6 + 25.7 + 25.9) ÷ 5 = 127 ÷ 5 = **25.4** |
| 7 | C | Float = LST − EST for activity W: 4 − 0 = **4 min** |
| 8 | C | $t_{1} = 240 \times 0.5^{0} = 240$ and $t_{3} = 240 \times 0.5^{2} = 60$, so the difference is **180 cm** |
| 9 | D | Ratio = −900 ÷ 1000 = −0.9, so $t_{4} = 1000 \times (-0.9)^{3} =$ **−729** |
| 10 | C | Osaka is 2 h ahead of Phnom Penh, so Phnom Penh is 30° further west: 135° E − 30° = **105° E** |
| 11 | B | r = −0.989 is strong and negative; the scatterplot is linear: **negative and linear** |
| 12 | A | r = Σ[(x−x̄)(y−ȳ)]/(sx·sy) ÷ (n − 1) = −4.5 ÷ 9 = **−0.50** |
| 13 | A | Seasonal indices sum to 4, so Q4 index = 4 − 2.4 = 1.6. Adjusted sales = 7200 ÷ 1.6 = **4500** |
| 14 | C | The repayment amount doesn't change the **effective annual rate**: only the nominal rate and the compounding frequency do |
| 15 | A | A good linear fit has residuals scattered randomly about 0 with **no pattern** 📐 |

### Section 2: short response (42 marks)

#### Q16 (3 marks) Arithmetic sequence
(Given $t_{1} = 25$ and the rule t(n+1) = t(n) + 8.)
a) $t_{2} = 25 + 8 =$ **33 seats**.
b) Row 1–4: **25, 33, 41, 49**. Total = 25 + 33 + 41 + 49 = **148**.
**Marks (guide):** second row (1), table (1), total (1).

#### Q17 (4 marks) Planar graph 📐
a) A planar graph can be **drawn so that no edges cross**.
b) The graph has **5 faces** (count the outside region).
c) v = 6, e = 9, f = 5: v + f − e = 6 + 5 − 9 = **2** ✓.
**Marks (guide):** definition (1), faces (1), vertices and edges (1), Euler's formula shown (1).

#### Q18 (4 marks) Compound interest
i = 0.042 ÷ 12 = 0.0035, n = 18 × 12 = 216.
$A = 3000 \times (1 + 0.0035)^{216} =$ **\$6380.79**.
Interest = 6380.79 − 3000 = **\$3380.79**.
**Marks (guide):** i and n (1), substitution (1), value (1), interest (1).

#### Q19 (4 marks) Scatterplot
Age (explanatory) on the horizontal axis; number of stands (response) on the vertical axis. Plot (50,20), (55,18), (60,16), (65,14), (70,13), (75,12), (80,10), (85,9), (90,8) with scales and labelled axes. The form is **linear** (negative direction).
**Marks (guide):** identify variables (1), accurate points (1), scales and labels (1), form linear (1).

#### Q20 (4 marks) Correlation and confounding
a) Pearson's r = **0.986**, a **strong** (positive) association.
b) A **confounding variable** is another variable that affects the response variable (and may also relate to the explanatory variable), so the observed association may not be causal.
c) Time of day: both air temperature and the number of vehicles are lower early and late in the day and higher in the middle of the day (when commuters arrive and park), so t could explain both.

#### Q21 (3 marks) Perpetuity
a) Quarterly rate = 5.2% ÷ 4 = **1.3%** (0.013).
b) Value = payment ÷ rate = 975 ÷ 0.013 = **\$75 000**.

#### Q22 (6 marks) Reducing balance loan
Monthly rate = 8.4% ÷ 12 = 0.7% = 0.007.
a) **A(n+1) = 1.007 × A(n) − 250, A(0) = 15 000**. (2 marks)
b) A(1) = 1.007 × 15 000 − 250 = 14 855. A(2) = 1.007 × 14 855 − 250 = **\$14 708.99**. (1 mark)
c) **Method 1:** reduction = 15 000 − 14 708.99 = 291.01. Repayments = 2 × 250 = 500. Interest = 500 − 291.01 = **\$208.99**.
**Method 2:** month 1 interest = 0.007 × 15 000 = 105; month 2 = 0.007 × 14 855 = 103.99; total **\$208.99**. (3 marks)

#### Q23 (4 marks) Minimum spanning tree 📐
a) Use Kruskal's or Prim's algorithm on the eight towns (7 edges). The guide's tree uses the edges **200, 210, 230, 235, 260, 280, 320 km**.
b) Total = 200 + 210 + 230 + 235 + 260 + 280 + 320 = **1735 km**. Since 1735 < 2000, **2000 km of pipeline is sufficient**.
**Marks (guide):** a spanning tree drawn (1), the minimum one (1), its length (1), a reasonableness statement linked to the working (1).

#### Q24 (5 marks) Adjacency matrix 📐
a) Build a 6 × 6 symmetric matrix (A to F in both axes), with 1 where an edge joins two students and 0 elsewhere. (2 marks: one row/column correct, then the whole matrix.)
b) The graph is **simple and connected** (no loops or multiple edges, one piece). It has no arrows or weights, so it is not directed or weighted, and the guide does not accept bipartite.
c) Students who study an identical subject to C: **B, D and E** (C's neighbours).
d) Draw a connected subgraph containing E with **3 edges and no cycles** (a tree with 4 vertices).

#### Q25 (5 marks) Seasonal index and deseasonalising
a) 2022 mean = (410 + 30 + 205 + 1135) ÷ 4 = **445**; 2023 mean = (390 + 20 + 150 + 1100) ÷ 4 = **415**.
Ratios (season ÷ mean), then average the two years:
| Season | 2022 | 2023 | **Index** |
|---|---|---|---|
| Autumn | 0.9213 | 0.9398 | **0.9306** |
| Winter | 0.0674 | 0.0482 | **0.0578** |
| Spring | 0.4607 | 0.3614 | **0.4111** |
| Summer | 2.5506 | 2.6506 | **2.6006** |

b) Deseasonalised = actual ÷ index: Autumn 130 ÷ 0.92 = 141.30; Winter 145 ÷ 1.02 = **142.16**; Spring 155 ÷ 1.12 = 138.39; Summer 132 ÷ 0.94 = 140.43.
**Winter** has the highest seasonally adjusted rainfall.

## Paper 2 (38 marks)

#### Q1 (5 marks) Two-way table
Let Year 12 = x, so Year 11 = x + 4 and 2x + 4 = 60, giving x = 28 and Year 11 = **32**.
Dancers: ¼ × 32 = 8 (Year 11) and ½ × 28 = 14 (Year 12), total 22.
Musicians: 32 − 8 = 24 (Year 11), 28 − 14 = 14 (Year 12), total **38**.
Percentage who are musicians = 38 ÷ 60 × 100 = **63.3%**.
**Marks (guide):** totals (1), dancers (1), musicians (1), row/column totals (1), percentage (1).

#### Q2 (4 marks) Hamiltonian cycle 📐
Draw the weighted graph with the 5 islands (Waiben, Ngurapai, Palilug, Keriri, Gealug) and 6 edges. The guide's cycle from Waiben is **W–G–P–K–N–W**:
14 + 16 + 25 + 20 + 18 = **93 min**.
Check that the cycle visits every vertex once and returns to the start.

#### Q3 (5 marks) Least-squares line to evaluate a notification
Data (latitude, UV index): (27, 12), (12, 13), (32, 11), (34, 9), (38, 6).
Enter in the calculator: slope **b = −0.227**, intercept **a = 16.7**, so **y = 16.7 − 0.227x**.
Hobart: x = 43 → y = 16.7 − 0.227 × 43 = **6.9 ≈ 7**.
A UV index of 7 is in the "**high**" category (6 and 7), so **the notification is reasonable**.
**Marks (guide):** slope and intercept (1), equation (1), substitution (1), prediction (1), reasonableness statement (1).

#### Q4 (5 marks) Project network 📐

<Diagram name="sol-2024-p2q4-bread" />
Activities (minutes): A measure ingredients 3 (none); B mix and prepare tin 5 (A); C leave dough to rise 20 (B); D pre-heat oven and tin 15 (B); E knead dough 7 (C); F bake 30 (D, E).
Forward scan (EST): A 0, B 3, C 8, D 8, E 28, F 35. Finish = 35 + 30 = **65 min**.
Backward scan (LST): F 35, E 28, D 20, C 8, B 3, A 0.
Critical path A–B–C–E–F (3 + 5 + 20 + 7 + 30 = 65). **D is non-critical**.
Float(D) = LST − EST = 20 − 8 = **12 minutes** (the same as 35 − 8 − 15).
**Marks (guide):** network (1), forward scan (1), backward scan (1), non-critical activity (1), float (1).

#### Q5 (6 marks) Assignment (Hungarian algorithm)
First fill the unknown distances (same longitude/latitude ideas as in 2025):
- A to P (x): same longitude, 8° apart: 111.2 × 8 ≈ **890 km**.
- A to R (y): same latitude (20° S), 11° apart: 111.2 × cos 20° × 11 ≈ **1149 km**.

| | P | Q | R |
|---|---|---|---|
| A | 890 | 600 | 1149 |
| B | 445 | 485 | 340 |
| C | 980 | 1170 | 770 |

Reduce rows, then columns, until the zeros can be covered by 3 lines (= 3 tasks). Allocation: **A→Q, B→P, C→R**, total **600 + 445 + 770 = 1815 km**.
Check by listing all 6 allocations (the guide's Method 3): 2145, 2400, **1815**, 1920, 2764, 2614. Minimum 1815.
**Marks (guide):** x (1), y (1), row/column reduction (1 + 1), allocation (1), total (1).

#### Q6 (6 marks) Arithmetic and geometric models
2021 (n = 1): meals $m_{1} = 60$ and accommodation $a_{1} = 2 \times 60 =$ **120**.
2025 → n = 5.
Meals: $m_{5} = 60 + 3(5 - 1) =$ **\$72**.
Accommodation: $a_{5} = 120 \times 1.1^{4} =$ **\$175.69**.
Total for 7 days = 7 × (72 + 175.69) = **\$1733.83**.
\$1500 < \$1733.83 < \$2000, so **the estimate is reasonable**.

#### Q7 (7 marks) Time zones and proportion
Total distance = 4828 + 7242 = **12 070 km**.
Time difference: Sydney (UTC+10) is 10 − (−8) = **18 h ahead** of Los Angeles.
Arrival in Sydney time = 6:50 pm Tue + 18 h = **12:50 pm Wednesday**.
Flight duration = 9:50 pm Tue to 12:50 pm Wed = **15 h**.
Fraction travelled = 4828 ÷ 12 070 = 40%, so time = 0.4 × 15 = **6 h**.
Sydney time = 9:50 pm Tuesday + 6 h = **3:50 am Wednesday**.
**Marks (guide):** total distance and time difference (1), arrival time in Sydney (1), duration (1), method (1), time elapsed (1), final time and day (1), logical organisation (1).

## How the 2024 guide awards marks
| Wording | What to do |
|---|---|
| "substitutes into appropriate rule" | Show the formula with your numbers in it |
| "determines / calculates …" | Final value with units |
| "provides appropriate statement of reasonableness linked to prior working" | "1735 < 2000, so …": compare your answer with the claim |
| "shows logical organisation, communicating key steps" | Q7: lay the steps out in order |
| FT (follow through) | Early slips don't cost later marks if your later method is right |

Patterns: four of seven Paper 2 questions end with a "**reasonable/estimate**" judgment or a "**determine … and justify**" decision, so always finish with a sentence.

See also [past papers analysis](/maths/past-papers) and the [2025 solutions](/maths/solutions-2025).
