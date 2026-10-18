from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]

# 5. What is the cheapest and the most expensive product in each category?
# Use $min and $max
for doc in db.products.aggregate([
    {"$sort": {"price": 1}},
    {"$group": {"_id": "$category",
                "cheapest_name": {"$first": "$name"},
                "most_expensive_name": {"$last": "$name"},
                "cheapest": {"$min": "$price"},
                "most_expensive": {"$max": "$price"}}}
]):
    print(f"""{doc["_id"].upper()}
{doc["most_expensive_name"]}: {doc["most_expensive"]}
{doc["cheapest_name"]}: {doc["cheapest"]}\n""")