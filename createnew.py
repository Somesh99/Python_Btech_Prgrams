import sqlite3

#Connecting to sqlite
conn = sqlite3.connect('example.db')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Doping EMPLOYEE table if already exists.
cursor.execute("DROP TABLE IF EXISTS ITEM1")
#cursor.execute("DESCRIBE login12")
#Creating table as per requirement
'''sql =CREATE TABLE EMPLOYEE(
   FIRST_NAME CHAR(20) NOT NULL,
   LAST_NAME CHAR(20),
   AGE INT,
   SEX CHAR(1),
   INCOME FLOAT
)
cursor.execute(sql)
'''
#print("Table created successfully........")
#pragma table_info([login12])
cursor.execute("PRAGMA table_info(login12)")
print (cursor.fetchall())

# Commit your changes in the database
conn.commit()

#Closing the connection
conn.close()
