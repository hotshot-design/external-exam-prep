# General Maths – worked examples and practice

::: tip Checked numbers
All answers below were calculated and rounded at the end. Keep full calculator precision in working and round only the final answer. Match the formulas to the QCAA formula book.
:::

## Unit 3

### 1. Least-squares line

<Diagram name="ex-1-lsl" />
Given $r = 0.8$, $s_x = 2$, $s_y = 5$, $\bar{x} = 10$, $\bar{y} = 40$.
- $m = r \times \dfrac{s_y}{s_x} = 0.8 \times \dfrac{5}{2} = 2$
- $c = \bar{y} - m\bar{x} = 40 - 2 \times 10 = 20$
- **Line:** $y = 2x + 20$
- **Interpretation:** for each 1 unit increase in x, y increases by 2 units on average. $R^2 = 0.8^2 = 0.64$, so **64%** of the variation in y is explained by x.

### 2. Moving averages (3-point mean)

<Diagram name="ex-2-moving" />
Data: 12, 15, 14, 18, 20, 19, 23
- $\dfrac{12+15+14}{3} =$ **13.7**
- $\dfrac{15+14+18}{3} =$ **15.7**
- $\dfrac{14+18+20}{3} =$ **17.3**
- $\dfrac{18+20+19}{3} =$ **19.0**
- $\dfrac{20+19+23}{3} =$ **20.7**

The first and last data points have no smoothed value.

### 3. Seasonal index and deseasonalising

<Diagram name="ex-3-seasonal" />
Quarterly sales:
| | Q1 | Q2 | Q3 | Q4 | Year average |
|---|---|---|---|---|---|
| Year 1 | 40 | 60 | 80 | 20 | 50 |
| Year 2 | 44 | 66 | 88 | 22 | 55 |

Percentage of year average: Year 1: 80%, 120%, 160%, 40%. Year 2: 80%, 120%, 160%, 40%.
**Seasonal indices:** Q1 0.80, Q2 1.20, Q3 1.60, Q4 0.40 (they sum to 4).
Deseasonalise Year 2 Q3: $\dfrac{88}{1.60} = 55$.

### 4. Sequences

<Diagram name="ex-4-depreciation" />
- **Arithmetic:** $t_1 = 12$, $d = 5$. $t_{20} = 12 + (20-1) \times 5 = 107$.
- **Geometric:** $t_1 = 3$, $r = 2$. $t_6 = 3 \times 2^{5} = 96$.
- **Diminishing-value depreciation:** \$10 000 depreciating 15% per year for 3 years: $10\,000 \times 0.85^{3} = \$6\,141.25$.

### 5. Earth geometry
- **Same meridian:** 27°S to 37°S → angular distance 10°. $D = 111.2 \times 10 = 1112$ km.
- **Same parallel:** two places at 30°S, 20° apart in longitude. $D = 111.2 \times \cos 30^\circ \times 20 \approx 1926$ km.
- **Time:** 45° of longitude = $45 \div 15 = 3$ hours. Places further **east** are ahead.

## Unit 4

### 6. Compound interest

<Diagram name="ex-6-compound" />
\$5 000 at 6% p.a. compounded **monthly** for 3 years.
- $i = \dfrac{0.06}{12} = 0.005$, $n = 3 \times 12 = 36$
- $A = 5000 \times 1.005^{36} = \$5\,983.40$
- Interest earned $= \$983.40$
- **Effective annual rate:** $(1.005)^{12} - 1 = 0.0617$, i.e. **6.17%**.

### 7. Reducing-balance loan (present value annuity)

<Diagram name="ex-7-loan" />
Borrow \$20 000 at 7.2% p.a., repaid **monthly** over 5 years.
- $i = \dfrac{0.072}{12} = 0.006$, $n = 60$
- Rearrange $A_{PV} = d \times \dfrac{1-(1+i)^{-n}}{i}$ for $d$: $d = \dfrac{20\,000 \times 0.006}{1 - 1.006^{-60}} \approx \$397.91$ per month
- Total repaid $\approx \$23\,874.83$; interest ≈ **\$3 874.83** (calculated from the unrounded payment).

