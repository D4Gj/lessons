import sqlite3

con = sqlite3.connect('mydb.db')


def sql_insert(con, entities):
    cursorObj = con.cursor()

    cursorObj.execute('INSERT INTO employees(id,name,salary,departament,position,hireDate) VALUES(?,?,?,?,?,?)',
                      entities)

    con.commit()


data = (2, 'Andrew', 800, 'IT', 'Backend', '2023-03-03')
sql_insert(con, data)
