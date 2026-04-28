import sqlite3
import bcrypt
from datetime import datetime


##### Beshary & Abdelkader #####

# Database connection
DB_PATH = "atm_system.db"

def hash_password(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed

def check_password(password, hashed):
    # Ensure the stored hash is bytes (sqlite may return str or memoryview)
    if isinstance(hashed, str):
        hashed = hashed.encode('utf-8')
    if isinstance(hashed, memoryview):
        hashed = bytes(hashed)
    return bcrypt.checkpw(password.encode(), hashed)

def initialize_database():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Create Account Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Account (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE, 
        password BLOB NOT NULL,
        email TEXT NOT NULL,
        phone TEXT,
        national_id TEXT,
        balance REAL DEFAULT 0,
        currency_type TEXT DEFAULT 'EGP'
    )
    """)
    
    # Create Transactions Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        type TEXT NOT NULL,
        date TEXT NOT NULL,
        amount REAL NOT NULL,
        state TEXT NOT NULL,
        sender INTEGER,
        recipient INTEGER,
        FOREIGN KEY(sender) REFERENCES Account(id),
        FOREIGN KEY(recipient) REFERENCES Account(id)
    )
    """)

    # Check if currency_type column exists in Account table, if not add it
    cursor.execute("PRAGMA table_info(Account)")
    columns = [column[1] for column in cursor.fetchall()]
    if 'currency_type' not in columns:
        cursor.execute("ALTER TABLE Account ADD COLUMN currency_type TEXT DEFAULT 'EGP'")

    #create Donations Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Donations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        donor_id INTEGER,
        organization TEXT,
        amount REAL,
        date TEXT,
        currency_type TEXT DEFAULT 'EGP',
        FOREIGN KEY(donor_id) REFERENCES Account(id)
    )
    """)

     # Create Currency Table 
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Currency (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE,
        conversion_rate_to_egp REAL NOT NULL
    )
    """)
    
    # Check if Currency table is empty and insert default currencies
    cursor.execute("SELECT COUNT(*) FROM Currency")
    currency_count = cursor.fetchone()[0]
    
    if currency_count == 0:
        # Insert default currencies with their conversion rates to EGP
        default_currencies = [
            ('EGP', 1.0),      # Egyptian Pound (base currency)
            ('USD', 48.5),     # US Dollar
            ('EUR', 53.2),     # Euro
            ('GBP', 62.1),     # British Pound
            ('SAR', 12.9),     # Saudi Riyal
            ('AED', 13.2),     # UAE Dirham
            ('KWD', 159.8),    # Kuwaiti Dinar
            ('QAR', 13.3),     # Qatari Riyal
            ('JOD', 68.4),     # Jordanian Dinar
        ]
        
        cursor.executemany("""
            INSERT INTO Currency (name, conversion_rate_to_egp) VALUES (?, ?)
        """, default_currencies)
    
    conn.commit()
    conn.close()

##### Beshary & Abdelkader #####