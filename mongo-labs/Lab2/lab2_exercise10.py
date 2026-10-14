from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]

# 10. Challenge: delete all orders with status 'new' placed before 2026-03-20
# Count them first
print(db.orders.count_documents({"status": "new", "order_date": {"$lt": datetime(2026, 3, 20)}}))
db.orders.delete_many({"status": "new", "order_date": {"$lt": datetime(2026, 3, 20)}})