from flask import render_template, request, Blueprint
from models.alert import Alert
from models.store import Store
from models.item import Item

alert_blueprint = Blueprint('alerts', __name__)

@alert_blueprint.route('/')
def index():
  alerts = Alert.all()
  return render_template('alerts/index.html', alerts=alerts)

@alert_blueprint.route('/new', methods=['GET', 'POST'])
def new_alert():
  if request.method == 'POST':
    item_url = request.form['item_url']
    price_limit = request.form['price_limit']

    store = Store.find_by_url(item_url)
    item = Item(item_url, store.tag_name, store.query)
    item.save_to_mongo()

    Alert(item._id, item.price_limit).save_to_mongo()

  return render_template('alerts/new_alert.html')