import sqlite3
from hashlib import sha256

# Function to create the database and users table
def initialize_database():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# Function to register a new user
def register_user(username, email, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    hashed_password = sha256(password.encode()).hexdigest()  # Hash the password for security
    try:
        cursor.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", (username, email, hashed_password))
        conn.commit()
        conn.close()
        return True, "Registration successful!"
    except sqlite3.IntegrityError:
        conn.close()
        return False, "Username or email already exists."

# Function to validate login credentials
def login_user(username, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    hashed_password = sha256(password.encode()).hexdigest()
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, hashed_password))
    user = cursor.fetchone()

    conn.close()

    if user:
        return True, "Login successful!"
    return False, "Invalid username or password."