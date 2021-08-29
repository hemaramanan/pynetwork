from pynetwork.models.inventory_m import *
from werkzeug.wrappers import response
from pynetwork.controller.inventory_c import *
from pynetwork import app
from flask import request


# Create the DB
@app.route('/admin/db', methods=['POST'])
def createdb():
    response = create_db()
    return{'Message': response}


# Add New device to the DB
@app.route('/inventory/devices/', methods=['POST'])
def addDevice():
    payload = request.get_json()
    response = add_device(payload)
    return {'message': response}

# Get all device from the DB


@app.route('/inventory/devices/', methods=['GET'])
def listDevice():
    response = list_devices()
    return {"devices": response}

# find multiple devices info from the DB


@app.route('/inventory/devices/find/', methods=['POST'])
def findDevice():
    payload = request.get_json()
    response = get_device_list(payload)
    return {"devices": response}

# Get one device


@app.route('/inventory/devices/device/', methods=['POST'])
def getDevice():
    payload = request.get_json()
    response = get_device(payload)
    return {"device": response}

# Update one device


@app.route('/inventory/devices/device/', methods=['PATCH'])
def updateDevice():
    payload = request.get_json()
    response = update_device(payload)
    return {"device": response}

# Delete one device


@app.route('/inventory/devices/device/', methods=['DELETE'])
def deleteDevice():
    payload = request.get_json()
    response = delete_device(payload)
    return {"message": response}
