from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb+srv://tejapn42:teja1209@cluster0.vbcpmqk.mongodb.net/')
db = client['hospital_database']
collection = db['patients']

# Define query to find the patient to delete
query = {"name": "John Doe"}

# Delete one record
try:
    result = collection.delete_one(query)
    print(result.deleted_count, "document deleted.")
except Exception as e:
    print("Error occurred:", e)
