# Paper Reproduction

Input: `samples/paper_reproduction.csv` (32 UNICON-derived intervention events).

Run:
```bash
python python/cli.py samples/paper_reproduction.csv --draws 2000 --seed 2026 --out outputs/paper_reproduction.json
```

Expected baseline frontier:
- U06 — LED Installation — SVG ≈ 0.048 — IC ≈ 0.233
- U05 — HVAC Tuning — SVG ≈ 0.711 — IC ≈ 0.395
- U04 — HVAC Tuning — SVG ≈ 0.752 — IC ≈ 0.408

Exact Python frontier frequencies with the fixed seed are 1.0000, 0.7535 and 0.8455 respectively. The manuscript reports these conventionally to one decimal percentage as 100.0%, 75.4% and 84.6%.

The paper-specific adapter uses:
- adjusted electricity reduction as the economic proxy;
- annualized kWh saved as the environmental proxy;
- capacity, with floor-area fallback, as the stakeholder-reach proxy;
- intervention type, floor area and pre-period coefficient of variation for complexity.

These are transparent research operationalisations for reproducing the published study. Organisations using the general Decision Studio should enter measures appropriate to their own decision context rather than treating the paper proxies as universal definitions.
