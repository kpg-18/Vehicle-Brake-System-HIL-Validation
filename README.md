# Vehicle Brake System HIL Validation

## Real-Time Brake Control, Safety Validation, and ADAS Fault Analysis

-------------------------------------------

### Automotive Embedded Systems | HIL Simulation | ECU Validation | ADAS Safety

-------------------------------------------

This project presents a real-time Hardware-in-the-Loop (HIL) brake system validation framework designed for automotive safety and ADAS-related development. It models the interaction between a physical brake pedal input, vehicle dynamics, ECU response, and fault-injection scenarios to evaluate braking performance under realistic operating conditions.

The simulation is suitable for concept validation, model-based design demonstration, and safety-critical system analysis in the context of automated driving and vehicle control engineering.

## Project Documentation

- [docs/title_page.md](docs/title_page.md) — formal title page
- [docs/executive_summary.md](docs/executive_summary.md) — one-page summary for submission
- [docs/architecture_diagram.md](docs/architecture_diagram.md) — MATLAB/Simulink-style block architecture
- [docs/portfolio_banner.md](docs/portfolio_banner.md) — polished banner for portfolio presentation

## Problem Statement
Modern brake systems must operate reliably under varying driver inputs, sensor conditions, and fault states. In safety-critical vehicle functions, even short latencies or incorrect sensor states can influence brake actuation and ADAS decision-making. This project addresses that need by developing a compact, Simulink-inspired HIL architecture that enables:

- brake pedal signal interpretation,
- ECU-level braking logic evaluation,
- sensor/actuator fault simulation,
- system latency measurement,
- lane-keep assist prototype behavior under braking conditions.

## Key Features
- Real-time brake pedal and ECU interaction model
- Live vehicle speed, brake pressure, and latency monitoring
- Fault injection for ADAS-relevant scenarios
- CAN bus communication mock for ECU signal exchange
- MATLAB/Simulink-inspired model structure for system traceability
- GUI dashboard for live monitoring and interaction
- Prototype lane-keep assist logic integrated into the validation loop

## System Scope
The framework includes the following functional elements:

1. Brake pedal input model
2. Brake plant and hydraulic response approximation
3. Wheel-speed and vehicle state estimation
4. ECU logic and supervisory control behavior
5. Fault injection layer for sensor offset, pressure degradation, actuator issues, and communication delay
6. Lane-keep assist coordination logic for vehicle stability support
7. Monitoring layer for safety validation metrics

## ADAS-Relevant Fault Scenarios
The project evaluates multiple fault modes that are relevant to functional safety and ADAS validation:

- Sensor offset / speed estimation error
- Actuator stuck condition
- Brake pressure drop
- Communication delay on the ECU network

These conditions are important because they can directly influence braking response, lane stability, and overall reliability in advanced vehicle systems.

## Simulation Methodology
The logic is structured to reflect a typical model-based development workflow:

- define brake input and system states,
- simulate actuation and vehicle response,
- estimate ECU processing delay,
- inject faults under controlled conditions,
- monitor system behavior against safety thresholds,
- assess LKA participation and overall vehicle stability.

This model was designed to be easy to extend and aligns with MATLAB/Simulink-based automotive development flows without requiring a full commercial simulation toolchain.

## Project Structure

- `src/` — core HIL models, ECU logic, dashboard, and CAN mock
- `tests/` — unit validation for simulation logic
- `submission_report.md` — engineering summary for portfolio/submission use
- `README.md` — project overview and usage guide

## Run the Simulation

```bash
python3 src/main.py
```

## Open the GUI Dashboard

```bash
python3 src/dashboard.py
```

## Review the MATLAB/Simulink-Style Architecture

The plant and controller hierarchy is represented in `src/simulink_like_model.py`, which organizes the system into blocks such as brake pedal input, brake plant, ECU controller, fault injection, LKA logic, CAN communication, and monitoring layers.

## Run the Tests

```bash
python3 -m pytest -q
```

## HIL Setup & Dummy Data

This repository does not include a physical HIL (Hardware-in-the-Loop) setup. For CI and local validation we provide a simple dummy-data generator that simulates common ADAS/brake fault scenarios. The script `src/dummy_hil.py` writes sample scenario data to `reports/dummy_hil_data.json`.

To generate dummy HIL data locally:

```bash
python3 src/dummy_hil.py
```

To run the test-suite and produce a self-contained HTML report (includes pass/fail, durations, and captured details) install the test-report plugin and run pytest with the `--html` option. A ready-to-use `requirements.txt` lists the plugin.

```bash
python3 -m pip install -r requirements.txt
PYTHONPATH=. python3 -m pytest --html=reports/test_report.html --self-contained-html
```

The generated HTML report will be at `reports/test_report.html` and the dummy HIL output (if generated) at `reports/dummy_hil_data.json`.

Generator options and example CLI flags
--------------------------------------

The dummy generator supports a few configurable options to better mimic different HIL run conditions:

- `--duration` : total simulation time in seconds (default: `10.0`)
- `--hz` : sample rate in Hz (default: `50.0`)
- `--seed` : optional integer seed for deterministic fault selection and noise
- `--out-json` : output JSON path (default: `reports/dummy_hil_data.json`)
- `--out-csv` : output CSV path (default: `reports/dummy_hil_data.csv`)

Example usage with custom options:

```bash
python3 src/dummy_hil.py --duration 20 --hz 100 --seed 42 --out-json reports/run1.json --out-csv reports/run1.csv
```

The generator will include a `meta` section describing the run (duration, sample rate, samples, chosen fault and injection time) and a `data` array of timestamped samples. Use the provided `scripts/plot_dummy_hil.py` to visualize these signals quickly.


## Example Output

```text
Real-Time Vehicle Brake System Simulation using HIL
ADAS fault scenario review:

Scenario: sensor_offset
  Pressure: 11.52 bar
  Latency: 19.80 ms
  Speed: 114.24 km/h
  LKA: active
```

## Engineering Relevance
This project demonstrates the core principles of real-time brake validation, including:

- brake system behavior under varying input conditions,
- ECU response monitoring,
- fault injection for safety analysis,
- latency characterization for time-critical vehicle functions,
- prototype ADAS logic integration for validation workflows.

## Professional Use Case
The project is suitable for:

- academic project submissions,
- automotive engineering portfolios,
- embedded systems and control demonstration work,
- safety validation concept presentations,
- model-based design discussion in driver assistance and braking systems.

## Notes
The implementation uses Python as a lightweight executable prototype for environments without access to MATLAB/Simulink. It can be extended into a more advanced HIL environment using a real brake pedal, DAQ interfaces, CAN transceivers, and production-grade ECU software.
