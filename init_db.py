import sqlite3

conn = sqlite3.connect('database.db')
print ("Opened database successfully")

conn.execute('CREATE TABLE FTD (Name TEXT, Age TEXT, Sex  TEXT, EROG1_score INTEGER,\
 EROG2_score INTEGER, EROG3_score INTEGER, VISPA_score INTEGER, EROG1_time DOUBLE, \
 EROG2_time DOUBLE, EROG3_time DOUBLE,VISPA_time DOUBLE)')
print ("Table created successfully")
conn.close()