from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]

# 6. Show the 5 cheapest products, cheapest first. Only name and price
for product in db.products.find({}, {"name": 1, "price": 1, "_id": 0}).sort("price", 1).limit(5):
    print(product)