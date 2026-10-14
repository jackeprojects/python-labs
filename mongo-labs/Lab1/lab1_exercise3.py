from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]

# 3. Python: Print the name and price of every product, one per line
for product in db.products.find():
    print(product["name"], product["price"])