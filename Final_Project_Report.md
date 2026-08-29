# Vehicle Brake System HIL Validation

## Final Year Project Report

### Department of Automotive / Embedded Systems
### Academic Year: 2026

---

## 1. Abstract
This project presents the design and implementation of a real-time Hardware-in-the-Loop (HIL) brake system simulation for evaluating braking performance, ECU response, fault-injection behavior, and ADAS-related lane-keep assist logic. The system models a brake pedal input, vehicle speed dynamics, brake pressure generation, and communication between the ECU and the vehicle network. The development is intended to reflect realistic automotive validation methodologies used in safety-critical systems and driver assistance engineering.

The central objective is to validate how the brake system responds under normal operating conditions and under fault states such as sensor offset, actuator stuck condition, pressure drop, and communication delay. The project also measures latency and evaluates whether a lane-keep assist function remains active or inactive based on vehicle operating conditions. The simulation is structured in a MATLAB/Simulink-inspired architecture to ensure compatibility with model-based design workflows used in automotive industries.

---

## 2. Introduction
Brake system performance is one of the most critical factors in vehicle safety. In modern automotive applications, brake-by-wire systems, electric brake actuators, and ADAS functions must respond accurately under variable conditions. Small delays or incorrect sensor states can have serious implications for safety and reliability. As a result, engineers increasingly rely on Hardware-in-the-Loop (HIL) testing and model-based validation to simulate real-world scenarios before deployment on road vehicles.

This project addresses the need for a compact and accessible HIL simulation framework capable of evaluating brake performance and ADAS-related faults. The system models key elements of vehicle braking, ECU logic, signal exchange through a CAN bus mock, and lane-keep assist logic. It is intended to demonstrate how control logic, fault scenarios, and latency effects can be studied in a safe and repeatable simulation environment.

---

## 3. Objectives
The main objectives of this project are:

1. To develop a real-time HIL simulation for a vehicle brake system.
2. To model the interaction between the brake pedal, ECU, and actuator response.
3. To evaluate braking performance under normal and fault conditions.
4. To analyze system latency and fault propagation.
5. To include a lane-keep assist prototype within the control architecture.
6. To structure the project in a MATLAB/Simulink-inspired model-based design format.

---

## 4. Literature Context and Motivation
ADAS and braking functions are closely linked because vehicle stability depends on the vehicle's ability to respond to driver inputs and environmental disturbances. Modern systems rely on accurate sensors, robust control logic, and rapid communication between control units. In real vehicle operation, faults such as wheel-speed sensor offset or communication delays can lead to degraded system performance.

A HIL environment enables the validation of such scenarios without requiring the full physical vehicle. It provides a realistic environment for testing ECU behavior under dynamic conditions and supports early validation of safety-critical functions. This project adopts this philosophy at a prototype level using a Python-based implementation to replicate the required control and analysis workflow.

---

## 5. System Architecture
The system is organized into a layered architecture inspired by MATLAB/Simulink block-based design.

### 5.1 Brake Pedal Input
This input layer simulates the driver’s brake demand based on pedal force. It provides the trigger signal that influences brake actuation and deceleration behavior.

### 5.2 Brake Plant and Vehicle Dynamics
The brake plant models the conversion of pedal force into brake pressure and resulting deceleration. Vehicle speed is reduced according to the simulated pressure response.

### 5.3 ECU Controller
The ECU supervises the braking decision and handles the logic associated with system response. It processes the input signals and identifies whether the system is operating within expected ranges.

### 5.4 Fault Injection Layer
The architecture includes a fault injection module that emulates:
- sensor offset,
- actuator stuck condition,
- brake pressure drop,
- communication delay.

These faults are relevant to ADAS-related validation because they can influence both driver assistance and vehicle safety functions.

### 5.5 Lane-Keep Assist Prototype
A lightweight LKA logic block evaluates whether lane support remains active given speed and steering conditions. This demonstrates how assistance functions can be integrated into a real-time braking framework.

### 5.6 CAN Bus Mock
The communication layer simulates ECU message exchange using a simplified CAN bus structure. This reflects how vehicle control messages are transmitted between embedded modules and monitoring systems.

### 5.7 Monitoring Layer
The monitoring layer captures output metrics such as:
- brake pressure,
- vehicle speed,
- system latency,
- LKA status,
- active fault condition.

---

## 6. Fault Scenarios Considered
The project evaluates the following fault cases:

### 6.1 Sensor Offset
This scenario represents wheel-speed sensor miscalibration or measurement drift. It can cause inaccurate speed estimation and lead to erroneous control decisions.

### 6.2 Actuator Stuck
This simulates a brake actuator that is partially or fully stuck, reducing the expected system response.

### 6.3 Brake Pressure Drop
This scenario models hydraulic or pneumatic pressure loss, which significantly affects braking force and stopping performance.

### 6.4 Communication Delay
This delay reflects possible time lag in ECU communication or CAN bus message propagation and directly impacts system responsiveness.

---

## 7. Methodology
The project follows a model-based simulation workflow:

1. Define a brake pedal input model.
2. Estimate braking force and pressure response.
3. Evaluate resulting vehicle speed reduction.
4. Simulate ECU processing latency.
5. Inject faults based on selected test cases.
6. Monitor output metrics and system behavior.
7. Assess whether the lane-keep assist remains active.
8. Compare results across varying fault conditions.

This approach is consistent with how modern automotive institutions validate control functions before full vehicle integration.

---

## 8. Results and Discussion
The simulation produced expected trends across all scenarios. Under higher brake pedal force, brake pressure increased, reducing vehicle speed more significantly. Fault cases caused variation in system responsiveness and latency, demonstrating the importance of fault-aware control logic.

The LKA logic remained active under suitable speed and steering conditions, while fault-induced degradation reduced system confidence. This confirms the relevance of the architecture for ADAS validation and safety assessment.

The results show that even a compact HIL prototype can provide valuable insight into system behavior, timing constraints, and failure effects before deeper integration with hardware or a full vehicle platform.

---

## 9. Applications
This project is applicable in multiple engineering contexts:

- brake-by-wire and brake control research,
- ADAS validation concept development,
- ECU testing and signal analysis,
- safety-critical functional monitoring,
- embedded systems and automotive communication training,
- portfolio and academic project demonstration.

---

## 10. Future Work
Future improvements may include:

- real CAN database and message definition implementation,
- improved hydraulic system modeling,
- more realistic vehicle dynamics and longitudinal control,
- integration with hardware pedals and data acquisition devices,
- a richer graphical dashboard with time-series plotting,
- extended ADAS features including emergency braking and stability assist.

---

## 11. Conclusion
The Vehicle Brake System HIL Validation project demonstrates how a real-time brake system simulation can be designed to evaluate safety-critical control scenarios, ADAS integration, and fault injection behavior. The methodology is aligned with modern automotive validation practices and offers a practical framework for developing and testing brake-related logic in a safe, repeatable simulation environment.

This work serves as a strong foundation for further expansion into more advanced HIL systems, full ECU integration, and real vehicle-level validation workflows.

---

## 12. References
- Automotive braking and vehicle dynamics principles
- ADAS validation methodologies and fault simulation practices
- MATLAB/Simulink model-based design workflow
- CAN communication concepts in embedded automotive systems

---

## 13. Appendices
- Simulation screenshots and output logs
- Fault scenario summary table
- Dashboard interpretation notes
- MATLAB/Simulink-inspired architecture overview
