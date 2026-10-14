from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]

# 1. Print the name of every product in the Accessories category
for product in db.products.find({"category": "Accessories"}):
    print(product["name"])