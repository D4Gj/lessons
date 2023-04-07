import sqlite3

con = sqlite3.connect('mydb.db')
cursorObj = con.cursor()

cursorObj.execute('create table if not exists projects(id time, name text)')

data = [(1, 'Pyqtcalc'), (2, 'db_selector'), (3, 'myide')]

cursorObj.executemany("Insert into projects values(?,?)", data)

con.commit()

con.close()