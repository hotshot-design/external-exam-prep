# General Maths – worked solutions, 2023 papers

::: warning No marking guide for 2023
The folder has the 2023 question books (`snr_maths_general_23_ea_*`) but **no 2023 marking guide**, so these solutions are **my own working**, not QCAA's. I re-checked every calculation by computer. Where a question needs a diagram, a table or an equation that didn't come through in the text, I say so and give the method instead of an invented answer (📐 = check the drawing in the book). Mark allocations come from the question book, but the criteria wording is based on how the 2024 and 2025 guides award marks. Questions © State of Queensland (QCAA), CC BY 4.0. Compare with the [2024](/maths/solutions-2024) and [2025](/maths/solutions-2025) solutions.
:::

## Paper 1

### Multiple choice
| Q | Ans | Reasoning |
|---|---|---|
| 1 | A | r = 0.23 is **weak positive** |
| 2 | ? | 📐 Read the time series plot: trending upward over time suggests *increasing*; a repeating pattern would be seasonal |
| 3 | B | Critical path PRSV = 38 + 32 + 34 + 26 = 130 min. 11:00 am + 2 h 10 min = **1:10 pm** |
| 4 | C | Field athletes preferring Y: 12 ÷ 40 = **30%** |
| 5 | B | The response variable (distance travelled) goes on the vertical axis, and the **explanatory variable (vehicle age) goes on the horizontal axis** |
| 6 | B | 40 fish in Jan 2022 (n = 1), doubling each year, reaching Jan 2030 at n = 9: a **geometric** rule with $t_{1} = 40, r = 2, n = 9 (40 \times 2^{8} = 10\,240 \ge 10\,000)$ |
| 7 | D | In a causal relationship the **response variable depends on the explanatory variable** |
| 8 | A | Q follows P (3 min) and both are critical: EST = **3**, LST = **3** |
| 9 | B | d = 9 − 3 = 6, so $t_{6} = 3 + 5 \times 6 =$ **33** |
| 10 | C | Index 1.0 = the mean quarter, so mean sales = 160. x = 0.95 × 160 = **152** and y = 128 ÷ 160 = **0.8** |
| 11 | C | Annuity, 0.4% a month: $500 \times ((1.004^{4} - 1) \div 0.004) =$ **\$2012.03** |
| 12 | ? | The recurrence relation did not extract. Evaluate it twice on \$6000 by calculator |
| 13 | ? | 📐 Draw an edge E–L, E–S, F–J, G–S, H–J, H–L and find the matching bipartite graph |
| 14 | B | LSL with days *d* as x and height *h* as y: **h = 0.6d + 5.7** (slope 0.6147, intercept 5.706) |
| 15 | B | Ratio 40 000 ÷ 50 000 = 0.8. Value after 4 years = $50\,000 \times 0.8^{4} =$ **\$20 480** |

### Short response (42 marks)

#### Q16 (3 marks) Time zones
Town A is at 90° W (UTC−6) and town B at 120° E (UTC+8). The difference is 210° of longitude, and the time difference is 14 hours (210 ÷ 15), with B ahead (east).
2:00 am + 14 h = **4:00 pm** (same day) in town B.

#### Q17 (4 marks) Loan repayment
Loan = 570 000 − 50 000 = **\$520 000**. Monthly rate = 6.6% ÷ 12 = 0.55%. n = 25 × 12 = 300.
Repayment = $P \times r \div (1 - (1 + r)^{-n}) =$ **\$3543.64** per month. (Or find the repayment that makes the balance zero after 300 months using the recurrence relation.)

#### Q18 (4 marks) Coordinates and time zones 📐
a) Closest to the equator: site **C** (12° S).
b) Site A (32° S 116° E) is in **Western Australia** (check the map).
c) Standard time zones are based on longitude. Sites **B and C** share 136° E, so they are in the same time zone (A at 116° E is 20° further west, about 1 h 20 min different).

#### Q19 (4 marks) Compare investments
$\mathrm{EAR} = (1 + i/n)^{n} - 1$.
Option A: $(1 + 0.056/12)^{12} - 1 =$ **5.746%**.
Option B: $(1 + 0.0562/4)^{4} - 1 =$ **5.740%**.
5.746% > 5.740%, so **Ngarra's decision is reasonable**: A is slightly better even though B has the higher nominal rate.

#### Q20 (4 marks) Euler's formula 📐
a) Count vertices, edges and faces on graph 1 and show v + f − e = 2.
b) The feature to change is **crossing edges** (an edge crossing another).
c) Move one edge so it doesn't cross another, keeping the same connections.

#### Q21 (4 marks) Flow network 📐
a) Capacity of cut X = sum of the capacities of the edges crossing the cut from the airport side to the town side.
b) Maximum flow = minimum cut: test cuts across the network and take the smallest.
c) Remove the roads connected to the bridge, redraw, and find the minimum cut again.
Edge capacities (vehicles/hour): 200, 120, 50, 100, 150, 80, 140.

