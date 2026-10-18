from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]

# 4. How many customers live in each city? Use $group, biggest city first
for doc in db.customers.aggregate([
    {"$group": {"_id": "$city", "customers": {"$sum": 1}}},  # step 1
    {"$sort": {"customers": -1}},
]):
    print(f"{doc["_id"]}: {doc["customers"]}")