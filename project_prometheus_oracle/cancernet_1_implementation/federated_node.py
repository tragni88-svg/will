
import numpy as np
import copy

# --- Simulation Configuration ---
N_FEATURES_GENOMIC = 1000 # e.g., gene expression values
N_FEATURES_IMAGING = 512  # e.g., features from a CNN processing a histology slide
N_SAMPLES_PER_NODE = 200
LEARNING_RATE = 0.01
N_LOCAL_EPOCHS = 5

# --- Helper Functions & Classes ---

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

class SimpleMultiModalNet:
    """A simplified multi-modal neural network for demonstration."""
    def __init__(self, input_dim_g, input_dim_i, hidden_dim=64):
        # Weights for genomic data
        self.weights_g = np.random.randn(input_dim_g, hidden_dim) * 0.1
        # Weights for imaging data
        self.weights_i = np.random.randn(input_dim_i, hidden_dim) * 0.1
        # Weights for the combined, final layer
        self.weights_final = np.random.randn(hidden_dim, 1) * 0.1

    def forward(self, x_g, x_i):
        # Process each modality separately
        self.hidden_g = sigmoid(np.dot(x_g, self.weights_g))
        self.hidden_i = sigmoid(np.dot(x_i, self.weights_i))
        
        # Fusion: simple averaging of the hidden representations
        self.hidden_combined = (self.hidden_g + self.hidden_i) / 2
        
        # Final prediction
        self.output = sigmoid(np.dot(self.hidden_combined, self.weights_final))
        return self.output

    def get_weights(self):
        """Return model weights for aggregation."""
        return [self.weights_g, self.weights_i, self.weights_final]

    def set_weights(self, weights):
        """Set model weights from aggregated server model."""
        self.weights_g, self.weights_i, self.weights_final = weights

class FederatedNode:
    """Represents a single node (e.g., a hospital) in the federated network."""
    def __init__(self, node_id):
        self.node_id = node_id
        self.model = SimpleMultiModalNet(N_FEATURES_GENOMIC, N_FEATURES_IMAGING)
        self.load_local_data()

    def load_local_data(self):
        """Simulates loading private, local data for this node."""
        print(f"[Node {self.node_id}] Loading local, private patient data...")
        # Create dummy data: genomic, imaging, and labels (0=healthy, 1=cancer)
        self.data_g = np.random.rand(N_SAMPLES_PER_NODE, N_FEATURES_GENOMIC)
        self.data_i = np.random.rand(N_SAMPLES_PER_NODE, N_FEATURES_IMAGING)
        self.labels = np.random.randint(0, 2, (N_SAMPLES_PER_NODE, 1))
        print(f"[Node {self.node_id}] Data loaded: {N_SAMPLES_PER_NODE} samples.")

    def train_local_model(self):
        """Trains the model on local data for a few epochs."""
        print(f"[Node {self.node_id}] Starting local training for {N_LOCAL_EPOCHS} epochs...")
        for epoch in range(N_LOCAL_EPOCHS):
            # --- Simplified Backpropagation ---
            # Forward pass
            output = self.model.forward(self.data_g, self.data_i)
            
            # Calculate error and delta
            error = self.labels - output
            d_output = error * sigmoid_derivative(output)
            
            # Backpropagate to final layer
            error_hidden_combined = d_output.dot(self.model.weights_final.T)
            d_hidden_combined = error_hidden_combined * sigmoid_derivative(self.model.hidden_combined)
            
            # Update weights
            self.model.weights_final += self.model.hidden_combined.T.dot(d_output) * LEARNING_RATE
            # (This is a simplification; a full implementation would backpropagate to g and i layers)

        print(f"[Node {self.node_id}] Local training complete.")
        return self.model.get_weights()

# --- Central Server Simulation ---

def federated_averaging(weight_updates):
    """Averages the weights from all participating nodes."""
    print("\n[Server] Aggregating model updates using Federated Averaging...")
    
    # Deep copy to ensure we have a clean structure
    avg_weights = copy.deepcopy(weight_updates[0])
    
    # Sum the weights from all other nodes
    for weights in weight_updates[1:]:
        for i in range(len(avg_weights)):
            avg_weights[i] += weights[i]
            
    # Average the weights
    for i in range(len(avg_weights)):
        avg_weights[i] /= len(weight_updates)
        
    print("[Server] Aggregation complete. New global model created.")
    return avg_weights

def main():
    """
    Main function to simulate a single round of federated learning.
    """
    print("==================================================")
    print("=== CANCERNET-1 FEDERATED LEARNING SIMULATOR ===")
    print("==================================================")

    # 1. Initialize nodes (hospitals)
    node1 = FederatedNode(node_id=1)
    node2 = FederatedNode(node_id=2)
    node3 = FederatedNode(node_id=3)
    nodes = [node1, node2, node3]

    # 2. Simulate a single round of federated learning
    print("\n--- Starting Federated Learning Round 1 ---")
    
    # Each node trains on its local data
    local_weight_updates = [node.train_local_model() for node in nodes]
    
    # The central server aggregates the updates
    global_model_weights = federated_averaging(local_weight_updates)
    
    # The server sends the new global model back to the nodes
    print("\n[Server] Distributing global model back to all nodes...")
    for node in nodes:
        node.model.set_weights(global_model_weights)
        print(f"[Node {node.node_id}] Received and updated to new global model.")

    print("\n==================================================")
    print("===      FEDERATED ROUND 1 COMPLETE          ===")
    print("==================================================")

if __name__ == "__main__":
    main()
