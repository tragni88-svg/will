from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import dropship_orchestrator
import random
import time
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for local development

# Load config once
config = dropship_orchestrator.load_config()

# Global State for Simulation
SIMULATION_STATE = {
    "traffic_multiplier": 1.5,
    "active_campaigns": ["google_smart"],
    "base_visitors": 120,
    "total_sales": 1240.50, # Pre-seeded for serverless feel
    "crm_contacts": [
        {"id": 1, "name": "Alice Smith", "email": "alice@example.com", "tags": ["lead"], "score": 10},
        {"id": 2, "name": "Bob Jones", "email": "bob@example.com", "tags": ["customer"], "score": 85},
        {"id": 3, "name": "Charlie Day", "email": "charlie@example.com", "tags": ["lead", "high-value"], "score": 45}
    ],
    "automations": [],
    "agents": {
        "sourcing": {"status": "active", "last_action": "Scanning AliExpress trends..."},
        "marketing": {"status": "active", "last_action": "Optimizing CPC bids..."},
        "support": {"status": "idle", "last_action": "Waiting for tickets..."},
        "scout": {"status": "active", "last_action": "Analyzing customer feedback..."}
    }
}

@app.route('/')
def index():
    # Serve the frontend from the parent directory
    return send_from_directory('..', 'app.paid.html')

@app.route('/api/stats', methods=['GET'])
def get_stats():
    # --- AGENT LOGIC ---
    # Marketing Agent: Auto-boost traffic if active
    if SIMULATION_STATE["agents"]["marketing"]["status"] == "active":
        if random.random() < 0.1: # 10% chance per tick to optimize
            SIMULATION_STATE["traffic_multiplier"] += 0.1
            SIMULATION_STATE["agents"]["marketing"]["last_action"] = f"Optimized ad spend (+0.1x traffic)"

    # Sourcing Agent: Find "new" products occasionally
    if SIMULATION_STATE["agents"]["sourcing"]["status"] == "active":
        if random.random() < 0.05:
            SIMULATION_STATE["agents"]["sourcing"]["last_action"] = f"Found trending item: 'Gadget-{random.randint(100,999)}'"
            
    # Support Agent: Resolve tickets
    if SIMULATION_STATE["agents"]["support"]["status"] == "active":
         if random.random() < 0.15:
            SIMULATION_STATE["agents"]["support"]["last_action"] = f"Resolved Ticket #{random.randint(1000,9999)}"
            
    # Scout Agent: Customer Service Insights
    if SIMULATION_STATE["agents"]["scout"]["status"] == "active":
        if random.random() < 0.08: # 8% chance to find an insight
            insights = [
                "Identified common question about shipping times.",
                "Detected user confusion regarding return policy.",
                "Flagged a positive product review for marketing.",
                "Noticed a trend in sizing questions for apparel."
            ]
            SIMULATION_STATE["agents"]["scout"]["last_action"] = random.choice(insights)
    
    # --- END AGENT LOGIC ---

    # Calculate traffic based on campaigns
    current_visitors = int(SIMULATION_STATE["base_visitors"] * SIMULATION_STATE["traffic_multiplier"])
    
    # Add some jitter
    current_visitors += random.randint(-10, 20)
    
    # Simulate conversions
    conversion_rate = 0.025 # 2.5%
    new_orders = 0
    
    # If we have high traffic, generate more orders
    if random.random() < (current_visitors * conversion_rate / 60): # Per request probability
        new_orders = 1
        sale_amount = random.uniform(20.0, 100.0)
        SIMULATION_STATE["total_sales"] += sale_amount
        
        # Add a new contact to CRM automatically on sale
        new_id = len(SIMULATION_STATE["crm_contacts"]) + 1
        SIMULATION_STATE["crm_contacts"].append({
            "id": new_id,
            "name": f"Customer {new_id}",
            "email": f"customer{new_id}@example.com",
            "tags": ["customer", "new_sale"],
            "score": 50
        })

    return jsonify({
        "daily_profit": round(SIMULATION_STATE["total_sales"] * 0.3, 2), # Assume 30% margin
        "active_orders": random.randint(10, 50) + new_orders,
        "live_visitors": current_visitors,
        "active_campaigns": SIMULATION_STATE["active_campaigns"],
        "crm_count": len(SIMULATION_STATE["crm_contacts"]),
        "agents": SIMULATION_STATE["agents"],
        "platform_status": {
            "shopify": "active",
            "amazon": "active",
            "ebay": "active"
        }
    })

@app.route('/api/agents/toggle', methods=['POST'])
def toggle_agent():
    data = request.json
    agent_name = data.get('agent')
    
    if agent_name in SIMULATION_STATE["agents"]:
        current = SIMULATION_STATE["agents"][agent_name]["status"]
        new_status = "active" if current == "idle" else "idle"
        SIMULATION_STATE["agents"][agent_name]["status"] = new_status
        return jsonify({"status": "success", "new_state": new_status})
    
    return jsonify({"status": "error", "message": "Agent not found"}), 404

@app.route('/api/crm/contacts', methods=['GET'])
def get_contacts():
    return jsonify(SIMULATION_STATE["crm_contacts"])

