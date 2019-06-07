import uuid
import re
from typing import Dict
from models.model import Model

class Store(Model):
    collection = "stores"

    def __init__(self, name: str, url_prefix: str, tag_name: str, query: Dict, _id: str = None):
      super().__init__()
      self.url_prefix = url_prefix
      self.tag_name = tag_name
      self.query = query
      self.price = None
      self.name = name
      self._id = _id or uuid.uuid4().hex

    def json(self) -> Dict:
      return {
        "_id": self._id,
        "url": self.url,
        "tag_name": self.tag_name,
        "query": self.query
      }

    @classmethod
    def get_by_name(cls, store_name: str) -> "Store":
      return cls.find_one_by("name", store_name)

    @classmethod
    def get_by_url_prefix(cls, url_prefix: str) -> "Store":
      return cls.find_one_by("url_prefix", url_prefix)

    @classmethod
    def find_by_url(cls, url: str) -> "Store":
      pattern = re.compile(r"(https?://.*?/)")
      match = pattern.search(url)
      url_prefix = match.group(1)
      return cls.get_by_url_prefix(url_prefix)