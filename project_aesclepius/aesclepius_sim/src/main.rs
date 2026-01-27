// Project AESCLEPIUS: HIV-1 Reservoir Eradication Simulation
// -----------------------------------------------------------

struct State {
    t_target: f64, // Uninfected CD4+ T cells
    t_latent: f64, // Latent Reservoir (The enemy)
    t_active: f64, // Actively infected
    virus: f64,    // Viral load
    crispr: f64,   // Therapeutic agent
}

struct Parameters {
    lambda_t: f64,        // T-cell production rate
    d_t: f64,             // T-cell death rate
    beta: f64,            // Infection rate
    delta: f64,           // Active infected cell death rate
    p: f64,               // Viral production per active cell
    c: f64,               // Viral clearance rate
    crispr_efficacy: f64, // Efficiency of excision
    crispr_decay: f64,    // Drug clearance rate
    activation_rate: f64, // Latent -> Active (Shock)
}

fn main() {
    println!("[*] Initiating AESCLEPIUS Protocol...");
    
    // Initial Conditions
    let mut state = State {
        t_target: 1000.0,
        t_latent: 1.0,
        t_active: 0.0,
        virus: 50.0,
        crispr: 0.0,
    };

    println!("[*] Initial Reservoir Size: {:.4} cells/mm^3", state.t_latent);

    let params = Parameters {
        lambda_t: 10.0,
        d_t: 0.01,
        beta: 2.4e-5,
        delta: 1.0,
        p: 2000.0,
        c: 23.0,
        crispr_efficacy: 0.05,
        crispr_decay: 0.1,
        activation_rate: 1e-3,
    };

    let dt = 0.01;
    let days = 365.0 * 2.0; // 2 years
    let steps = (days / dt) as usize;

    for i in 0..steps {
        let t = (i as f64) * dt;

        // --- Therapy Injection Schedule ---
        // ART Therapy: Starts Day 0, reduces infection rate by 99.9%
        let current_beta = if t > 0.0 { params.beta * 0.001 } else { params.beta };

        // Inject CRISPR-LNP weekly for the first 6 months (days 100 to 280)
        if t > 100.0 && t < 280.0 {
            // Simple check for weekly injection: roughly every 7 days
            let day_mod = t % 7.0;
            if day_mod < dt {
                state.crispr += 50.0; // INCREASED Dose unit (was 10.0)
            }
        }

        // --- Differential Equations ---

        // Cure Rate (Excision)
        let cure_rate = params.crispr_efficacy * state.crispr * state.t_latent;

        // 1. Uninfected Cells
        let dt_target = params.lambda_t 
                        - params.d_t * state.t_target 
                        - current_beta * state.t_target * state.virus 
                        + cure_rate;

        // 2. Latent Reservoir
        let new_latent = 0.01 * current_beta * state.t_target * state.virus;
        let activation = params.activation_rate * state.t_latent;
        let dt_latent = new_latent 
                        - activation 
                        - (0.01 * state.t_latent) // Natural death of latent cells
                        - cure_rate;

        // 3. Active Infected
        let new_active = 0.99 * current_beta * state.t_target * state.virus;
        let dt_active = new_active + activation - params.delta * state.t_active;

        // 4. Free Virus
        let d_virus = params.p * state.t_active - params.c * state.virus;

        // 5. CRISPR Agent
        let d_crispr = -params.crispr_decay * state.crispr;

        // Update State (Euler Method)
        state.t_target += dt_target * dt;
        state.t_latent += dt_latent * dt;
        state.t_active += dt_active * dt;
        state.virus += d_virus * dt;
        state.crispr += d_crispr * dt;

        // Prevent negatives
        if state.t_target < 0.0 { state.t_target = 0.0; }
        if state.t_latent < 0.0 { state.t_latent = 0.0; }
        if state.t_active < 0.0 { state.t_active = 0.0; }
        if state.virus < 0.0 { state.virus = 0.0; }
        if state.crispr < 0.0 { state.crispr = 0.0; }
    }

    report(state);
}

fn report(state: State) {
    println!("----------------------------------------");
    println!("SIMULATION COMPLETE");
    println!("----------------------------------------");
    println!("Final Latent Reservoir: {:.10} cells/mm^3", state.t_latent);
    println!("Final Viral Load:       {:.10} copies/ml", state.virus);

    if state.t_latent < 1e-6 {
        println!("\n>>> RESULT: FUNCTIONAL CURE ACHIEVED <<<");
        println!(">>> STATUS: HIV-1 ERADICATED");
    } else {
        println!("\n>>> RESULT: FAILURE. RESERVOIR PERSISTS.");
    }
}
