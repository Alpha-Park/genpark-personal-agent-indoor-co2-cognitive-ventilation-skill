# -*- coding: utf-8 -*-
"""
Personal Agent Indoor CO2 Cognitive Ventilation Client
Zero-dependency indoor air mass balance differential equation modeler,
Satish cognitive performance impairment calculator, and ventilation purge scheduler.
"""

import math
from typing import Dict, List, Any, Optional

class PersonalAgentIndoorCO2CognitiveVentilation:
    """
    Models indoor carbon dioxide buildup in offices and bedrooms.
    Quantifies cognitive performance impairment and calculates optimal ventilation windows.
    """

    def forecast_indoor_co2_accumulation(
        self,
        room_volume_m3: float,
        occupants_count: int = 1,
        air_changes_per_hour_ach: float = 0.5,
        initial_co2_ppm: float = 450.0,
        duration_hours: float = 4.0
    ) -> Dict[str, Any]:
        """
        Mass balance CO2 model:
        C(t) = C_ambient + (G / Q) * (1 - exp(-Q*t/V)) + (C0 - C_ambient) * exp(-Q*t/V)
        G = human generation rate (~18 Liters CO2/hour per sedentary adult).
        Q = ventilation volume flow rate (V * ACH m^3/h).
        """
        v = max(10.0, float(room_volume_m3))
        n_people = max(1, int(occupants_count))
        ach = max(0.05, min(10.0, float(air_changes_per_hour_ach)))
        c0 = max(400.0, float(initial_co2_ppm))
        t = max(0.5, float(duration_hours))
        c_ambient = 420.0

        # Human CO2 generation: 18 Liters/h = 0.018 m^3/h per person
        g_total = n_people * 0.018
        q = v * ach

        # Steady-state asymptote: C_ss = C_ambient + (G / Q) * 10^6 ppm
        c_ss = c_ambient + (g_total / max(1e-6, q)) * 1_000_000.0

        # Terminal CO2 at duration t
        exp_decay = math.exp(-ach * t)
        c_terminal = c_ss * (1.0 - exp_decay) + c0 * exp_decay
        c_terminal = round(c_terminal, 1)

        # Time to cross 1000 ppm cognitive threshold
        if c_ss > 1000.0 and c0 < 1000.0:
            # 1000 = C_ss * (1 - exp(-ach * t)) + C0 * exp(-ach * t)
            # 1000 - C_ss = exp(-ach * t) * (C0 - C_ss)
            ratio = (1000.0 - c_ss) / (c0 - c_ss)
            t_to_1000 = round(-math.log(max(1e-6, ratio)) / ach, 2)
        elif c0 >= 1000.0:
            t_to_1000 = 0.0
        else:
            t_to_1000 = None

        return {
            "room_volume_m3": v,
            "occupants_count": n_people,
            "air_changes_per_hour_ach": ach,
            "initial_co2_ppm": c0,
            "duration_hours": t,
            "predicted_terminal_co2_ppm": c_terminal,
            "steady_state_ceiling_co2_ppm": round(c_ss, 1),
            "hours_until_1000ppm_threshold": t_to_1000,
            "air_quality_verdict": "CRITICAL_COGNITIVE_HAZARD" if c_terminal >= 1500.0 else ("MODERATE_STUFFINESS" if c_terminal >= 1000.0 else "EXCELLENT_AIR_EXCHANGE")
        }

    def evaluate_co2_cognitive_performance_impairment(
        self,
        current_co2_ppm: float
    ) -> Dict[str, Any]:
        """
        Quantifies Satish et al. cognitive performance decline curves based on CO2 concentration.
        """
        ppm = max(400.0, float(current_co2_ppm))

        # Impairment curve starting above 600 ppm
        if ppm <= 600.0:
            impairment_pct = 0.0
            verdict = "PEAK_COGNITIVE_CLARITY"
        elif ppm <= 1000.0:
            impairment_pct = round((ppm - 600.0) * 0.035, 1)
            verdict = "MILD_DECISION_MAKING_SLUMP"
        elif ppm <= 1500.0:
            impairment_pct = round(14.0 + (ppm - 1000.0) * 0.07, 1)
            verdict = "SEVERE_STRATEGIC_THINKING_DECLINE (Up to 50% drop in complex initiative)"
        else:
            impairment_pct = round(min(75.0, 49.0 + (ppm - 1500.0) * 0.04), 1)
            verdict = "LETHARGY_AND_EXECUTIVE_COLLAPSE (Acute somnolence and headache)"

        return {
            "co2_concentration_ppm": ppm,
            "estimated_cognitive_impairment_pct": impairment_pct,
            "cognitive_performance_index": round(100.0 - impairment_pct, 1),
            "clinical_verdict": verdict,
            "ventilation_action_required": ppm >= 950.0
        }

    def calculate_optimal_ventilation_purge_window(
        self,
        room_volume_m3: float,
        occupants_count: int = 1,
        target_ceiling_ppm: float = 900.0
    ) -> Dict[str, Any]:
        """
        Calculates required natural purge duration (window open: ~5 ACH) to drop CO2 back to 500 ppm.
        """
        v = max(10.0, float(room_volume_m3))
        target = max(600.0, float(target_ceiling_ppm))

        # Purge with open window: ACH ~ 6.0
        purge_ach = 6.0
        # Time to clear: C(t) = C_ambient + (C_start - C_ambient) * exp(-ACH * t)
        # Drop from target to 500 ppm: (500 - 420) / (target - 420) = exp(-6 * t)
        ratio = (500.0 - 420.0) / max(1.0, target - 420.0)
        purge_hours = -math.log(max(0.01, ratio)) / purge_ach
        purge_minutes = round(max(3.0, purge_hours * 60.0), 1)

        return {
            "room_volume_m3": v,
            "target_ceiling_ppm": target,
            "open_window_purge_ach": purge_ach,
            "recommended_purge_window_minutes": purge_minutes,
            "actionable_rule": f"Open window for {int(purge_minutes)} minutes to flush room back to baseline 500 ppm."
        }
