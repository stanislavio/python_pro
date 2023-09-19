from pymongo import MongoClient


client = MongoClient('mongodb://localhost:27017/')

db = client.test

collection = db.mycollection


post = {"author": "John Doe",
        "text": "Hello, MongoDB!",
        "tags": ["mongodb", "python", "pymongo"]}

post_id = collection.insert_one(post).inserted_id

new_posts = [{"author": "Jane Doe",
              "text": "Another post!",
              "tags": ["bulk", "insert"]},
             {"author": "John Doe",
              "text": "Again, another post!",
              "tags": ["bulk", "insert"]}]

result = collection.insert_many(new_posts)


for post in collection.find():
    print(post)


for post in collection.find({"author": "John Doe"}):
    print(post)


collection.update_one({"author": "John Doe"},
                      {"$set": {"text": "Updated!"}})

collection.update_many({"author": "John Doe"},
                       {"$set": {"text": "Updated!"}})

collection.delete_one({"author": "John Doe"})

collection.delete_many({"author": "John Doe"})
