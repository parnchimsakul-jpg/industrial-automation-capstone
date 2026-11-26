# Robotics Integration: ABB GoFa & NEXT CMR1000 AMR

## 1. ABB GoFa Collaborative Robot (CRB 15000)
- **Controller**: OmniCore C30
- **Programming Language**: RAPID / Wizard Easy Programming
- **Key Manuals**:
  - Product Specification: `3HAC077390-001`
  - Product Manual: `3HAC077389-001`
- **Simulation**: Download ABB RobotStudio to obtain exact 3D models and program virtual controller stations.

## 2. NEXT CMR1000 / SMR1000 Heavy-Duty AMR
- **Payload Capacity**: 1,000 kg
- **Navigation**: Dual LiDAR SLAM + Optical 3D depth cameras
- **Interfaces**: Fleet Management (RCS), Modbus TCP, ROS2 / REST API over Wi-Fi
- **Tasks**:
  - SLAM environment mapping
  - Precision docking at SMT Unloader station
  - Transporting completed PCB magazines to the box packing station
