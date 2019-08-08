import uuid
from dataclasses import dataclass, field
from typing import Dict, List

from models.model import Model
import models.user.errors as UserErrors
from common.database import Database
from common.utils import Utils

@dataclass
class User(Model):
  collection: str = field(init=False, default='users')
  email: str
  password: str
  _id: str = field(default_factory=lambda: uuid.uuid4().hex)

  @classmethod
  def find_by_email(cls, email: str) -> "User":
    try:
      return cls.find_one_by('email', email)
    except TypeError:
      raise UserErrors.UserNotFoundError('A user with this email was not found.')

  @classmethod
  def register_user(cls, email: str, password: str) -> bool:
    if not Utils.email_is_valid(email):
      raise UserErrors.InvalidEmailError('The email does not have the right format')

    try:
      cls.find_by_email(email)
      raise UserErrors.UserAlreadyRegisteredError('The email you used to register already exists in the database')
    except UserErrors.UserNotFoundError:
      User(email, password).save_to_mongo()

  def json(self) -> Dict:
    return {
      '_id': self._id,
      'email': self.email,
      'password': self.password
    }
