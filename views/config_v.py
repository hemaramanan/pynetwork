from pynetwork import app
from flask import request
from pynetwork.models.inventory_m import get_device_list
from pynetwork.controller.config_c import config_cisco_cli


# Add New device to the DB
@app.route('/inventory/config/cisco/', methods=['POST'])
def ConfigCiscoCli():
    payload = request.get_json()
    commands = payload["commands"]
    devices = get_device_list(payload)
    response = config_cisco_cli(devices, commands)
    return {"response": response}
