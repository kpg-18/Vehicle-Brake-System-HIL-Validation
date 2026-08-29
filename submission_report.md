# Real-Time Vehicle Brake System Simulation using HIL

## Executive Summary
This project presents a compact Hardware-in-the-Loop (HIL) brake system simulation designed to emulate real-world brake-by-wire behavior for ADAS-relevant validation. It models the interaction between the brake pedal, vehicle dynamics, ECU logic, sensor feedback, lane-keep assist logic, and fault-injection scenarios.

## Objectives
- Develop a real-time brake system simulation that reflects hardware-in-the-loop validation flows.
- Integrate a physical brake pedal model and ECU logic to monitor live response.
- Evaluate braking performance, latency, and response reliability during fault-injection tests.
- Validate lane-keep assist behavior under realistic operating conditions.
- Represent the structure in a MATLAB/Simulink-inspired architecture suitable for further expansion.

## System Architecture
The model follows a layered structure:
1. Brake pedal input layer
2. Brake plant and vehicle dynamics layer
3. Sensor acquisition and ECU supervision layer
4. Fault injection and diagnostic monitoring layer
5. Lane-keep assist and safety logic layer
6. CAN bus communication mock for signal exchange

## Fault Scenarios Evaluated
- Sensor offset
- Actuator stuck condition
- Brake pressure drop
- ECU communication delay

These scenarios are relevant to ADAS validation because they directly influence safety-critical braking decisions under real-world uncertainty.

## Results
The simulation confirms that changes in pedal force and fault conditions alter brake pressure, vehicle deceleration, and system latency. The lane-keep assist logic remains active when the vehicle speed is sufficient and the steering deviation stays within safe thresholds, reflecting a plausible prototype ADAS function.

## Engineering Relevance
This project aligns with functional validation approaches used for ADAS and safety-related automotive systems. It demonstrates how HIL principles can be applied to test control response, identify latency impacts, and assess reliability under induced fault conditions without requiring a full physical vehicle test bench.

## Future Extension
The prototype can be expanded with:
- a genuine CAN database and ECU message definitions,
- a Simulink block diagram equivalent,
- a graphical HMI dashboard,
- hardware-in-the-loop I/O interfacing with real pedals or DAQ devices,
- more realistic brake hydraulics and controller logic.

## Conclusion
This simulation is a practical demonstration of a real-time brake system HIL platform for automotive safety validation, fault analysis, and ADAS function prototyping.
