import os
import sqlite3

db_filename = 'myprogram.db'
db_is_new = not os.path.exists(db_filename)
schema_filename = 'dz_schema.sql'
# conn = sqlite3.connect(db_filename)
with sqlite3.connect(db_filename) as conn:
    if db_is_new:
        print('Создаём scheme bd')
        with open(schema_filename, 'rt') as f:
            schema = f.read()
        conn.executescript(schema)
        log = input('Login:')
        passw = input('Password:')
        conn.executescript(f"""
        insert into users (login, password)
        values ('{log}','{passw}');
        """)
    else:
        log = input('Login:')
        passw = input('Password:')
        conn.executescript(f"""
                insert into users (login, password)
                values ('{log}','{passw}');
                """)
        print('Данные успешон сохранены')
