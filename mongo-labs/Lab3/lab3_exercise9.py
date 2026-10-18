from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]

# 9. Revenue per status: for each status, the total quantity times unit_price
for doc in db.orders.aggregate([
    {"$unwind": "$items"},
    {"$group": {"_id": "$status",
     "revenue": {"$sum": {"$multiply": ["$items.quantity", "$items.unit_price"]}}}}
]):
    print(f"{doc['_id']}: {doc['revenue']}")