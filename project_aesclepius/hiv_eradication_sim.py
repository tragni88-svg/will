import numpy as np
import matplotlib.pyplot as plt

# Project AESCLEPIUS: HIV-1 Reservoir Eradication Simulation
# -----------------------------------------------------------
# Models the dynamics of HIV-1 infection and the effect of a 
# CRISPR-Cas9 Dual-Vector therapy targeting the LTR region.

class AesclepiusSim:
    def __init__(self):
        # Time parameters (days)
        self.dt = 0.01
        self.days = 365 * 2  # Simulate 2 years
        self.steps = int(self.days / self.dt)
        self.time = np.linspace(0, self.days, self.steps)

        # Initial Conditions (per mm^3 blood)
        self.T_target = 1000.0  # Uninfected CD4+ T cells
        self.T_latent = 1.0     # Latent Reservoir (The enemy)
        self.T_active = 0.0     # Actively infected
        self.Virus = 50.0       # Viral load
        self.CRISPR = 0.0       # Therapeutic agent

        # Parameters
        self.lambda_t = 10.0    # T-cell production rate
        self.d_t = 0.01         # T-cell death rate
        self.beta = 2.4e-5      # Infection rate
        self.delta = 1.0        # Active infected cell death rate
        self.p = 2000.0         # Viral production per active cell
        self.c = 23.0           # Viral clearance rate
        
        # Therapy Parameters
        self.crispr_efficacy = 0.95  # Efficiency of excision per unit drug
        self.crispr_decay = 0.1      # Drug clearance rate
        self.activation_rate = 1e-3  # Latent -> Active (Shock)
        self.art_efficacy = 0.999    # ART viral suppression
        
    def run(self):
        # Arrays to store history
        history = {
            'T_target': np.zeros(self.steps),
            'T_latent': np.zeros(self.steps),
            'T_active': np.zeros(self.steps),
            'Virus': np.zeros(self.steps),
            'CRISPR': np.zeros(self.steps)
        }
        
        # Set initial values
        T, L, A, V, D = self.T_target, self.T_latent, self.T_active, self.Virus, self.CRISPR
        
        print(f"[*] Starting AESCLEPIUS Simulation...")
        print(f"[*] Initial Reservoir Size: {L:.4f} cells/mm^3")
        
        for i in range(self.steps):
            t = self.time[i]
            
            # --- Therapy Injection Schedule ---
            # Inject CRISPR-LNP weekly for the first 6 months
            if 100 < t < 500 and i % (7 / self.dt) < 1:
                D += 20.0  # Dose unit
                
            # --- Differential Equations ---
            
            # 1. Uninfected Cells (Production - Death - Infection + Cured)
            # Note: Successful CRISPR excision converts Latent -> Uninfected (Cured)
            cure_rate = self.crispr_efficacy * D * L
            dT = self.lambda_t - self.d_t * T - self.beta * T * V + cure_rate
            
            # 2. Latent Reservoir (Infection Fraction - Activation - Death - CURE)
            # A fraction (0.01) of infections become latent
            new_latent = 0.01 * self.beta * T * V
            activation = self.activation_rate * L
            dL = new_latent - activation - (0.01 * L) - cure_rate
            
            # 3. Active Infected (Infection Fraction + Activation - Death)
            new_active = 0.99 * self.beta * T * V
            dA = new_active + activation - self.delta * A
            
            # 4. Free Virus (Production - Clearance) - ART Suppressed
            dV = (self.p * A * (1 - self.art_efficacy)) - self.c * V
            
            # 5. CRISPR Agent (Decay)
            dD = -self.crispr_decay * D
            
            # Update States (Euler Method)
            T += dT * self.dt
            L += dL * self.dt
            A += dA * self.dt
            V += dV * self.dt
            D += dD * self.dt
            
            # Prevent negatives
            T = max(0, T); L = max(0, L); A = max(0, A); V = max(0, V); D = max(0, D)
            
            # Store history
            history['T_target'][i] = T
            history['T_latent'][i] = L
            history['T_active'][i] = A
            history['Virus'][i] = V
            history['CRISPR'][i] = D
            
        self.history = history
        return history

    def report(self):
        final_L = self.history['T_latent'][-1]
        final_V = self.history['Virus'][-1]
        
        print("-" * 40)
        print("SIMULATION COMPLETE")
        print("-" * 40)
        print(f"Final Latent Reservoir: {final_L:.10f} cells/mm^3")
        print(f"Final Viral Load:       {final_V:.10f} copies/ml")
        
        if final_L < 1e-6:
            print("\n>>> RESULT: FUNCTIONAL CURE ACHIEVED <<<")
            print(">>> STATUS: HIV-1 ERADICATED")
        else:
            print("\n>>> RESULT: FAILURE. RESERVOIR PERSISTS.")

if __name__ == "__main__":
    sim = AesclepiusSim()
    sim.run()
    sim.report()
