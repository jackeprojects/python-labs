from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]

# 4. Python: How many customers live in Uppsala? Use count_documents
print(db.customers.count_documents({"city": "Uppsala"}))