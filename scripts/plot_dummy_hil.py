import argparse
import json
import os
import matplotlib.pyplot as plt
from src.dummy_hil import simulate_time_series


def load_json(path):
    with open(path, "r") as f:
        return json.load(f)


def plot_data(data, title="Dummy HIL Signals"):
    samples = data["data"]
    t = [s["t"] for s in samples]
    pedal = [s["pedal_position_pct"] for s in samples]
    speed = [s["vehicle_speed_kmh"] for s in samples]
    pressure = [s["brake_pressure_bar"] for s in samples]
    wheel0 = [s["wheel_speeds_kmh"][0] for s in samples]

    plt.figure(figsize=(10, 8))

    plt.subplot(4, 1, 1)
    plt.plot(t, pedal, label="Pedal (%)")
    plt.ylabel("Pedal %")
    plt.legend()

    plt.subplot(4, 1, 2)
    plt.plot(t, speed, label="Vehicle speed (km/h)")
    plt.ylabel("km/h")
    plt.legend()

    plt.subplot(4, 1, 3)
    plt.plot(t, pressure, label="Brake pressure (bar)")
    plt.ylabel("bar")
    plt.legend()

    plt.subplot(4, 1, 4)
    plt.plot(t, wheel0, label="Wheel0 speed (km/h)")
    plt.ylabel("km/h")
    plt.xlabel("time (s)")
    plt.legend()

    plt.suptitle(title)
    plt.tight_layout(rect=[0, 0, 1, 0.97])
    plt.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Plot dummy HIL signals from JSON or simulate on-the-fly")
    parser.add_argument("--json", type=str, help="Path to dummy HIL JSON file", default=None)
    parser.add_argument("--duration", type=float, help="Duration in seconds for on-the-fly sim", default=10.0)
    parser.add_argument("--hz", type=float, help="Sample rate for on-the-fly sim", default=50.0)
    parser.add_argument("--seed", type=int, help="Seed for deterministic sim", default=None)
    args = parser.parse_args()

    if args.json and os.path.exists(args.json):
        data = load_json(args.json)
    else:
        data = simulate_time_series(duration_s=args.duration, sample_hz=args.hz, seed=args.seed)

    plot_data(data, title=f"Dummy HIL Signals ({len(data['data'])} samples)")
