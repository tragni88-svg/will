import json
import requests
import time
import hashlib
from typing import Dict, List, Optional

def load_config(config_path='config.json'):
    """Loads the master configuration file."""
    with open(config_path, 'r') as f:
        return json.load(f)

def save_config(config, config_path='config.json'):
    """Saves the configuration file."""
    with open(config_path, 'w') as f:
        json.dump(config, f, indent=4)

def create_shopify_product(product_data: Dict, shopify_config: Dict) -> bool:
    """Creates a product listing on Shopify."""
    store_url = shopify_config['store_url']
    api_key = shopify_config['api_key']
    api_secret = shopify_config['api_secret']
    
    if not all([store_url, api_key, api_secret]):
        print("[ERROR] Shopify credentials not configured. Please update config.json.")
        return False
    
    # Shopify API endpoint
    url = f"https://{store_url}.myshopify.com/admin/api/2023-10/products.json"
    
    # Product data payload
    payload = {
        "product": {
            "title": product_data['title'],
            "body_html": product_data.get('description', ''),
            "vendor": "Dropship Manager",
            "product_type": product_data.get('category', 'General'),
            "variants": [{
                "price": str(product_data['selling_price']),
                "sku": product_data.get('sku', f"SKU-{int(time.time())}"),
                "inventory_management": None,  # We'll manage inventory separately
                "fulfillment_service": "manual"
            }],
            "images": [{"src": img_url} for img_url in product_data.get('image_urls', [])]
        }
    }
    
    try:
        response = requests.post(
            url,
            json=payload,
            auth=(api_key, api_secret),
            headers={"Content-Type": "application/json"}
        )
        
        if response.status_code == 201:
            print(f"[SUCCESS] Product '{product_data['title']}' listed on Shopify.")
            return True
        else:
            print(f"[ERROR] Shopify API error: {response.status_code} - {response.text}")
            return False
            
    except Exception as e:
        print(f"[ERROR] Exception creating Shopify product: {e}")
        return False

def fetch_aliexpress_products(keywords: str, aliexpress_config: Dict) -> List[Dict]:
    """Fetches products from AliExpress API."""
    app_key = aliexpress_config['app_key']
    app_secret = aliexpress_config['app_secret']
    
    if not all([app_key, app_secret]):
        print("[ERROR] AliExpress credentials not configured. Please update config.json.")
        return []
    
    # AliExpress API endpoint
    api_url = "https://api-sg.aliexpress.com/rest"
    
    # API parameters
    method = 'aliexpress.ds.product.get'
    timestamp = str(int(time.time() * 1000))
    
    params = {
        'app_key': app_key,
        'method': method,
        'sign_method': 'sha256',
        'timestamp': timestamp,
        'product_id': '1005003086262355',  # Example product ID
        'ship_to_country': 'US',
        'target_currency': 'USD',
        'target_language': 'en'
    }
    
    # Generate signature
    sorted_params = sorted(params.items())
    sign_string = app_secret + ''.join([f'{k}{v}' for k, v in sorted_params]) + app_secret
    params['sign'] = hashlib.sha256(sign_string.encode('utf-8')).hexdigest().upper()
    
    try:
        response = requests.get(api_url, params=params)
        
        if response.status_code == 200:
            data = response.json()
            print(f"[SUCCESS] Fetched product data from AliExpress.")
            
            # Parse and return product data
            if 'result' in data and 'products' in data['result']:
                products = []
                for item in data['result']['products']:
                    product = {
                        'title': item.get('product_title', ''),
                        'cost_of_goods': float(item.get('sale_price', {}).get('value', 0)),
                        'shipping_cost': 0.0,  # Will need to calculate separately
                        'description': item.get('product_detail_url', ''),
                        'image_urls': [img.get('image_url', '') for img in item.get('product_images', [])],
                        'supplier_rating': 98,  # Placeholder
                        'shipping_time_days': 12  # Placeholder
                    }
                    products.append(product)
                return products
            else:
                print(f"[ERROR] Unexpected AliExpress API response format: {data}")
                return []
        else:
            print(f"[ERROR] AliExpress API error: {response.status_code} - {response.text}")
            return []
            
    except Exception as e:
        print(f"[ERROR] Exception fetching AliExpress products: {e}")
        return []

def setup_store_accounts(config):
    """Sets up store accounts with proper payout configuration."""
    print("=== Setting Up Store Accounts ===")
    print(f"Beneficiary: {config['accounts']['payout_beneficiary']}")
    
    # Shopify setup
    shopify_config = config['platforms']['shopify']
    if shopify_config['api_key'] and shopify_config['api_secret'] and shopify_config['store_url']:
        print("[INFO] Shopify credentials configured.")
        print(f"Store URL: {shopify_config['store_url']}.myshopify.com")
        print("[ACTION REQUIRED] Ensure payout settings are configured to William Tragni in Shopify admin.")
    else:
        print("[WARNING] Shopify credentials not configured. Please update config.json.")
    
    # Amazon setup
    amazon_config = config['platforms']['amazon']
    if amazon_config['seller_id'] and amazon_config['mws_auth_token']:
        print("[INFO] Amazon credentials configured.")
        print(f"Seller ID: {amazon_config['seller_id']}")
        print("[ACTION REQUIRED] Ensure payout settings are configured to William Tragni in Amazon Seller Central.")
    else:
        print("[WARNING] Amazon credentials not configured. Please update config.json.")
    
    # eBay setup
    ebay_config = config['platforms']['ebay']
    if ebay_config['app_id'] and ebay_config['cert_id'] and ebay_config['dev_id'] and ebay_config['auth_token']:
        print("[INFO] eBay credentials configured.")
        print("[ACTION REQUIRED] Ensure payout settings are configured to William Tragni in eBay Seller Hub.")
    else:
        print("[WARNING] eBay credentials not configured. Please update config.json.")

def main():
    """Main orchestration function."""
    config = load_config()
    
    print("=== Dropshipping Account Setup ===")
    setup_store_accounts(config)
    
    print("\n=== Testing Product Vetting ===")
    
    # Test with sample products
    sample_products = [
        {
            "title": "Smart Fitness Tracker",
            "cost_of_goods": 12.50,
            "shipping_cost": 3.50,
            "supplier_rating": 97,
            "shipping_time_days": 10,
            "description": "Advanced fitness tracker with heart rate monitor and GPS.",
            "image_urls": ["https://example.com/image1.jpg"],
            "category": "Electronics"
        }
    ]
    
    # Import the vet_product function from the main orchestrator
    import importlib.util
    spec = importlib.util.spec_from_file_location("orchestrator", "dropship_orchestrator.py")
    orchestrator = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(orchestrator)
    
    approved_products = []
    for product in sample_products:
        vetted_product = orchestrator.vet_product(product, config)
        if vetted_product:
            approved_products.append(vetted_product)
    
    print(f"\n=== Testing Shopify Integration ===")
    if approved_products:
        for product in approved_products:
            create_shopify_product(product, config['platforms']['shopify'])
    
    print(f"\n=== Testing AliExpress Integration ===")
    aliexpress_products = fetch_aliexpress_products("fitness tracker", config['suppliers']['aliexpress'])
    if aliexpress_products:
        print(f"Found {len(aliexpress_products)} products from AliExpress.")
        for product in aliexpress_products[:2]:  # Test with first 2 products
            vetted_product = orchestrator.vet_product(product, config)
            if vetted_product:
                create_shopify_product(vetted_product, config['platforms']['shopify'])

if __name__ == "__main__":
    main()
