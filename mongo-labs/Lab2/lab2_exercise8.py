from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]

# 8. Raise the price of all Accessories by 20kr with $inc.
# Print Accessories
db.products.update_many({"category": "Accessories"}, {"$inc": {"price": 20}})

for product in db.products.find({"category": "Accessories"}):
    print(product)