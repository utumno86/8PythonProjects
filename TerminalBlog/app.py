__author__ = 'utumno86'

import pymongo

uri = "mongodb://127.0.0.1:27017"
client = pymongo.MongoClient(uri)
database = client["fullstack"]
collection = database["posts"]

students = [student for student in collection.find({})]
print(students)