@app.route('/api/crm/automate', methods=['POST'])
def trigger_automation():
    data = request.json
    sequence_name = data.get('sequence', 'default_nurture')
    
    # Simulate processing logic
    time.sleep(1) 
    
    SIMULATION_STATE["automations"].append({
        "sequence": sequence_name,
        "timestamp": time.time(),
        "affected_contacts": len(SIMULATION_STATE["crm_contacts"])
    })
    
    return jsonify({
        "status": "success",
        "message": f"Triggered '{sequence_name}' for {len(SIMULATION_STATE['crm_contacts'])} contacts.",
        "details": "Emails queued, tags applied."
    })

@app.route('/api/marketing/launch', methods=['POST'])
def launch_campaign():
    data = request.json
    platform = data.get('platform', 'unknown')
    
    # Boost traffic
    boost = 0.0
    if platform == 'google':
        boost = 2.5
    elif platform == 'tiktok':
        boost = 5.0 # Viral spike
    elif platform == 'fanbasis':
        boost = 3.0 # Targeted
        
    SIMULATION_STATE["traffic_multiplier"] += boost
    SIMULATION_STATE["active_campaigns"].append(platform)
    
    return jsonify({
        "status": "success",
        "message": f"Launched {platform} campaign",
        "new_multiplier": SIMULATION_STATE["traffic_multiplier"]
    })

import urllib.parse

# Helper for Image Generation
def get_image_url(title):
    safe_title = urllib.parse.quote(title)
    return f"https://core-normal.traeapi.us/api/ide/v1/text_to_image?prompt={safe_title}&image_size=square"

@app.route('/api/chat', methods=['POST'])
def chat_agent():
    data = request.json
    message = data.get('message', '').lower()
    
    response = "I'm analyzing your store data. Ask me about profit, products, or traffic."
    
    if "profit" in message or "money" in message:
        profit = SIMULATION_STATE["total_sales"] * 0.3
        response = f"Your estimated daily profit is ${profit:.2f}. We are tracking at a 30% margin."
    elif "product" in message or "sell" in message:
        response = "Electronics and Home Decor are trending. I recommend adding more 'Smart' devices to the catalog."
    elif "traffic" in message or "visitor" in message:
        response = f"Traffic is {SIMULATION_STATE['traffic_multiplier']}x normal levels. Consider launching a TikTok campaign to boost this."
    elif "hello" in message or "hi" in message:
        response = "Hello! I'm SalesApe. I'm here to help you optimize your dropshipping empire."
        
    return jsonify({"response": response})

@app.route('/api/products', methods=['GET'])
def get_products():
    # Fetch live products using the orchestrator
    # We'll default to a search query "smart home" for demo purposes
    products = dropship_orchestrator.search_aliexpress_products("smart home", config)
    
    # Vet them for Shopify just to show approved ones
    vetted_products = []
    for p in products:
        result = dropship_orchestrator.vet_product(p, config, platform='shopify')
        if result:
            result['image_url'] = get_image_url(result['title'])
            vetted_products.append(result)
            
    # If no live API key, return mock data
    if not vetted_products:
        mock_items = [
            {"title": "Smart LED Strip Lights", "selling_price": 24.99, "cost_of_goods": 8.50, "source": "AliExpress"},
            {"title": "WiFi Smart Plug", "selling_price": 15.99, "cost_of_goods": 4.20, "source": "AliExpress"},
            {"title": "Bluetooth Tracker", "selling_price": 19.99, "cost_of_goods": 3.50, "source": "AliExpress"},
            {"title": "Portable Neck Fan", "selling_price": 29.99, "cost_of_goods": 9.50, "source": "AliExpress"},
            {"title": "Galaxy Star Projector", "selling_price": 45.99, "cost_of_goods": 18.20, "source": "AliExpress"},
            {"title": "Magnetic Car Phone Mount", "selling_price": 12.99, "cost_of_goods": 2.10, "source": "AliExpress"},
            {"title": "Adjustable Posture Corrector", "selling_price": 22.50, "cost_of_goods": 5.40, "source": "AliExpress"},
            {"title": "Waterproof Phone Pouch", "selling_price": 9.99, "cost_of_goods": 1.20, "source": "AliExpress"},
            {"title": "Sunset Lamp Projection", "selling_price": 18.99, "cost_of_goods": 6.80, "source": "AliExpress"},
            {"title": "Silicone Kitchen Utensil Set", "selling_price": 34.99, "cost_of_goods": 12.50, "source": "AliExpress"},
            {"title": "Digital Mirror Alarm Clock", "selling_price": 16.99, "cost_of_goods": 5.90, "source": "AliExpress"},
            {"title": "Fast Wireless Charger Stand", "selling_price": 27.99, "cost_of_goods": 8.90, "source": "AliExpress"},
            {"title": "Ultrasonic Mini Humidifier", "selling_price": 19.99, "cost_of_goods": 6.30, "source": "AliExpress"}
        ]
        
        for item in mock_items:
            item['image_url'] = get_image_url(item['title'])
            vetted_products.append(item)
        
    return jsonify(vetted_products[:20]) # Return top 20

if __name__ == '__main__':
    print("Starting Dropship Manager API on port 5000...")
    app.run(debug=True, port=5000)
