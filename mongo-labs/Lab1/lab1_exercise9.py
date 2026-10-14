from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]

# 9. Python: Print every customer as 'First Last (City)'
# Customers without a city should show (unknown)
for customer in db.customers.find():
    print(f"{customer['first_name']} {customer['last_name']} ({customer.get('city', 'unknown')})")