# SVDF Decision Studio — Complete User Guide

## A practical guide for first-time users

**SVDF Decision Studio** helps an organisation compare several worthwhile projects when it cannot implement all of them at once.

The software does **not** simply declare one project the winner. It asks:

> **Which projects cannot be clearly beaten by another project that provides at least as much shared value with no greater implementation complexity?**

Those projects form the **Shared Value Decision Frontier (SVDF)**.

This guide explains every page and every field using a simple university example. The same procedure can be used by a company, hospital, municipality, public agency, NGO, or other organisation.

---

# Before You Begin

Suppose a university is considering five sustainability projects:

| Project ID | Project |
|---|---|
| U-SOLAR | Rooftop solar |
| U-LED | LED retrofit |
| U-HVAC | HVAC optimisation |
| U-METER | Smart metering |
| U-WATER | Rainwater harvesting |

The university has limited money and management capacity. All five projects may be useful, but they differ in value, implementation difficulty, evidence quality, and organisational readiness.

SVDF helps management identify the strategically efficient alternatives before a final funding decision is made.

---

# Page 1 — Context

## Purpose of this page

Before entering project scores, tell the software **what decision is actually being made**.

A decision model is meaningful only when the alternatives are competing within the same decision context.

## 1. Organisation

**What it means:**  
The institution or organisational unit making the decision.

**Example value:**  
`Usha Martin University`

Other examples:

- `ABC Hospital`
- `Ranchi Municipal Corporation`
- `XYZ Manufacturing Ltd.`

**Why it is used:**  
The final report needs to identify whose portfolio is being analysed.

**Do not enter:** the project name here.

## 2. Decision Owner

**What it means:**  
The person, committee, or organisational body responsible for considering the recommendation.

**Example value:**  
`University Sustainability Committee`

Other examples:

- `Vice Chancellor`
- `Board Investment Committee`
- `Chief Sustainability Officer`

**Why it is used:**  
SVDF provides decision support. It does not replace the person or committee with authority to make the actual decision.

## 3. Decision Question

This is one of the most important fields.

**Example:**  
`Which campus sustainability projects should receive further investment review for FY 2027?`

**Why it is used:**  
It establishes what the alternatives are competing for.

A good question identifies a real management decision.

**Good:**

> Which sustainability investments should receive further funding review for FY 2027?

**Weak:**

> Which project is best?

“Best” is too vague. Best in cost, environmental benefit, ease of implementation, stakeholder impact, or some combination?

SVDF exists precisely because these dimensions may conflict.

## 4. Optional Budget

**Example:**  
`10000000`

If the currency is INR, this represents ₹1 crore.

**Why it is used:**  
The software can identify whether the stated CAPEX of a project lies within the declared budget.

### Important distinction

**Budget is not Implementation Complexity.**

A project can be expensive but operationally simple. Another can be relatively inexpensive but extremely difficult to coordinate.

SVDF therefore keeps financial budget and implementation complexity separate.

Leave this field blank if no budget has yet been approved.

## 5. Currency

**Example:**  
`INR`

Other examples:

- `USD`
- `EUR`
- `GBP`

**Why it is used:**  
It tells the reader how monetary values such as CAPEX should be interpreted.

It does not affect the frontier mathematics.

## 6. Decision Date

**Example:**  
`2026-08-12`

**Why it is used:**  
A decision analysis represents evidence available at a particular point in time. Costs, technologies, and organisational priorities may later change.

Recording the date creates an audit trail.

## 7. Context and Constraints

This is a free-text field.

**Example:**

> The university intends to reduce electricity use and environmental impact while maintaining normal academic operations. Capital funding and implementation capacity are limited. Projects causing major teaching disruption should be carefully reviewed.

**Why it is used:**  
Not every relevant management consideration can be represented by SVG and IC.

This field records important conditions that management should remember when interpreting the results.

---

# Page 2 — Projects

## Purpose of this page

Now tell SVDF **which alternatives are actually competing**.

A frontier cannot be calculated for one project in isolation. SVDF is comparative.

## 1. Project ID

