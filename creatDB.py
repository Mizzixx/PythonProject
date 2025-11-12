import sqlite3

conn = sqlite3.connect('myTest.db')
db0bject = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS users (id integer PRIMARY KEY AUTOINCREMENT, username text, password text)""")


new_function = """INSERT INTO users (username, password) VALUES (?, ?)"""