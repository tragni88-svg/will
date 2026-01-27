# app.paid.ai - AI as a Service (Monetization Ready)

A complete Pay-per-use AI platform with Authentication, Database, and Stripe Payments.

## Features
- **User Accounts:** Email/Password registration and login.
- **Persistent Credits:** Credits stored in SQLite database.
- **Secure Payments:** Stripe Checkout integration linked to user accounts.
- **Pay-per-use:** Credits deducted per API call.

## 💰 How to Monetize (Go Live)

To start accepting real money, follow these steps:

1.  **Stripe Account:**
    *   Go to [Stripe.com](https://stripe.com) and create an account.
    *   Activate "Payments".

2.  **Get Live Keys:**
    *   In Stripe Dashboard -> Developers -> API Keys.
    *   Copy `Publishable key` (pk_live_...) and `Secret key` (sk_live_...).

3.  **Deploy the App:**
    *   Use a hosting provider like **Render**, **Railway**, or **Heroku**.
    *   Connect your GitHub repository.
    *   Set the Build Command: `npm install`
    *   Set the Start Command: `node server.js`

4.  **Configure Environment Variables (in Hosting Dashboard):**
    *   `STRIPE_SECRET_KEY`: Your sk_live_... key.
    *   `JWT_SECRET`: A long random string (e.g. generated via `openssl rand -hex 32`).
    *   `FRONTEND_URL`: Your deployed URL (e.g. `https://my-app.onrender.com`).

5.  **Setup Webhooks (Critical for Credit Delivery):**
    *   In Stripe Dashboard -> Developers -> Webhooks.
    *   Add Endpoint: `https://your-app.onrender.com/webhook`
    *   Select Event: `checkout.session.completed`
    *   Copy the `Signing secret` (whsec_...) and add it to your Environment Variables as `STRIPE_WEBHOOK_SECRET`.

6.  **Update Frontend:**
    *   In `index.html`, replace `STRIPE_PUBLISHABLE_KEY` with your `pk_live_...` key.

## Local Development

1.  **Install:**
    ```bash
    npm install
    ```

2.  **Run:**
    ```bash
    node server.js
    ```
    Open [http://localhost:3000](http://localhost:3000).

3.  **Test Payments:**
    *   Use Stripe Test Cards (4242 4242 4242 4242).
    *   Use the `stripe-cli` to forward webhooks locally if testing credit updates:
        `stripe listen --forward-to localhost:3000/webhook`

## Tech Stack
- **Frontend:** React, Tailwind CSS
- **Backend:** Node.js, Express
- **Database:** SQLite (File-based)
- **Auth:** JWT (JSON Web Tokens)
