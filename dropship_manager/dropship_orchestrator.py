import json
import math
import requests

def load_config(config_path='config.json'):
    """Loads the master configuration file."""
    with open(config_path, 'r') as f:
        return json.load(f)

def vet_product(product, config, platform: str = 'shopify'):
    """Vets a product against financial and supplier quality rules for a specific platform."""
    # Supplier quality checks
    supplier_rating = product.get('supplier_rating', 0)
    shipping_time = product.get('shipping_time_days', 999)
    min_rating = config['suppliers']['aliexpress']['min_supplier_rating']
    max_shipping = config['suppliers']['aliexpress']['max_shipping_days']

    if supplier_rating < min_rating:
        print(f"[REJECTED] {product['title']}: Supplier rating {supplier_rating}% is below the {min_rating}% threshold.")
        return None
    if shipping_time > max_shipping:
        print(f"[REJECTED] {product['title']}: Shipping time of {shipping_time} days exceeds the {max_shipping}-day limit.")
        return None

    # Financial viability checks
    cost_of_goods = product['cost_of_goods']
    shipping_cost = product['shipping_cost']
    min_profit = config['financials']['min_profit_margin_usd']
    platform_fee_pct = config['financials']['platform_fees_percentage'][platform]
    ad_spend_pct = config['financials']['ad_spend_percentage']

    # Formula to determine the final selling price
    # It calculates the price needed to cover all costs and fees while ensuring the minimum profit.
    required_price = (cost_of_goods + shipping_cost + min_profit) / (1 - (platform_fee_pct / 100) - (ad_spend_pct / 100))
    
    # Apply psychological pricing (round up to the nearest dollar, then subtract 1 cent)
    selling_price = math.ceil(required_price) - 0.01

    # Final verification of profit
    net_revenue = selling_price * (1 - (platform_fee_pct / 100) - (ad_spend_pct / 100))
    profit = net_revenue - cost_of_goods - shipping_cost

    if profit < min_profit:
        print(f"[REJECTED] {product['title']}: Cannot meet the ${min_profit:.2f} profit margin. Calculated profit: ${profit:.2f}")
        return None

    print(f"[APPROVED] {product['title']}: Selling Price: ${selling_price:.2f} | Est. Profit: ${profit:.2f}")
    product['selling_price'] = selling_price
    return product

def search_aliexpress_products(query: str, config: dict):
    """Searches for products on AliExpress using a third-party API."""
    api_key = config.get('suppliers', {}).get('aliexpress', {}).get('rapidapi_key')
    if not api_key or api_key == "YOUR_RAPIDAPI_KEY":
        print("[WARNING] AliExpress API key not configured. Skipping live product search.")
        return []

    url = "https://aliexpress-api2.p.rapidapi.com/search"
    querystring = {"SearchText": query}
    headers = {
        "x-rapidapi-host": "aliexpress-api2.p.rapidapi.com",
        "x-rapidapi-key": api_key
    }

    try:
        response = requests.get(url, headers=headers, params=querystring)
        response.raise_for_status()  # Raise an exception for bad status codes
        data = response.json()
        
        products = []
        if 'body' in data and 'products' in data['body']:
            for item in data['body']['products']:
                # Extracting price is complex due to different formats, this is a simplified approach
                price_str = item.get('price', {}).get('current', '0').replace('$', '').replace(',', '')
                try:
                    price = float(price_str)
                except ValueError:
                    price = 0.0

                product = {
                    "title": item.get('title', 'No Title'),
                    "cost_of_goods": price,
                    "shipping_cost": 5.00,  # Placeholder, shipping API would be separate
                    "supplier_rating": 95, # Placeholder, not available in this API
                    "shipping_time_days": 15, # Placeholder
                    "source_url": item.get('url', '')
                }
                products.append(product)
        print(f"[INFO] Found {len(products)} products on AliExpress for query: '{query}'")
        return products
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Failed to fetch products from AliExpress: {e}")
        return []


if __name__ == '__main__':
    config = load_config()
    print("--- Dropship Orchestrator Initialized ---")
    print(f"Enforcing Minimum Profit Margin: ${config['financials']['min_profit_margin_usd']:.2f}")

    # --- Live Product Sourcing ---
    print("\n--- Sourcing Products from AliExpress ---")
    # You can change this query to find different types of products
    search_query = "smartwatch"
    live_products = search_aliexpress_products(search_query, config)

    if not live_products:
        print("[INFO] No live products to vet. Exiting.")
    else:
        # --- Multi-Platform Vetting ---
        platforms = ['shopify', 'amazon', 'ebay']
        for platform in platforms:
            print(f"\n--- Vetting Products for {platform.upper()} ---")
            # Use a fresh copy of live_products for each platform
            products_to_vet = [p.copy() for p in live_products]
            approved_products = [p for p in (vet_product(p, config, platform=platform) for p in products_to_vet) if p is not None]
            print(f"--- {platform.upper()} Vetting Complete ---")
            print(f"{len(approved_products)} of {len(products_to_vet)} products approved for listing on {platform.upper()}.")
