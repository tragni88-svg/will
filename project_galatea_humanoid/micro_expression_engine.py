import numpy as np
import matplotlib.pyplot as plt
import time

class FacialActionUnit:
    """
    Represents a specific facial muscle group (Action Unit) controlled by a servo.
    Based on Ekman's Facial Action Coding System (FACS).
    """
    def __init__(self, name, au_id):
        self.name = name
        self.au_id = au_id
        self.intensity = 0.0 # 0.0 (relaxed) to 1.0 (max contraction)
        self.target_intensity = 0.0

    def update(self, step_size=0.05):
        """Linearly interpolates towards target intensity with a smoothing factor."""
        diff = self.target_intensity - self.intensity
        self.intensity += diff * step_size
        return self.intensity

class Emotion:
    """Defines a target configuration of Action Units for a specific emotion."""
    def __init__(self, name, au_config):
        self.name = name
        self.au_config = au_config # Dict of {au_id: target_intensity}

class MicroExpressionEngine:
    def __init__(self):
        # Define virtual servos / muscles
        self.action_units = {
            1: FacialActionUnit("Inner Brow Raiser", 1),
            2: FacialActionUnit("Outer Brow Raiser", 2),
            4: FacialActionUnit("Brow Lowerer", 4),
            6: FacialActionUnit("Cheek Raiser", 6),       # Critical for "real" smiles
            12: FacialActionUnit("Lip Corner Puller", 12), # Smile
            15: FacialActionUnit("Lip Corner Depressor", 15), # Frown
            26: FacialActionUnit("Jaw Drop", 26)
        }
        
        # Define basic emotions
        self.emotions = {
            "Neutral": Emotion("Neutral", {1:0, 2:0, 4:0, 6:0, 12:0, 15:0, 26:0}),
            "Joy": Emotion("Joy", {1:0, 2:0, 4:0, 6:0.8, 12:0.9, 15:0, 26:0.1}),
            "Surprise": Emotion("Surprise", {1:0.9, 2:0.9, 4:0, 6:0, 12:0, 15:0, 26:0.6}),
            "Anger": Emotion("Anger", {1:0, 2:0, 4:0.9, 6:0.3, 12:0, 15:0.3, 26:0.1}),
            "Sadness": Emotion("Sadness", {1:0.8, 2:0, 4:0.6, 6:0, 12:0, 15:0.7, 26:0})
        }
        
        self.current_emotion = "Neutral"
        self.micro_expression_active = False
        self.micro_timer = 0

    def set_emotion(self, emotion_name):
        if emotion_name in self.emotions:
            print(f"Transitioning to: {emotion_name}")
            self.current_emotion = emotion_name
            target_config = self.emotions[emotion_name].au_config
            
            for au_id, target in target_config.items():
                self.action_units[au_id].target_intensity = target

    def trigger_micro_expression(self, expression_name, duration_frames=10):
        """Triggers a fleeting, sub-conscious expression (approx 200ms)."""
        print(f"*** MICRO-EXPRESSION: {expression_name} ***")
        # Save current state logic would go here in a full implementation
        # For now, we momentarily override targets
        if expression_name in self.emotions:
            target_config = self.emotions[expression_name].au_config
            for au_id, target in target_config.items():
                # Micro-expressions are often partial intensity but very fast
                self.action_units[au_id].target_intensity = target * 0.7 

    def run_simulation(self, duration_seconds=5, fps=30):
        frames = int(duration_seconds * fps)
        history = {au_id: [] for au_id in self.action_units}
        time_axis = []

        print("Starting Simulation...")
        for f in range(frames):
            t = f / fps
            time_axis.append(t)
            
            # Scenario Script
            if f == 10: self.set_emotion("Joy")
            if f == 60: self.trigger_micro_expression("Anger") # Flash of anger
            if f == 70: self.set_emotion("Joy") # Return to Joy immediately
            if f == 110: self.set_emotion("Surprise")

            # Update all servos
            for au_id, au in self.action_units.items():
                val = au.update(step_size=0.1) # Fast update for responsiveness
                history[au_id].append(val)

        return time_axis, history

def plot_simulation(time_axis, history):
    plt.figure(figsize=(12, 8))
    
    # Plot key AUs
    plt.plot(time_axis, history[12], label="AU12 (Smile)", color='gold', linewidth=2)
    plt.plot(time_axis, history[4], label="AU4 (Frown/Brow)", color='red', linestyle='--')
    plt.plot(time_axis, history[1], label="AU1 (Inner Brow)", color='blue', alpha=0.7)
    plt.plot(time_axis, history[6], label="AU6 (Cheek/Eye)", color='green', alpha=0.7)

    plt.title('Project Galatea: Micro-Expression Dynamics')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Servo Intensity (0.0 - 1.0)')
    plt.axvspan(2.0, 2.33, color='red', alpha=0.1, label='Micro-Expression Window')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    output_file = 'micro_expression_plot.png'
    plt.savefig(output_file)
    print(f"Expression plot saved to {output_file}")

if __name__ == "__main__":
    engine = MicroExpressionEngine()
    t, h = engine.run_simulation(duration_seconds=5)
    plot_simulation(t, h)
