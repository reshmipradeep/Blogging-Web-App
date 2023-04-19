from pymongo import MongoClient

# Define the MongoDB URI
mongo_uri = "mongodb://rrrteam:cloud23@mongodb-service-name:27017"

# Create a MongoClient instance
client_no = MongoClient(mongo_uri)

# Get the blog database and posts collection
database = client_no.blog
posts = database.posts

# Define a list of posts to insert
recent_posts = [
    {"title": "Post 1", "author": "This is the content of post 1."},
    {"title": "Post 2", "author": "This is the content of post 2."},
    {"title": "Post 3", "author": "This is the content of post 3."}
]

# Insert the new posts into the posts collection
result_value = posts.insert_many(recent_posts)

# Print the inserted record IDs
print(f"Inserted {len(result_value.inserted_ids)} records with IDs: {result.inserted_ids}")
