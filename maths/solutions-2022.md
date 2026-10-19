# General Maths – worked solutions, 2022 papers

::: tip Source and how to use
Built from the QCAA **2022 General Mathematics** Paper 1 and Paper 2 books and the 2022 marking guide (`snr_maths_general_22_ea_*` in the [paper files](/maths/papers); CC BY 4.0, © State of Queensland (QCAA)). Answers and mark allocations come from the guide and every number has been re-calculated. The 2022 paper was set under the earlier syllabus, but **every question below is still in scope** for 2026 (all of it sits in Unit 3 or Unit 4 of the 2025 syllabus). Questions that depend on a diagram are marked 📐: open the question book for the drawing. Compare with the [2023](/maths/solutions-2023), [2024](/maths/solutions-2024) and [2025](/maths/solutions-2025) solutions. **Attempt first, then compare.**
:::

## Paper 1 (57 marks)

### Section 1: multiple choice (15 marks)
| Q | Ans | Reasoning |
|---|---|---|
| 1 | B | 📐 Watch the news (10 min) runs from node EST 3 to node LST 33, so float = 33 − 3 − 10 = **20 min**. Every other activity lies on the critical path |
| 2 | C | Count the dots: **6 vertices** 📐 |
| 3 | A | Mean of min and max: (22.1+31.8)/2 = 26.95, 23.7, 28.1, 27.2, 25.4. Values between about 23 and 28, so plot (A) 📐 |
| 4 | D | $T_{1} = 4$, add 2 each week: 4, 6, 8, … a **straight line of dots**, weeks on the horizontal axis 📐 |
| 5 | B | May's 3-point average = (Apr + May + Jun) ÷ 3 = **73** (table partly garbled in the text; the guide answer is B) 📐 |
| 6 | C | Semi-Eulerian has two odd vertices (A and D). **Adding an edge between them** makes all degrees even 📐 |
| 7 | C | Only one zero per row/column works: E→M, F→L, G→V 📐 |
| 8 | A | 2018 lies **inside** 2010–2020, so it is **interpolated**; the trend value is about 2.7 million 📐 |
| 9 | B | A spanning tree touches all vertices with **no cycle** and 3 edges for 4 vertices 📐 |
| 10 | D | Explanatory first, response second: daily temperature → ice cream sales |
| 11 | D | t = 26.781 + 12.974 × 5 = 91.651 ≈ **92** |
| 12 | C | Strong negative: tightly clustered points sloping down 📐 |
| 13 | D | Percentages are by **column** (Machinery). 10% of those unsatisfactory in Machinery were satisfactory in Electrical |
| 14 | A | Perth UTC+8, NZ winter UTC+13: 5 h behind. 6:30 pm − 5 h = **1:30 pm** |
| 15 | A | 556 ÷ 111.2 = 5°. Same meridian, 2° N to 3° S = 2 + 3 = **5°** (opposite hemispheres, so add) |

### Section 2: short response (42 marks)

#### Q16 (3 marks) Least-squares line
Enter (1, 86), (2, 180), …, (6, 335) in the calculator.
a) **n = 42.6t + 55.4** (1 mark).
b) t = 21: n = 42.6 × 21 + 55.4 = **950 sales** (substitution 1, prediction 1).
Note: month 21 is well outside the data (months 1–6), so this is **extrapolation** and is only a rough guide.

#### Q17 (4 marks) Recurrence relation for compound interest
a) r = 1 + i = 1.00375, so i = 0.00375 per month. Annual rate = 0.00375 × 12 = **4.5% p.a.** (substitution 1, rate 1).
b) Recursion: $A_{1} = 50\,187.50, A_{2} = 50\,375.70, A_{3} = 50\,564.61, A_{4} = 50\,754.23, A_{5} = 50\,944.56, A_{6} = 51\,135.60$. It first exceeds \$51 000 after **6 months** (method 1, answer 1).

#### Q18 (4 marks) Arithmetic sequence from a graph 📐
Graph points (weeks 1 to 5): 87, 209, 331, 453, 575.
$t_{1} =$ **87**, d = 209 − 87 = **122**.
$t_{n} = 87 + (n - 1) \times 122$, so $t_{25} = 87 + 24 \times 122 =$ **3015 songs**.
**Marks (guide):** $t_{1} (1), d (1)$, arithmetic rule used (1), prediction (1).

