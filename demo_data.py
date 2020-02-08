
import sqlite3

conn = sqlite3.connect('demo_data.sqlite3')
curs = conn.cursor()

query = 

"""CREATE TABLE demo (
    id    SERIAL PRIMARY KEY,
    s VARCHAR(10) NOT NULL, 
    x INTEGER, 
    y INTEGER 
 );

 """
 curs.execute(query)

query = """INSERT INTO demo (s, x, y)
VALUES ('g', 3, 9)
"""
curs.execute(query)
conn.commit()

query = """

INSERT INTO demo (s, x, y)
VALUES ('v', 5, 7)
"""

curs.execute(query)
conn.commit()

query = """

INSERT INTO demo (s, x, y)
VALUES ('f', 8, 7)

"""

conn.commit()

#Number of rows?

query1 = """

SELECT COUNT(*) FROM demo;

"""
results1 = curs.execute(query1).fetchall()

results1

#How many rows have both x and y at least 5?

query2 = """

SELECT COUNT (*) FROM demo
WHERE x >  4 
AND y > 4;

"""
results2 = curs.execute(query2).fetchall()

results2

query3 = 

"""

SELECT COUNT (DISTINCT y) FROM demo;

"""

results3 = curs.execute(query3).fetchall()

results3



