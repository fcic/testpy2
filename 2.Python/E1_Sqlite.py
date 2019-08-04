import sqlite3

conn =sqlite3.connect('test.db')
# conn.cursor().execute('create table fcictest(id int,name text)')
conn.cursor().execute('''insert into fcictest values(1,'fcic')''')
# conn.cursor().execute('select * from fcictest')
conn.commit()
conn.close()