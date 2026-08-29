from src.dummy_hil import simulate_time_series


def test_simulate_time_series_structure():
    out = simulate_time_series(duration_s=1.0, sample_hz=10.0, seed=123)
    assert isinstance(out, dict)
    assert "meta" in out and "data" in out

    meta = out["meta"]
    assert meta["duration_s"] == 1.0
    assert meta["sample_hz"] == 10.0
    assert meta["samples"] == 10

    data = out["data"]
    assert isinstance(data, list) and len(data) == 10

    # Check a sample contains expected keys
    sample = data[0]
    expected_keys = [
        "t",
        "wall_time",
        "pedal_position_pct",
        "vehicle_speed_kmh",
        "wheel_speeds_kmh",
        "brake_pressure_bar",
        "ecu_command",
        "can_messages",
        "fault_active",
    ]
    for k in expected_keys:
        assert k in sample

    # wheel speeds must be list of 4
    assert isinstance(sample["wheel_speeds_kmh"], list)
    assert len(sample["wheel_speeds_kmh"]) == 4