### 8. Future value annuity (savings)

<Diagram name="ex-8-annuity" />
Deposit \$200 monthly at 4.8% p.a. compounded monthly for 10 years.
- $i = 0.004$, $n = 120$
- $A_{FV} = 200 \times \dfrac{1.004^{120} - 1}{0.004} \approx \$30\,726.39$
- Total deposits $= 200 \times 120 = \$24\,000$; interest ≈ **\$6 726.39**.

### 9. Perpetuity

<Diagram name="ex-9-perpetuity" />
Receive \$500 per quarter from an investment earning 4% p.a. compounded quarterly.
- $i = \dfrac{0.04}{4} = 0.01$
- $A = \dfrac{d}{i} = \dfrac{500}{0.01} = \$50\,000$

### 10. Graph theory

<Diagram name="ex-10-wheel" />
- **Euler's formula:** a planar graph has $v = 6$, $e = 10$. $f = 2 + e - v = 2 + 10 - 6 = 6$ faces.
- **Eulerian circuit:** degrees 2, 4, 2, 4, 2 are all even (and the graph is connected), so an Eulerian circuit exists.
- **Eulerian trail:** exactly two odd-degree vertices (all other even).

### 11. Critical path analysis

<Diagram name="ex-11-critical" />
| Activity | Duration | Predecessors |
|---|---|---|
| A | 3 | none |
| B | 4 | A |
| C | 2 | A |
| D | 5 | B, C |
| E | 3 | D |

- Path A→B→D→E = 3 + 4 + 5 + 3 = **15**; path A→C→D→E = 3 + 2 + 5 + 3 = 13.
- **Critical path:** A, B, D, E. **Minimum project time:** 15.
- **Float for C:** 15 − 13 = **2** (C can be delayed by 2 without delaying the project).

### 12. Flow network (min cut = max flow)
Edges (capacity): S→A 10, S→B 8, A→B 3, A→T 7, B→T 9.
| Cut (source side) | Edges crossing S-side → T-side | Capacity |
|---|---|---|
| {S} | S→A, S→B | 18 |
| {S, A} | S→B, A→B, A→T | 18 |
| {S, B} | S→A, B→T | 19 |
| {S, A, B} | A→T, B→T | **16** |

**Minimum cut = 16, so maximum flow = 16.**

### 13. Hungarian algorithm (assignment)

<Diagram name="ex-13-hungarian" />
Cost matrix (rows = workers, columns = jobs):
| | J1 | J2 | J3 |
|---|---|---|---|
| W1 | 9 | 2 | 7 |
| W2 | 6 | 4 | 3 |
| W3 | 5 | 8 | 1 |

**Steps:** row reduction (subtract each row minimum): rows become $[7,0,5]$, $[3,1,0]$, $[4,7,0]$. Column reduction (subtract column minimum): column 1 min 3, giving $[4,0,5]$, $[0,1,0]$, $[1,7,0]$. Cover all zeros with the minimum lines (3 lines needed = n, so optimal).
**Assignment:** W1 → J2 (2), W2 → J1 (6), W3 → J3 (1). **Minimum total cost = 9.**
(For a **maximisation** problem, subtract every entry from the largest entry first.)

---

### 14. Time zones, then distance and time together

<Diagram name="ex-14-flight" />
Flight from Sydney (UTC+10) departs 9:50 pm Tuesday and lands in Los Angeles (UTC−8) at 6:50 pm Tuesday (local). Total distance 12 070 km. When has it flown 4828 km?
- Time difference = 10 − (−8) = **18 h** (Sydney is ahead).
- Arrival in Sydney time = 6:50 pm Tuesday + 18 h = **12:50 pm Wednesday**, so the flight takes **15 h**.
- Fraction flown = 4828 ÷ 12 070 = 0.4, so time flown = 0.4 × 15 = **6 h**.
- Sydney time = 9:50 pm Tuesday + 6 h = **3:50 am Wednesday**.

