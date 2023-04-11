import os
import sqlite3

db_filename = 'myprogram.db'
db_is_new = not os.path.exists(db_filename)
schema_filename = 'dz_schema.sql'
# conn = sqlite3.connect(db_filename)
with sqlite3.connect(db_filename) as conn:
    cursor = conn.cursor()
    if db_is_new:
        print('Создаём scheme bd')
        with open(schema_filename, 'rt') as f:
            schema = f.read()
        conn.executescript(schema)
        log = input('Login:')
        passw = input('Password:')
        cursor.execute(f"Select login from users where login='{log}'")
        data = cursor.fetchall()
        print(data, len(data))
        if passw.isdigit() and len(data) == 0:
            conn.executescript(f"""
                    insert into users (login, password)
                    values ('{log}','{passw}');
                    """)
            print('Данные успешно сохранены')
        else:
            print('Пароль должен быть только из чисел. Либо пользователь уже существует')

    else:
        log = input('Login:')
        passw = input('Password:')
        cursor.execute(f"Select * from users where login='{log}'")
        data = cursor.fetchall()
        print(data, len(data))
        if passw.isdigit() and len(data) == 0:
            conn.executescript(f"""
                    insert into users (login, password)
                    values ('{log}','{passw}');
                    """)
            print('Данные успешон сохранены')
        else:
            print('Пароль должен быть только из чисел. Либо пользователь уже существует')
