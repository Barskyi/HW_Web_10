from pymongo import MongoClient
import certifi


def get_mongodb():
    client = MongoClient(f"mongodb+srv://barskyi:olenkadodman69@barskyidb.hgjpvmn.mongodb.net",
                         tlsCAFile=certifi.where())

    db = client.HW_Web_10
    return db
