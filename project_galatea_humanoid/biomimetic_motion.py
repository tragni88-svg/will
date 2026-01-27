import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

class BiomimeticJoint:
    def __init__(self, name, current_pos=0.0):
        self.name = name
        self.current_pos = current_pos
        self.target_pos = current_pos
        self.velocity = 0.0
        self.muscle_tension = 0.5 # 0.0 (relaxed) to 1.0 (tense)

    def generate_human_path(self, target, duration_steps=100):
        """
        Generates a motion path that mimics human muscle movement.
        Humans don't move linearly; we accelerate and decelerate (sigmoid).
        """
        t = np.linspace(0, 1, duration_steps)
        
        # Sigmoid function for 'ease-in-ease-out' movement
        # Adjust steepness based on muscle tension
        steepness = 10 + (self.muscle_tension * 5)
        sigmoid = 1 / (1 + np.exp(-steepness * (t - 0.5)))
        
        # Scale to target range
        path = self.current_pos + (target - self.current_pos) * sigmoid
        
        # Add "Biological Noise" (Subtle tremors/imperfections)
        noise_magnitude = 0.002 * (1.1 - self.muscle_tension) # More tension = less tremor
        noise = np.random.normal(0, noise_magnitude, duration_steps)
        
        # Smooth the noise to make it organic, not jittery
        smoothed_noise = np.convolve(noise, np.ones(5)/5, mode='same')
        
        return path + smoothed_noise

def simulate_hand_reach():
    """Simulates a hand reaching out to touch an object gently."""
    print("--- Simulating Biomimetic Hand Reach ---")
    
    # Define joints
    shoulder = BiomimeticJoint("Shoulder", 0)
    elbow = BiomimeticJoint("Elbow", 10)
    wrist = BiomimeticJoint("Wrist", 0)
    
    # Target positions (degrees)
    shoulder_path = shoulder.generate_human_path(45, duration_steps=200) # Lift arm
    elbow_path = elbow.generate_human_path(90, duration_steps=200)    # Extend arm
    wrist_path = wrist.generate_human_path(15, duration_steps=200)    # Tilt hand
    
    # Visualize the motion
    time_steps = np.arange(200)
    
    plt.figure(figsize=(10, 6))
    plt.plot(time_steps, shoulder_path, label='Shoulder Flexion', color='blue')
    plt.plot(time_steps, elbow_path, label='Elbow Extension', color='green')
    plt.plot(time_steps, wrist_path, label='Wrist Deviation', color='red')
    
    plt.title('Project Galatea: Biomimetic Motion Profile')
    plt.xlabel('Time (ms)')
    plt.ylabel('Joint Angle (degrees)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    output_file = 'biomimetic_motion_plot.png'
    plt.savefig(output_file)
    print(f"Motion profile generated and saved to {output_file}")
    print("Note the S-curve shape: This represents natural muscle acceleration/deceleration.")
    print("Note the micro-variations: This represents biological 'aliveness'.")

if __name__ == "__main__":
    simulate_hand_reach()