**Example:**  
`U-SOLAR`

**Meaning:**  
A short, unique identifier.

Other examples:

- `U-LED`
- `U-HVAC`
- `H-SOLAR`
- `CITY-BUS`

**Why it is used:**  
Short IDs make graphs, tables, and exported results easier to read.

**Rule:**  
Every project must have a different ID.

Do not give two projects the same ID.

## 2. Project Name

**Example:**  
`Rooftop solar`

**Meaning:**  
A plain-language description of the alternative.

**Why it is used:**  
Management should understand the project without having to interpret technical codes.

Use:

`LED retrofit`

rather than:

`Project 2A-REV`

unless the latter is an established internal project name.

## 3. Category

Where used, category provides a descriptive grouping such as:

- `Energy`
- `Water`
- `Waste`
- `Mobility`
- `Digital`
- `Community`

**Why it is used:**  
It helps organise the portfolio and final report.

Category does not automatically alter SVG or IC.

## 4. CAPEX

**Example for Rooftop Solar:**  
`9500000`

Meaning:

₹9,500,000 = ₹95 lakh.

**Why it is used:**  
CAPEX lets management compare the project with the optional budget.

> **CAPEX is kept separate from Implementation Complexity.**

Do not put a difficulty score in this field.

## 5. Loading a CSV

Instead of entering projects manually, you can upload a CSV such as:

`university_energy.csv`

The core columns are:

```text
project_id
project_name
economic_value
environmental_value
stakeholder_reach
implementation_burden
scale
volatility
```

The supplied university CSV additionally contains CAPEX, evidence, and organisational-answerability fields.

---

# Page 3 — Shared Value

## Purpose of this page

This page asks:

> **How much value does each project create?**

SVDF represents shared value using three dimensions:

**Economic Value + Environmental Value + Stakeholder Reach**

These dimensions remain separate before they are combined into Shared Value Gain.

## 1. Economic Value

### Meaning

The economic or institutional benefit expected from the project.

It could represent:

- annual financial saving;
- net present value;
- avoided cost;
- productivity gain;
- revenue contribution; or
- a carefully defined economic-benefit score.

### University example

Rooftop Solar:

`18`

LED Retrofit:

`8`

### Why it is used

A sustainability project should not be evaluated only for environmental attractiveness. Management must also understand the institutional or economic value it creates.

### Critical rule

The meaning must remain the same across the portfolio.

If `18` means **₹18 lakh annual saving** for solar, then `8` should mean **₹8 lakh annual saving** for LED.

Do **not** use annual saving for Project A, ROI percentage for Project B, and NPV for Project C in the same column.

Convert them first to a common measure.

## 2. Environmental Value

### Meaning

The environmental benefit created by the project.

Possible measures include:

- annual electricity saved;
- annual CO₂ avoided;
- water conserved;
- waste diverted;
- renewable electricity produced; or
- a consistently constructed environmental-benefit score.

### University example

Rooftop Solar:

`22`

LED Retrofit:

`9`

### Why it is used

A project with good financial returns does not necessarily produce the strongest environmental benefit.

SVDF therefore keeps environmental value visible rather than treating sustainability as a side effect of ROI.

### Consistency rule

If this column represents tonnes of CO₂ avoided annually, use tonnes of CO₂ avoided annually for **every project**.

## 3. Stakeholder Reach

### Meaning

How many people, sites, users, customers, students, employees, or community members materially benefit from the intervention.

### University examples

Rooftop Solar:

`4200`

LED Retrofit:

`5100`

Smart Metering:

`6000`

### Why it is used

Creating Shared Value is broader than private financial return.

A project that affects a large student or staff community may create a different kind of strategic value from a narrowly targeted intervention.

### What counts as reach?

Count stakeholders who are meaningfully affected.

Do not artificially inflate this number by counting people with no material connection to the intervention.

## How SVDF combines the three dimensions

For project \(j\), Shared Value Gain is conceptually:

\[
SVG_j=(E_jV_jS_j)^{1/3}
\]

under the equal-weight baseline.

Where:

