import sqlite3
import datetime

con = sqlite3.connect('mydb.db')
cursorObj = con.cursor()

cursorObj.execute('create table if not exists assignments(id time, name text,date date)')

data = [(1, 'Pyqtcalc', datetime.date(2020, 1, 2)), (2, 'db_selector', datetime.datetime(2022, 1, 2, 10, 20, 30)), (3,
                                                                                                                    'myide',
                                                                                                                    datetime.date(
                                                                                                                        2022,
                                                                                                                        12,
                                                                                                                        12))]

cursorObj.executemany("Insert into assignments values(?,?,?)", data)

con.commit()

con.close()
