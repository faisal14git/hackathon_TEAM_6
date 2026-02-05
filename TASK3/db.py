import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(os.getenv("MONGO_URI"))
db = client.newsdb
collection = db.articles

def save_article(article):
    collection.insert_one(article)
