# Capstone Project Master Plan & To-Do List

## Project Goal
Integrate an end-to-end automated manufacturing and packaging line:
1. SMT assembly of PCBs.
2. In-line dispensing, inspection, and unloading into magazines.
3. Intralogistics transport via NEXT CMR1000 AMR with ABB GoFa Cobot.
4. Final packaging into boxes (connecting to the Automated Box Folding System).
5. Build a high-fidelity **Digital Twin / Visual Twin Simulation** of the entire cell.

---

## Task Breakdown & Checklist

### Phase 1: Machine Physical Setup & Documentation Recovery
- [ ] **Collect Machine Backups**:
  - Connect a flash drive to the industrial PCs of the SMT machines (`WS-8Y`, `ZB-800A`, `ZB-4535LYS`, `ZBRF-835`).
  - Copy all user manuals, calibration profiles, and software installers located on their `C:\` or `D:\` drives.
- [ ] **Facility & Utility Check**:
  - Verify electrical supply (220V 1-phase vs 380V 3-phase for the `ZBRF-835` reflow oven).
  - Verify clean dry compressed air supply (CDA, ~0.5 to 0.7 MPa) for the pick-and-place nozzles, pneumatic cylinders, and loader/unloader.
  - Verify exhaust ventilation for the reflow oven soldering fumes.
- [ ] **SMEMA Cable Interconnect**:
  - Wire standard SMEMA cables (4-pin or 14-pin connectors) between consecutive conveyors and machines (`Loader -> Printer -> WS-8Y -> Oven -> AOI -> Dispenser -> Unloader`).
  - Test the handshake logic (Board Available $\leftrightarrow$ Machine Ready).

---

### Phase 2: Robotics & Intralogistics (ABB GoFa + NEXT AMR)
- [ ] **ABB GoFa CRB 15000 Setup**:
  - Power on OmniCore C30 controller and test FlexPendant.
  - Setup tool center point (TCP) for the end-effector gripper.
  - Configure SafeMove zones around the mobile platform boundaries.
- [ ] **NEXT CMR1000 / SMR1000 AMR Setup**:
  - Drive AMR via manual pendant/app to generate 2D/3D LiDAR SLAM map of the lab/workshop.
  - Set up navigation waypoints:
    - *Waypoint A*: PCB Unloader station (`ZB2535XBJ`).
    - *Waypoint B*: Box folding & packing station.
    - *Waypoint C*: Automated charging dock.
- [ ] **Handshake & Communication**:
  - Establish wireless communication (Modbus TCP, MQTT, or ROS2) between the PLC / central controller and the AMR + GoFa arm.

---

### Phase 3: Digital Twin & Visual Simulation (No OEM CAD Workaround)
Since OEM CAD models are not provided by the manufacturer, follow this visual twin strategy:
- [ ] **3D Scanning / Reverse Modeling**:
  - Measure external envelope dimensions (length, width, height, track height) of each machine.
  - Download official ABB CAD model for the GoFa CRB 15000 from the ABB RobotStudio library (ABB provides exact, free CAD models of all their arms).
  - Model simple block/bounding-box exterior shells in Fusion 360 for the Zhengbang machines using the reference photos in `assets/picture of the machine/`.
- [ ] **Choose Digital Twin Platform**:
  - *Option A (Recommended for Robotics & PLC)*: **ABB RobotStudio** with PowerPac / Smart Components (ideal for the GoFa arm, kinematics, and virtual PLC signal link via OPC UA).
  - *Option B (Recommended for Full Production Line Logistics)*: **Visual Components** or **Siemens Tecnomatix Process Simulate / Plant Simulation**.
  - *Option C (Open Source / Academic)*: **NVIDIA Isaac Sim (Omniverse)** or **Gazebo (ROS2)** for AMR navigation and cobot manipulation.
- [ ] **Link Simulation to Logic**:
  - Connect GX Works3 (or Siemens/Codesys virtual PLC) to the digital twin using OPC UA or Modbus TCP.
  - Test line pacing, cycle times, bottleneck analysis, and material flow.

---

### Phase 4: Integration with the Box Folding System
- [ ] Link the finished PCB transfer process to the Automated Box Folding station.
- [ ] Program the ABB GoFa cobot to pick packed PCBs and insert them into the folded carton.
