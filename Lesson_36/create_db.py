import os
import sqlite3

db_filename = 'todo.db'
db_is_new = not os.path.exists(db_filename)
conn = sqlite3.connect(db_filename)
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS users(
    userid INT PRIMARY KEY,
    fname TEXT,
    lname TEXT,
    gender TEXT);
""")
cur.execute("""CREATE TABLE IF NOT EXISTS orders(
    orderid INT PRIMARY KEY,
    date DATE,
    userid TEXT,
    total TEXT);
""")
conn.commit()
conn.close()