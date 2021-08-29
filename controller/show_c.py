from flask.wrappers import Response
from netmiko import cisco_base_connection as ciscon
from pynetwork.models.inventory_m import get_device_list


def show_cisco_cli(devices, commands):
    response = dict()
    for device in devices:
        with ciscon.CiscoBaseConnection(**device) as conn:
            if conn.find_prompt != 0:
                coommandRespons = list()
                print("Connection is OK", device['host'])
                print("*" * 60)
                # Display the Prompt
                print(conn.find_prompt())
                # Send one cisco command
                for command in commands:
                    resp = conn.send_command(command)
                    coommandRespons.append(resp)
                # Get / Split only the interface name
                # Ifce = resp.split()[0]
                response.update({device["host"]: coommandRespons})
                print(resp)
                # return(Ifce)
                print('*' * 25, "Next Device", '*' * 25)
            else:
                print(conn.session_log)

    return (response)

# devices = ["192.168.200.101"]
# a = show_cisco_cli(devices)
