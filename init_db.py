import sqlite3

conn = sqlite3.connect('database.db')
print ("Opened database successfully")

conn.execute('CREATE TABLE FTD (Name TEXT, Age TEXT, Sex  TEXT, EROG1_score INTEGER,\
 EROG2_score INTEGER, EROG3_score INTEGER, VISPA_score INTEGER,\
  EROG1_time_Q1 DOUBLE,EROG1_time_Q2 DOUBLE,EROG1_time_Q3 DOUBLE,EROG1_time_Q4 DOUBLE,EROG1_time_Q5 DOUBLE,EROG1_time_Q6 DOUBLE,EROG1_time_Q7 DOUBLE, \
  EROG2_time_Q1 DOUBLE,EROG2_time_Q2 DOUBLE,EROG2_time_Q3 DOUBLE,EROG2_time_Q4 DOUBLE,EROG2_time_Q5 DOUBLE,EROG2_time_Q6 DOUBLE,EROG2_time_Q7 DOUBLE, \
  EROG3_time_Q1 DOUBLE,EROG3_time_Q2 DOUBLE,EROG3_time_Q3 DOUBLE,EROG3_time_Q4 DOUBLE,EROG3_time_Q5 DOUBLE,EROG3_time_Q6 DOUBLE,EROG3_time_Q7 DOUBLE, \
  VISPA_time_Q1 DOUBLE,VISPA_time_Q2 DOUBLE,VISPA_time_Q3 DOUBLE,VISPA_time_Q4 DOUBLE,VISPA_time_Q5 DOUBLE,VISPA_time_Q6 DOUBLE,VISPA_time_Q7 DOUBLE)')
print ("Table created successfully")
conn.close()