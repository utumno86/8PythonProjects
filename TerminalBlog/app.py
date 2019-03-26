__author__ = 'utumno86'

from models.post import Post
import pymongo

uri = "mongodb://127.0.0.1:27017"
client = pymongo.MongoClient(uri)

post = Post("Post 1 title", "post 1 content", "post 1 author")
post2 = Post("Post 2 title", "post 2 content", "post 2 author")

print(post.content)
print(post2.content)

