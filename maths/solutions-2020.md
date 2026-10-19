# General Maths – worked solutions, 2020 papers

::: tip Source and how to use
Built from the QCAA **2020 General Mathematics** Paper 1 and Paper 2 books and the 2020 marking guide (`snr_maths_general_20_ea_*` in the [paper files](/maths/papers); CC BY 4.0, © State of Queensland (QCAA)). Answers and mark allocations come from the guide and every number has been re-calculated. The 2020 paper was set under the earlier syllabus and was **larger than the current format**: Paper 1 was **60 marks** (15 multiple choice + 11 short response worth 45) and Paper 2 was **40 marks** (7 questions). **Every question below is still in scope** for 2026 (Unit 3 or Unit 4 of the 2025 syllabus). Questions that depend on a diagram are marked 📐: open the question book for the drawing. Compare with the [2021](/maths/solutions-2021) and [2022](/maths/solutions-2022) solutions. **Attempt first, then compare.**
:::

## Paper 1 (60 marks)

### Section 1: multiple choice (15 marks)
| Q | Ans | Reasoning |
|---|---|---|
| 1 | C | A justified linear model has residuals **randomly scattered about 0**, no pattern 📐 |
| 2 | A | NSW is on daylight saving (UTC+11): 10:00 am. Standard NSW time is 9:00 am. SA (standard +9.5, with daylight saving) = **9:30 am**; QLD (+10, no daylight saving) = **9:00 am** 📐 |
| 3 | C | 4, 2, 0, −2: d = **−2** |
| 4 | D | A geometric sequence plots as a **curve** (constant ratio, not constant difference) 📐 |
| 5 | B | b = r·s_y ÷ s_x, then a = ȳ − b·x̄ (guide: B) |
| 6 | B | $A_{1} = 1.015 \times 10\,000 - 700 = 9450$; $A_{2} = 1.015 \times 9450 - 700 =$ **\$8891.75** |
| 7 | C | Minimum spanning tree: **12 km** 📐 |
| 8 | B | Points slope down and sit close to a line: **strong negative** 📐 |
| 9 | D | More ice blocks and more fans sold both rise in hot months, so it is a **positive association**, not causation |
| 10 | D | The smoothed series is shorter at the ends and flatter than the original 📐 |
| 11 | B | Guide answer **B**: a 4 × 4 symmetric matrix; check each edge in the graph and that T's row matches 📐 |
| 12 | A | **Greatest float = 2 days** (LST − EST for the non-critical activities) 📐 |
| 13 | A | Planar graph, 5 vertices, 4 faces: e = v + f − 2 = 5 + 4 − 2 = **7 edges** 📐 |
| 14 | C | Students: 12 of (48 + 12) = **20%** drive |
| 15 | A | After 7 terms Annuities 1 and 2 are higher than 3: **higher regular deposits** is the plausible reason 📐 |

### Section 2: short response (45 marks)

#### Q16 (3 marks) Walk, trail, cycle 📐
a) AFCFB: starts and ends at different vertices, repeats edge FC: **open walk** (1).
b) AFCEFBA: starts and ends at A, no edge repeated, vertex F repeated: **closed trail** (1).
c) ABCDEFA: closed, no edge or vertex repeated: **cycle** (1).

#### Q17 (3 marks) Distance along a parallel
Mount Gambier 140°47′ E and Bairnsdale 147°37′ E on 37°50′ S. Angular distance = 147°37′ − 140°47′ = **6°50′** (= 6.833°) (1).
D = 111.2 × cos(37°50′) × 6.833 (1) = **600 km** to the nearest km (600.14) (1).

#### Q18 (4 marks) Arithmetic sequence from two terms
$t_{3} = t_{1} + 2d$: 439 = 353 + 2d, so 2d = 86, **d = 43** (2).
$t_{6} = 353 + 5 \times 43 =$ **568 people** (substitution 1, answer 1).

#### Q19 (4 marks) Predict, then judge with r and R²
a) y = 2.3 × 12 + 31.4 = **59 fish** (1).
b) r = 0.688 is a **moderate** (positive) linear association (1). $R^{2} = 0.473$, so **47% of the variation** in fish caught is explained by hours fished (1). The prediction of 59 fish **may be valid**, but with only a moderate association other factors also matter (1).

