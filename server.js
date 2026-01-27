require('dotenv').config();
const express = require('express');
const cors = require('cors');
const stripe = require('stripe')(process.env.STRIPE_SECRET_KEY);
const jwt = require('jsonwebtoken');
const bcrypt = require('bcrypt');
const db = require('./database');

const app = express();
const JWT_SECRET = process.env.JWT_SECRET || 'your-secret-key-change-in-prod';

// Middleware
app.use(cors());

// Webhook must be before express.json() to get raw body
app.post('/webhook', express.raw({ type: 'application/json' }), async (req, res) => {
  const sig = req.headers['stripe-signature'];
  let event;

  try {
    event = stripe.webhooks.constructEvent(req.body, sig, process.env.STRIPE_WEBHOOK_SECRET);
  } catch (err) {
    console.error(`Webhook Error: ${err.message}`);
    return res.status(400).send(`Webhook Error: ${err.message}`);
  }

  // Handle the event
  if (event.type === 'checkout.session.completed') {
    const session = event.data.object;
    const userId = session.client_reference_id;
    const credits = parseInt(session.metadata.credits);

    if (userId && credits) {
      try {
        await db.addCredits(userId, credits, session.id);
        console.log(`Added ${credits} credits to user ${userId}`);
      } catch (err) {
        console.error('Database error in webhook:', err);
      }
    }
  }

  res.json({ received: true });
});

app.use(express.json());
app.use(express.static('.'));

// Auth Middleware
function authenticateToken(req, res, next) {
  const authHeader = req.headers['authorization'];
  const token = authHeader && authHeader.split(' ')[1];
  if (!token) return res.sendStatus(401);

  jwt.verify(token, JWT_SECRET, (err, user) => {
    if (err) return res.sendStatus(403);
    req.user = user;
    next();
  });
}

// Routes

// Register
app.post('/auth/register', async (req, res) => {
  try {
    const { email, password } = req.body;
    if (!email || !password) return res.status(400).json({ error: 'Email and password required' });
    
    const user = await db.createUser(email, password);
    const token = jwt.sign({ id: user.id, email: user.email }, JWT_SECRET);
    res.json({ token, user: { id: user.id, email: user.email, credits: user.credits } });
  } catch (err) {
    if (err.message.includes('UNIQUE constraint failed')) {
      return res.status(400).json({ error: 'Email already exists' });
    }
    res.status(500).json({ error: 'Server error' });
  }
});

// Login
app.post('/auth/login', async (req, res) => {
  try {
    const { email, password } = req.body;
    const user = await db.getUserByEmail(email);
    
    if (!user || !(await bcrypt.compare(password, user.password_hash))) {
      return res.status(401).json({ error: 'Invalid credentials' });
    }

    const token = jwt.sign({ id: user.id, email: user.email }, JWT_SECRET);
    res.json({ token, user: { id: user.id, email: user.email, credits: user.credits } });
  } catch (err) {
    res.status(500).json({ error: 'Server error' });
  }
});

// Get Current User (Credits)
app.get('/auth/me', authenticateToken, async (req, res) => {
  try {
    const user = await db.getUserById(req.user.id);
    if (!user) return res.sendStatus(404);
    res.json(user);
  } catch (err) {
    res.sendStatus(500);
  }
});

// Create Checkout Session
app.post('/create-checkout-session', authenticateToken, async (req, res) => {
  try {
    const { credits, price } = req.body;
    const userId = req.user.id;

    if (!credits || !price || credits <= 0 || price <= 0) {
      return res.status(400).json({ error: 'Invalid credits or price parameters.' });
    }

    const frontendUrl = process.env.FRONTEND_URL || req.headers.origin || 'http://localhost:3000';

    const session = await stripe.checkout.sessions.create({
      payment_method_types: ['card'],
      client_reference_id: userId.toString(), // Important for matching in webhook
      line_items: [
        {
          price_data: {
            currency: 'usd',
            product_data: {
              name: `${credits} AI Credits`,
              description: `Purchase ${credits} credits for app.paid.ai`,
            },
            unit_amount: Math.round(price * 100),
          },
          quantity: 1,
        },
      ],
      mode: 'payment',
      success_url: `${frontendUrl}?success=true`,
      cancel_url: `${frontendUrl}?canceled=true`,
      metadata: {
        credits: credits.toString(),
      },
    });

    res.json({ sessionId: session.id, url: session.url });
  } catch (error) {
    console.error('Stripe Error:', error);
    res.status(500).json({ error: error.message });
  }
});

// Chat Endpoint (Consumes Credits)
app.post('/api/chat', authenticateToken, async (req, res) => {
  try {
    const { message } = req.body;
    const userId = req.user.id;

    // Deduct 1 credit
    const newBalance = await db.deductCredits(userId, 1);

    // Simulate AI response
    // In production, call Anthropic/OpenAI here
    await new Promise(r => setTimeout(r, 1000));
    const response = `AI Response to: "${message}". (Remaining Credits: ${newBalance})`;

    res.json({ response, credits: newBalance });
  } catch (err) {
    if (err.message === 'Insufficient credits') {
      return res.status(402).json({ error: 'Insufficient credits' });
    }
    res.status(500).json({ error: 'Server error' });
  }
});

// Health check
app.get('/health', (req, res) => {
  res.json({ status: 'ok' });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
