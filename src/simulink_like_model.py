from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List


@dataclass
class Block:
    name: str
    block_type: str
    description: str


class SimulinkLikeModel:
    """Minimal MATLAB/Simulink-style model structure for project traceability."""

    def __init__(self) -> None:
        self.blocks: List[Block] = [
            Block("Brake Pedal Input", "Source", "Driver brake pedal force and pedal travel signal."),
            Block("Brake Plant", "Continuous", "Hydraulic/brake-pressure response with actuator dynamics."),
            Block("Wheel Speed Sensor", "Sensor", "Vehicle speed and wheel deceleration measurement."),
            Block("ECU Controller", "Controller", "Brake-by-wire logic and safety supervision."),
            Block("Fault Injection", "Subsystem", "Sensor offset, pressure drop, communication delay simulation."),
            Block("LKA Controller", "Controller", "Prototype lane-keep assist logic."),
            Block("CAN Communication", "Bus", "Mock bus transferring ECU signals to the vehicle network."),
            Block("Monitoring", "Scope", "Latency, pressure, and fault validation outputs."),
        ]

    def model_summary(self) -> Dict[str, List[str]]:
        return {
            "in_ports": ["BrakePedalForce", "VehicleSpeed", "SteeringAngle"],
            "out_ports": ["BrakePressure", "ECUState", "LKAState", "FaultStatus"],
            "blocks": [block.name for block in self.blocks],
        }
