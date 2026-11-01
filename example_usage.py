# -*- coding: utf-8 -*-
import json
from client import PersonalAgentIndoorCO2CognitiveVentilation

ventilation = PersonalAgentIndoorCO2CognitiveVentilation()

print("=" * 64)
print("DEMO: Personal Indoor CO2 & Cognitive Performance Shield")
print("=" * 64)

# 1. Forecast CO2 buildup in home office
forecast = ventilation.forecast_indoor_co2_accumulation(
    room_volume_m3=35.0,  # 3m x 4m x 2.9m bedroom/office
    occupants_count=1,
    air_changes_per_hour_ach=0.35,  # Closed doors/windows
    initial_co2_ppm=450.0,
    duration_hours=4.0
)
print(f"\n1. Office CO2 Forecast (Closed Room, 35 m^3, 1 Occupant):")
print(f"   Initial: {forecast['initial_co2_ppm']} ppm -> After 4h: {forecast['predicted_terminal_co2_ppm']} ppm")
print(f"   Hours to 1000 ppm Impairment Threshold: {forecast['hours_until_1000ppm_threshold']} hours")
print(f"   Air Quality Verdict: {forecast['air_quality_verdict']}")

# 2. Evaluate cognitive performance impairment
impair = ventilation.evaluate_co2_cognitive_performance_impairment(current_co2_ppm=1420.0)
print(f"\n2. Cognitive Impairment at 1,420 ppm:")
print(f"   Cognitive Loss: -{impair['estimated_cognitive_impairment_pct']}% (Index: {impair['cognitive_performance_index']}/100)")
print(f"   Clinical Diagnosis: {impair['clinical_verdict']}")

# 3. Calculate purge window
purge = ventilation.calculate_optimal_ventilation_purge_window(room_volume_m3=35.0, target_ceiling_ppm=1400.0)
print(f"\n3. Optimal Air Purge Window:")
print(f"   Prescribed Window Open Time: {purge['recommended_purge_window_minutes']} minutes")
print(f"   Guidance: {purge['actionable_rule']}")
