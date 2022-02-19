import sqlite3
conn=sqlite3.connect('example.db')
c=conn.cursor()
c.execute('create table acc(id real,bal real,irate real)')
list1=[(100,1000,4),
       (101,1000,4),
       (102,1000,4),
       (103,1000,4),
       (104,1000,4),
       (105,1000,4),
       (106,1000,4),
       (107,1000,4),
       (108,1000,4),
       (109,1000,4)]
c.executemany('INSERT INTO acc VALUES (?,?,?)',list1)
conn.commit()
acc=int(input('enter valid acc number'))
import sqlite3
conn=sqlite3.connect('example.db')
c=conn.cursor()
for r in c.execute("select * from acc where id='acc'"):
    print(r)
