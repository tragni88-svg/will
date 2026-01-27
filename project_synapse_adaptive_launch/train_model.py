import pandas as pd
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import joblib
import os

# --- Configuration ---
SEQUENCE_LENGTH = 10  # Number of past app launches to consider for the next prediction
BATCH_SIZE = 64
NUM_EPOCHS = 5
EMBEDDING_DIM_STATIC = 10 # For hour, day_of_week
EMBEDDING_DIM_CONTEXT = 16 # For location, device_state
EMBEDDING_DIM_APP = 32 # For app_name (previous apps)
HIDDEN_DIM = 128
LEARNING_RATE = 0.001

# --- PyTorch Dataset for Sequences ---
class AppLaunchDataset(Dataset):
    """Custom Dataset for creating sequences of app launches."""
    def __init__(self, features, labels, sequence_length):
        self.features = features
        self.labels = labels
        self.sequence_length = sequence_length

    def __len__(self):
        return len(self.features) - self.sequence_length

    def __getitem__(self, idx):
        # The sequence of features ends at idx + sequence_length
        sequence = self.features[idx:idx + self.sequence_length]
        # The label is the app launch that immediately follows the sequence
        label = self.labels[idx + self.sequence_length]
        return torch.tensor(sequence, dtype=torch.long), torch.tensor(label, dtype=torch.long)

# --- LSTM Model Definition ---
class SynapseLSTM(nn.Module):
    def __init__(self, vocab_sizes, embedding_dims, hidden_dim):
        super(SynapseLSTM, self).__init__()
        self.hidden_dim = hidden_dim

        # Embedding layers for each categorical feature
        self.hour_embedding = nn.Embedding(vocab_sizes['hour'], embedding_dims['hour'])
        self.day_embedding = nn.Embedding(vocab_sizes['day_of_week'], embedding_dims['day_of_week'])
        self.location_embedding = nn.Embedding(vocab_sizes['location_context'], embedding_dims['location_context'])
        self.device_embedding = nn.Embedding(vocab_sizes['device_state'], embedding_dims['device_state'])
        self.app_embedding = nn.Embedding(vocab_sizes['app_name'], embedding_dims['app_name'])

        # Calculate concatenated embedding size
        concat_embedding_dim = sum(embedding_dims.values())

        # LSTM layer
        self.lstm = nn.LSTM(concat_embedding_dim, hidden_dim, batch_first=True)

        # Final fully connected layer
        self.fc = nn.Linear(hidden_dim, vocab_sizes['app_name']) # Output is a prediction for the next app

    def forward(self, x):
        # x shape: (batch_size, sequence_length, num_features)
        
        # Apply embeddings to each feature in the sequence
        hour_embeds = self.hour_embedding(x[:, :, 0])
        day_embeds = self.day_embedding(x[:, :, 1])
        location_embeds = self.location_embedding(x[:, :, 2])
        device_embeds = self.device_embedding(x[:, :, 3])
        app_embeds = self.app_embedding(x[:, :, 4]) # previous app is the 5th feature

        # Concatenate embeddings
        embeds = torch.cat((hour_embeds, day_embeds, location_embeds, device_embeds, app_embeds), dim=2)

        # LSTM forward pass
        lstm_out, _ = self.lstm(embeds)

        # We only care about the output of the last time step
        final_output = lstm_out[:, -1, :]
        
        # Final prediction
        logits = self.fc(final_output)
        return logits

