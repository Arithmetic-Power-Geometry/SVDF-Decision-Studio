# SVDF Decision Studio

**Shared Value Decision Frontier decision-support software for universities, companies, hospitals, municipalities and other organisations.**

Copyright © 2026 Mohammad Amir Khusru Akhtar  
Usha Martin University, Ranchi, Jharkhand, India  
License: Apache License 2.0

<a href="https://www.apache.org/licenses/LICENSE-2.0"
   target="_blank"
   rel="noopener noreferrer">Apache License 2.0</a>

## Problem first
Organisations often have several projects that all look worthwhile, but money, time, staff and managerial attention are limited. A normal weighted ranking can hide important trade-offs because one very strong dimension can compensate for a weak one.

SVDF changes the first strategic screening question:

> Which alternatives cannot be clearly beaten on both shared value and implementation complexity?

## What the system does
The browser app guides the user through 10 pages:
1. Define the decision and decision owner.
2. Add competing projects.
3. Enter economic, environmental and stakeholder-reach evidence.
4. Enter implementation burden, scale and volatility.
5. Record evidence source and confidence.
6. Set baseline weights and optional budget.
7. Compute SVG, IC and the non-dominated frontier.
8. Recompute the frontier across alternative value and complexity weights.
9. Record an EA-inspired organisational-answerability diagnostic.
10. Generate a detailed management report and export CSV/JSON.

## Core model
For project j, SVG is a weighted geometric mean of normalized economic value, environmental value and stakeholder reach. The paper baseline uses equal value weights.

Implementation Complexity uses:

`IC_j = 0.40 B_j + 0.35 L_j + 0.25 R_j`

where:
- **B — implementation burden:** how hard the project itself is to deliver;
- **L — scale:** how large the implementation is;
- **R — volatility/uncertainty:** how unstable or uncertain the operating baseline/evidence is.

The 40:35:25 weights are a declared baseline model specification, not universal empirically estimated constants. The robustness module varies both value and complexity weights across 2,000 draws by default.

A project is dominated if another alternative has lower-or-equal IC and higher-or-equal SVG, with at least one strict improvement. Non-dominated projects form the frontier.

## Normalisation
The generic software uses within-portfolio percentile ranks. Scores are therefore relative to the alternatives being considered. Changing the portfolio can change normalized values and the frontier.

## Organisational answerability
Frontier membership is not automatic funding approval. The system keeps six EA-inspired checks separate rather than hiding them inside one score: Difference, Availability, Orientation, Integration, Temporality and Answerability.

## Evidence discipline
Every project can record an evidence source, confidence and note. Evidence confidence is reported separately. It does not secretly alter SVG or IC. Optional CAPEX and budget are also kept separate from IC.

## Samples
The `samples/` folder contains the exact paper-reproduction dataset, six broader scenarios and a blank template:
- paper reproduction (32 UNICON-derived interventions);
- university energy;
- corporate decarbonisation;
- hospital sustainability;
- manufacturing efficiency;
- municipal projects;
- digital infrastructure;
- blank portfolio template.

These are demonstration scenarios for learning and testing, not empirical claims.

## Run in browser
For local use, serve the repository root so sample files can be loaded:

```bash
python -m http.server 8000
```

Then open `http://localhost:8000/web/`. The browser app also deploys through GitHub Pages.

The **paper_reproduction** sample uses the original 32-intervention paper schema. The Python/GitHub Actions engine is the audit-grade reproduction path because it uses a fixed seed. The browser robustness view is interactive and may vary slightly between runs.

## Python CLI
```bash
python python/cli.py samples/university_energy.csv --draws 2000 --out outputs/university_energy.json
```

## Optional API
```bash
pip install -r requirements.txt
uvicorn api_server:app --app-dir python --reload
```
Then POST a project portfolio to `/analyze`.

## Tests
```bash
python -m pytest -q
```

## GitHub Actions
Two workflows are included:
- **Run SVDF Decision Studio** — manual `Run workflow` button, tests all code and reproduces all bundled scenarios as downloadable artifacts.
- **Deploy SVDF Decision Studio to Pages** — publishes the static browser app.

For Pages, set **Settings → Pages → Source → GitHub Actions** once.

## Required CSV fields
`project_id, project_name, economic_value, environmental_value, stakeholder_reach, implementation_burden, scale, volatility`

Recommended:
`capex, evidence_source, evidence_confidence, evidence_note`

EA fields:
`ea_difference, ea_availability, ea_orientation, ea_integration, ea_temporality, ea_answerability`

## Responsible interpretation
SVDF is a decision-support system, not an automatic decision-maker. It does not replace financial due diligence, engineering assessment, stakeholder consultation, ethics review, regulatory review, safety assessment or managerial judgement.

## Research basis
The software generalises the research design introduced in **Not Every Green Investment Creates Shared Value: A Shared Value Decision Frontier for Resource-Constrained Universities**. The paper demonstrates the model on 32 pre-2020 LED and HVAC interventions. The Decision Studio broadens the input layer while preserving the core SVG–IC–frontier logic.

## Citation
Akhtar, Mohammad Amir Khusru. (2026). *SVDF Decision Studio: Shared Value Decision Frontier decision-support software* (Version 2.0). Apache License 2.0.

Repository: https://github.com/Arithmetic-Power-Geometry/SVDF-Decision-Studio
