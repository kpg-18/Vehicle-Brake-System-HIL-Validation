import json
import time
import random
import os
import math
from typing import Dict, Any, List


def simulate_time_series(duration_s: float = 10.0, sample_hz: float = 50.0, seed: int | None = None):
    """Simulate time-series signals for a brake HIL prototype.

    Signals produced per timestamp:
      - pedal_position (%)
      - vehicle_speed_kmh
      - wheel_speeds_kmh (4 wheels)
      - brake_pressure_bar
      - ecu_command (0/1)
      - can_messages (list of simple dicts)

    Faults are injected at deterministic times when a seed is provided.
    """
    if seed is not None:
        random.seed(seed)

    n = int(duration_s * sample_hz)
    dt = 1.0 / sample_hz
    t0 = time.time()

    samples: List[Dict[str, Any]] = []

    # choose a fault scenario and injection time
    fault_types = [None, "sensor_offset", "actuator_stuck", "pressure_drop", "comm_delay"]
    fault = random.choice(fault_types)
    fault_start = random.uniform(duration_s * 0.2, duration_s * 0.6) if fault else None

    for i in range(n):
        ts = i * dt

        # driver pedal: a smooth press and release with small noise
        pedal = max(0.0, 100.0 * (0.5 * (1 + math.sin(2 * math.pi * (ts / duration_s))) ) )
        pedal += random.gauss(0, 1.0)

        # vehicle speed follows pedal with a lag and some dynamics
        speed = 50.0 + 40.0 * math.tanh(pedal / 100.0)
        speed += 5.0 * math.sin(2 * math.pi * ts / (duration_s / 2 + 1))
        speed += random.gauss(0, 0.5)

        # wheel speeds (kms) differ slightly per wheel
        wheel_speeds = [max(0.0, speed + random.gauss(0, 0.8)) for _ in range(4)]

        # brake pressure roughly proportional to pedal but with actuator dynamics
        pressure = 0.1 * pedal + 0.2 * math.sin(2 * math.pi * ts * 0.5) + random.gauss(0, 0.05)
        pressure = max(0.0, pressure)

        # ECU command state (1 when braking command > threshold)
        ecu_cmd = 1 if pressure > 5.0 else 0

        # CAN message examples (timestamped simple frames)
        can_msgs = [
            {"id": 0x100, "signal": "pedal", "value": round(pedal, 2)},
            {"id": 0x101, "signal": "pressure", "value": round(pressure, 3)},
            {"id": 0x200, "signal": "speed", "value": round(speed, 2)},
        ]

        # Inject faults by altering signals after fault_start
        if fault and fault_start is not None and ts >= fault_start:
            if fault == "sensor_offset":
                # wheel speed sensors report an offset
                wheel_speeds = [w + 10.0 for w in wheel_speeds]
            elif fault == "actuator_stuck":
                # pressure freezes at a previous value (simulate stuck)
                pressure = pressure if i == int(fault_start * sample_hz) else samples[-1]["brake_pressure_bar"]
            elif fault == "pressure_drop":
                # sudden pressure drop
                pressure = max(0.0, pressure * 0.4)
            elif fault == "comm_delay":
                # simulate delayed CAN frames by adding latency field
                for m in can_msgs:
                    m["latency_ms"] = random.uniform(50, 300)

        samples.append({
            "t": round(ts, 4),
            "wall_time": round(t0 + ts, 6),
            "pedal_position_pct": round(pedal, 3),
            "vehicle_speed_kmh": round(speed, 3),
            "wheel_speeds_kmh": [round(w, 3) for w in wheel_speeds],
            "brake_pressure_bar": round(pressure, 4),
            "ecu_command": ecu_cmd,
            "can_messages": can_msgs,
            "fault_active": fault if (fault and fault_start is not None and ts >= fault_start) else None,
        })

    meta = {
        "generated_at": t0,
        "duration_s": duration_s,
        "sample_hz": sample_hz,
        "samples": len(samples),
        "fault": fault,
        "fault_start_s": fault_start,
        "seed": seed,
    }

    return {"meta": meta, "data": samples}


def save_outputs(data: Dict[str, Any], out_json: str = "reports/dummy_hil_data.json", out_csv: str | None = None):
    os.makedirs(os.path.dirname(out_json), exist_ok=True)
    with open(out_json, "w") as f:
        json.dump(data, f, indent=2)
    if out_csv:
        # write a compact CSV with a subset of fields
        import csv

        with open(out_csv, "w", newline="") as cf:
            writer = csv.writer(cf)
            writer.writerow(["t", "pedal_pct", "speed_kmh", "pressure_bar", "ecu_cmd", "fault_active"])
            for s in data["data"]:
                writer.writerow([s["t"], s["pedal_position_pct"], s["vehicle_speed_kmh"], s["brake_pressure_bar"], s["ecu_command"], s["fault_active"]])


def generate_dummy_data(path_json: str = "reports/dummy_hil_data.json", path_csv: str = "reports/dummy_hil_data.csv", duration_s: float = 10.0, sample_hz: float = 50.0, seed: int | None = None):
    out = simulate_time_series(duration_s=duration_s, sample_hz=sample_hz, seed=seed)
    save_outputs(out, out_json=path_json, out_csv=path_csv)
    print(f"Wrote dummy HIL JSON to {path_json} ({out['meta']['samples']} samples)")
    print(f"Wrote dummy HIL CSV to {path_csv}")


if __name__ == "__main__":
    # default run: 10s at 50 Hz
    generate_dummy_data()
