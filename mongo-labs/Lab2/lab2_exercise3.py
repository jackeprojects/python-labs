from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]

# 3. Show customers who live in Stockholm or Malmö, use $in
for customer in db.customers.find({"city": {"$in": ["Stockholm", "Malmö"]}}):
    print(customer["first_name"], customer["last_name"], customer["city"])