import sqlite3
from sqlite3 import Error


def sql_conn():
    try:
        con = sqlite3.connect('mydb.db')
        print(con.total_changes)
        return con
    except Error:
        print(Error)


def sql_table(con):
    cursorObj = con.cursor()
    cursorObj.execute("CREATE TABLE employees(id integer PRIMARY KEY, name text, salary real, departament text, "
                      "position text, hireDate date)")
    con.commit()

con = sql_conn()
sql_table(con)