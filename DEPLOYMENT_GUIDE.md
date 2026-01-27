# app.paid.ai - Deployment Guide

## Quick Deployment Options

### Option 1: Deploy to Netlify (Fastest - 2 minutes)

1. **Sign up for Netlify** (free): https://www.netlify.com/
2. **Drag and drop** the `app.paid.ai.html` file into Netlify's drop zone
3. **Get your live URL** instantly (e.g., `your-site-name.netlify.app`)
4. **Optional**: Set up custom domain at `app.paid.ai`

### Option 2: Deploy to Vercel (Fast - 3 minutes)

1. **Sign up for Vercel** (free): https://vercel.com/
2. Install Vercel CLI: `npm install -g vercel`
3. Run in the directory: `vercel`
4. Follow prompts to deploy
5. Get instant live URL

### Option 3: Deploy to GitHub Pages (Free)

1. Create a new GitHub repository
2. Upload `app.paid.ai.html` and rename to `index.html`
3. Go to Settings → Pages
4. Select main branch as source
5. Your site will be live at `username.github.io/repo-name`

### Option 4: Deploy to Cloudflare Pages (Fast & Free)

1. Sign up at https://pages.cloudflare.com/
2. Connect your GitHub repository or upload files
3. Deploy with one click
4. Free SSL, CDN, and custom domain support

## Setting Up Stripe Payments

### Step 1: Create Stripe Account
1. Go to https://stripe.com/
2. Sign up for an account
3. Complete verification

### Step 2: Get API Keys
1. Go to Stripe Dashboard → Developers → API Keys
2. Copy your **Publishable Key** (starts with `pk_live_...` for production)
3. Keep your **Secret Key** safe (starts with `sk_live_...`)

### Step 3: Update the App
Replace line 109 in `app.paid.ai.html`:
```javascript
const stripe = Stripe('pk_live_YOUR_ACTUAL_PUBLISHABLE_KEY');
```

### Step 4: Set Up Backend for Payments

You need a backend to handle Stripe checkout. Here are options:

#### A. Use Netlify Functions (Recommended for beginners)
- Already included in the deployment files
- Serverless, no server management needed
- Scales automatically

#### B. Use Vercel Serverless Functions
- Similar to Netlify
- Great performance
- Easy setup

#### C. Deploy Node.js Backend
- Full control
- Can use services like Railway, Render, or Fly.io
- See `server.js` in deployment files

## Environment Variables

Set these in your hosting platform:

```
STRIPE_SECRET_KEY=sk_live_your_secret_key_here
STRIPE_PUBLISHABLE_KEY=pk_live_your_publishable_key_here
```

## Custom Domain Setup

### For app.paid.ai:

1. **Buy domain** at Namecheap, GoDaddy, or Cloudflare
2. **Add DNS records** in your domain registrar:
   - For Netlify: CNAME record pointing to your Netlify URL
   - For Vercel: CNAME record pointing to `cname.vercel-dns.com`
   - For Cloudflare Pages: Follow their nameserver instructions

3. **Configure in hosting platform**:
   - Add custom domain in platform settings
   - Wait for SSL certificate (automatic, ~5 minutes)

## Testing Before Going Live

1. **Test with Stripe Test Mode**:
   - Use test key: `pk_test_...`
   - Test card: `4242 4242 4242 4242`
   - Any future expiry date and CVC

2. **Verify all features work**:
   - Credit purchases
   - AI chat functionality
   - Credit persistence

3. **Switch to production keys** when ready

## Recommended: Complete Production Setup

For a fully functional production app, I've included:
- `server.js` - Node.js backend for Stripe
- `netlify.toml` - Netlify configuration
- `vercel.json` - Vercel configuration
- Serverless function for payment processing

## Security Checklist

- ✅ Never expose Stripe secret key in frontend
- ✅ Use HTTPS (automatic with Netlify/Vercel)
- ✅ Validate payments server-side
- ✅ Set up webhook for payment confirmations
- ✅ Test thoroughly in test mode first

## Need Help?

- Stripe Docs: https://stripe.com/docs
- Netlify Docs: https://docs.netlify.com/
- Vercel Docs: https://vercel.com/docs

## Estimated Timeline

- **Basic deployment**: 5 minutes
- **Custom domain**: 15 minutes
- **Stripe setup**: 30 minutes
- **Full production setup**: 2 hours

Choose the deployment option that fits your needs. Start with Option 1 (Netlify) for the fastest path to live!
