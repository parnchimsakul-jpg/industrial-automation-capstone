# Digital Twin & 3D Simulation Guide

## Overview
This directory stores 3D CAD models, line layouts, and simulation project files for the visual twin of the SMT & Robotic Packaging facility.

## Structure
- `models/`: 
  - Simplified envelope / bounding-box CAD models (`.step`, `.stl`, `.f3d`) for Huaqi Zhengbang SMT machines.
  - Official ABB GoFa CRB 15000 CAD (exported directly from ABB RobotStudio).
  - Parametric chassis model of the NEXT CMR1000 AMR.
- `simulation/`: 
  - Station layouts, kinematics definitions, ABB RobotStudio station files (`.rsst`), or Visual Components / Isaac Sim assets.

## Simulation Targets
1. **Kinematic Reachability**: Ensure ABB GoFa arm can reach magazine racks on the AMR and the unloader exit chute.
2. **Line Cycle Time & Throughput**: Model the bottleneck station (typically Pick & Place `WS-8Y` or Reflow Oven `ZBRF-835`).
3. **AMR Fleet Dispatch**: Simulate AMR transit times between SMT unload and box packaging stations.
