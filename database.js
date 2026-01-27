const sqlite3 = require('sqlite3').verbose();
const bcrypt = require('bcrypt');

const db = new sqlite3.Database('./database.sqlite', (err) => {
  if (err) {
    console.error('Error opening database:', err.message);
  } else {
    console.log('Connected to the SQLite database.');
    initDb();
  }
});

function initDb() {
  db.serialize(() => {
    // Users table
    db.run(`CREATE TABLE IF NOT EXISTS users (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      email TEXT UNIQUE NOT NULL,
      password_hash TEXT NOT NULL,
      credits INTEGER DEFAULT 0,
      created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )`);

    // Transactions table (for audit)
    db.run(`CREATE TABLE IF NOT EXISTS transactions (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      user_id INTEGER,
      amount INTEGER,
      type TEXT, -- 'purchase', 'usage'
      stripe_session_id TEXT,
      created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
      FOREIGN KEY(user_id) REFERENCES users(id)
    )`);
  });
}

const Database = {
  createUser: (email, password) => {
    return new Promise(async (resolve, reject) => {
      try {
        const hash = await bcrypt.hash(password, 10);
        db.run('INSERT INTO users (email, password_hash) VALUES (?, ?)', [email, hash], function(err) {
          if (err) return reject(err);
          resolve({ id: this.lastID, email, credits: 0 });
        });
      } catch (e) {
        reject(e);
      }
    });
  },

  getUserByEmail: (email) => {
    return new Promise((resolve, reject) => {
      db.get('SELECT * FROM users WHERE email = ?', [email], (err, row) => {
        if (err) return reject(err);
        resolve(row);
      });
    });
  },

  getUserById: (id) => {
    return new Promise((resolve, reject) => {
      db.get('SELECT id, email, credits FROM users WHERE id = ?', [id], (err, row) => {
        if (err) return reject(err);
        resolve(row);
      });
    });
  },

  addCredits: (userId, amount, stripeSessionId = null) => {
    return new Promise((resolve, reject) => {
      db.serialize(() => {
        db.run('UPDATE users SET credits = credits + ? WHERE id = ?', [amount, userId], (err) => {
          if (err) return reject(err);
        });
        db.run('INSERT INTO transactions (user_id, amount, type, stripe_session_id) VALUES (?, ?, ?, ?)', 
          [userId, amount, 'purchase', stripeSessionId], (err) => {
            if (err) return reject(err);
            resolve(true);
        });
      });
    });
  },

  deductCredits: (userId, amount) => {
    return new Promise((resolve, reject) => {
      db.get('SELECT credits FROM users WHERE id = ?', [userId], (err, row) => {
        if (err) return reject(err);
        if (!row || row.credits < amount) return reject(new Error('Insufficient credits'));
        
        db.run('UPDATE users SET credits = credits - ? WHERE id = ?', [amount, userId], (err) => {
          if (err) return reject(err);
          resolve(row.credits - amount);
        });
      });
    });
  }
};

module.exports = Database;
