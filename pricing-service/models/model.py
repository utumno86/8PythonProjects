from abc import ABCMeta, abstractmethod
from typing import Dict, List
from common.database import Database

class Model(metaclass=ABCMeta):
  collection = "models"

  def __init__(self, *args, **kwargs):
    pass

  @abstractmethod
  def json(self):
    raise NotImplementedError

  @classmethod
  def all(cls) -> List:
    elements_from_db = Database.find(cls.collection, {})
    return [cls(**element) for element in elements_from_db]
