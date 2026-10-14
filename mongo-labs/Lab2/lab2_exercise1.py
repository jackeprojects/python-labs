from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]

# 1. Show name and price of all products that cost more than 1000kr
for product in db.products.find({"price": {"$gt": 1000}}):
    print(product["name"], product["price"])