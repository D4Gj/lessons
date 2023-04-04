import sqlite3

con = sqlite3.connect('mydb.db')


def sql_update(con):
    cursorObj = con.cursor()
    cursorObj.execute('UPDATE employees SET name = "Vasya" WHERE id = 2')
    con.commit()


sql_update(con)
