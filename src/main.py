from brake_hil import BrakeHILSystem, FaultScenario, generate_fault_scenarios


def run_demo() -> None:
    scenarios = generate_fault_scenarios()
    print("Real-Time Vehicle Brake System Simulation using HIL")
    print("ADAS fault scenario review:\n")

    for scenario in scenarios:
        system = BrakeHILSystem(initial_speed_kph=120.0, brake_pedal_force=48.0, fault=scenario.name, fault_severity=scenario.severity)
        result = system.run_cycle(duration_s=1.5)
        print(f"Scenario: {scenario.name.value}")
        print(f"  Pressure: {result.brake_pressure_bar:.2f} bar")
        print(f"  Latency: {result.latency_ms:.2f} ms")
        print(f"  Speed: {result.vehicle_speed_kph:.2f} km/h")
        print(f"  LKA: {result.lka_status}")
        print()


if __name__ == "__main__":
    run_demo()
