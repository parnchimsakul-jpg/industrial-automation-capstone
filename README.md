# Automated Box Folding System - Capstone Project

## Overview
This project focuses on the design, simulation, and implementation of an automated box folding system (tailored for PCB packaging) using **Autodesk Fusion** for mechanical CAD/assembly and **Mitsubishi GX Works3** for PLC ladder logic programming.

---

## Workspace Structure

```
capstone project/
├── cad/                     # Mechanical design & CAD files (Fusion 360)
│   ├── exports/             # Exported STEP, IGES, STL, DXF, or drawings
│   └── archive/             # Old revisions and design iterations
├── plc/                     # Control system & automation logic
│   ├── gxworks3_project/    # GX Works3 workspace / project files (.gx3 / .gxw)
│   ├── io_mapping/          # I/O assignment sheets, memory registers, sensors/actuators
│   └── backups/             # Dated logic backups and snapshots
├── specs/                   # Box dimensions, tolerances, PCB constraints, actuator specs
├── docs/                    # Documentation, presentations, and reports
│   ├── slides/              # Slide presentations and design reviews
│   └── notes/               # Meeting notes, troubleshooting, and logs
└── assets/                  # Photos, diagrams, and video demos
```

---

## Technology Stack
- **CAD**: Autodesk Fusion (Fusion 360)
- **PLC Programming**: Mitsubishi GX Works3 (Ladder Logic / Function Block Diagram)
- **Hardware Targets**: Mitsubishi iQ-F / iQ-R series PLC (or FX series), pneumatic actuators / servo drives, sensors (proximity, photoelectric).

---

## Key References & Files
- [Initial Slide / Problem Statement](file:///c:/capstone%20project/Why%20we%20couldn't%20fold%20box%20that%20fits%20the%20pcb.pdf)
- [I/O Mapping Template](file:///c:/capstone%20project/plc/io_mapping/io_mapping.md)
- [Box & PCB Specifications](file:///c:/capstone%20project/specs/box_pcb_specs.md)
