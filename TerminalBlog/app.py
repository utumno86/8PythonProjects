import pymongo
from models.menu import Menu
from database import Database

Database.initialize()

menu = Menu()

menu.run_menu()



