import requests
from bs4 import BeautifulSoup
from serpapi import GoogleSearch
import flask
from _init_ import app
import json
from newspaper import Article
import nltk
nltk.download('punkt')


def validate_query(query):
    if len(query) == 0 or query is None:
        return False
    return True
    

def search_query(query):
    search_parameters = {
        "q": query,
        "tbm": "nws",
        "api_key": "58bfb1bc053f52b6cdbd32fd0c926cbc0828c70e1a3ff52f9cfb1625bd512bd0"
    }

    search = GoogleSearch(search_parameters)
    search_results = search.get_dict()
    articles = search_results["news_results"]
    return articles


def parse_article(article):
    article_source = Article(article["link"])

    article_source.download()

    article_source.parse()

    article_source.nlp()

    article["keywords"] = article_source.keywords

    article["summary"] = article_source.summary

    article["text"] = article_source.text

    article["images"] = article_source.images

    article["movies"] = article_source.movies

    return article


def search(query):
    return search_query(query)



def inspect_all_articles(articles, network=None):
    limited = True if network is None else False
    full_articles = []
    for article in articles:
        if limited:
            if article["source"] == network:
                full_articles.append(parse_article(article))
        else:
            full_articles.append(parse_article(article))
    return full_articles

#driver
@app.route("/web_scraping/scraper", methods=["GET"])
def search_retriever(query, network=None):
    if validate_query(query) is False:
        flask.abort(404)
    all_articles = search(query)
    processed_articles = inspect_all_articles(all_articles, network)
    return flask.jsonify(json.dumps(processed_articles))