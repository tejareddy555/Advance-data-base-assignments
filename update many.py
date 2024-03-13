from pymongo import MongoClient



uri = "mongodb+srv://tejapn42:teja1209@cluster0.vbcpmqk.mongodb.net/"

# Connect to MongoDB Atlas
client = MongoClient(uri)
db = client['hospital_database']
collection = db['patients']

# Define query to find patients to update
query = {"age": {"$gt": 30}}  # Example: Update patients older than 30

# Define new data to update
new_data = {"$set": {"diagnosis": "High Blood Pressure"}}

# Update multiple records
try:
    result = collection.update_many(query, new_data)
    print(result.modified_count, "documents updated.")
except Exception as e:
    print("Error occurred:", e)
