# Method and Governance Note

SVDF is a transparent portfolio-screening method. Shared Value Gain, Implementation Complexity, budget, evidence quality and organisational answerability are deliberately kept separate.

## Shared Value Gain
SVG uses a geometric aggregation of three normalized value dimensions. Raw measures are organisation-specific, but their meanings must remain consistent across alternatives in the same analysis.

## Implementation Complexity
IC is a weighted combination of burden, scale and volatility. It is not CAPEX, duration or risk in isolation.

## Dominance
Alternative a dominates b when `IC_a <= IC_b` and `SVG_a >= SVG_b`, with at least one strict improvement.

## Robustness
The Python engine varies value weights with Dirichlet(6,6,6) and complexity weights with Dirichlet(8,7,5) across 2,000 draws by default using seed 2026. The static browser app performs the same conceptual analysis but browser random generation is not archived with a deterministic seed. For audit-grade reproducibility, use the Python engine or GitHub Actions artifact.

## Evidence governance
Do not manufacture missing evidence. Missing values should remain missing or be declared as estimates with an evidence note.

## Decision governance
The frontier is a shortlist, not automatic approval. Final decisions may legitimately exclude a frontier project because of budget, safety, law, ethics, timing or strategy.

## Audit trail
Archive the input CSV, software version/commit, decision context, output CSV/JSON, final report and meeting record where the decision was taken.