# --- Model Training Pipeline ---
def train_model(data_path, model_dir):
    """Loads data, preprocesses for LSTM, trains, and saves the model."""
    print("--- Starting Synapse-1 LSTM Model Training ---")

    # 1. Load Data
    print("Loading a subset of data to conserve memory...")
    df = pd.read_csv(data_path, nrows=20000) # Use only the first 20,000 rows
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['hour'] = df['timestamp'].dt.hour
    df['day_of_week'] = df['timestamp'].dt.dayofweek
    # The target is the current app, the features are from the past
    df['previous_app'] = df['app_name'].shift(1).fillna('none')

    # 2. Encode ALL categorical features
    print("Encoding categorical features...")
    encoders = {}
    # Encode context features first
    for col in ['hour', 'day_of_week', 'location_context', 'device_state']:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        encoders[col] = le

    # Create a unified encoder for all app names (current and previous)
    app_encoder = LabelEncoder()
    all_apps = pd.concat([df['app_name'], df['previous_app']]).unique()
    app_encoder.fit(all_apps)
    encoders['app_name'] = app_encoder # Use a single encoder for all apps

    # Transform feature and target columns using the unified app encoder
    df['previous_app'] = app_encoder.transform(df['previous_app'])
    labels = app_encoder.transform(df['app_name'])
    
    # Features for the LSTM
    feature_columns = ['hour', 'day_of_week', 'location_context', 'device_state', 'previous_app']
    features = df[feature_columns].values

    # 3. Create Datasets and DataLoaders
    X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

    train_dataset = AppLaunchDataset(X_train, y_train, SEQUENCE_LENGTH)
    test_dataset = AppLaunchDataset(X_test, y_test, SEQUENCE_LENGTH)

    train_loader = DataLoader(train_dataset, batch_size=BATCH_SIZE, shuffle=True)
    test_loader = DataLoader(test_dataset, batch_size=BATCH_SIZE, shuffle=False)

    print(f"Created {len(train_loader)} training batches and {len(test_loader)} testing batches.")

    # 4. Initialize Model, Loss, and Optimizer
    vocab_sizes = {
        'hour': len(encoders['hour'].classes_),
        'day_of_week': len(encoders['day_of_week'].classes_),
        'location_context': len(encoders['location_context'].classes_),
        'device_state': len(encoders['device_state'].classes_),
        'app_name': len(encoders['app_name'].classes_) # Unified app vocabulary
    }
    embedding_dims = {
        'hour': EMBEDDING_DIM_STATIC,
        'day_of_week': EMBEDDING_DIM_STATIC,
        'location_context': EMBEDDING_DIM_CONTEXT,
        'device_state': EMBEDDING_DIM_CONTEXT,
        'app_name': EMBEDDING_DIM_APP
    }

    model = SynapseLSTM(vocab_sizes, embedding_dims, HIDDEN_DIM)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=LEARNING_RATE)

    print("Starting model training...")
    # 5. Training Loop
    for epoch in range(NUM_EPOCHS):
        model.train()
        total_loss = 0
        for sequences, labels in train_loader:
            optimizer.zero_grad()
            outputs = model(sequences)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
            total_loss += loss.item()
        
        avg_loss = total_loss / len(train_loader)
        print(f"Epoch [{epoch+1}/{NUM_EPOCHS}], Loss: {avg_loss:.4f}")

    # 6. Evaluation
    print("Evaluating model...")
    model.eval()
    correct = 0
    total = 0
    batch_count = 0
    with torch.no_grad():
        for sequences, labels in test_loader:
            batch_count += 1
            outputs = model(sequences)
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

    print(f"Evaluation completed over {batch_count} batches.")
    accuracy = 100 * correct / total
    print(f"Model Accuracy on Test Set: {accuracy:.2f}%")

    # 7. Save the Model and Encoders
    print(f"Saving model and supporting files to: {model_dir}")
    if not os.path.exists(model_dir):
        os.makedirs(model_dir)
        
    torch.save(model.state_dict(), os.path.join(model_dir, 'synapse_lstm_model.pth'))
    joblib.dump(encoders, os.path.join(model_dir, 'encoders.joblib'))

    print("--- Model Training Complete ---")

# --- Main Execution ---
if __name__ == "__main__":
    data_file = "c:\\Users\\bigwi\\Documents\\trae_projects\\google social media\\project_synapse_adaptive_launch\\data\\simulated_app_launches.csv"
    model_output_dir = "c:\\Users\\bigwi\\Documents\\trae_projects\\google social media\\project_synapse_adaptive_launch\\model"
    train_model(data_file, model_output_dir)
