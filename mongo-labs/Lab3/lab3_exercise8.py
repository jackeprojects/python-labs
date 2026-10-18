from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]

# 8. How many units of each category have been sold?
# Use $unwind and $lookup, skip cancelled orders
for doc in db.orders.aggregate([
    {"$match": {"status": {"$ne": "cancelled"}}},
    {"$unwind": "$items"},
    {"$lookup": {
        "from": "products",
        "localField": "items.product_id",
        "foreignField": "_id",
        "as": "product"
    }},
    {"$unwind": "$product"},
    {"$group": {"_id": "$product.category", "units_sold": {"$sum": "$items.quantity"}}}
]):
    print(f"{doc["_id"]}: {doc["units_sold"]} units sold")