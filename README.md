# SMT Automation & Digital Twin - Capstone Project

## Overview
This repository contains engineering documentation, control logic, CAD models, and simulation files for an automated **SMT (Surface Mount Technology) assembly line**, integrated with an **Autonomous Mobile Robot (AMR)** and **Collaborative Robot (Cobot)** material handling cell, paired with a complete **Digital / Visual Twin Simulation**.

---

## Workspace Structure

```
capstone project/
├── digital_twin/            # Digital / visual twin simulation assets
│   ├── models/              # Simplified bounding-box shells & OEM robot CAD
│   └── simulation/          # RobotStudio / Visual Components / Isaac Sim files
│
├── smt_line/                # Physical SMT machine configs & protocols
│   ├── machine_profiles/    # Dimension sheets, feeder setups, thermal profiles
│   └── smema_wiring/        # Inter-machine SMEMA handshake & wiring schematics
│
├── robotics/                # AMR & Cobot integration
│   ├── abb_gofa/            # ABB GoFa CRB 15000 RAPID code & OmniCore configs
│   └── next_amr/            # NEXT CMR1000 AMR SLAM maps, waypoints, RCS scripts
│
├── plc/                     # Mitsubishi GX Works3 ladder logic & I/O mapping
│   ├── gxworks3_project/    # GX Works3 workspace / project files (.gx3 / .gxw)
│   ├── io_mapping/          # I/O assignment sheets, memory registers, sensors
│   └── backups/             # Dated logic backups and snapshots
│
├── cad/                     # Autodesk Fusion 360 models & mechanical drawings
│   ├── exports/             # Exported STEP, IGES, STL, DXF files
│   └── archive/             # Old revisions & initial mechanism concepts
│
├── docs/                    # Master documentation & action items
│   ├── immediate_tasks/     # High-priority task lists & lab checklists
│   ├── equipment_inventory.md # Full machine breakdown & serial/model specifications
│   ├── manuals_reference.md   # Manual document IDs, vendor portals, retrieval guides
│   ├── production_line_architecture.md # Layout flowchart & network architecture
│   └── todo_list.md         # 4-Phase master implementation roadmap
│
├── specs/                   # Mechanical/electrical specifications & calculation tools
└── assets/                  # Machine photographs, lab layout imagery, references
```

---

## Machine Inventory

| Step | Machine | Model | Manufacturer |
| :--- | :--- | :--- | :--- |
| **01** | Automatic PCB Loader | `ZB2535SBJ` | Zhejiang Huaqi Zhengbang |
| **02** | Solder Paste Printer | `ZB-4535LYS` | Zhejiang Huaqi Zhengbang |
| **03** | SMT Chip Mounter (8-Head) | `WS-8Y` | Zhejiang Huaqi Zhengbang |
| **04** | Hot-Air Reflow Oven | `ZBRF-835` | Zhejiang Huaqi Zhengbang |
| **05** | Online 2D AOI Inspection | `ZB-800A` | Zhejiang Huaqi Zhengbang |
| **06** | Dispensing / Assembly Robot | DRS Series SCARA | Delta Electronics |
| **07** | Automatic PCB Unloader | `ZB2535XBJ` | Zhejiang Huaqi Zhengbang |
| **08** | Collaborative Robot | GoFa™ CRB 15000 | ABB Robotics |
| **09** | Heavy-Duty AMR | CMR1000 / SMR1000 | NEXT Robotics |

---

## Quick Links
- [Immediate Lab Action Plan](file:///c:/capstone%20project/docs/immediate_tasks/immediate_tasks.md)
- [Equipment Inventory & Specs](file:///c:/capstone%20project/docs/equipment_inventory.md)
- [Machine Manuals Reference](file:///c:/capstone%20project/docs/manuals_reference.md)
- [System Architecture](file:///c:/capstone%20project/docs/production_line_architecture.md)
