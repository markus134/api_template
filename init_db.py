import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS messages (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   content TEXT
                )''')

# Insert some initial messages
cursor.execute("INSERT INTO messages (content) VALUES (?)", ("Hello, world!",))
cursor.execute("INSERT INTO messages (content) VALUES (?)", ("Welcome to the chat!",))
cursor.execute("INSERT INTO messages (content) VALUES (?)", ("This is a test message.",))

conn.commit()
conn.close()
