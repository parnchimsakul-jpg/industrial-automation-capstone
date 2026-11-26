"""
Conveyor Motor Sizing & Dynamics Calculator
Automated Box Folding System - Capstone Project
"""

import math

def calculate_conveyor_motor(
    sprocket_teeth=19,
    chain_pitch_mm=12.7,       # #40 chain (0.5 inch = 12.7 mm)
    linear_speed_m_s=0.15,      # 150 mm/s
    total_moving_mass_kg=8.0,   # chain + aluminum paddles + boxes + payload
    accel_time_s=0.2,           # acceleration time to full speed
    friction_coeff=0.25,        # sliding friction (chain on wear strip / guide)
    safety_factor=2.0,          # safety margin for starts/stops & misalignment
    gearbox_ratio=1.0,          # gear ratio if using a geared motor (e.g. 10:1 or 20:1)
    gearbox_efficiency=0.85     # typical planetary / spur gear efficiency
):
    # 1. Sprocket Geometry
    pitch_m = chain_pitch_mm / 1000.0
    pitch_diameter_m = pitch_m / math.sin(math.pi / sprocket_teeth)
    sprocket_radius_m = pitch_diameter_m / 2.0
    
    # 2. Kinematics
    omega_shaft = linear_speed_m_s / sprocket_radius_m # rad/s
    shaft_rpm = (omega_shaft * 60.0) / (2.0 * math.pi)
    motor_rpm = shaft_rpm * gearbox_ratio
    
    # 3. Dynamic Forces & Torques
    # Friction load
    f_friction = total_moving_mass_kg * 9.81 * friction_coeff
    t_friction_shaft = f_friction * sprocket_radius_m
    
    # Linear acceleration load
    acceleration = linear_speed_m_s / accel_time_s
    f_accel = total_moving_mass_kg * acceleration
    t_accel_shaft = f_accel * sprocket_radius_m
    
    # Rotational inertia of sprockets (estimated 4 sprockets @ 0.25 kg each)
    j_sprockets = 4 * (0.5 * 0.25 * (sprocket_radius_m ** 2))
    alpha_shaft = acceleration / sprocket_radius_m
    t_rot_accel_shaft = j_sprockets * alpha_shaft
    
    # Total Shaft Torque
    t_peak_shaft = t_friction_shaft + t_accel_shaft + t_rot_accel_shaft
    t_design_shaft = t_peak_shaft * safety_factor
    
    # Motor Torque (reflected through gearbox)
    t_motor_design = t_design_shaft / (gearbox_ratio * gearbox_efficiency)
    p_mechanical_watts = t_friction_shaft * omega_shaft
    p_motor_rating_watts = (t_motor_design * (motor_rpm * 2 * math.pi / 60))
    
    return {
        "sprocket_pitch_dia_mm": pitch_diameter_m * 1000.0,
        "shaft_rpm": shaft_rpm,
        "motor_rpm": motor_rpm,
        "t_friction_shaft_Nm": t_friction_shaft,
        "t_accel_shaft_Nm": t_accel_shaft,
        "t_peak_shaft_Nm": t_peak_shaft,
        "t_design_shaft_Nm": t_design_shaft,
        "t_motor_design_Nm": t_motor_design,
        "p_mechanical_watts": p_mechanical_watts,
        "p_motor_rating_watts": p_motor_rating_watts
    }

if __name__ == "__main__":
    print("=" * 60)
    print("CONVEYOR MOTOR SIZING REPORT (DIRECT DRIVE vs 10:1 GEARMOTOR)")
    print("=" * 60)
    
    direct = calculate_conveyor_motor(gearbox_ratio=1.0)
    geared = calculate_conveyor_motor(gearbox_ratio=10.0)
    
    print(f"Sprocket Pitch Diameter: {direct['sprocket_pitch_dia_mm']:.1f} mm")
    print(f"Conveyor Shaft Speed   : {direct['shaft_rpm']:.1f} RPM")
    print(f"Peak Shaft Torque      : {direct['t_peak_shaft_Nm']:.2f} N.m")
    print(f"Design Shaft Torque (2x Safety Factor): {direct['t_design_shaft_Nm']:.2f} N.m")
    print("-" * 60)
    print("Case 1: Direct Drive Stepper / BLDC (1:1 ratio)")
    print(f"  Motor RPM: {direct['motor_rpm']:.1f} RPM | Motor Holding Torque Needed: {direct['t_motor_design_Nm']:.2f} N.m ({direct['t_motor_design_Nm']*100:.0f} N.cm)")
    print("-" * 60)
    print("Case 2: Geared Stepper / Gearmotor (10:1 ratio)")
    print(f"  Motor RPM: {geared['motor_rpm']:.1f} RPM | Motor Holding Torque Needed: {geared['t_motor_design_Nm']:.2f} N.m ({geared['t_motor_design_Nm']*100:.0f} N.cm)")
    print("=" * 60)
