#!/usr/bin/env python
# coding: utf-8

import torch
import joblib
import pandas as pd
import numpy as np
from train_model import SynapseLSTM, SEQUENCE_LENGTH

# --- Prediction Pipeline ---

def load_model_and_encoders(model_dir):
    """Loads the trained model and encoders from disk."""
    print("Loading model and encoders...")
    
    # Load encoders
    encoders = joblib.load(f"{model_dir}/encoders.joblib")
    
    # Re-create model architecture
    vocab_sizes = {
        'hour': len(encoders['hour'].classes_),
        'day_of_week': len(encoders['day_of_week'].classes_),
        'location_context': len(encoders['location_context'].classes_),
        'device_state': len(encoders['device_state'].classes_),
        'app_name': len(encoders['app_name'].classes_)
    }
    # Note: These dimensions must match the training script
    embedding_dims = {
        'hour': 10,
        'day_of_week': 10,
        'location_context': 16,
        'device_state': 16,
        'app_name': 32
    }
    hidden_dim = 128

    model = SynapseLSTM(vocab_sizes, embedding_dims, hidden_dim)
    
    # Load the trained weights
    model.load_state_dict(torch.load(f"{model_dir}/synapse_lstm_model.pth"))
    model.eval() # Set model to evaluation mode
    
    print("Model and encoders loaded successfully.")
    return model, encoders

def predict_next_apps(model, encoders, current_sequence, top_n=3):
    """Predicts the top N most likely next apps based on a sequence."""
    
    # 1. Preprocess the input sequence
    # Convert the list of dicts to a DataFrame
    df = pd.DataFrame(current_sequence)
    
    # Apply the same feature engineering and encoding as in training
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['hour'] = df['timestamp'].dt.hour
    df['day_of_week'] = df['timestamp'].dt.dayofweek
    
    # Encode features using the loaded encoders. The original loop was flawed.
    # This corrected logic explicitly transforms each feature column.
    for col in ['hour', 'day_of_week', 'location_context', 'device_state']:
        encoder = encoders[col]
        df[col] = encoder.transform(df[col])

    # Encode the 'previous_app' column using the unified 'app_name' encoder
    app_encoder = encoders['app_name']
    df['previous_app'] = df['previous_app'].apply(lambda x: x if x in app_encoder.classes_ else 'none')
    df['previous_app'] = app_encoder.transform(df['previous_app'])

    # 2. Prepare the tensor for the model
    # Ensure we only use the required feature columns
    feature_columns = ['hour', 'day_of_week', 'location_context', 'device_state', 'previous_app']
    sequence_data = df[feature_columns].values
    
    # The model expects a batch, so we add a batch dimension
    sequence_tensor = torch.tensor(sequence_data, dtype=torch.long).unsqueeze(0)
    
    # 3. Make the prediction
    with torch.no_grad():
        output = model(sequence_tensor)
        probabilities = torch.softmax(output, dim=1)
    
    # 4. Get Top N predictions
    top_probs, top_indices = torch.topk(probabilities, top_n)
    
    # 5. Decode the predictions
    app_encoder = encoders['app_name']
    predicted_apps = app_encoder.inverse_transform(top_indices.numpy().flatten())
    
    return list(zip(predicted_apps, top_probs.numpy().flatten()))

# --- Main Execution ---
if __name__ == "__main__":
    model_dir = "c:\\Users\\bigwi\\Documents\\trae_projects\\google social media\\project_synapse_adaptive_launch\\model"
    model, encoders = load_model_and_encoders(model_dir)

    # Example: Simulate a recent history of app launches
    # This sequence must be of length SEQUENCE_LENGTH (10)
    sample_sequence = [
        {'timestamp': '2026-01-27 08:00:00', 'previous_app': 'Gmail', 'location_context': 'home', 'device_state': 'active'},
        {'timestamp': '2026-01-27 08:01:00', 'previous_app': 'Chrome', 'location_context': 'home', 'device_state': 'active'},
        {'timestamp': '2026-01-27 08:02:00', 'previous_app': 'Google Calendar', 'location_context': 'home', 'device_state': 'active'},
        {'timestamp': '2026-01-27 08:03:00', 'previous_app': 'Google Maps', 'location_context': 'home', 'device_state': 'active'},
        {'timestamp': '2026-01-27 08:04:00', 'previous_app': 'YouTube', 'location_context': 'home', 'device_state': 'active'},
        {'timestamp': '2026-01-27 08:05:00', 'previous_app': 'Gmail', 'location_context': 'home', 'device_state': 'active'},
        {'timestamp': '2026-01-27 08:06:00', 'previous_app': 'Chrome', 'location_context': 'home', 'device_state': 'active'},
        {'timestamp': '2026-01-27 08:07:00', 'previous_app': 'Google Calendar', 'location_context': 'home', 'device_state': 'active'},
        {'timestamp': '2026-01-27 08:08:00', 'previous_app': 'Google Maps', 'location_context': 'home', 'device_state': 'active'},
        {'timestamp': '2026-01-27 08:09:00', 'previous_app': 'YouTube', 'location_context': 'home', 'device_state': 'active'},
    ]

    predictions = predict_next_apps(model, encoders, sample_sequence)

    print("\n--- Adaptive Quick-Launch Predictions ---")
    print("Based on your recent activity, the next app you are likely to open is:")
    for i, (app, prob) in enumerate(predictions):
        print(f"{i+1}. {app} (Confidence: {prob:.2f})")


