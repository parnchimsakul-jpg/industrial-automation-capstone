# SMT Line & Digital Twin: Immediate Action Plan

## Priority 1: In-Lab Physical Data Gathering (First 48 Hours)

### Task 1.1: Measure External Envelope Dimensions (For Visual Twin Bounding Boxes)
*Because the vendor did not supply 3D CAD files, we model simplified external shells in Fusion 360 using bounding-box dimensions:*
- [ ] Measure **Track Centerline Height** (from floor to PCB rail top, standard is ~900 mm $\pm 20$ mm).
- [ ] Record outer dimensions ($L \times W \times H$) for:
  - `ZB2535SBJ` Automatic Loader
  - `ZB-4535LYS` Automatic Solder Paste Printer
  - Link Conveyor 1 (Printer $\rightarrow$ WS-8Y)
  - `WS-8Y` 8-Head SMT Pick & Place Machine
  - Link Conveyor 2 (WS-8Y $\rightarrow$ Reflow Oven)
  - `ZBRF-835` Multi-Zone Reflow Oven
  - Link Conveyor 3 (Reflow Oven $\rightarrow$ AOI)
  - `ZB-800A` 2D AOI Inspection System
  - `Delta SCARA` Dispensing Station
  - `ZB2535XBJ` Automatic Unloader
- [ ] Record overall line total length and footprint layout on the lab floor.

### Task 1.2: Retrieve Internal Machine Manuals & Software
- [ ] Plug a FAT32/NTFS USB flash drive into the industrial PCs on:
  - `WS-8Y` Chip Mounter
  - `ZB-800A` AOI Machine
  - `ZB-4535LYS` Solder Paste Printer
- [ ] Copy the entire `Documentation`, `Manuals`, `Backup`, or `Drivers` folders off their local `C:\` or `D:\` drives into `smt_line/machine_profiles/`.

### Task 1.3: Facility Power & Pneumatics Verification
- [ ] Check main supply lines against machine nameplates:
  - `ZBRF-835` Reflow Oven: Check if 3-phase 380V or single-phase 220V is wired; verify rated kW.
  - Compressed Dry Air (CDA): Ensure regulator delivers stable 0.5–0.7 MPa to `WS-8Y` and `ZB2535SBJ`.
  - Check exhaust ducting for reflow oven fumes.

---

## Priority 2: SMEMA Signal & Interlock Verification

- [ ] Inspect the standard 14-pin or 4-pin SMEMA ports on adjacent machines.
- [ ] Document pin assignments in [`smt_line/smema_wiring/`](file:///c:/capstone%20project/smt_line/smema_wiring/):
  - Upstream Board Available contact
  - Downstream Machine Ready contact
- [ ] Ensure all emergency stop (E-stop) chains are properly closed.

---

## Priority 3: Mobile Robotics & Cobot Setup

### ABB GoFa CRB 15000:
- [ ] Power up the OmniCore C30 controller; verify FlexPendant boots with no critical safety faults.
- [ ] Install **ABB RobotStudio** on your workstation.
- [ ] Import the official OEM 3D CAD model of GoFa CRB 15000 from the RobotStudio built-in library into [`digital_twin/models/`](file:///c:/capstone%20project/digital_twin/models/).

### NEXT CMR1000 / SMR1000 AMR:
- [ ] Connect to the AMR's onboard Wi-Fi / Web UI or handheld pendant.
- [ ] Perform an initial manual drive around the lab room to generate the 2D LiDAR SLAM floor map.
- [ ] Mark off no-go zones, charging station dock, and docking waypoints at the `ZB2535XBJ` unloader.

---

## Priority 4: Digital / Visual Twin Construction

- [ ] In Fusion 360, create a single master assembly: `ASM_SMT_Production_Line.step` based on the envelope dimensions recorded in Task 1.1.
- [ ] Assemble the line in order: Loader $\rightarrow$ Printer $\rightarrow$ Pick & Place $\rightarrow$ Oven $\rightarrow$ AOI $\rightarrow$ Dispenser $\rightarrow$ Unloader.
- [ ] Import the master layout into your chosen simulation environment (**ABB RobotStudio** / **Visual Components** / **Isaac Sim**) for kinematic animation and cycle time analysis.
