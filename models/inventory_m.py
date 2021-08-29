from re import template
from flask.sessions import NullSession

from werkzeug.wrappers import response
from pynetwork import app
from flask_sqlalchemy import SQLAlchemy
from pynetwork.controller.inventory_c import get_model_as_dict
from sqlalchemy.orm import aliased, query


app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite://///home/dev/pynetwork/pynetwork/data/pynetwork.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Define the Datamodel
class Device(db.Model):
    host = db.Column(db.Text, primary_key=True)
    username = db.Column(db.Text, nullable=False)
    password = db.Column(db.Text, nullable=False)
    port = db.Column(db.Integer, default=22)
    # credential_template = db.Column(db.Text)

# Create the Database


def create_db():
    db.create_all()
    return("Database Created")


# Add New device to the DB
def add_device(deviceDic):
    device_obj = Device(**deviceDic)
    db.session.add(device_obj)
    db.session.commit()
    return("Device Added to Pynetwork")

# Retrive list of device from DB


def list_devices():
    all_device_obj = Device.query.all()
    all_device_list = list()
    for device_obj in all_device_obj:
        all_device_list.append(get_model_as_dict(device_obj))
    return all_device_list

# Get one Device from variable


def get_device(deviceDic):
    find_hostname = deviceDic["host"]
    record = Device.query.filter_by(host=find_hostname).first_or_404(
        description='device - {} does not not exist'.format(find_hostname))
    response = get_model_as_dict(record)
    return (response)

# Update one Device variables/ Properties


def update_device(deviceDic):
    find_hostname = deviceDic["host"]
    record = Device.query.filter_by(host=find_hostname).first_or_404(
        description='device - {} does not not exist '.format(find_hostname))
    record.username = deviceDic["username"]
    record.password = deviceDic["password"]
    record.port = deviceDic["port"]
    # record.credential_template = deviceDic["credential_template"]
    response = get_model_as_dict(record)
    db.session.commit()
    return (response)

# Delete one Device from DB


def delete_device(deviceDic):
    find_hostname = deviceDic["host"]
    record = Device.query.filter_by(host=find_hostname).first_or_404(
        description='device - {} does not not exist '.format(find_hostname))
    db.session.delete(record)
    db.session.commit()
    return ("Sucessfully deleted")

# Get the device parameters from device/devices and make it into list.


def get_device_list(deviceNames):
    devices = deviceNames["devices"]
    device_list = list()
    for device in devices:
        record = Device.query.filter_by(host=device).first()
        if record:
            device_list.append(get_model_as_dict(record))
        else:
            device_list.append("{} does not not exist ".format(device))
    print(device_list)
    return(device_list)
