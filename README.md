# genpark-personal-agent-indoor-co2-cognitive-ventilation-skill

![Tests](https://img.shields.io/badge/tests-passing-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![Dependencies](https://img.shields.io/badge/dependencies-zero-success)
![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)

GenPark Personal Agent Indoor CO2 Cognitive Ventilation models indoor air quality mass balances and Satish cognitive impairment curves to ensure workspaces maintain peak oxygenation.

```mermaid
flowchart TD
    A[Room Volume, Occupants & Ventilation ACH] --> B[Mass Balance CO2 Differential Equation Solver]
    B --> C[Predicted Indoor CO2 ppm & Time-to-1000ppm]
    C --> D[Satish Cognitive Impairment Function]
    D --> E[Strategic Decision-Making Degradation %]
    E --> F[Timed Fresh Air Purge Interval Scheduler]
```

## Features
- **Differential Mass Balance Engine**: Models dynamic CO2 accumulation curves based on human metabolic exhalation.
- **Cognitive Impairment Mapping**: Translates raw ppm numbers into executive function and decision-making penalties.
- **Smart Purge Prescriptions**: Calculates exact window-opening minutes needed to flush spaces back to outdoor baselines.

## Quickstart

```python
from client import PersonalAgentIndoorCO2CognitiveVentilation

vent = PersonalAgentIndoorCO2CognitiveVentilation()
res = vent.forecast_indoor_co2_accumulation(30.0, 1, 0.4)
print("Predicted CO2:", res["predicted_terminal_co2_ppm"], "ppm")
```

## FastMCP Integration

```bash
python -m genpark-personal-agent-indoor-co2-cognitive-ventilation-skill.mcp_server
```

## License
MIT
