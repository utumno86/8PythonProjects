class User(object):
  def __init__(self, email, password):
    self.email = email
    self.password = password

  def get_by_email(self):
    data = Database.find_one("users", {"email": self.email})

  def get_by_id(self):
    pass

  def login_valid(self):
    pass

  def register(self):
    pass

  def login(self):
    pass

  def get_blogs(self):
    pass