import sqlite3

con = sqlite3.connect('mydb.db')


def sql_fetch(con):
    cursorObj = con.cursor()
    data = cursorObj.execute('SELECT name,position,salary FROM employees')
    print(data)
    # rows = cursorObj.fetchall()
    # print(rows)
    # for row in rows:
    #     print(row)
    [print(row) for row in cursorObj.fetchall()]


def sql_fetch_salary(con):
    cursorObj = con.cursor()
    data = cursorObj.execute('SELECT name,position,salary FROM employees WHERE salary > 100')
    print(data)
    # rows = cursorObj.fetchall()
    # print(rows)
    # for row in rows:
    #     print(row)
    [print(row) for row in cursorObj.fetchall()]
    print(cursorObj.execute('SELECT name,position,salary FROM employees').rowcount)
    rows = cursorObj.execute('SELECT name,position,salary FROM employees WHERE salary > 100').fetchall()
    print(len(rows))


def sql_delete(con):
    cursorObj = con.cursor()
    print(cursorObj.execute('DELETE FROM employees').rowcount)
    con.commit()


def sql_fetch_tables(con):
    cursorObj = con.cursor()
    cursorObj.execute('SELECT name from sqlite_master where type = "table"')

    print(cursorObj.fetchall())


def sql_new_table(con):
    cursorObj = con.cursor()
    cursorObj.execute('CREATE TABLE if not exists projects(id integer, name text)')

    con.commit()


def sql_drop(con):
    cursorObj = con.cursor()
    cursorObj.execute('drop table if exists projects')
    con.commit()


def sql_check_exist(con):
    cursorObj = con.cursor()
    cursorObj.execute('SELECT name from sqlite_master Where type="table" and name="projects"')

    print(cursorObj.fetchall())


# sql_drop(con)
# sql_fetch_new_table(con)
# sql_delete(con)
# sql_fetch(con)
# sql_fetch_salary(con)
sql_check_exist(con)
sql_fetch_tables(con)
