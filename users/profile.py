from re import L
import database
import flask
from _init_ import app
import json
from datetime import datetime


class userProfile:
    def _init_(self, inputName):
        profile_json = json.dumps(list(database.db_user_profile.find({"name": inputName})))
        profile = json.loads(profile_json)
        searches_json = json.dumps(list(database.db_user_searches.find({"name": inputName})))
        searches = json.loads(searches_json)
        articles_json = json.dumps(list(database.db_user_articles.find({"name": inputName})))
        articles = json.loads(articles_json)
        self.name = profile['name']
        self.email = profile['email']
        self.username = profile['username']
        self.password = profile['password']
        self.all_searches = searches['name']
        self.clicked_articles = articles['name']
        
    def get_name(self):
        return self.name

    def get_all_searches(self):
        return self.all_searches

    def get_most_recent_search(self):
        return self.all_searches[-1]
    
    def add_search_to_history(self, searchInput):
        database.db_user_searches.update({'name': self.name}, {'$push', {'searches.$', {'keywords': searchInput, 'date': str(datetime.now())}}})
        self.searches.append(searchInput)

    def delete_searches(self, num_of_searches):
        pass

    def get_all_articles(self): 
        return self.articles

    def get_most_recent_article(self):
        return self.articles[-1]

    def add_article_to_history(self):
        pass


    def delete_articles(self, num_of_articles):
        pass


@app.route("/users/profile/all_searches", methods=["GET"])
def get_all_searches_helper():
    return flask.session["user"].get_all_searches()


@app.route("/users/profile/most_recent_search", methods=["GET"])
def get_most_recent_search():
    return flask.session["user"].get_most_recent_search()