- \(E_j\) = normalized economic value;
- \(V_j\) = normalized environmental value;
- \(S_j\) = normalized stakeholder reach.

The software first converts raw values into **within-portfolio percentile scores**.

### Why a geometric mean?

Suppose a project has excellent economic and environmental performance but zero stakeholder value.

An ordinary additive score could allow the strong dimensions to compensate completely for the missing dimension.

The geometric mean does not.

If one normalized component is zero, SVG becomes zero.

This makes SVG deliberately less compensatory.

---

# Page 4 — Implementation Complexity

## Purpose of this page

A project can create large shared value and still be difficult to implement.

SVDF therefore asks:

> **How difficult is this project to deliver?**

Three dimensions are used.

## 1. Implementation Burden

### Meaning

How difficult the project itself is to execute.

Consider:

- technical difficulty;
- procurement;
- permissions;
- specialist expertise;
- installation disruption;
- coordination; and
- operational changes.

### Example

Rooftop Solar:

`7`

LED Retrofit:

`2`

### Why?

Replacing existing lamps with LEDs is usually less difficult than designing, procuring, and installing a large rooftop solar system.

Therefore LED receives lower implementation burden in this example.

### Interpretation

**Higher = harder to implement.**

## 2. Scale

### Meaning

How large the implementation is.

Scale can reflect:

- number of buildings;
- number of sites;
- systems affected;
- departments involved;
- geographic coverage; or
- organisational reach.

### Example

Rooftop Solar:

`8`

LED Retrofit:

`5`

### Why it is used

Two technically similar projects can create very different management challenges if one affects one building and the other affects an entire campus.

### Important

Scale does **not** mean benefit.

A large implementation may have large benefits, but scale here represents the size of the implementation task.

## 3. Volatility / Uncertainty

### Meaning

How unstable or uncertain the operating baseline or evidence is.

### Example

Rooftop Solar:

`4`

HVAC Optimisation:

`6`

LED Retrofit:

`2`

### Why might HVAC have higher volatility?

HVAC performance can depend strongly on:

- temperature;
- humidity;
- occupancy;
- operating hours;
- seasonal conditions; and
- control settings.

The expected result can therefore be harder to judge than a relatively predictable LED replacement.

### Interpretation

**Higher volatility = greater implementation or evaluation complexity.**

## Implementation Complexity equation

The baseline model uses:

\[
IC_j=0.40B_j+0.35L_j+0.25R_j
\]

where:

- \(B_j\) = normalized implementation burden;
- \(L_j\) = normalized scale;
- \(R_j\) = normalized volatility.

The baseline places:

- **40% on burden**
- **35% on scale**
- **25% on volatility**

These are **declared modelling choices**, not universal laws.

That is why Page 8 later examines whether conclusions survive alternative specifications.

---

# Page 5 — Evidence

## Purpose of this page

A decision model is only as credible as the evidence entered into it.

This page asks:

> **Where did these numbers come from, and how much confidence should management place in them?**

## 1. Evidence Source

### Example for Rooftop Solar

`feasibility study`

### LED example

`energy audit`

### HVAC example

`BMS analysis`

### Why it is used

A value of `22` by itself tells a reviewer very little.

Management needs to know whether it came from:

- a meter;
- audited accounts;
- an engineering study;
- supplier quotation;
- survey;
- pilot;
- consultant estimate; or
- informal judgement.

This creates traceability.

## 2. Evidence Confidence

Available values are:

- **High**
- **Medium**
- **Low**

### High confidence

Examples:

- audited data;
- metered consumption;
- signed quotation;
- completed feasibility study;
- verified historical records.

Example:

`Rooftop Solar → high`

### Medium confidence

Examples:

- credible engineering estimate;
- internal modelling;
- pilot study;
- consultant estimate with assumptions.

Example:

`HVAC Optimisation → medium`

### Low confidence

Examples:

- preliminary estimate;
- incomplete baseline;
- informal expert judgement;
- unverified assumption.

### Why confidence is not secretly included in SVG

This is deliberate.

