# API Integration

Optional FastAPI endpoints:
- `GET /health`
- `POST /analyze`

Example request:
```json
{
  "projects": [
    {"project_id":"P1","project_name":"LED retrofit","economic_value":10,"environmental_value":12,"stakeholder_reach":3000,"implementation_burden":2,"scale":4,"volatility":2},
    {"project_id":"P2","project_name":"Rooftop solar","economic_value":20,"environmental_value":25,"stakeholder_reach":2500,"implementation_burden":7,"scale":7,"volatility":4}
  ],
  "draws": 2000,
  "seed": 2026,
  "budget": 10000000
}
```
Private credentials should be handled by the calling organisation. The static GitHub Pages app intentionally does not store secrets.
