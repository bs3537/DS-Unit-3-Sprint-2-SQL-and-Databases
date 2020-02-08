
import sqlite3

conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()

#Ten most expensive items by unit price in the database?

query= 

"""

SELECT ProductName, UnitPrice FROM Product
ORDER BY UnitPrice DESC
LIMIT 10;

"""

results1 = curs.execute(query).fetchall()

results1

#The most expensive item is Cote de Blaye (Unit price 263.50 from the output)

#Average age of an employee at the time of hire?

query2 = 
"""
SELECT AVG(HireDate - BirthDate)
FROM Employee
"""
results2 = curs.execute(query2).fetchall()

results2
#The answer is 37.22 years.


#What are ten most expensive items in the database and their suppliers?

query3 = 

"""
SELECT a.ProductName, a.UnitPrice, a.SupplierId, b.CompanyName
FROM Product as a
LEFT JOIN Supplier b ON b.Id = a.SupplierId
ORDER BY a.UnitPrice DESC
LIMIT 10;
"""

results3 = curs.execute(query3).fetchall()

results3

#The most expensive item is Cote de Blaye (Unit price 263.50 from the output) with supplied ID 18 or Aux joyeux...

#What is the largest category (by the number of unique products in it)?

query4 = 

"""
SELECT CategoryName
FROM Product
INNER JOIN Category
ON Product.CategoryId = Category.Id
GROUP BY CategoryId
ORDER BY COUNT(DISTINCT Product.Id) DESC
LIMIT 1;

"""
#The answer for above is confections.

results4 = curs.execute(query4).fetchall()

results4

cur.close()





