import uuid
import datetime
from models.post import Post
from common.database import Database

class Blog(object):
  def __init__(self, author, title, description, _id=None):
    self.title = title
    self.description = description
    self.author = author
    self._id = uuid.uuid4().hex if _id is None else _id

  def new_post(self, title, content, date=datetime.datetime.utcnow()):
    post = Post(blog_id=self._id,
            author = self.author,
            title=title,
            content=content,
            created_date=date
    )
    post.save_to_mongo()

  def get_posts(self):
    return Post.from_blog(self._id)

  def save_to_mongo(self):
    Database.insert(collection='blogs', data=self.json())

  def json(self):
    return {
      '_id': self._id,
      'author': self.author,
      'description': self.description,
      'title': self.title
    }

  @classmethod
  def from_mongo(cls, id):
    blog_data = Database.find_one(collection='blogs', query={'_id': id})
    return cls(**blog_data)