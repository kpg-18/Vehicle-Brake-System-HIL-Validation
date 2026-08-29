from __future__ import annotations

import math
import tkinter as tk
from tkinter import ttk

from brake_hil import BrakeHILSystem, FaultScenario


class BrakeDashboard:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Brake HIL Dashboard")
        self.root.geometry("760x520")

        self.system = BrakeHILSystem(initial_speed_kph=120.0, brake_pedal_force=45.0)

        self.speed_var = tk.StringVar(value="120.00 km/h")
        self.pressure_var = tk.StringVar(value="13.50 bar")
        self.latency_var = tk.StringVar(value="18.00 ms")
        self.lka_var = tk.StringVar(value="active")
        self.fault_var = tk.StringVar(value="none")

        title = ttk.Label(root, text="Real-Time Vehicle Brake System Simulation", font=("Segoe UI", 16, "bold"))
        title.pack(pady=(16, 8))

        controls = ttk.Frame(root, padding=12)
        controls.pack(fill="x")

        ttk.Label(controls, text="Brake pedal force: ").grid(row=0, column=0, sticky="w", padx=4, pady=4)
        self.force_scale = ttk.Scale(controls, from_=0, to_=100, orient="horizontal", command=self._update_from_slider)
        self.force_scale.set(45)
        self.force_scale.grid(row=0, column=1, sticky="ew", padx=4, pady=4)

        ttk.Label(controls, text="Fault scenario: ").grid(row=1, column=0, sticky="w", padx=4, pady=4)
        self.fault_combo = ttk.Combobox(
            controls,
            values=["none", FaultScenario.SENSOR_OFFSET.value, FaultScenario.ACTUATOR_STUCK.value, FaultScenario.BRAKE_PRESSURE_DROP.value, FaultScenario.COMMUNICATION_DELAY.value],
            state="readonly",
        )
        self.fault_combo.set("none")
        self.fault_combo.grid(row=1, column=1, sticky="ew", padx=4, pady=4)

        self._update_from_slider(45)

        metrics = ttk.Frame(root, padding=12)
        metrics.pack(fill="x")

        ttk.Label(metrics, text="Vehicle speed", font=("Segoe UI", 12, "bold")).grid(row=0, column=0, sticky="w")
        ttk.Label(metrics, textvariable=self.speed_var, font=("Segoe UI", 11)).grid(row=0, column=1, sticky="w", padx=10)
        ttk.Label(metrics, text="Brake pressure", font=("Segoe UI", 12, "bold")).grid(row=1, column=0, sticky="w")
        ttk.Label(metrics, textvariable=self.pressure_var, font=("Segoe UI", 11)).grid(row=1, column=1, sticky="w", padx=10)
        ttk.Label(metrics, text="System latency", font=("Segoe UI", 12, "bold")).grid(row=2, column=0, sticky="w")
        ttk.Label(metrics, textvariable=self.latency_var, font=("Segoe UI", 11)).grid(row=2, column=1, sticky="w", padx=10)
        ttk.Label(metrics, text="LKA state", font=("Segoe UI", 12, "bold")).grid(row=3, column=0, sticky="w")
        ttk.Label(metrics, textvariable=self.lka_var, font=("Segoe UI", 11)).grid(row=3, column=1, sticky="w", padx=10)
        ttk.Label(metrics, text="Fault", font=("Segoe UI", 12, "bold")).grid(row=4, column=0, sticky="w")
        ttk.Label(metrics, textvariable=self.fault_var, font=("Segoe UI", 11)).grid(row=4, column=1, sticky="w", padx=10)

    def _update_from_slider(self, value: str) -> None:
        try:
            force = float(value)
        except ValueError:
            return

        selected_fault = self.fault_combo.get()
        fault = None if selected_fault == "none" else FaultScenario(selected_fault)
        self.system = BrakeHILSystem(initial_speed_kph=120.0, brake_pedal_force=force, fault=fault)
        result = self.system.run_cycle(duration_s=1.5)

        self.speed_var.set(f"{result.vehicle_speed_kph:.2f} km/h")
        self.pressure_var.set(f"{result.brake_pressure_bar:.2f} bar")
        self.latency_var.set(f"{result.latency_ms:.2f} ms")
        self.lka_var.set(result.lka_status)
        self.fault_var.set(result.fault_name or "none")

    def run(self) -> None:
        self.root.mainloop()


def launch_dashboard() -> None:
    root = tk.Tk()
    app = BrakeDashboard(root)
    app.run()


if __name__ == "__main__":
    launch_dashboard()
