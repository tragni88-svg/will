
import numpy as np
import matplotlib.pyplot as plt
from mhd_engine_model import MHDEngine

class VehicleModel:
    """
    A simplified model of the Chimera vehicle for flight dynamics simulation.
    """
    def __init__(self, mass, inertia_tensor):
        self.mass = mass
        self.I = inertia_tensor  # Vehicle's inertia tensor
        
        # State variables
        self.position = np.zeros(3)
        self.velocity = np.zeros(3)
        self.attitude = np.zeros(3)  # [roll, pitch, yaw]
        self.angular_velocity = np.zeros(3) # [p, q, r]

    def update_state(self, total_force, total_torque, dt):
        """
        Updates the vehicle's state using simple Euler integration.
        """
        # Update linear dynamics
        acceleration = total_force / self.mass
        self.velocity += acceleration * dt
        self.position += self.velocity * dt
        
        # Update angular dynamics
        angular_acceleration = np.linalg.inv(self.I) @ total_torque
        self.angular_velocity += angular_acceleration * dt
        self.attitude += self.angular_velocity * dt

class FlightController:
    """
    Simulates the integrated MHD engine and flight control system.
    """
    def __init__(self, vehicle, num_segments=8):
        self.vehicle = vehicle
        self.num_segments = num_segments
        
        # Position of each engine segment around the CoM
        self.angles = np.linspace(0, 2 * np.pi, num_segments, endpoint=False)
        self.segment_positions = np.array([np.cos(self.angles), np.sin(self.angles), np.zeros(num_segments)]).T * 10 # 10m radius

        # --- MHD Engine Setup ---
        self.engines = []
        for i in range(num_segments):
            # For a toroidal setup, B is azimuthal, v is radial
            B_field = np.array([-np.sin(self.angles[i]), np.cos(self.angles[i]), 0]) * 5.0 # 5T field
            # Velocity will be modulated, so we start with a base vector
            v_plasma = np.array([np.cos(self.angles[i]), np.sin(self.angles[i]), 0])
            engine = MHDEngine(
                magnetic_field_strength=B_field,
                plasma_velocity=v_plasma, # This will be scaled
                plasma_charge_density=0.025
            )
            self.engines.append(engine)

        # PD Controller Gains
        self.Kp = 8.0  # Increased gains for responsiveness
        self.Kd = 12.0 # Increased gains for damping

    def run_simulation(self, duration, dt, initial_pitch_disturbance=5.0):
        """
        Runs the full flight simulation with integrated MHD physics.
        """
        self.vehicle.attitude[1] = np.deg2rad(initial_pitch_disturbance)
        
        num_steps = int(duration / dt)
        history = {'time': [], 'roll': [], 'pitch': [], 'thrust': []}
        
        base_thrust_for_hover = (self.vehicle.mass * 9.81) / self.num_segments
        # Estimate required velocity for hover from one engine
        # F = q * v * B * L => v = F / (q * B * L)
        # Assuming channel volume of 2.5, let's use an effective length L=sqrt(2.5)
        channel_vol = 2.5
        v_hover = base_thrust_for_hover / (0.025 * 5.0 * channel_vol)


        for i in range(num_steps):
            # --- Control System ---
            error = -self.vehicle.attitude
            error_dot = -self.vehicle.angular_velocity
            required_torque = self.Kp * error + self.Kd * error_dot
            
            # --- Thrust Allocation (now controls plasma velocity) ---
            thrust_commands = np.ones(self.num_segments) * v_hover
            thrust_commands -= required_torque[0] * np.sin(self.angles) * 100 # Scale factor for torque control
            thrust_commands -= required_torque[1] * np.cos(self.angles) * 100 # Scale factor for torque control
            
            thrust_commands = np.clip(thrust_commands, 0, v_hover * 2)
            
            # --- Physics (Calculate thrust from each MHD engine) ---
            total_force = np.zeros(3)
            total_torque = np.zeros(3)
            total_thrust_magnitude = 0

            for j in range(self.num_segments):
                # Set the plasma velocity based on the command
                self.engines[j].plasma_velocity = np.array([np.cos(self.angles[j]), np.sin(self.angles[j]), 0]) * thrust_commands[j]
                
                # Get the thrust vector from the physics model
                thrust_vector = self.engines[j].get_thrust(channel_volume=channel_vol)
                
                # The force is perpendicular to B and v, creating vertical lift (Z-axis)
                # This is a simplification; a real model would use the cross product result directly
                lift_force = np.array([0, 0, np.linalg.norm(thrust_vector)])
                
                total_force += lift_force
                total_torque += np.cross(self.segment_positions[j], lift_force)
                total_thrust_magnitude += np.linalg.norm(lift_force)

            # Add gravity
            gravity_force = np.array([0, 0, -self.vehicle.mass * 9.81])
            total_force += gravity_force

            # Update vehicle state
            self.vehicle.update_state(total_force, total_torque, dt)
            
            # Record data
            history['time'].append(i * dt)
            history['roll'].append(np.rad2deg(self.vehicle.attitude[0]))
            history['pitch'].append(np.rad2deg(self.vehicle.attitude[1]))
            history['thrust'].append(total_thrust_magnitude)
            
        return history

def plot_history(history, filename="flight_stability_plot.png"):
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10), sharex=True)
    
    ax1.plot(history['time'], history['pitch'], label='Pitch Angle')
    ax1.plot(history['time'], history['roll'], label='Roll Angle')
    ax1.set_title('Project Chimera: Active Stability Control (High-Fidelity)')
    ax1.set_ylabel('Angle (degrees)')
    ax1.grid(True)
    ax1.legend()
    ax1.axhline(0, color='black', linewidth=0.5, linestyle='--')

    ax2.plot(history['time'], history['thrust'], label='Total Thrust', color='r')
    ax2.set_xlabel('Time (s)')
    ax2.set_ylabel('Thrust (N)')
    ax2.grid(True)
    ax2.legend()
    ax2.axhline(VEHICLE_MASS * 9.81, color='blue', linewidth=0.5, linestyle='--', label='Hover Thrust')

    plt.tight_layout()
    plt.savefig(filename)
    print(f"Flight stability plot saved to {filename}")

if __name__ == '__main__':
    # --- Vehicle Parameters ---
    VEHICLE_MASS = 15000 # kg (Increased mass)
    VEHICLE_RADIUS = 12 # m
    I_zz = 0.5 * VEHICLE_MASS * VEHICLE_RADIUS**2
    I_xx = I_yy = 0.25 * VEHICLE_MASS * VEHICLE_RADIUS**2
    INERTIA = np.diag([I_xx, I_yy, I_zz])

    # --- Simulation ---
    chimera = VehicleModel(mass=VEHICLE_MASS, inertia_tensor=INERTIA)
    controller = FlightController(chimera, num_segments=8)
    
    # Run simulation for 10 seconds
    flight_data = controller.run_simulation(duration=10, dt=0.01, initial_pitch_disturbance=5.0)
    
    # Plot the results
    plot_history(flight_data, filename="c:/Users/bigwi/Documents/trae_projects/google social media/project_chimera/flight_stability_plot_hifi.png")

