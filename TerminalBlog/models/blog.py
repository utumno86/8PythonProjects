import uuid
from models.post import Post

class Blog(object):
  def __init__(self, author, title, description, id=None):
    self.title = title
    self.description = description
    self.author = author
    self.id = uuid.uuid4().hex if id is None else id

  def new_post(self):
    title = input("Enter post title:")
    content = input("Enter post content:")
    date = input("Enter post date, or leave it blank for today:")
    post = Post(blog_id=self.id,
            author = self.author,
            title=title,
            content=content,
            date=date)

  def get_posts(self):
    pass

  def save_to_mongo(self):
    pass

  def json(self):
    pass

  def get_from_mongo(self):
    pass