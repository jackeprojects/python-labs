from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]

# 5. Which products have the tag sport? Show name and tags, without _id
for product in db.products.find({"tags": "sport"}, {"name": 1, "tags": 1, "_id": 0}):
    print(product)