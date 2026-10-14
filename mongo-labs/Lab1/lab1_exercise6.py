from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]

# 6. Python: Print the first name of every customer who gets the newsletter
for customer in db.customers.find({"newsletter": True}):
    print(customer["first_name"])