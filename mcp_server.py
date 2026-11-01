# -*- coding: utf-8 -*-
"""
Personal Agent Indoor CO2 Cognitive Ventilation FastMCP Server
"""

import json
from typing import Dict, List, Any, Optional
from mcp.server.fastmcp import FastMCP
from client import PersonalAgentIndoorCO2CognitiveVentilation

mcp = FastMCP("genpark-personal-agent-indoor-co2-cognitive-ventilation-skill")
ventilation = PersonalAgentIndoorCO2CognitiveVentilation()

@mcp.tool()
def forecast_indoor_co2_accumulation(
    room_volume_m3: float,
    occupants_count: int = 1,
    air_changes_per_hour_ach: float = 0.5,
    initial_co2_ppm: float = 450.0,
    duration_hours: float = 4.0
) -> str:
    """
    Forecasts indoor CO2 buildup and time until cognitive impairment thresholds are breached.
    """
    res = ventilation.forecast_indoor_co2_accumulation(room_volume_m3, occupants_count, air_changes_per_hour_ach, initial_co2_ppm, duration_hours)
    return json.dumps(res, indent=2)

@mcp.tool()
def evaluate_co2_cognitive_performance_impairment(current_co2_ppm: float) -> str:
    """
    Calculates cognitive performance decline percentage based on indoor CO2 concentration.
    """
    res = ventilation.evaluate_co2_cognitive_performance_impairment(current_co2_ppm)
    return json.dumps(res, indent=2)

@mcp.tool()
def calculate_optimal_ventilation_purge_window(
    room_volume_m3: float,
    occupants_count: int = 1,
    target_ceiling_ppm: float = 900.0
) -> str:
    """
    Calculates necessary window opening duration to purge CO2 back to outdoor baseline levels.
    """
    res = ventilation.calculate_optimal_ventilation_purge_window(room_volume_m3, occupants_count, target_ceiling_ppm)
    return json.dumps(res, indent=2)

def main():
    print("Testing Indoor CO2 Cognitive Ventilation FastMCP Server:")
    print(evaluate_co2_cognitive_performance_impairment(1250.0))

if __name__ == "__main__":
    main()
