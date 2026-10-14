from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]

# 7. Which orders contain product 2?
for order in db.orders.find({"items.product_id": 2}):
    print(order)