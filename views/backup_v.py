from pynetwork import app
from flask import request
from pynetwork.models.inventory_m import get_device_list
from pynetwork.controller.backup_c import backup_cisco_config, list_cisco_backup, delete_cisco_backup


# Backup selected device config
@app.route('/inventory/backup/cisco/', methods=['POST'])
def backupCiscoConfig():
    payload = request.get_json()
    devices = get_device_list(payload)
    response = backup_cisco_config(devices)
    return {"response": response}


# List all the Backuped config in the list

@app.route('/inventory/backup/cisco/', methods=['GET'])
def listCiscoBackup():
    response = list_cisco_backup()
    return {"response": response}


# Delete the Backuped config in the list

@app.route('/inventory/backup/cisco/', methods=['DELETE'])
def deleteCiscoBackup():
    payload = request.get_json()["fileName"]
    response = delete_cisco_backup(payload)
    return {"response": response}
