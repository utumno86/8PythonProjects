from typing import Dict
import pymongo

class Database(object):
  URI = "mongodb://127.0.0.1:27017/pricing"
  DATABASE = pymongo.MongoClient(URI).get_database()

  # @staticmethod
  # def initialize():
  #   pass

  @staticmethod
  def insert(collection: str, data: Dict):
    Database.DATABASE[collection].insert(data)

  @staticmethod
  def find(collection: str, query: Dict) -> pymongo.cursor:
    return Database.DATABASE[collection].find(query)

  # @staticmethod
  # def find_one(collection, query):
  #   return Database.DATABASE[collection].find_one(query)
