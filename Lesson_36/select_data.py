import sqlite3

con = sqlite3.connect('mydb.db')


def sql_select_all_empl(con):
    cursorObj = con.cursor()
    data = cursorObj.execute('SELECT * from employees')
    con.commit()
    print(data.description)


sql_select_all_empl(con)
