from flask import Flask
app = Flask(__name__)
from pynetwork.views import inventory_v
from pynetwork.views import show_v
from pynetwork.views import config_v