#### Q19 (4 marks) Time series 📐
a) **Trend:** positive (long-term increase) because rainfall generally rises over the years. **Seasonality:** the series is seasonal, with a high 4th quarter every year. (1 + 1)
b) y = 1.763x + 156.5. **y-intercept:** the model predicts about **156.5 mm** of rainfall in the quarter before the data begins (quarter 4 of 2015, x = 0). **Slope:** rainfall increases by about **1.763 mm per quarter** on average. (1 + 1)

#### Q20 (4 marks) Hungarian algorithm (minimum, 3 × 3)
| | A | B | C |
|---|---|---|---|
| Store 1 | 19 | 17 | 24 |
| Store 2 | 15 | 14 | 22 |
| Store 3 | 23 | 16 | 40 |

Row reduction (subtract 17, 14, 16): rows become [2, 0, 7], [1, 0, 8], [7, 0, 24].
Column reduction (subtract 1 from column A, 7 from column C): [1, 0, 0], [0, 0, 1], [6, 0, 17].
Zeros are covered by 3 lines, so the assignment is: **Store 1 → C, Store 2 → A, Store 3 → B**.
Minimum distance = 24 + 15 + 16 = **55 km**.
**Marks (guide):** row reduction (1), column reduction (1), allocation (1), minimum total (1). (Check by trying all 6 pairings: 55 is the smallest.)

#### Q21 (5 marks) Graph terms and adjacency matrix 📐

<Diagram name="sol-2022-p1q21-graph" />
Edges: D–P (two edges), D–W, D–R, W–P, W–C, W–R (two edges), W–B, P–C, B–C.
a) A cycle through R and P, for example **R–W–P–D–R** (1).
b) Degrees: D = 4, P = 4, W = 6, R = 3, C = 3, B = 2. Exactly two odd vertices (R and C), so the graph is **semi-Eulerian** (1 + 1).
c) Order B, C, D, P, R, W (2 marks: labelled matrix, then correct values):

|  | B | C | D | P | R | W |
|---|---|---|---|---|---|---|
| B | 0 | 1 | 0 | 0 | 0 | 1 |
| C | 1 | 0 | 0 | 1 | 0 | 1 |
| D | 0 | 0 | 0 | 2 | 1 | 1 |
| P | 0 | 1 | 2 | 0 | 0 | 1 |
| R | 0 | 0 | 1 | 0 | 0 | 2 |
| W | 1 | 1 | 1 | 1 | 2 | 0 |

Double edges are entered as **2**.

#### Q22 (4 marks) Distance along a meridian 📐
a) Marovoay about **16.1° S**, Iakora about **23.1° S** (both 46.6° E; guide accepts ±0.2°) (1).
b) Same hemisphere, so subtract: angular distance = 23.1 − 16.1 = **7°** (1). D = 111.2 × 7 (1) = **778.4 ≈ 778 km** (1, with units).

#### Q23 (4 marks) Line through two points
a) m = (40 − 20) ÷ (7 − 2) = **4**. p − 20 = 4(n − 2), so **p = 4n + 12** (2).
b) n = 15: p = 4 × 15 + 12 = **\$72 per hour** (2). (15 years is beyond the plotted data, so this is extrapolation.)

#### Q24 (5 marks) Scatterplot 📐
a) Temperature is the **explanatory** variable (horizontal) and pies sold is the **response** (vertical). Plot (29, 32), (20, 39), (31, 25), (27, 33), (23, 37), (25, 35), (22, 37), (33, 30) with scales and labels (3 marks: variables, points, scaling and labels).
b) **Strong, negative** (and linear) association (1 + 1). Calculator check: r ≈ −0.905.

#### Q25 (5 marks) Loan amount from repayments
a) i = 0.024 ÷ 12 = 0.002, n = 15 × 12 = 180, d = 993.14 (1).
$A = 993.14 \times (1 - 1.002^{-180}) \div 0.002 =$ **\$150 000** (substitution 1, amount 1).
b) **\$A_{n}\$₊$_{1} = 1.002A_{n} - 993.14$** (formula chosen 1, relation 1). $(A_{0} = 150\,000.)$

## Paper 2 (38 marks)

#### Q1 (4 marks) Reverse-engineering from a deseasonalised value
Seasonal indices sum to 4: 1.11 + 1.42 + 0.62 + x = 4, so autumn's index x = **0.85** (2 marks).
Actual = deseasonalised × index = 36.4 × 0.85 = 30.94 thousand (method 1), so **30 940 swimsuits** (1).

