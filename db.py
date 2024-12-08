from pymongo import MongoClient

from pymongo.mongo_client import MongoClient
import pandas as pd
import json



uri="mongodb+srv://krishanu_patidar1:8ZmOETbXCoYAZDj1@cluster0.kmcznzi.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"



# Create a new client and connect to the server
client = MongoClient(uri)



# Accessing the 'ecommerce' database
db = client['ecommerce']

# Accessing the 'data' collection in the 'ecommerce' database
collection = db['data']

# Document to be inserted
document = {"name": "John Doe", "email": "john@example.com", "age": 30}

# Inserting the document into the collection
collection.insert_one(document)

print("Document inserted successfully!")