#### Q20 (4 marks) Home loan repayment
i = 0.065 ÷ 12 = 0.005416…, n = 25 × 12 = 300 (1).
\$350\,000 = M \times (1 - (1 + i)^{-300}) \div i = M \times 148.102\$… (1), so M = 2363.225… (1).
**\$2363.23 per month** for 25 years (1, with units and rounding).

#### Q21 (5 marks) Maximum flow, minimum cut 📐

<Diagram name="sol-2020-p1q21-flow" />
Arcs: Warehouse→A 50, A→Shelter 20, Warehouse→B 30, B→Shelter 40, Warehouse→C 40, C→B 20, C→Shelter 30.
a) Seven valid cuts (1 mark for all cuts, 1 for capacities):
| Cut | Capacity |
|---|---|
| 1 | 50 + 30 + 40 = 120 |
| 2 | 50 + 30 + 20 + 30 = 130 |
| 3 | 50 + 40 + 40 = 130 |
| 4 | 50 + 40 + 30 = 120 |
| 5 | 20 + 30 + 40 = 90 |
| 6 | 20 + 40 + 40 = 100 |
| 7 | 20 + 40 + 30 = 90 |

Minimum cut = **90**, so maximum flow = **90 tonnes per day** (1).
b) With A unusable the capacities become 70, 80, 80, 70, 70, 80, 70. The minimum cut is now 70, so the new maximum flow is **70 tonnes per day** (2). (Remove arcs through A: W→A and A→Shelter.)

#### Q22 (4 marks) Percentaged two-way table and association
a) Column totals: 115 (change) and 95 (do not change) (1).
| | Change uniform | Do not change |
|---|---|---|
| Junior staff | 92 ÷ 115 = **80%** | 28 ÷ 95 = **29.5%** |
| Senior staff | 23 ÷ 115 = **20%** | 67 ÷ 95 = **70.5%** |
| Total | 100% | 100% |

(1 for a correct percentaged table.)
b) There **is** an association: **80% of those wanting change are junior** compared with only 29.5% of those not wanting change, and 70.5% of the "do not change" group are senior (1 + 1). Comparing percentages across the categories is what shows an association.

#### Q23 (4 marks) Flight and time zones
Depart Brisbane 10:45 pm Monday (UTC+10). Add 14 h 35 min: 37:20 Monday = **1:20 pm Tuesday** Brisbane time (2).
Dubai is UTC+4, 6 hours behind Brisbane: **7:20 am Tuesday** in Dubai (2).

#### Q24 (4 marks) Reading a least-squares line; interpolation and extrapolation 📐
a) At 9 days the line gives **11 cm** (1).
b) 9 days is within the data, so **interpolation** (1).
c) The line does give about 32 cm at day 29 (1), but day 29 is far outside the data (the plotted data stops at about 25 days), and the data points appear to **level off** at about 25 cm, so extrapolating a straight line is unreliable (1).

#### Q25 (5 marks) Effective interest rate comparison
Option 1: $(1 + 0.07/4)^{4} - 1 =$ **0.07186** (7.186%).
Option 2: $(1 + 0.068/12)^{12} - 1 =$ **0.07016** (7.016%).
**Option 1 is better** because it has the higher effective annual rate (1 mark for each substitution, each value, and the decision).

#### Q26 (5 marks) Geometric decay model
a) r = 1 − 0.17 = **0.83** (1). Let n = years since 2015: **$t_{n} = 483 \times 0.83^{n-1}$** (1).
b) Beginning of 2021 is n = 6 (1): $t_{6} = 483 \times 0.83^{5} = 190.26 (1)$, so about **190 birds** (1).

## Paper 2 (40 marks)

#### Q1 (5 marks) Linear decrease: arithmetic sequence or linear function
Option 1 (arithmetic): $t_{1} = 12\,500$, $d = -135$, $t_{n} = 5000$. $5000 = 12\,500 - 135(n - 1)$, so 135(n − 1) = 7500, n − 1 = 55.56, n = 56.56. About **56 minutes**.
Option 2 (linear): y = −135x + 12 500, set y = 5000: 135x = 7500, **x = 55.56 ≈ 56 minutes**.
**Marks (guide):** define variables (1), parameters (1), substitution (1), solve (1), sensible rounded answer (1).

#### Q2 (5 marks) Correlation coefficient: is it appropriate? 📐
Scatterplot of people (x) against water use (y): points (6, 990), (2, 160), (4, 320), (5, 480), (5, 410), (4, 280), (3, 240), (1, 130), (6, 940), (7, 1340) (1).
Calculator: **r = 0.886**, a **very strong positive** association (1 + 1).
However, the scatterplot is **curved (non-linear)**, so the linear correlation coefficient **should not be used** to describe it (1 + 1).
*Key idea:* r only measures strength of a **linear** association. Always plot first.

