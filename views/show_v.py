from pynetwork import app
from flask import request
from pynetwork.models.inventory_m import get_device_list
from pynetwork.controller.show_c import show_cisco_cli


# Add New device to the DB
@app.route('/inventory/show/cisco/', methods=['POST'])
def showCiscoCli():
    payload = request.get_json()
    commands = payload["commands"]
    devices = get_device_list(payload)
    response = show_cisco_cli(devices, commands)
    return {"response": response}
