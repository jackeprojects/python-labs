from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]

# 5. Python: Find the product named Sandals with find_one and print stock
product = db.products.find_one({"name": "Sandals"})
print(product["stock"])