from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb+srv://tejapn42:teja1209@cluster0.vbcpmqk.mongodb.net/')
db = client['hospital_database']
collection = db['patients']

# Define query to find the patient to update
query = {"name": "John Doe"}

# Define new data to update
new_data = {"$set": {"diagnosis": "Pneumonia"}}

# Update one record
try:
    result = collection.update_one(query, new_data)
    print(result.modified_count, "document updated.")
except Exception as e:
    print("Error occurred:", e)
