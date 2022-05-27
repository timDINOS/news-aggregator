import pymongo

client = pymongo.MongoClient()

db_user_profile = client['users']
collection_user_profile = db_user_profile['users']

