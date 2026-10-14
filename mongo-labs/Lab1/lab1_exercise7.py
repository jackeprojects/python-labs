from pymongo import MongoClient
from pprint import pprint

client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]

# 7. Python: Add yourself as a customer with insert_one, without an _id.
# Print the inserted_id. Then find yourself again with find_one and your email.
# Print yourself with pprint
result = db.customers.insert_one({
    "first_name": "Jacke",
    "last_name": "Jackesson",
    "email": "jacke@jacke.com"
})
print(result.inserted_id)

search_result = db.customers.find_one({"email": "jacke@jacke.com"})
pprint(search_result)