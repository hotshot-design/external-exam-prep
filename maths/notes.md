# General Maths – revision notes

::: warning The formula book is provided in the exam
Know **which** formula to use and **how** to use it with your calculator. Formulas below are from the syllabus subject matter. Confirm the exact notation against the QCAA formula book.
:::

## Unit 3

### Bivariate data

<Diagram name="maths-residuals" caption="Residual plots" />

<Diagram name="maths-scatter-lsl" caption="Least-squares line" />
- **Categorical:** two-way frequency table → percentage by the explanatory variable (column/row) → compare percentages to describe an association.
- **Numerical:** scatterplot; describe **direction** (positive/negative), **form** (linear/non-linear), **strength** (strong/moderate/weak).
- **r** (Pearson's) measures strength of a linear association: closer to ±1 = stronger.
- **$R^2$** $= r^2$ – the proportion of variation in y explained by x (as a %).
- **Least-squares line:** $y = mx + c$, with $m = r \times \dfrac{s_y}{s_x}$ and $c = \bar{y} - m\bar{x}$.
- **Residual plot:** random scatter about 0 supports a linear model; a pattern means non-linear.
- Interpret **slope** ("for each 1 unit increase in x, y increases/decreases by m on average") and **intercept** (value of y when x = 0, if meaningful).
- **Interpolation** (inside data range) is reliable; **extrapolation** (outside) is risky.
- **Association ≠ causation:** possible explanations: coincidence, a third (confounding) variable.

### Time series

<Diagram name="maths-time-series" caption="Time series" />
- Components: **trend**, **seasonality**, **irregular fluctuations**.
- **Moving average** (odd number of points): smooth data; mean or median.
- **Seasonal index (average percentage method):** average the percentages of each season's value against the yearly average; deseasonalised value = actual ÷ seasonal index.
- Fit a least-squares line to the deseasonalised data to model long-term trend.

### Sequences (growth and decay)

<Diagram name="maths-sequences" caption="Arithmetic and geometric sequences" />
- **Arithmetic** (linear): $t_n = t_1 + (n-1)d$. Recurrence: $t_{n+1} = t_n + d$. Models simple interest, flat-rate depreciation (straight-line).
- **Geometric** (exponential): $t_n = t_1 \cdot r^{\,n-1}$. Recurrence: $t_{n+1} = r\,t_n$. Models population growth, reducing-balance depreciation (r < 1 = decay).

### Earth geometry and time zones

<Diagram name="maths-time-zones" caption="Time zones" />

<Diagram name="maths-earth" caption="Earth geometry" />
- Great circles; latitude (N/S of equator), longitude (E/W of Greenwich).
- **Same meridian:** $D = 111.2 \times \text{angular distance}$ (km)
- **Same parallel:** $D = 111.2 \times \cos\theta \times \text{angular distance}$ ($\theta$ = latitude)
- Time: **15° longitude = 1 hour**; east is ahead of GMT/UTC. Watch the **International Date Line** and **daylight saving**.
- **Opposite hemispheres:** *add* the angles (18.7° N and 12.4° S on one meridian: $18.7 + 12.4 = 31.1^\circ$, so $D = 111.2 \times 31.1 \approx 3458$ km). Same hemisphere: *subtract*.
- **Time difference:** difference = (offset of the later-timezone place) − (offset of the other). Example: Nagano GMT+9 and Santa Cruz GMT−8 differ by 17 h, so 2:00 pm Monday in Nagano is 9:00 pm Sunday in Santa Cruz. Daylight saving adds 1 h to the offset (NZ summer = GMT+13).
- **Time with distance:** find the total flight time from local departure/arrival times (after converting time zones), then use proportion (distance travelled ÷ total distance × flight time). Used in 2024 Q7.
- **Longitude from time difference:** 2 h ahead = 30° further east (Osaka 135° E, so a place 2 h behind is 105° E).

## Unit 4

### Loans, investments, annuities

<Diagram name="maths-reducing-balance" caption="Reducing-balance loan" />
| Concept | Formula / recurrence |
|---|---|
| Compound interest (recurrence) | $A_{n+1} = r\,A_n$, where $r = 1 + i$ |
| Compound interest (formula) | $A = P(1+i)^n$ |
| Effective annual rate | $i_{\text{effective}} = (1+i)^k - 1$ ($k$ = periods per year) |
| Annuity present value (reducing balance loan) | $A_{n+1} = r\,A_n - d$; $A_{PV} = d \times \dfrac{1-(1+i)^{-n}}{i}$ |
| Annuity future value (savings with deposits) | $A_{n+1} = r\,A_n + d$; $A_{FV} = d \times \dfrac{(1+i)^{n}-1}{i}$ |
| Perpetuity | $A = \dfrac{d}{i}$ |

**Tips:** $i$ = annual rate ÷ periods per year; $n$ = years × periods per year; on a scientific calculator, use the **recurrence** (type the starting value, then repeatedly apply the rule with the Ans key) or the formula; check units; round only at the end. Total interest = total payments − principal.

### Method details tested in 2020–22
- **Residual** = actual − predicted. Positive residual means the point is above the line.
- **Line from r, sd and means:** slope $m = \dfrac{r\,s_y}{s_x}$; intercept $c = \bar{y} - m\bar{x}$. For a table x = 1…n, get x̄ and s(x) from the calculator.
- **Describing an association in a two-way table:** convert to percentages **within each category of the explanatory variable**, then compare the percentages. A big difference suggests an association.
- **"What does the slope mean?"** Give the change in y for each 1-unit increase in x, in context, with units.
- **Interpolation vs extrapolation:** inside the data range is interpolation (more reliable); outside is extrapolation (less reliable, say so).
- **Actual from deseasonalised:** actual = deseasonalised × seasonal index. Seasonal indices sum to the number of seasons.
- **Recurrence to a rate:** if $A_{n+1} = r\,A_n - d$, then $r = 1 + i$, so $i = r - 1$ per period (multiply by periods per year for the annual rate).
- **Annuity + lump sum:** find each separately, then add. **Perpetuity then annuity:** price the perpetuity (d ÷ i) to get the target, then find the deposit that reaches it.
- **Weekly or fortnightly vs monthly:** use i = annual rate ÷ periods per year and n = years × periods per year for each, then compare totals.
- **Geometric from two terms:** $r^{\text{gap}} = t_2 \div t_1$. Define n clearly (e.g. n = years since the start).
- **Sunrise and longitude:** 15° = 1 hour. Sunrise an hour earlier means the place is 15° further east.

### Graphs and networks

<Diagram name="maths-euler" caption="Euler's formula" />
- **Terms:** vertex, edge, loop, degree, simple, complete, bipartite, directed, weighted, **connected** (one piece), **subgraph** (part of a graph), **face** (region, including the outside); open vs closed **walk**; semi-Eulerian (Eulerian trail but not circuit); **adjacency matrix**.
- **Adjacency matrix:** an n × n table (same vertex order on both axes) with the number of edges between each pair (0 or 1 for a simple graph; symmetric if undirected). Example: edges A–B, A–C, B–C, C–D give rows A: 0 1 1 0; B: 1 0 1 0; C: 1 1 0 1; D: 0 0 1 0.
- **Planar graphs, Euler's formula:** $v + f - e = 2$.
- **Walk / trail / path / circuit / cycle:**
  | Term | Repeated edges? | Repeated vertices? | Closed? |
  |---|---|---|---|
  | Walk | allowed | allowed | open or closed |
  | Trail | no | allowed | open (a closed trail is a circuit) |
  | Path | no | no | open |
  | Circuit | no | allowed | closed |
  | Cycle | no | no (except start = end) | closed |
- **Adjacency matrix:** a double edge between two vertices gives an entry of 2; a loop adds 2 to the degree.
- **Valid cut (flow networks):** the source is on one side and the sink on the other. Add only the capacities of edges directed from the source side to the sink side.
- **Eulerian trail/circuit:** uses every edge once. Circuit: all vertices even degree. Trail: exactly 2 odd vertices.
- **Hungarian algorithm adjustment:** if fewer than n lines cover all the zeros, subtract the smallest uncovered value from every uncovered entry and add it to entries covered twice, then recheck. When n lines cover the zeros, assign using the zeros.
- **Hamiltonian path/cycle:** visits every vertex once (trial and error).
- **Shortest path:** trial and error on weighted graphs.

### Networks and decision mathematics

<Diagram name="maths-hungarian" caption="Hungarian algorithm" />

<Diagram name="maths-critical-path" caption="Critical path" />

<Diagram name="maths-flow" caption="Flow network" />

<Diagram name="maths-mst" caption="Minimum spanning tree" />
- **Minimum spanning tree:** connects all vertices at least total weight; use Kruskal's (shortest edge that doesn't form a cycle) or Prim's.
- **Critical path analysis (activity on arc):** forward scan → EST; backward scan → LST; critical activities have float = 0 (LST − EST for activity start); project time = longest path. **Float** = LST − EST.
- **Flow networks:** source, sink; capacity of a **cut** = sum of capacities of edges crossing from source side to sink side; **max flow = min cut**.
- **Hungarian algorithm (3×3 to 5×5):** row reduction → column reduction → cover zeros with min lines → adjust until lines = n → assign. For **maximum** problems, convert (subtract each value from the largest) first.

## Exam technique
- Paper 1: lots of short routine items — speed and accuracy; avoid calculator slips (check mode and brackets).
- Paper 2: contextual multi-step problems; show **working**, state **units**, write conclusions in context ("The model predicts…").
- "Justify" / "evaluate reasonableness": refer to **context** (interpolation/extrapolation, r and R², limits).
- Check answers make sense (money not negative, probabilities between 0 and 1, etc.).
