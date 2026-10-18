from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]

# 7. For each order, show the _id and the number of items in it.
# Use $project with $size
for doc in db.orders.aggregate([
    {"$project": {
        "_id": 1,
        "items": {"$size": "$items"}
    }}
]):
    print(f"Order {doc["_id"]}: {doc["items"]} items")