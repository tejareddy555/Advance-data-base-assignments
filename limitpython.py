from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import datetime

uri = "mongodb+srv://tejapn42:teja1209@cluster0.vbcpmqk.mongodb.net/"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

try:
    # Send a ping to confirm a successful connection
    client.admin.command('ping')

    # Get reference to 'sample_training' database
    db = client.sample_training

    # Get reference to 'zips' collection
    accounts_collection = db.zips

    new = [
    {
       "$group":{
       "_id":"$state",
	   "total_pop":{"$sum":"$pop"}
	}
    },
    {
    "$match":{
    "total_pop":{"$lt":1000000}}
    }
    ]

    result = list(accounts_collection.aggregate(new))

    if result:
        print(result)
    else:
        print("No documents in the collection")


except Exception as e:
    print(e)
finally:
    client.close()