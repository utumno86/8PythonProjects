import uuid
from typing import Dict
from dataclasses import dataclass, field
from models.item import Item
from models.model import Model

@dataclass(eq=False)
class Alert(Model):
  collection: str = field(init=False, default="alerts")
  item_id: str
  price_limit: float
  name: str = field(default="Test")
  _id: str = field(default_factory=lambda: uuid.uuid4().hex)

  def __post_init__(self):
    self.item = Item.get_by_id(self.item_id)

  def json(self) -> Dict:
    return {
      "_id": self._id,
      "price_limit": self.price_limit,
      "item_id": self.item_id,
      "name": self.name
    }

  def load_item_price(self):
    self.item.load_price()
    return self.item.price

  def notify_if_price_reached(self):
    if self.item.price < self.price_limit:
      print(f"Item {self.item} has reached a price under {self.price_limit}. Latest price: {self.item.price}.")