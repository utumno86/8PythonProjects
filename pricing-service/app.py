# from flask import Flask
# from learning import learning_blueprint
from models.alert import Alert

alert = Alert("2b16b22529e74c92b3d263e5cb29ccd3", 2000)
alert.save_to_mongo()

# app = Flask(__name__)

# app.register_blueprint(learning_blueprint)

# if __name__ == '__main__':
#   app.run()
