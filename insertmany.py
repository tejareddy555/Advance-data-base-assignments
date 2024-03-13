from pymongo import MongoClient
import datetime

# Connect to MongoDB
client = MongoClient('mongodb+srv://tejapn42:teja1209@cluster0.vbcpmqk.mongodb.net/')
db = client['hospital_database']
collection = db['patients']

# Define patient data
patients_data = [
    {
        "name": "John Doe",
        "age": 35,
        "admission_date": datetime.datetime.now(),
        "diagnosis": "Flu"
    },
    {
        "name": "Jane Smith",
        "age": 28,
        "admission_date": datetime.datetime.now(),
        "diagnosis": "Broken leg"
    }
]

# Insert many records
try:
    result = collection.insert_many(patients_data)
    print("Inserted patient IDs:", result.inserted_ids)
except Exception as e:
    print("Error occurred:", e)
