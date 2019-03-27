from models.post import Post
from database import Database
import pymongo

__author__ = 'utumno86'

Database.initialize()

posts = Post.from_blog('123')

for post in posts:
  print(post)


