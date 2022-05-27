import database
import flask





def insert_into_db(new_user):
    database.collection_user_profile.insert_one(new_user)