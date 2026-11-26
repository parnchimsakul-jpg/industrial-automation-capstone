# PLC I/O Mapping & Device List

## System Overview
- **PLC Model**: [e.g., Mitsubishi FX5U / iQ-F Series]
- **Programming Environment**: Mitsubishi GX Works3
- **Language**: Ladder Diagram (LD)

---

## Digital Inputs (X)

| Address | Signal Name | Device Type | Function / Description | State / Logic (NO/NC) |
|---------|-------------|-------------|------------------------|-----------------------|
| `X0`    | `PB_START`  | Push Button | System Start / Cycle Run | NO |
| `X1`    | `PB_STOP`   | Push Button | Normal Cycle Stop      | NC |
| `X2`    | `EMG_STOP`  | E-Stop      | Emergency Stop Circuit | NC |
| `X3`    | `SEN_BOX_IN`| Photoelectric | Cardboard blank detected | NO |
| `X4`    | `CYL1_EXT_LS`| Reed Switch| Cylinder 1 Extended Limit | NO |
| `X5`    | `CYL1_RET_LS`| Reed Switch| Cylinder 1 Retracted Limit | NO |
| `X6`    | `CYL2_EXT_LS`| Reed Switch| Cylinder 2 Extended Limit | NO |
| `X7`    | `CYL2_RET_LS`| Reed Switch| Cylinder 2 Retracted Limit | NO |

---

## Digital Outputs (Y)

| Address | Signal Name | Actuator Type | Function / Description |
|---------|-------------|---------------|------------------------|
| `Y0`    | `SOL_CYL1_EXT` | Solenoid Valve | Extend Flap Fold Cylinder 1 |
| `Y1`    | `SOL_CYL1_RET` | Solenoid Valve | Retract Flap Fold Cylinder 1 |
| `Y2`    | `SOL_CYL2_EXT` | Solenoid Valve | Extend Bottom Fold Cylinder 2 |
| `Y3`    | `SOL_CYL2_RET` | Solenoid Valve | Retract Bottom Fold Cylinder 2 |
| `Y10`   | `LAMP_RUN`     | Pilot Lamp    | System Running Indicator (Green) |
| `Y11`   | `LAMP_FAULT`   | Pilot Lamp    | Fault / E-Stop Active (Red) |

---

## Internal Relays / Markers (M)

| Address | Identifier | Purpose / State |
|---------|------------|-----------------|
| `M0`    | `SYS_RUN`  | Master Run Interlock |
| `M10`   | `SEQ_STEP_1` | Step 1: Feeding blank |
| `M11`   | `SEQ_STEP_2` | Step 2: Side fold sequence |
| `M12`   | `SEQ_STEP_3` | Step 3: End tuck / final fold |
