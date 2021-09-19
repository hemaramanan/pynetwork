from flask.wrappers import Response
from netmiko import cisco_base_connection as ciscon
from netmiko.ssh_exception import NetMikoTimeoutException
from paramiko.ssh_exception import SSHException
from netmiko.ssh_exception import AuthenticationException


def show_cisco_cli(devices, commands):
    response = dict()

    for device in devices:
        coommandRespons = list()
        ip_address_of_device = device["host"]
        try:
            net_connect = ciscon.CiscoBaseConnection(**device)
        except (AuthenticationException):
            print('Authentication failure: ' + ip_address_of_device)
            response.update({device["host"]: ["Authentication Error"]})
            continue
        except (NetMikoTimeoutException):
            print('Timeout to device: ' + ip_address_of_device)
            response.update({device["host"]: ["Timeout Error"]})
            continue
        except (EOFError):
            print('End of file while attempting device ' + ip_address_of_device)
            response.update(
                {device["host"]: ["End of file Error"]})
            continue
        except (SSHException):
            print('SSH Issue. Are you sure SSH is enabled? ' + ip_address_of_device)
            response.update({device["host"]: ["SSH Protocol Error"]})
            continue
        except Exception as unknown_error:
            print('Some other error: ' + str(unknown_error))
            response.update({device["host"]: ["Unknown Error"]})
            continue

        print(net_connect.find_prompt())
        for command in commands:
            output = net_connect.send_command(command)
            print(f"Executing >> {command} >> on device >> ",
                  device['host'], "\n", "*" * 60)
            print(output)
            coommandRespons.append(
                f"{command}\n----------------------------------------------------- \n"+str(output))
        response.update({device["host"]: coommandRespons})
        net_connect.disconnect()

    return (response)
