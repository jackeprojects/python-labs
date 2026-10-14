from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]

# 2. Show orders that aren't delivered. Print _id and status
for order in db.orders.find({"status": {"$ne": "delivered"}}):
    print(order["_id"], order["status"])