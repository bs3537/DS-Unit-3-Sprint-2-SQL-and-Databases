#In anaconda prompt, first do the following:
#conda create -n db-env python=3.7
#conda activate db-env
#pip install psycopg2 python-dotenv pandas



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

#Create titanic table:
query = """
CREATE TABLE titanic2 (
    id    SERIAL PRIMARY KEY,
    Survived VARCHAR(10) NOT NULL, 
    Pclass VARCHAR(10) NOT NULL, 
    Name VARCHAR(100) NOT NULL, 
    Sex VARCHAR(10) NOT NULL, 
    Age VARCHAR(10) NOT NULL, 
    Siblings VARCHAR(10) NOT NULL, 
    Parents VARCHAR(10) NOT NULL, 
    Fare VARCHAR(15) NOT NULL
);


"""
cur.execute(query)

query2 = """
\COPY titanic2 FROM 'titanic.csv' WITH FORMAT csv;;

"""

cur.execute(query2)

#query3 = """

#SELECT * FROM titanic2;

#"""
#cur.execute(query3)

### 
#results = cur.fetchall()

#print(results)

#commit the insert new rows query

conn.commit()