from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class CANMessage:
    id: str
    data: Dict[str, float]
    timestamp: float = 0.0


class CANBusMock:
    """A simplified CAN bus mock representing ECU-to-vehicle communication."""

    def __init__(self) -> None:
        self.messages: List[CANMessage] = []

    def transmit(self, message: CANMessage) -> None:
        self.messages.append(message)

    def receive(self, message_id: str | None = None) -> List[CANMessage]:
        if message_id is None:
            return list(self.messages)
        return [msg for msg in self.messages if msg.id == message_id]

    def clear(self) -> None:
        self.messages.clear()

    def packet_loss_rate(self, loss_probability: float = 0.05) -> None:
        if loss_probability > 0.0:
            keep = [msg for msg in self.messages if len(msg.data) % 2 == 0]
            self.messages = keep
