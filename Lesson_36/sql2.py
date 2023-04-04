import os
import sqlite3

db_filename = 'todo.db'
db_is_new = not os.path.exists(db_filename)
schema_filename = 'todo_schema.sql'
conn = sqlite3.connect(db_filename)
with sqlite3.connect(db_filename) as conn:
    if db_is_new:
        print('Создаём scheme bd')
        with open(schema_filename, 'rt') as f:
            schema = f.read()
        conn.executescript(schema)
        print('Передаём начальные данные')
        conn.executescript("""
        insert into project (name, description, deadline)
        values ('pymotw', 'Python module of the week','2022-11-02');
        insert into task (details, status, deadline, project)
        values('info about SELECT','done','2022-04-29', 'pymotw');
        insert into task (details, status, deadline, project)
        values('sqlite3 history telling','active','2023-04-04', 'pymotw');
        """)
    else:
        print('Database exists, assume schema does too')