### 15. Loan recurrence, balance and interest
\$15 000 loan at 8.4% p.a. compounding monthly, \$250 repaid at the end of each month.
- Monthly rate = 0.084 ÷ 12 = 0.007, so $\mathbf{A_{n+1} = 1.007\,A_n - 250,\; A_0 = 15\,000}$.
- A(1) = 1.007 × 15 000 − 250 = 14 855. A(2) = 1.007 × 14 855 − 250 = **\$14 708.99**.
- Interest in the first two months = total repayments − reduction in balance = 500 − (15 000 − 14 708.99) = **\$208.99**. (Check: 0.007 × 15 000 + 0.007 × 14 855 = 105 + 103.99.)

### 16. Adjacency matrix and Euler trail

<Diagram name="ex-16-adjacency" />
Graph with edges A–B, A–C, B–C, C–D.
- Matrix (rows/columns A–D): A [0 1 1 0], B [1 0 1 0], C [1 1 0 1], D [0 0 1 0].
- Degrees: A 2, B 2, C 3, D 1 (sum 8 = 2 × 4 edges). Exactly two odd vertices (C and D), so an **Eulerian trail** exists from C to D (for example C–A–B–C–D) but no Eulerian circuit.

## Practice questions (answers at the end)
1. $r = -0.9$, $s_x = 4$, $s_y = 12$, $\bar{x} = 20$, $\bar{y} = 100$. Find the least-squares line and $R^2$.
2. Calculate the 3-point moving average of 8, 10, 13, 12, 15.
3. An arithmetic sequence has $t_1 = 7$, $d = 4$. Find $t_{15}$.
4. A geometric sequence has $t_1 = 5$, $r = 3$. Find $t_4$.
5. How much is \$2 000 worth after 2 years at 5% p.a. compounded quarterly?
6. A perpetuity pays \$1 200 per year at 6% p.a. How much is invested?
7. A connected planar graph has $v = 8$, $f = 7$. Find $e$.
8. A project has $A(2) \to B(5) \to D(4)$ and $A(2) \to C(6) \to D(4)$. Find the critical path, minimum time and the float of the non-critical activity.
9. A time difference of 5 hours corresponds to how many degrees of longitude?
10. Explain why extrapolation is risky when using a least-squares line.

### Answers
1. $m = -0.9 \times \dfrac{12}{4} = -2.7$; $c = 100 - (-2.7)(20) = 154$; $\mathbf{y = -2.7x + 154}$; $R^2 = 0.81$ (**81%**).
2. $\dfrac{8+10+13}{3} =$ **10.3**; 11.67 → **11.7**; 13.33 → **13.3**. (Values: 10.3, 11.7, 13.3.)
3. $7 + 14 \times 4 = 63$.
4. $5 \times 3^{3} = 135$.
5. $i = 0.0125$, $n = 8$: $2000 \times 1.0125^{8} \approx \$2\,208.97$ (rounded).
6. $A = \dfrac{1200}{0.06} = \$20\,000$.
7. $v + f - e = 2$ → $8 + 7 - e = 2$ → $\mathbf{e = 13}$.
8. A→C→D = 2 + 6 + 4 = 12 (**critical**); A→B→D = 11. **Minimum time 12.** B has float 1.
9. $5 \times 15 = 75^\circ$.
10. Extrapolating predicts outside the data range, where the linear relationship may not continue; the model has no evidence there, so predictions may be inaccurate.

## Calculator habits
- Clear memory; check the calculator is in **normal/scientific mode** and degrees.
- Use brackets around `(1 + i)` and the denominator in annuity formulas.
- Store `i` and `n` to avoid retyping.
- Write the formula, substitute values, then the answer with units, then a sentence in context for Paper 2.
