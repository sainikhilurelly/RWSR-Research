import numpy as np
import matplotlib.pyplot as plt

# --- Physical Parameters ---
g = 9.81              # Gravity (m/s^2)
m_body = 1.0          # Mass of the robot body (kg)
l_com = 0.15          # Distance to Center of Mass (m)
inertia_wheel = 0.01  # Moment of Inertia of the wheel (kg*m^2)
dt = 0.01             # Small sampling time for stability

# --- PID Gains (Your "Perfect Spot" Knobs) ---
# Start with these and tune as we discussed: 
# Increase Kp for strength, Kd to stop shaking, Ki for precision [cite: 14, 16, 26, 27, 29]
Kp = 10.0  
Ki = 0.1   
Kd = 1.0   

# --- Limits ---
MAX_TORQUE = 2.0      # Motor torque limit (Nm) [cite: 32]
MAX_RPM = 5000        # Motor speed saturation limit 

# --- Initial State ---
theta = 0.1           # Initial tilt angle (radians)
theta_dot = 0.0       # Initial angular velocity
wheel_speed_rpm = 0.0
error_sum = 0.0
last_error = 0.0

# Data storage for plotting
results = {'time': [], 'theta': [], 'rpm': []}

# --- Simulation Loop ---
time_range = np.arange(0, 10, dt)
for t in time_range:
    # 1. Calculate Error (Target is 0 degrees) [cite: 31]
    error = 0 - theta
    error_sum += error * dt
    error_rate = (error - last_error) / dt
    
    # 2. PID Control Output (Torque) [cite: 26, 28, 29]
    torque = (Kp * error) + (Ki * error_sum) + (Kd * error_rate)
    
    # 3. Apply Saturation (The "Research Problem") [cite: 2, 32]
    torque = np.clip(torque, -MAX_TORQUE, MAX_TORQUE)
    
    # Check if motor has hit Max RPM 
    if abs(wheel_speed_rpm) >= MAX_RPM:
        torque = 0  # Motor can't accelerate anymore; stability is lost
    
    # 4. Physics Engine (Momentum Coupling) 
    # Torque on wheel creates opposite reaction on body
    gravity_torque = m_body * g * l_com * np.sin(theta)
    theta_accel = (gravity_torque - torque) / (m_body * l_com**2)
    
    # Update States
    theta_dot += theta_accel * dt
    theta += theta_dot * dt
    
    # Update Wheel Speed (Integration of torque/inertia)
    wheel_accel = torque / inertia_wheel
    wheel_speed_rpm += (wheel_accel * dt) * (60 / (2 * np.pi)) # Convert to RPM
    
    last_error = error
    
    # Store results
    results['time'].append(t)
    results['theta'].append(np.degrees(theta))
    results['rpm'].append(wheel_speed_rpm)

# --- Visualization (The "Proof" Graphs) --- [cite: 3, 4]
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

# Top Plot: Tilt Angle
ax1.plot(results['time'], results['theta'], color='blue', label='Tilt Angle (deg)')
ax1.axhline(0, color='black', linestyle='--')
ax1.set_ylabel('Degrees')
ax1.set_title('Robot Stability (Angle)')
ax1.legend()

# Bottom Plot: Wheel Speed & Saturation
ax2.plot(results['time'], results['rpm'], color='green', label='Wheel Speed (RPM)')
ax2.axhline(MAX_RPM, color='red', linestyle='--', label='Max RPM (Saturation)')
ax2.axhline(-MAX_RPM, color='red', linestyle='--')
ax2.set_ylabel('RPM')
ax2.set_xlabel('Time (s)')
ax2.set_title('Actuator Saturation Monitoring')
ax2.legend()

plt.tight_layout()
plt.show() # Use plt.savefig('stability_graph.png') if running on mobile [cite: 20]