#### Q22 (4 marks) Scatterplot
a) Hours of sleep (explanatory) on the horizontal axis and distance (response) on the vertical axis. Points: (7,5), (7.5,7), (8,5), (6.5,7), (9.5,4), (6,8), (8.5,6). Scale and label both axes.
b) The association is **negative**: more sleep goes with less distance.

#### Q23 (5 marks) Network graph 📐
a) Degree of E = number of edge ends at E (a loop counts 2).
b) Count the edges between D and E (could be more than one).
c) Build a 5 × 5 matrix (A–E), entry = number of edges between the two vertices, symmetric.

#### Q24 (5 marks) Project scheduling
a) Network (durations in minutes). Forward scan (EST) and backward scan (LST):
| Task | Duration | EST | LST |
|---|---|---|---|
| A | 2 | 0 | 0 |
| B | 20 | 2 | 28 |
| C | 6 | 2 | 2 |
| D | 8 | 2 | 36 |
| E | 40 | 8 | 8 |
| F | 4 | 10 | 44 |
| G | 2 | 48 | 48 |

b) Paths into G: A–C–E–G = 2 + 6 + 40 + 2 = 50; A–B–G = 24; A–D–F–G = 16. The **critical activities are A, C, E and G** and the **minimum completion time is 50 minutes**.

#### Q25 (5 marks) Distance between locations 📐
Read the latitudes and longitudes of X and Y from the map to the nearest degree, then find the angular distances. If they differ in both latitude and longitude, use the formula from the formula book for the distance. Check the book's formula before using it.

## Paper 2

#### Q1 (5 marks) Hungarian algorithm 📐
The matrix of times (Jane, Knox, Levi against S, C, R) lost some entries in extraction, so I can't give a number safely. Method: subtract the row minimum from each row, then the column minimum from each column, cover all zeros with the fewest lines. If lines = 3, assign using the zeros, and add the original times for the minimum total.

#### Q2 (4 marks) Deseasonalise
Yearly means: 2021 = (285 + 28 + 195 + 460) ÷ 4 = **242**; 2022 = (276 + 22 + 170 + 392) ÷ 4 = **215**.
Seasonal indices (average of the two years' ratios): Autumn **1.23**, Winter **0.109**, Spring **0.798**, Summer **1.862**.
Deseasonalised = value ÷ index:
| | Autumn | Winter | Spring | Summer |
|---|---|---|---|---|
| 2021 | 231.6 | 256.8 | 244.3 | 247.0 |
| 2022 | 224.3 | 201.8 | 213.0 | 210.5 |

(This assumes the question wants the index derived from the two years, as in 2024 Q25.)

#### Q3 (5 marks) Missing cable 📐
Idea: find the MST with cable C closed. With C reopened the MST total drops by 1 km, so C replaces an edge that is 1 km longer than C in the original cycle. Length(C) = (replaced edge) − 1. New total = old MST − 1.

#### Q4 (5 marks) Correlation and prediction
Temperature vs fish: r = **0.309** (weak). People fishing vs fish: r = **0.807** (strong).
So **the number of people fishing (p)** is the explanatory variable with the stronger linear association (Jiro's view).
Least-squares line: **f = 10.893p − 129.84**. For p = 50: f = 10.893 × 50 − 129.84 ≈ **415 fish**.
(The 25 °C information is not used, since temperature is the weaker predictor.)

#### Q5 (7 marks) Patrol route 📐
Lengths follow $t_{n} = 1 + 2(n - 1)$: $t_{1} = 1, t_{2} = 3, t_{3} = 5$, and the labels $t_{1} + t_{2} = 4, 2t_{1} = 2, 2t_{2} = 6$. Substitute, then find the shortest closed route visiting all eight sites (Hamiltonian cycle) from A. Time = distance ÷ 40 km/h + 8 sites × 15 min of checking (check whether A counts as a site to check), starting from 9:00 am.

#### Q6 (7 marks) Two linear models
Industry B has the higher $R^{2} (0.96)$, so Leigh (40) is in **B**; Tony (50) is in **A**.
Least-squares lines (age x, balance y):
- A: y = 7910x − 205 520
- B: y = 9570x − 243 440

Leigh (B, x = 40): 9570 × 40 − 243 440 = **\$139 360**.
Tony (A, x = 50): 7910 × 50 − 205 520 = **\$189 980**.
Difference = **\$50 620**.

#### Q7 (5 marks) Is the investment large enough?
Balance after 5 years = $100\,000 \times (1 + 0.038 \div 12)^{60} =$ **\$120 888.66**.
A perpetuity paying \$6000 a year at 4% p.a. needs 6000 ÷ 0.04 = **\$150 000**.
\$120 888.66 < \$150 000, so **the investment is not large enough**. The shortfall is about **\$29 111**.
Advice: invest more or wait longer, accept a smaller payment (at 4% the \$120 889 supports about \$4836 a year), or find a higher interest rate.

## Check yourself
Because there's no 2023 guide, try these steps: (1) do every question by hand first; (2) compare with the numbers above; (3) for 📐 questions, solve from the book and use my method notes only as a check. If you find a mistake, trust the book and your teacher.

See also [past papers analysis](/maths/past-papers) and [worked examples](/maths/worked-examples).