#### Q3 (6 marks) Missing data values from a least-squares line
y = 2.1875x + 0.0625 passes through (x̄, ȳ). x̄ = (4 + 3 + 8 + 4 + 6) ÷ 5 = **5** (1).
ȳ = 2.1875 × 5 + 0.0625 = **11** (1).
Sum of y = 5 × 11 = 55. The known y values 4, 16 and 8 sum to 28, so 55 = 28 + p + q and **p + q = 27** (1).
q = p + 3: 2p + 3 = 27, **p = 12, q = 15** (1 + 1). Organisation (1).
*Check:* the line fitted to (4, 12), (3, 4), (8, 16), (4, 8), (6, 15) has slope 2.1875 and intercept 0.0625, r = 0.875.

#### Q4 (5 marks) Seasonal indices and deseasonalising 📐
Yearly averages: 2018 = (64 + 98 + 116 + 122) ÷ 4 = **100**; 2019 = (87 + 156 + 180 + 177) ÷ 4 = **150** (1).
Ratios to the yearly average (1): 2018: 0.64, 0.98, 1.16, 1.22. 2019: 0.58, 1.04, 1.20, 1.18.
Seasonal indices (average of the two years) (1): **Q1 0.61, Q2 1.01, Q3 1.18, Q4 1.20** (sum = 4).
Deseasonalised = actual ÷ index (1): 2018: 104.9, 97.0, 98.3, 101.7. 2019: 142.6, 154.5, 152.5, 147.5.
Plot the eight deseasonalised points on the same axes as the original data and join them (1).

#### Q5 (5 marks) Hungarian algorithm with a matrix
| | Task 1 | Task 2 | Task 3 |
|---|---|---|---|
| A | 3 | 3 | 1 |
| B | 4 | 7 | 2 |
| C | 4 | 4 | 1 |

Row reduction (subtract 1, 2, 1): [2, 2, 0], [2, 5, 0], [3, 3, 0] (1).
Only 1 line covers the zeros, so reduce columns (subtract 2 from column 1 and 2 from column 2): [0, 0, 0], [0, 3, 0], [1, 1, 0] (1).
Three lines are needed, so assign: **A → Task 2 (3), B → Task 1 (4), C → Task 3 (1)** (1).
Minimum cost = 3 + 4 + 1 = **\$8000** (1). Organisation (1).

#### Q6 (7 marks) Project scheduling: is three workers enough? (complex unfamiliar)

<Diagram name="sol-2020-p2q6-tasks" />
Tasks: A 3 (–), B 4 (–), C 2 (A), D 8 (C), E 5 (C), F 4 (B), G 3 (B), H 1 (E, F), I 2 (G), J 3 (H, I). 📐 (the question gives a table, but check the network in the book)
Forward scan: A 0, B 0, C 3, F 4, G 4, D 5, E 5, I 7, H 10, J 11. Finish = 11 + 3 = **14 days** (network 1, EST 1, LST 1; minimum time 1).
Critical path A – C – E – H – J = 3 + 2 + 5 + 1 + 3 = 14.
Only A and B can start on day 0 and a third worker is only useful from day 4 (C, F and G running together). At day 5, tasks **D, E, F and G** are all available: with 3 workers D cannot be finished by day 14 while the critical path stays on time (checked by trying every possible task order).
The owner's belief is **not reasonable**: **at least 4 workers** are needed to finish in 14 days (1 evaluation, 1 organisation).

#### Q7 (7 marks) Annuity savings to buy a perpetuity (multi-topic)
**Step 1 (perpetuity):** i = 0.0576 ÷ 12 = 0.0048 (1). A = d ÷ i = 3600 ÷ 0.0048 = **\$750 000** (1 + 1) needed at age 65.
**Step 2 (savings annuity):** i = 0.042 ÷ 12 = 0.0035, n = 20 × 12 = 240 (1).
\$750\,000 = M \times [(1.0035^{240} - 1) \div 0.0035] = M \times 375.13\$… (1 + 1).
M = **\$1999.29 per month** (1 + 1 for organisation).
*Key idea:* the perpetuity price (the "A") becomes the **future value** target of the savings annuity. Two formulas chained.
