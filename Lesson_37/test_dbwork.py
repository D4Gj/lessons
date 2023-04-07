import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()
cursor.execute("""Create table if not exists students(name text, lastname text,course text)""")
# cursor.execute("""INSERT into students(name,lastname,course) values ('Иван', 'Иванов', 'Python')""")
# user = ('Сергей', 'Иванов', 'C#')
# cursor.execute('Insert into students VALUES(?,?,?)', user)
# users = [('Сергей', 'Иванов', 'C++'), ('Иван', 'Иванов', 'C++')]
# cursor.executemany('Insert into students values(?,?,?)', users)
# conn.commit()

cursor.execute("Select * from students")

# print(cursor.fetchone())
# print(cursor.fetchmany(2))
print(cursor.fetchall())
conn.close()
