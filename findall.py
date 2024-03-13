from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb+srv://tejapn42:teja1209@cluster0.vbcpmqk.mongodb.net/')
db = client['hospital_database']
collection = db['patients']

# Find all records
try:
    cursor = collection.find({})
    print("All patients:")
    for patient in cursor:
        print(patient)
except Exception as e:
    print("Error occurred:", e)
