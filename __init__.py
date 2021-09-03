from flask_cors import CORS, cross_origin
from flask import Flask
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
from pynetwork.views import inventory_v
from pynetwork.views import show_v
from pynetwork.views import config_v
from pynetwork.views import backup_v