#### Q2 (5 marks) Evaluate the reasonableness of advice (annuity comparison)
Monthly deposit M: $51\,343.85 = M \times [(1 + 0.086/12)^{48} - 1] \div (0.086/12) = M \times 57.0487$, so **M = \$900** (substitution 1, M 1).
Fortnightly: d = 450, i = 0.079 ÷ 26, n = 4 × 26 = 104.
$A = 450 \times [(1 + 0.079/26)^{104} - 1] \div (0.079/26) =$ **\$54 941.61** (1).
Difference = 54 941.61 − 51 343.85 = **\$3597.76** (1).
Since 3597.76 > 3000, the advice is **reasonable** (1).

#### Q3 (5 marks) "Show that" with r, sx and the mean
x = 1, 2, …, 10: x̄ = **5.5**, $s_{x} =$ **3.02765** (1).
b = r × s_$y \div s_{x} = 0.9987 \times 3010 \div 3.02765 =$ **992.878** (1).
a = ȳ − b·x̄ = 9660 − 992.878 × 5.5 = **4199.17** (1).
x = 11: y = 4199.17 + 992.878 × 11 = 15 120.83 ≈ **\$15 121** (1). Logical organisation (1).
**Calculator tip:** enter 1 to 10 in a list and read $s_{x}$ (sample standard deviation).

#### Q4 (5 marks) Shortest path using a network diagram 📐

<Diagram name="sol-2022-p2q4-shortest" />
Table (distances in km): Manon–Veria 16, Manon–Bolint 34, Manon–Alin 33, Veria–Bolint 12, Veria–Alin 15, Bolint–Recen 10, Farra–Recen 15, Farra–Alin 23, Recen–Alin 15.
Draw the six towns with these edges (2 marks). Trial and error: M–V–B–R–F = 16 + 12 + 10 + 15 = **53 km** (the others are longer: M–V–A–F = 54, M–A–F = 56) (2 marks).
New road = 53 − 4 = **49 km** (1).

#### Q5 (5 marks) Minimum spanning tree: evaluate the manager's belief 📐

<Diagram name="sol-2022-p2q5-mst" />
Edges (m): RC–FW 70, RC–SS 120, FW–T 50, FW–CP 170, SS–T 110, T–EA 95, EA–BC 65, CP–BC 60, BC–WS 170, BC–LS 165, SS–WS 185, WS–LS 65. Total = 1325 m.
Minimum spanning tree (8 edges for 9 locations): 50 + 60 + 65 + 65 + 70 + 95 + 110 + 165 = 680 m.
Paths removed = 1325 − 680 = **645 m** (these are 120, 185, 170, 170).
Saving = 645 × 214 = **\$138 030** per year (1).
Because 138 030 > 138 000, the manager's belief is **reasonable** (1), but only just. (Marks: tree 1, removed length 1, saving 1, comparison 1, organisation 1.)

#### Q6 (7 marks) Arithmetic and geometric sequences from line equations (complex unfamiliar)
Slopes: −0.8, 0.4, −0.2 is **geometric**: $t_{1} = -0.8, r = -0.5$. Line 5 slope = −$0.8 \times (-0.5)^{4} =$ **−0.05**.
y-intercepts: 1.2, 2.7, 4.2 is **arithmetic**: $t_{1} = 1.2, d = 1.5$. Line 5 intercept = 1.2 + 4 × 1.5 = **7.2**.
Line 5: y = −0.05x + 7.2. Intersect with Line 1: −0.8x + 1.2 = −0.05x + 7.2, so −0.75x = 6, **x = −8**, y = −0.8(−8) + 1.2 = **7.6**.
**Intersection (−8, 7.6).**
**Marks (guide):** slope sequence (1), intercept sequence (1), Line 5 slope (1), Line 5 intercept (1), x (1), y (1), organisation (1).

#### Q7 (7 marks) Time zones with a ship's travel time 📐
The map shows X at GMT −12, Tarawa at GMT +12, Queensland at GMT +10.
Travel time = 1350 ÷ 50 = **27 hours** (2 marks).
Tarawa is 12 − (−12) = **24 hours ahead** of X (1). Queensland is **2 hours behind** Tarawa (1).
Message sent 6:12 am Wed (X time) = 6:12 am **Thu** in Tarawa. Plus 27 h = **9:12 am Fri** (Tarawa).
Queensland = 9:12 am Fri − 2 h = **7:12 am Friday** (2 marks) (organisation 1).
