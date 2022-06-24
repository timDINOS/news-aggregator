import pymongo

client = pymongo.MongoClient()

db_user_profile = client['users']
collection_user_profile = db_user_profile['users']

db_user_searches = client['searches']
collection_user_searches = db_user_searches['searches']

db_user_articles = client['articles']
collection_user_articles = db_user_articles['articles']