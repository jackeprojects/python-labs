from pymongo import MongoClient
from pprint import pprint

client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]

# 8. Python: Add 2 products with insert_many with _id's 13 and 14, include tags
# Print how many products there are
result = db.products.insert_many([
    {"_id": 13, "name": "Gloves Red", "category": "Accessories", "price": 59, "stock": 10,
     "tags": ["winter", "leather"], "details": {"color": "red", "material": "leather"}},
    {"_id": 14, "name": "Gloves Blue", "category": "Accessories", "price": 59, "stock": 10,
     "tags": ["winter", "leather"], "details": {"color": "blue", "material": "leather"}}
])
print(db.products.count_documents({}))