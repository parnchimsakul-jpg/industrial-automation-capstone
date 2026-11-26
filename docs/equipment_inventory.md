# SMT & Robotic Assembly Production Line Equipment Specification

## 1. Overview
This facility is an automated SMT (Surface Mount Technology) and PCB manufacturing / packaging cell integrated with autonomous material handling (AMR) and collaborative robotic handling (Cobot).

---

## 2. Equipment Inventory & Identification

### Station 1: PCB Loading
- **Machine**: Automatic PCB Magazine Loader
- **Model**: **ZB2535SBJ** (Zhejiang Huaqi Zhengbang Automation Technology Co., Ltd.)
- **Function**: Automatically pushes bare PCBs from standard magazine racks onto the production conveyor track.
- **Interfaces**: SMEMA standard interface (upstream/downstream handshaking), digital input/output, touch screen HMI.

---

### Station 2: Solder Paste Printing
- **Machine**: Fully Automatic Solder Paste Stencil Printer
- **Model**: **ZB-4535LYS** (Zhejiang Huaqi Zhengbang)
- **Function**: Stencil alignment and squeegee application of solder paste onto bare PCB pads using optical vision positioning.
- **Interfaces**: SMEMA input/output, internal industrial PC / monitor, pneumatic squeegee pressure regulators.

---

### Station 3: Inspection / Buffer Conveyors
- **Machine**: Intermediate PCB Link Conveyors (Inspection / Cooling / Transit)
- **Model**: Standard SMT Rail Conveyors with width adjustment handwheels and photoelectric stop sensors.
- **Function**: Transport boards between stations; manual inspection / buffer stations.

---

### Station 4: Component Pick and Place (Chip Mounter)
- **Machine**: 8-Head Automatic SMT Pick and Place Machine
- **Model**: **WS-8Y** (Zhejiang Huaqi Zhengbang)
- **Function**: High-speed placement of SMD chips, ICs, and discrete components using multi-nozzle flying vision cameras and tape/reel feeder banks.
- **Interfaces**: Integrated control PC (monitor, keyboard, trackball), emergency stop loop, SMEMA conveyor link.

---

### Station 5: Reflow Soldering
- **Machine**: Multi-Zone Lead-Free Hot Air Reflow Oven
- **Model**: **ZBRF-835** (Zhejiang Huaqi Zhengbang)
- **Function**: Controlled thermal profile heating and cooling to melt solder paste and establish mechanical/electrical joints.
- **Key Features**: Multi-temperature zones, mesh belt + chain rail dual conveyor, exhaust duct connections.

---

### Station 6: Automated Optical Inspection (AOI)
- **Machine**: Online 2D Automated Optical Inspection System
- **Model**: **ZB-800A** (Zhejiang Huaqi Zhengbang)
- **Function**: High-resolution camera inspection for missing components, misalignment, solder bridging, tombstoning, and polarity errors post-reflow.
- **Interfaces**: Dual-display / high-res inspection monitor, statistical process control (SPC) software, SMEMA pass/fail routing.

---

### Station 7: Secondary Assembly / Dispensing Cell
- **Machine**: Selective Robotic Dispensing / Assembly Unit
- **Robot Arm**: **Delta DRS Series SCARA Robot** (DRS40L / DRS60L) or Delta 4-Axis Arm
- **Function**: Dispenses adhesives, conformal coating, underfill, or performs high-speed component insertion / screwdriving before offloading.
- **Controller**: Delta ASDA-MS / DCS series controller programmed via DRAStudio.

---

### Station 8: PCB Unloading
- **Machine**: Automatic PCB Magazine Unloader
- **Model**: **ZB2535XBJ** (Zhejiang Huaqi Zhengbang)
- **Function**: Receives completed boards from the line and stacks them safely into anti-static magazine racks.
- **Interfaces**: SMEMA interface, rack elevator stepper/servo mechanism.

---

### Station 9: Mobile Robotics & Intralogistics
1. **Cobot Mobile Manipulator**:
   - **Robot Arm**: **ABB GoFa™ CRB 15000** (6-axis collaborative robot, payload 5kg / 10kg / 12kg)
   - **Controller**: ABB OmniCore C30
   - **Tooling**: SICK safety scanner / optical sensors, vacuum gripper / mechanical gripper.
2. **Autonomous Mobile Robot (AMR) Base**:
   - **Model**: **NEXT CMR1000 / SMR1000** (Heavy-duty 1,000 kg payload platform)
   - **Navigation**: Dual LiDAR SLAM navigation, optical depth cameras, safety bumpers.
   - **Function**: Docking between production lines, magazine rack transport, finished PCB batch transfer, and box loading interaction.
