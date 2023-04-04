# https://sqlitebrowser.org/dl/
import os
import sqlite3

db_filename = 'todo.db'
db_is_new = not os.path.exists(db_filename)
conn = sqlite3.connect(db_filename)
if db_is_new:
    print('Создана новая база данных')
else:
    print('Уже существует')

conn.close()