import uuid
import datetime
from models.post import Post
from database import Database

class Blog(object):
  def __init__(self, author, title, description, id=None):
    self.title = title
    self.description = description
    self.author = author
    self._id = uuid.uuid4().hex if id is None else id

  def new_post(self):
    title = input("Enter post title:")
    content = input("Enter post content:")
    date = input("Enter post date (in format DDMMYYYY), or leave it blank for today:")
    if date == "":
      date = datetime.datetime.utcnow()
    else:
      date = datetime.datetime.strptime(date, "%d%m%Y")

    post = Post(blog_id=self._id,
            author = self.author,
            title=title,
            content=content,
            date=date
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
    return cls(author=blog_data['author'],
                title=blog_data['title'],
                description=blog_data['description'],
                id=blog_data['_id'])