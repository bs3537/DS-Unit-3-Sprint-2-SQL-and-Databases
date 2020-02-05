#anaconda prompt
#move to folder with file
##conda create -n db-env python=3.7
#conda activate db-env
#pip install pymongo[srv]
import pymongo
#connect to client
client = pymongo.MongoClient("mongodb+srv://user:password@cluster0-4d5yc.mongodb.net/test?retryWrites=true&w=majority")

#Create an insert entry in rpg database (also creates the rpg database)
db = client.rpg

#specify name of the collection in database whre entry to be made (also creates the collection)
collection = db.characters

#enter details of new entry in the collection
collection.insert_one({
    "id": 1,
    "name": "Aliquid iste optio reiciendi",
    "level": 0,
    "experience": 0,
    "hp": 10,
    "strength": 1,
    "intelligence": 1,
    "dextrity": 1,
    "wisdom": 1
})

#second character entry
collection.insert_one({
    "id": 2,
    "name": "Optio dolorem ex a",
    "level": 0,
    "experience": 0,
    "hp": 10,
    "strength": 1,
    "intelligence": 1,
    "dextrity": 1,
    "wisdom": 1
})

#Create new collection=armory item in rpg database
collection = db.armory_item

#insert new entry in armory item collection in rpg database
collection.insert_one({
    "id": 1,
    "name": "Libero facere dolore, as",
    "value": 0,
    "weight": 0,   
})

#Working with MongoDB is easier than PostgreSQL. 
#It is easier to visualize the information in MongoDB's document format rather than PostgreSQL where the data is scattered across various tables.

