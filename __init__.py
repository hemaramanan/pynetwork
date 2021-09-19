from flask import Flask
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config["CONFIG_FOLDER"] = "/data/backup_config/"
from pynetwork.views import inventory_v
from pynetwork.views import show_v
from pynetwork.views import config_v
from pynetwork.views import backup_v