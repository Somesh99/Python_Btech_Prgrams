import sqlite3
conn=sqlite3.connect('example.db')
c=conn.cursor()
#c.execute("CREATE TABLE login12 (name TEXT, password TEXT)")
#print ("table is created")
c.execute("select * from login12")
results=list(c.fetchall())
print(results)
conn.commit()
conn.close()
