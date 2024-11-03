from pymongo import MongoClient

# MongoDB setup
client = MongoClient('mongodb://localhost:27017/')  # Adjust the connection string as needed
db = client['bank_statements']  # Create/select a database
collection = db['statements']  # Create/select a collection

def save_in_database(data):
    # Save the valid data in MongoDB
    
    return collection.insert_many(data)

def find(inserted_id):
    # Save the valid data in MongoDB
    return collection.find({"id": inserted_id})  # Fetch the saved document

def getAll():
    return collection.find()
