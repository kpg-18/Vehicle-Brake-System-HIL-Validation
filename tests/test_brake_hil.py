from src.brake_hil import BrakeHILSystem, FaultScenario, generate_fault_scenarios


def test_brake_hil_system_tracks_basic_metrics():
    system = BrakeHILSystem(initial_speed_kph=120.0, brake_pedal_force=42.0)
    result = system.run_cycle(duration_s=2.0)

    assert result.vehicle_speed_kph <= 120.0
    assert result.brake_pressure_bar > 0.0
    assert result.latency_ms >= 0.0
    assert result.lka_status in {"active", "inactive"}


def test_fault_scenarios_include_adas_relevant_cases():
    faults = generate_fault_scenarios()
    assert len(faults) >= 4
    assert FaultScenario.SENSOR_OFFSET in [f.name for f in faults]
    assert FaultScenario.ACTUATOR_STUCK in [f.name for f in faults]
