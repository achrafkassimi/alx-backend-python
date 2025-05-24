import sqlite3
import functools

def test():

    # Connect to a database (or create it if it doesn't exist)
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Create a table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    ''')

    # Insert values
    cursor.execute('''
        INSERT INTO users (name, email) VALUES (?, ?)
    ''', ("Alice", "alice@example.com"))

    cursor.execute('''
        INSERT INTO users (name, email) VALUES (?, ?)
    ''', ("Bob", "bob@example.com"))

    # Commit changes and close the connection
    conn.commit()
    conn.close()


# Decorator to log SQL queries
def log_queries(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        query = kwargs.get('query') or (args[0] if args else None)
        if query:
            print(f"[SQL LOG] Executing query: {query}")
        else:
            print("[SQL LOG] No query found in arguments.")
        return func(*args, **kwargs)
    return wrapper

@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results


test()
# Fetch users while logging the query
users = fetch_all_users(query="SELECT * FROM users")
