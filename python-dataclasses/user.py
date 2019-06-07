import uuid
from typing import Dict
from dataclasses import dataclass, field

@dataclass
class User:
  username: str
  password: str = field(repr=False, compare=False)
  _id: str = field(default_factory=lambda: uuid.uuid4().hex)
  country: str = field(default="United Kingdom")

  def json(self) -> Dict:
    return {
      "_id": self._id,
      "username": self.username
    }