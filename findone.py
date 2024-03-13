from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb+srv://tejapn42:teja1209@cluster0.vbcpmqk.mongodb.net/')
db = client['hospital_database']
collection = db['patients']

# Define a query to find one patient record
query = {"name": "John Doe"}

# Find one record
try:
    result = collection.find_one(query)
    if result:
        print("Found patient:")
        print(result)
    else:
        print("Patient not found.")
except Exception as e:
    print("Error occurred:", e)
