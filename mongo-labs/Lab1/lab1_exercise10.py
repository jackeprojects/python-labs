from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]

# 10. Challenge: Print every order as 'Order 1:2 items'
for order in db.orders.find():
    print(f"Order {order["_id"]}:{len(order["items"])} items")