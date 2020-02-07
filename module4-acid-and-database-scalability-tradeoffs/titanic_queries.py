

import psycopg2

import os

from dotenv import load_dotenv

load_dotenv() #looks inside .env file for environmental variables


#passes environmental variable values

DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")





### Connect to ElephantSQL-hosted PostgreSQL

##Environmental variables hide the secret credentials> create .env file with credentials
conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                        password=DB_PASSWORD, host=DB_HOST)
### A "cursor", a structure to iterate over db records to perform queries
cur = conn.cursor()

#How many passengers survived?
query= """
SELECT COUNT(survived) FROM titanic2
WHERE survived=1
"""
#How many passengers died?
query= """
SELECT COUNT(survived) FROM titanic2
WHERE survived=0
"""

#How many passengers were in each class?

query = """
SELECT COUNT(pclass) FROM titanic2
GROUP BY pclass
"""
#How many passengers survived in each class?
#Number of survived
query = """
SELECT pclass, SUM(survived) FROM titanic2
GROUP BY pclass
"""

#What was the average age of survivers vs. non-survivers?
#Survivers
query = """
SELECT
	AVG (age) as average_age
FROM titanic2
WHERE survived = 1
"""
#28.41 years

#Non survivers
query = """
SELECT
	AVG (age) as average_age
FROM titanic2
WHERE survived = 0
"""
#30.15 years

#Average age in each passenger class?
query =
"""
SELECT
	AVG (age) as average_age,
	pclass
FROM titanic2
GROUP BY pclass
ORDER BY pclass
"""
#What was the average fare by passenger class?
query =
"""
SELECT
	pclass,
	Avg(fare)
FROM titanic2
GROUP BY pclass
ORDER BY pclass
"""

#What was the average fare by survival?

query =
"""
SELECT
	survived,
	Avg(fare)
FROM titanic2
GROUP BY survived
ORDER BY survived DESC
"""

#How many siblings/spouses aboard on average?
query = 

"""
SELECT
	Avg(siblings)
FROM titanic2
"""

#How many siblings/spouses aboard on average by passenger class?

query = 
"""

SELECT
	pclass,
	Avg(siblings)
FROM titanic2
GROUP BY pclass
ORDER BY pclass 
"""

#How many siblings/spouses aboard on average by survival?

query =
"""
SELECT
	survived,
	Avg(siblings)
FROM titanic2
GROUP BY survived
ORDER BY survived DESC
"""

#How many parents/children aboard on average by passenger class?
query =
"""
SELECT
	pclass,
	Avg(parents) as average_parents_children
FROM titanic2
GROUP BY pclass
ORDER BY pclass 
"""

#How many parents/children aboard on average by survival?

query = 
"""
SELECT
	survived,
	Avg(parents)
FROM titanic2
GROUP BY survived
ORDER BY survived DESC
"""

#Do any passengers have same name?

query = 
"""
SELECT
	name
FROM titanic2
GROUP BY name 
HAVING COUNT(*) > 1
"""

cur.execute(query)
























