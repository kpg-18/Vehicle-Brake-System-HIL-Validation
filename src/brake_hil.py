from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import List


class FaultScenario(Enum):
    SENSOR_OFFSET = "sensor_offset"
    ACTUATOR_STUCK = "actuator_stuck"
    BRAKE_PRESSURE_DROP = "brake_pressure_drop"
    COMMUNICATION_DELAY = "communication_delay"


@dataclass
class SimulationResult:
    vehicle_speed_kph: float
    brake_pressure_bar: float
    latency_ms: float
    lka_status: str
    fault_name: str | None = None


@dataclass
class FaultInjection:
    name: FaultScenario
    severity: float
    description: str


class LaneKeepAssist:
    def __init__(self):
        self.active = False

    def update(self, vehicle_speed_kph: float, brake_pressure_bar: float, steering_error: float) -> str:
        if vehicle_speed_kph > 30.0 and abs(steering_error) < 0.25 and brake_pressure_bar < 18.0:
            self.active = True
        else:
            self.active = False
        return "active" if self.active else "inactive"


class BrakeHILSystem:
    def __init__(
        self,
        initial_speed_kph: float = 120.0,
        brake_pedal_force: float = 45.0,
        fault: FaultScenario | None = None,
        fault_severity: float = 0.15,
    ) -> None:
        self.vehicle_speed_kph = initial_speed_kph
        self.brake_pedal_force = brake_pedal_force
        self.fault = fault
        self.fault_severity = fault_severity
        self.lka = LaneKeepAssist()

    def apply_fault(self) -> float:
        if self.fault is None:
            return 1.0

        if self.fault == FaultScenario.SENSOR_OFFSET:
            return 1.0 - self.fault_severity
        if self.fault == FaultScenario.ACTUATOR_STUCK:
            return 0.6
        if self.fault == FaultScenario.BRAKE_PRESSURE_DROP:
            return 0.7
        if self.fault == FaultScenario.COMMUNICATION_DELAY:
            return 0.9
        return 1.0

    def compute_brake_pressure(self) -> float:
        pedal_factor = self.brake_pedal_force / 100.0
        base_pressure = 30.0 * pedal_factor
        fault_factor = self.apply_fault()
        pressure = max(0.0, base_pressure * fault_factor)
        return pressure

    def compute_latency(self) -> float:
        base_latency_ms = 15.0 + (self.brake_pedal_force / 10.0)
        if self.fault == FaultScenario.COMMUNICATION_DELAY:
            base_latency_ms += 20.0 * self.fault_severity
        return max(0.0, base_latency_ms)

    def run_cycle(self, duration_s: float = 1.0) -> SimulationResult:
        brake_pressure_bar = self.compute_brake_pressure()
        latency_ms = self.compute_latency()

        decel_factor = brake_pressure_bar / 30.0
        speed_drop = min(self.vehicle_speed_kph, 10.0 * decel_factor * duration_s)
        self.vehicle_speed_kph = max(0.0, self.vehicle_speed_kph - speed_drop)

        steering_error = 0.12 if self.vehicle_speed_kph > 60.0 else 0.40
        lka_status = self.lka.update(self.vehicle_speed_kph, brake_pressure_bar, steering_error)

        return SimulationResult(
            vehicle_speed_kph=round(self.vehicle_speed_kph, 2),
            brake_pressure_bar=round(brake_pressure_bar, 2),
            latency_ms=round(latency_ms, 2),
            lka_status=lka_status,
            fault_name=self.fault.value if self.fault else None,
        )


def generate_fault_scenarios() -> List[FaultInjection]:
    return [
        FaultInjection(FaultScenario.SENSOR_OFFSET, 0.20, "Wheel-speed sensor offset causing false deceleration estimation."),
        FaultInjection(FaultScenario.ACTUATOR_STUCK, 0.35, "Brake actuator stuck at an intermediate position."),
        FaultInjection(FaultScenario.BRAKE_PRESSURE_DROP, 0.30, "Hydraulic pressure drop reduces braking force."),
        FaultInjection(FaultScenario.COMMUNICATION_DELAY, 0.25, "CAN or ECU communication delay affecting brake response."),
    ]


def main() -> None:
    system = BrakeHILSystem(initial_speed_kph=120.0, brake_pedal_force=42.0)
    result = system.run_cycle(duration_s=2.0)
    print(f"Simulation time: 2.00 s")
    print(f"Vehicle speed: {result.vehicle_speed_kph:.2f} km/h")
    print(f"Brake pressure: {result.brake_pressure_bar:.2f} bar")
    print(f"Latency: {result.latency_ms:.2f} ms")
    print(f"LKA status: {result.lka_status}")
    if result.fault_name:
        print(f"Fault: {result.fault_name}")


if __name__ == "__main__":
    main()
