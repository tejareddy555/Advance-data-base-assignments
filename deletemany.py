
from pymongo import MongoClient

# Connect to MongoDB Atlas
client = MongoClient('mongodb+srv://tejapn42:teja1209@cluster0.vbcpmqk.mongodb.net/hospital_database')
db = client['hospital_database']
collection = db['patients']

# Define query to find patients to delete
query = {"age": {"$gt": 30}}  # Example: Delete patients older than 30

# Delete multiple records
try:
    result = collection.delete_many(query)
    print(result.deleted_count, "documents deleted.")
except Exception as e:
    print("Error occurred during deletion:", e)
