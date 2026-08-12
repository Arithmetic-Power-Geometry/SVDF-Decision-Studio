# Data Dictionary

## General portfolio schema

| Field | Required | Meaning | Guidance |
|---|---|---|---|
| project_id | Yes | Unique project code | Short and stable, e.g. P01 |
| project_name | Yes | Human-readable alternative | Use a decision-friendly name |
| economic_value | Yes | Economic benefit | Use one consistent metric across the portfolio |
| environmental_value | Yes | Environmental benefit | Use one consistent metric across the portfolio |
| stakeholder_reach | Yes | Material stakeholder reach | People, sites, customers, staff, students or communities |
| implementation_burden | Yes | Direct delivery difficulty | Technical difficulty, approvals, procurement, disruption, specialist need |
| scale | Yes | Size of implementation | Sites, systems, departments, geography or people affected |
| volatility | Yes | Baseline/evidence instability | Higher means more unstable or uncertain |
| capex | No | Capital expenditure | Kept separate from IC |
| evidence_source | Recommended | Provenance of evidence | Audit, meter, quote, study, survey, estimate |
| evidence_confidence | Recommended | high / medium / low | Reported separately |
| evidence_note | No | Key assumptions and caveats | Plain text |
| ea_difference | No | yes / partial / no / unknown | Can the problem/opportunity be distinguished? |
| ea_availability | No | yes / partial / no / unknown | Does evidence reach decision-makers? |
| ea_orientation | No | yes / partial / no / unknown | Is the project linked to a declared goal? |
| ea_integration | No | yes / partial / no / unknown | Are relevant perspectives brought together? |
| ea_temporality | No | yes / partial / no / unknown | Can performance be tracked through time? |
| ea_answerability | No | yes / partial / no / unknown | Can evidence change institutional action? |

## Measurement rule
Do not mix meanings inside one column. If economic value is annual savings for one project, it should not be NPV for another project in the same run unless you first convert them to a common declared scale.

## Direction rule
The current implementation assumes larger economic, environmental and stakeholder values are better, while larger burden, scale and volatility mean greater complexity.
