from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]

# 9. Add the tag "new" to Rain Jacket without creating duplicates.
# Give it a field "restock_date" with today's date, use datetime.now
db.products.update_one(
    {"name": "Rain Jacket"},
    {"$addToSet": {"tags": "new"},
    "$set": {"restock_date": datetime.now()}})
print(db.products.find_one({"name": "Rain Jacket"}))