Suppose Project A has very high estimated value but medium-confidence evidence.

SVDF should show both facts:

> **High apparent value**

and

> **Medium evidence confidence**

It should not silently alter the project score without telling the manager.

This preserves transparency.

## 3. Evidence Note

### Example

> Savings estimate assumes present occupancy and electricity tariff remain broadly stable during the first operating year.

### Why it is used

Important assumptions may not fit into numeric fields.

The evidence note lets the decision-maker understand what could make the estimate wrong.

---

# Page 6 — Preferences

## Purpose of this page

This page controls the declared model specification.

## 1. Shared-Value Weights

The baseline uses equal importance:

| Dimension | Baseline weight |
|---|---:|
| Economic | 0.333 |
| Environmental | 0.333 |
| Stakeholder reach | 0.333 |

### Why?

The baseline begins without assuming that one shared-value dimension is inherently more important than another.

An organisation may change these values if it has a defensible reason.

For example, a university facing a binding carbon-reduction target might choose to place greater emphasis on environmental value.

Any change should be documented.

## 2. Complexity Weights

Baseline:

| Dimension | Weight |
|---|---:|
| Implementation burden | 0.40 |
| Scale | 0.35 |
| Volatility | 0.25 |

### Why these weights?

The model treats direct implementation burden as the strongest complexity component, followed by rollout scale and then baseline or evidence volatility.

> **0.40, 0.35, and 0.25 are not natural constants.**

They are transparent modelling conventions.

This is precisely why SVDF includes robustness analysis rather than pretending one weighting system is unquestionably correct.

## 3. Robustness Draws

**Default:**  
`2000`

### Meaning

The software recomputes the frontier under many alternative value and complexity weight specifications.

### Why 2,000?

It provides a substantial sensitivity exercise without making the analysis unnecessarily cumbersome.

For normal use, retain:

`2000`

unless you have a specific methodological reason to change it.

---

# Page 7 — Shared Value Decision Frontier

## Purpose of this page

The software now combines the previous information.

Each project receives two main coordinates:

- **SVG — Shared Value Gain**
- **IC — Implementation Complexity**

The preferred direction is:

> **Higher SVG and lower IC**

## What does “dominates” mean?

Suppose Project A has:

- at least as much shared value as Project B; and
- no greater implementation complexity.

If it is strictly better on at least one of these dimensions, Project A **dominates** Project B.

Formally, \(a\) dominates \(b\) when:

\[
IC_a \le IC_b
\]

and

\[
SVG_a \ge SVG_b
\]

with at least one strict inequality.

## What is a frontier project?

A project is on the frontier if **no other available project dominates it**.

### Layman example

Imagine:

**Project A**

- Shared value = 0.80
- Complexity = 0.30

**Project B**

- Shared value = 0.60
- Complexity = 0.50

A is better in value **and** easier.

Therefore B has little strategic reason to survive the first screening.

Now consider:

**Project C**

- Shared value = 0.90
- Complexity = 0.70

A and C represent a genuine trade-off.

A is easier.

C provides more value.

Neither clearly defeats the other.

Both may therefore belong on the frontier.

## How to read the graph

**Move upward:** greater shared value.

**Move left:** lower implementation complexity.

The most interesting strategic area is therefore toward the **upper-left**.

But there does not have to be one single “best” point.

That is central to SVDF.

---

# Page 8 — Robustness

## Purpose of this page

A manager might reasonably ask:

> **Would these same projects survive if we changed the weights?**

This page answers that question.

The software recomputes the frontier across **2,000 alternative value and complexity weight specifications**.

## Frontier Frequency

Suppose a project has:

`84.6%`

frontier frequency.

### Meaning

It remained non-dominated in 84.6% of the tested alternative specifications.

That suggests its frontier position is relatively robust to reasonable changes in weighting.

If another project survives only:

`18%`

its frontier status is much more sensitive to modelling choices.

## Very important

Frontier frequency is **not**:

- probability that the project will succeed;
- a p-value;
- a confidence interval; or
- probability that management should fund it.

It is a **specification-sensitivity measure**.

