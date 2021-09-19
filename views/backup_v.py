from pynetwork import app
from flask import request
from pynetwork.models.inventory_m import get_device_list
from pynetwork.controller.backup_c import *
from flask import send_file


@app.route('/inventory/backup/cisco/', methods=['POST'])
def backupCiscoConfig():
    """Backup selected device config"""
    payload = request.get_json()
    devices = get_device_list(payload)
    response = backup_cisco_config(devices)
    return {"response": response}


@app.route('/inventory/backup/cisco/', methods=['GET'])
def listCiscoBackup():
    """List all the Backuped config in the list"""
    response = list_cisco_backup()
    return {"response": response}


@app.route('/inventory/backup/cisco/', methods=['DELETE'])
def deleteCiscoBackup():
    """Delete the Backuped config in the list"""
    payload = request.get_json()["fileName"]
    response = delete_cisco_backup(payload)
    return {"response": response}


@app.route('/inventory/backup/cisco/export/', methods=['POST'])
def exportCiscoBackup():
    """Export the selected config files"""
    payload = request.get_json()
    print(payload)
    response = export_cisco_backup(payload)
    return response
