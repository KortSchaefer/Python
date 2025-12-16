# original code
'''import sqlite3
from getpass import getpass

def login():
    conn = sqlite3.connect("app.db")
    cur = conn.cursor()

    username = input("Username: ")
    password = getpass("Password: ")

    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    print("DEBUG SQL:", query)  # left in by a developer

    cur.execute(query)
    row = cur.fetchone()

    if row:
        print("Login successful!")
    else:
        print("Invalid username or password.")

    conn.close()

if __name__ == "__main__":
    login()'''

# Fixed code
import sqlite3
from getpass import getpass
import base64, hashlib, hmac, os

# Secure password hashing using PBKDF2 with SHA-256
def hash_password(password: str) -> str:
    salt = os.urandom(16)
    dk = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 200_000)
    return base64.b64encode(salt + dk).decode()
# Verify password against stored hash
def verify_password(password: str, stored: str) -> bool:
    data = base64.b64decode(stored.encode())
    salt, dk = data[:16], data[16:]
    new_dk = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 200_000)
    return hmac.compare_digest(dk, new_dk)
# Original Login function
def login():
    conn = sqlite3.connect("app.db")
    cur = conn.cursor()

    username = input("Username: ")
    password = getpass("Password: ")

    # Use parameterized queries to prevent SQL injection
    query = "SELECT password FROM users WHERE username = ?"
    cur.execute(query, (username,))
    row = cur.fetchone()
    # Remove debug print statement

    if row and verify_password(password, row[0]):
        print("Login successful!")
    else:
        print("Invalid username or password.")

    conn.close()

if __name__ == "__main__":
    login()