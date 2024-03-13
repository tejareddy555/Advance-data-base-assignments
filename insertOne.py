from pymongo import MongoClient
import datetime

# Connect to MongoDB
client = MongoClient('mongodb+srv://tejapn42:teja1209@cluster0.vbcpmqk.mongodb.net/')
db = client['hospital_database']
collection = db['patients']

# Define patient data
patient_data = {
    "name": "John Doe",
    "age": 35,
    "admission_date": datetime.datetime.now(),
    "diagnosis": "Flu"
}

# Insert one record
result = collection.insert_one(patient_data)
print("Inserted patient ID:", result.inserted_id)
