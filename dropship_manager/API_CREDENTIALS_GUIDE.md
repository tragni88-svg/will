# Dropshipping API Credentials Guide

## Shopify API Credentials

### Step 1: Create a Shopify Partner Account
1. Go to https://partners.shopify.com/
2. Click "Join now" and create your account
3. Once approved, create a development store

### Step 2: Generate API Credentials
1. From your Shopify admin, go to Settings > Apps and sales channels
2. Click "Develop apps" > "Create an app"
3. Name your app "Dropship Manager"
4. Configure API scopes:
   - `read_products, write_products`
   - `read_orders, write_orders`
   - `read_customers, write_customers`
5. Click "Install app" and reveal your API credentials

### Required Credentials:
- **API Key**: Found in your app dashboard
- **API Secret**: Found in your app dashboard
- **Store URL**: Your store name (without .myshopify.com)

## Amazon MWS/SP-API Credentials

### Step 1: Create Amazon Seller Account
1. Go to https://sellercentral.amazon.com/
2. Create a Professional seller account ($39.99/month)
3. Complete identity verification

### Step 2: Register for SP-API
1. From Seller Central, go to Apps > Develop apps
2. Create new app with IAM role
3. Configure OAuth redirect URLs
4. Generate refresh token

### Required Credentials:
- **Seller ID**: Found in Seller Central > Settings > Account Info
- **MWS Auth Token**: Generated when authorizing your application

## eBay API Credentials

### Step 1: Create eBay Developer Account
1. Go to https://developer.ebay.com/
2. Click "Join" and create account
3. Create a new app in the Developer Dashboard

### Step 2: Generate Keys
1. Go to My Account > Application Keys
2. Create a new key set
3. Generate User Token with proper scopes

### Required Credentials:
- **App ID (Client ID)**: From your app dashboard
- **Cert ID (Client Secret)**: From your app dashboard
- **Dev ID**: Developer account ID
- **Auth Token**: User access token

## AliExpress API Credentials

### Step 1: Register for AliExpress Open Platform
1. Go to https://open.aliexpress.com/
2. Create developer account
3. Create new application

### Step 2: Configure Application
1. Set up OAuth redirect URLs
2. Configure API permissions
3. Generate App Key and Secret

### Required Credentials:
- **App Key**: From your application dashboard
- **App Secret**: From your application dashboard

## CJ Dropshipping API (Alternative Supplier)

### Step 1: Create CJ Account
1. Go to https://cjdropshipping.com/
2. Create business account
3. Complete verification

### Step 2: Get API Access
1. Contact CJ support for API access
2. Provide business verification documents
3. Receive API credentials

## Spocket API (Alternative Supplier)

### Step 1: Create Spocket Account
1. Go to https://spocket.co/
2. Create business account
3. Upgrade to paid plan for API access

### Step 2: Generate API Key
1. Go to Settings > API
2. Generate API key
3. Configure webhook endpoints

## Important Security Notes:

1. **Never share API credentials** in public repositories
2. **Use environment variables** for production deployments
3. **Rotate keys regularly** for security
4. **Monitor API usage** for unauthorized access
5. **Set up proper webhook endpoints** for order notifications

## Next Steps:

1. Choose your preferred suppliers (AliExpress + 1-2 alternatives)
2. Create accounts on all chosen platforms
3. Apply for API access (may take 1-7 business days)
4. Update config.json with real credentials
5. Test the integration with sample products

## Support Contacts:

- **Shopify**: https://help.shopify.com/en/api
- **Amazon**: https://developer.amazonservices.com/
- **eBay**: https://developer.ebay.com/support
- **AliExpress**: https://open.aliexpress.com/doc
- **CJ Dropshipping**: support@cjdropshipping.com
- **Spocket**: support@spocket.co