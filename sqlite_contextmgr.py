# sqlite_contextmgr.py
import sqlite3

# Define the context manager class
class SQLiteDB:
    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = None

    def __enter__(self):
        # Open a connection to the SQLite database
        self.conn = sqlite3.connect(self.db_path)
        return self.conn

    def __exit__(self, exc_type, exc_value, traceback):
        # Close the connection to the SQLite database
        if self.conn:
            self.conn.close()

# Usage example
if __name__ == "__main__":
    db_path = 'example.db'

    # Use the context manager to open the SQLite database
    with SQLiteDB(db_path) as conn:
        cursor = conn.cursor()

        # Perform database operations
        cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)''')
        cursor.execute('''INSERT INTO users (name) VALUES (?)''', ('Alice',))
        cursor.execute('''INSERT INTO users (name) VALUES (?)''', ('Bob',))

        # Retrieve data from the database
        cursor.execute('''SELECT * FROM users''')
        rows = cursor.fetchall()
        for row in rows:
            print(row)
