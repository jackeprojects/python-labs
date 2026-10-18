from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]

# 6. How many orders does each customer have (all statuses)?
# Show only customers with 2 or more orders
for doc in db.orders.aggregate([
    {"$group": {"_id": "$customer_id",
     "orders": {"$sum" : 1}}},
     {"$match": {"orders": {"$gte": 2}}}
]):
    print(f"Customer {doc["_id"]}: {doc["orders"]} orders")