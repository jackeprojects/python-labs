from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]

# 4. Which products are white? Use dot notation
for product in db.products.find({"details.color": "white"}):
    print(product["name"], product["details"]["color"])