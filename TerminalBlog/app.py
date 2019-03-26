from models.post import Post
import pymongo
__author__ = 'utumno86'


post = Post("Post 1 title", "post 1 content", "post 1 author")
post2 = Post("Post 2 title", "post 2 content", "post 2 author")

print(post.content)
print(post2.content)