It answers:

> How often does this project remain strategically non-dominated when the declared weighting conventions are varied?

---

# Page 9 — Organisational Answerability

## Purpose of this page

This is where the light **Experience Architecture (EA)** component enters.

A project can look excellent mathematically and still fail organisationally.

The question becomes:

> **Can the organisation actually act on what the evidence says?**

SVDF asks six separate questions.

The available responses are:

- **Yes**
- **Partial**
- **No**
- **Unknown**

## 1. Difference

### Question

Can the organisation clearly distinguish the problem or opportunity?

### Rooftop Solar example

`Yes`

### Why?

The university can clearly identify the opportunity: replace part of grid electricity with on-site solar generation.

### Example of “No”

Management says it wants to “improve sustainability” but cannot specify what operational problem the proposed intervention addresses.

## 2. Availability

### Question

Is relevant evidence available to the people who must decide?

### Rooftop Solar

`Yes`

because a feasibility study is available.

### Smart Metering example

`Partial`

This could mean some consumption information exists, but decision-makers do not yet have complete building-level data.

### Why this matters

Data that exist somewhere in the organisation but cannot reach the decision-maker are of limited practical use.

## 3. Orientation

### Question

Is the project connected to a declared institutional goal, strategy, or obligation?

### Example

`Yes`

if rooftop solar supports an approved energy-reduction or sustainability strategy.

### “No” example

The project sounds attractive but has no relationship to any recognised organisational objective.

## 4. Integration

### Question

Are the relevant perspectives brought together?

These may include:

- finance;
- facilities;
- engineering;
- sustainability;
- academics;
- procurement; and
- stakeholder interests.

### Rooftop Solar example

`Partial`

### Why might it be partial?

Engineering and environmental assessments may be complete, but finance, procurement, or academic-operational implications may not yet have been fully integrated.

### Why this matters

A technically excellent project can fail because departments assess it separately rather than as one institutional decision.

## 5. Temporality

### Question

Can performance be tracked over time against a meaningful baseline?

### Rooftop Solar example

`Yes`

because electricity generation and grid consumption can be monitored over time.

### Rainwater Harvesting example

`Partial`

if seasonal water data or a reliable pre-intervention baseline are incomplete.

### Why it matters

Without a baseline and follow-up period, management may never know whether the project actually produced the expected benefit.

## 6. Answerability

This is the most important final condition.

### Question

Can the evidence actually change institutional action?

For example, can evidence lead management to:

- fund;
- reject;
- delay;
- redesign;
- expand;
- reduce;
- pilot; or
- stop

the project?

### Rooftop Solar example

`Partial`

### Why?

The project may be well supported technically, but final funding authority, procurement approval, or capital allocation may still be unresolved.

### LED example

`Yes`

The evidence may already be sufficient for management to decide whether to proceed.

## How the software interprets these answers

If all six are **Yes**:

> **Decision-ready**

If some are **Partial** or **Unknown**, but none is No:

> **Conditionally decision-ready**

If one or more is **No**:

> **Not decision-ready**

This organisational diagnostic remains separate from SVG and IC.

That is deliberate.

A project can therefore be:

> **On the strategic frontier but not yet organisationally decision-ready.**

That is a useful management finding rather than a contradiction.

---

# Page 10 — Decision Report

## Purpose of this page

The final page converts the analysis into a decision record.

It is not merely a graph.

The report brings together what management entered, what the model calculated, and what remains unresolved.

## 1. Decision Context

Shows:

- organisation;
- decision question;
- decision owner; and
- budget where supplied.

This tells future readers **what decision the analysis was designed to support**.

## 2. Executive Finding

Example:

> 2 of 5 alternatives survive the Shared Value Decision Frontier.

This does **not** mean:

> Fund both immediately.

It means:

> These projects were not clearly dominated by another project under the submitted evidence and baseline specification.

## 3. Model

The report records how:

- SVG was calculated;
- IC was calculated; and
- dominance was defined.

This prevents the recommendation from becoming a black box.

## 4. Frontier Graph and Table

For each project, the output can show:

