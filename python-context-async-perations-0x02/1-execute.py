import sqlite3

class ExecuteQuery:
    def __init__(self, query, params=None, db_name='users.db'):
        self.query = query
        self.params = params or ()
        self.db_name = db_name
        self.conn = None
        self.results = None

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        cursor = self.conn.cursor()
        cursor.execute(self.query, self.params)
        self.results = cursor.fetchall()
        return self.results

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn:
            self.conn.close()

def test():

    # Connect to a database (or create it if it doesn't exist)
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Create a table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            age INTEGER NOT NULL
        )
    ''')

    # Insert values
    cursor.execute('''
        INSERT INTO users (name, email, age) VALUES (?, ?, ?)
    ''', ("Alice", "alice@example.com", 16))

    cursor.execute('''
        INSERT INTO users (name, email, age) VALUES (?, ?, ?)
    ''', ("Bob", "bob@example.com", 50))
    # Commit changes and close the connection
    conn.commit()
    conn.close()


# test()

# Usage example
with ExecuteQuery("SELECT * FROM users WHERE age > ?", (25,)) as results:
    for row in results:
        print(row)
