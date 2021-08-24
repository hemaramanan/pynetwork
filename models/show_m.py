from pynetwork import app
from flask_sqlalchemy import SQLAlchemy
from pynetwork.controller.inventory_c import get_model_as_dict

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite://///home/dev/pynetwork/pynetwork/data/inventory.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Device(db.Model):
    hostname = db.Column(db.Text,primary_key=True)
    username = db.Column(db.Text,nullable=False)
    password = db.Column(db.Text,nullable=False)
    ssh_port = db.Column(db.Integer,default=22)
    credential_template = db.Column(db.Text)


# Get the device parameters from device/devices and make it into list.

def get_device_list(deviceNames):
    device_list = list()
    for device in deviceNames:
        record = Device.query.filter_by(hostname=device).first()
        device_list.append(get_model_as_dict(record))
    return(device_list)