import csv
import random
from datetime import datetime, timedelta

# --- Simulation Parameters ---

# Define common apps and their typical usage contexts
APP_PROFILES = {
    "com.google.android.gm": {"context": ["work", "morning"], "weight": 8},
    "com.google.android.apps.maps": {"context": ["travel"], "weight": 6},
    "com.google.android.youtube": {"context": ["home", "evening"], "weight": 9},
    "com.android.chrome": {"context": ["work", "home"], "weight": 10},
    "com.google.android.calendar": {"context": ["work", "morning"], "weight": 7},
    "com.spotify.music": {"context": ["travel", "gym"], "weight": 8},
    "com.instagram.android": {"context": ["home", "evening"], "weight": 7},
    "com.whatsapp": {"context": ["work", "home"], "weight": 9},
    "com.google.android.apps.photos": {"context": ["home", "travel"], "weight": 5},
}

# Define user contexts over a day
DAY_CONTEXTS = {
    "morning": (7, 10),   # 7 AM - 10 AM
    "work": (10, 17),     # 10 AM - 5 PM
    "travel": (17, 18),   # 5 PM - 6 PM (commute)
    "evening": (18, 23),  # 6 PM - 11 PM
    "home": (0, 24),      # Home is a general context
    "gym": (18, 19)       # 6 PM - 7 PM
}

# --- Data Generation Logic ---

def get_context(current_time):
    """Determines the current user context based on the time of day."""
    hour = current_time.hour
    contexts = ["home"] # User is always at home in this simulation for simplicity
    for context, (start, end) in DAY_CONTEXTS.items():
        if start <= hour < end:
            contexts.append(context)
    return contexts

def choose_app(contexts):
    """Chooses an app to launch based on the current context."""
    weighted_apps = []
    for app, profile in APP_PROFILES.items():
        # Increase weight if app context matches current user context
        relevance = len(set(profile["context"]) & set(contexts))
        weight = profile["weight"] + (relevance * 5) # Boost weight for relevant apps
        weighted_apps.extend([app] * weight)
    
    return random.choice(weighted_apps)

def generate_dataset(file_path, days=30):
    """Generates a simulated app launch dataset for a specified number of days."""
    print(f"Generating {days} days of simulated app launch data...")
    header = ["timestamp", "app_name", "location_context", "device_state"]
    
    with open(file_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        
        start_time = datetime(2026, 1, 1, 7, 0, 0) # Start on Jan 1, 2026, at 7 AM
        current_time = start_time
        
        for _ in range(days * 24 * 20): # Simulate ~20 app launches per hour
            # Introduce random time jumps between launches (1 to 15 minutes)
            current_time += timedelta(minutes=random.randint(1, 15))
            
            if current_time.hour < 7: # Simulate sleep
                continue

            contexts = get_context(current_time)
            app_to_launch = choose_app(contexts)
            
            # Simulate device state
            device_state = random.choice(["active", "charging", "headphones_in"])
            location = random.choice(["home", "work", "gym", "transit"])

            writer.writerow([
                current_time.isoformat(),
                app_to_launch,
                location,
                device_state
            ])

    print(f"Dataset successfully generated at: {file_path}")

# --- Main Execution ---

if __name__ == "__main__":
    output_file = "c:\\Users\\bigwi\\Documents\\trae_projects\\google social media\\project_synapse_adaptive_launch\\data\\simulated_app_launches.csv"
    generate_dataset(output_file, days=90) # Generate a richer 90-day dataset
