from flask import Flask
app = Flask(__name__)

from pynetwork.views import inventory_v
# from pynetwork.controller import inventory_c
