---
name: genpark-personal-agent-indoor-co2-cognitive-ventilation-skill
description: Personal Agent Indoor CO2 Cognitive Ventilation. Forecasts carbon dioxide buildup in rooms via mass balance differential equations, quantifies cognitive impairment, and schedules window-open purge cycles.
license: MIT
version: 1.0.0
tools:
  - forecast_indoor_co2_accumulation
  - evaluate_co2_cognitive_performance_impairment
  - calculate_optimal_ventilation_purge_window
---

# Personal Agent Indoor CO2 Cognitive Ventilation

## Overview & Agent Behavioral Directives
You are a sovereign Personal Agent workspace environmental and cognitive health guardian. Your purpose is to protect user strategic thinking and executive function from invisible carbon dioxide accumulation in enclosed offices and bedrooms.

## When to Activate This Skill
- When an agent or user reviews office dimensions, indoor sensors, or closed-door work sessions.
- When evaluating afternoon brain fog, sluggishness, or headache risks in conference rooms or home offices.
- When scheduling optimal fresh air purge intervals to preserve peak cognitive throughput.

## How to Execute

### Option 1: Zero-Dependency Python Execution
```python
from client import PersonalAgentIndoorCO2CognitiveVentilation

vent = PersonalAgentIndoorCO2CognitiveVentilation()
res = vent.evaluate_co2_cognitive_performance_impairment(1200.0)
print("Cognitive Impairment:", res["estimated_cognitive_impairment_pct"], "%")
```

### Option 2: FastMCP Tool Calling
- `forecast_indoor_co2_accumulation(room_volume_m3, occupants_count, air_changes_per_hour_ach, initial_co2_ppm, duration_hours)`
- `evaluate_co2_cognitive_performance_impairment(current_co2_ppm)`
- `calculate_optimal_ventilation_purge_window(room_volume_m3, occupants_count, target_ceiling_ppm)`

## Core Mathematical Principles
1. **Mass Balance Buildup**: $C(t) = C_{	ext{ambient}} + rac{G}{Q}(1 - e^{-ACH \cdot t}) + C_0 e^{-ACH \cdot t}$.
2. **Satish Cognitive Decline**: $	ext{CO}_2 > 1000\ 	ext{ppm}$ causes direct degradation of high-level decision making and strategic planning.
