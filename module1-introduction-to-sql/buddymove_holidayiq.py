import pandas as pd

df = pd.read_csv('buddymove_holidayiq.csv')
shape = df.shape
print("dataframe size=", shape)

import sqlite3

conn = sqlite3.connect('buddymove_holidayiq.sqlite3')
curs = conn.cursor()

#df.to_sql('review', con=conn)

#query = """SELECT * FROM review"""

#curs.execute(query).fetchall()

#How many total rows are there?
query2 = """SELECT COUNT(*)
FROM review;
"""

results1 = curs.execute(query2).fetchall()

print("Total number of rows=", results1)

query3= """
SELECT count(r.User Id)
FROM review as r
WHERE Nature >100 AND Shopping >100;
"""
results2 = curs.execute(query3).fetchall()

print("Number of users meeting condition=", results2)
