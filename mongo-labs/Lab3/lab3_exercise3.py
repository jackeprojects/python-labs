from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]

# 3. Create a collection newsletter_signups with validation:
# email is required and must be a string, and source can only be "web" or "store" (look up enum)
# Insert one valid and one invalid document

db.create_collection("newsletter_signups", validator={"$jsonSchema": {
    "required" : ["email"],
    "properties": {
        "email": {"bsonType": "string"},
        "source": {"bsonType": "string", "enum": ["web", "store"]}
    }
}})

db.newsletter_signups.insert_one({"email": "test@test.com", "source": "web"})
db.newsletter_signups.insert_one({"email": "test@test.com", "source": "online"})