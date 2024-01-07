import json
import certifi
from bson.objectid import ObjectId
from mystery_password import PASSWORD, NAME
from pymongo import MongoClient

client = MongoClient(f"mongodb+srv://{NAME}:{PASSWORD}@barskyidb.hgjpvmn.mongodb.net", tlsCAFile=certifi.where())

db = client.HW_Web_10

with open("quotes.json", "r", encoding="utf-8") as fd:
    quotes = json.load(fd)

for quote in quotes:
    author = db.authors.find_one({"fullname": quote["author"]})
    if author:
        db.quotes.insert_one({
            "quote": quote["quote"],
            "tags": quote["tags"],
            "author": ObjectId(author["_id"])
        })