- Project ID;
- Project name;
- SVG;
- IC;
- frontier status;
- robustness or frontier frequency;
- budget status; and
- evidence confidence.

This allows management to understand **why** one project survived and another did not.

## 5. Robustness

The report shows whether the frontier changes substantially when the weighting assumptions change.

A project that survives under many specifications deserves different interpretation from one that appears on the frontier only under a narrow weighting convention.

## 6. Organisational Answerability

The report distinguishes projects that are:

- Decision-ready;
- Conditionally decision-ready; or
- Not decision-ready.

This prevents strategic attractiveness from being confused with institutional capacity to act.

## 7. Evidence and Limitations

SVDF explicitly reminds the user that:

- scores are relative to the submitted portfolio;
- IC is not CAPEX;
- evidence confidence is separate;
- results depend on data quality;
- the frontier is not a causal claim; and
- the software does not replace professional review.

## 8. Recommended Next Steps

For frontier projects, management should normally:

1. verify source data and measurement units;
2. resolve weak or low-confidence evidence;
3. check CAPEX against available budget;
4. conduct engineering and technical review;
5. check legal, safety, and procurement constraints;
6. resolve organisational-answerability weaknesses; and
7. make the final management decision.

---

# Complete University Example

Using `university_energy.csv`, the input logic can be read as follows.

## Rooftop Solar

| Field | Example value | Why it is used |
|---|---:|---|
| Project ID | U-SOLAR | Unique identifier |
| Project name | Rooftop solar | Human-readable project name |
| Economic value | 18 | Economic benefit measure |
| Environmental value | 22 | Environmental benefit measure |
| Stakeholder reach | 4200 | Material reach |
| Implementation burden | 7 | Relatively difficult delivery |
| Scale | 8 | Large implementation |
| Volatility | 4 | Moderate uncertainty |
| CAPEX | 9,500,000 | Separate monetary requirement |
| Evidence source | Feasibility study | Provenance |
| Evidence confidence | High | Strength of evidence |
| Difference | Yes | Opportunity is clear |
| Availability | Yes | Evidence reaches decision-makers |
| Orientation | Yes | Linked to institutional objective |
| Integration | Partial | Some organisational perspectives remain incomplete |
| Temporality | Yes | Performance can be monitored |
| Answerability | Partial | Evidence exists, but final institutional action is not fully enabled |

## LED Retrofit

| Field | Example value |
|---|---:|
| Project ID | U-LED |
| Economic value | 8 |
| Environmental value | 9 |
| Stakeholder reach | 5100 |
| Implementation burden | 2 |
| Scale | 5 |
| Volatility | 2 |
| CAPEX | 1,800,000 |
| Evidence source | Energy audit |
| Evidence confidence | High |
| Difference | Yes |
| Availability | Yes |
| Orientation | Yes |
| Integration | Yes |
| Temporality | Yes |
| Answerability | Yes |

This immediately shows why SVDF is useful.

**Solar has stronger economic and environmental values in this example, but it is also substantially more difficult and expensive to implement. LED has lower value on some dimensions but is easier and organisationally more ready.**

A simple “highest benefit wins” ranking can obscure this trade-off.

SVDF preserves it.

---

# The Most Important Rules for Using SVDF

1. **Compare projects belonging to the same real decision.**
2. **Keep the meaning and unit of each input column consistent across projects.**
3. **Do not manufacture numbers merely to complete the form.**
4. **Record where evidence came from.**
5. **Keep CAPEX separate from Implementation Complexity.**
6. **Do not interpret a frontier project as an automatic winner.**
7. **Use robustness to see whether conclusions depend heavily on weights.**
8. **Use organisational answerability to determine whether the institution can act.**
9. **Keep the input CSV and exported results as part of the decision audit trail.**
10. **Final approval remains a management decision, not a software decision.**

---

# One-line interpretation

> **SVDF does not ask “Which project has the highest score?” It asks “Which projects remain strategically defensible when shared value, implementation difficulty, model sensitivity, evidence quality, and organisational capacity to act are made visible?”**
