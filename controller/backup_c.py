from genericpath import isfile
from netmiko import cisco_base_connection as ciscon
from netmiko.ssh_exception import NetMikoTimeoutException
from paramiko.ssh_exception import SSHException
from netmiko.ssh_exception import AuthenticationException
from time import localtime, strftime
from os import listdir, remove
from os.path import isfile


# Backup the configuration for selected device
def backup_cisco_config(devices):
    response = dict()

    for device in devices:
        coommandRespons = list()
        ip_address_of_device = device["host"]
        try:
            net_connect = ciscon.CiscoBaseConnection(**device)
        except (AuthenticationException):
            print('Authentication failure: ' + ip_address_of_device)
            response.update({device["host"]: "Authentication failure"})
            continue
        except (NetMikoTimeoutException):
            print('Timeout to device: ' + ip_address_of_device)
            response.update({device["host"]: "Timeout to device"})
            continue
        except (EOFError):
            print('End of file while attempting device ' + ip_address_of_device)
            response.update(
                {device["host"]: "End of file while attempting device"})
            continue
        except (SSHException):
            print('SSH Issue. Are you sure SSH is enabled? ' + ip_address_of_device)
            response.update({device["host"]: "SSH Protocol Error"})
            continue
        except Exception as unknown_error:
            print('Some other error: ' + str(unknown_error))
            response.update({device["host"]: "Unknown Error"})
            continue

        print(net_connect.find_prompt())
        print(f"Running configuration Backup on on device >> ",
              device['host'], "\n", "*" * 60)
        output = net_connect.send_command("show run")
        if output:
            current_time = strftime("%b_%Y_%X", localtime())
            with open(f"./pynetwork/data/backup_config/{ip_address_of_device}_{current_time}", 'w') as src:
                src.writelines(output)
            print("Configuration sucessfully backued on ./data/backup_config")
            response.update({device["host"]: "Backup completed "})
        net_connect.disconnect()

    return (response)


# List all the backuped configuration exist on the dir
def list_cisco_backup():
    backup_file_list = list()
    backup_file_list = listdir("./pynetwork/data/backup_config/")
    return(backup_file_list)


# Delete the specific file form dir

def delete_cisco_backup(payload):
    response = str
    backup_file_name = payload[0]
    if isfile(f"./pynetwork/data/backup_config/{backup_file_name}"):
        delete_backup_file = remove(
            f"./pynetwork/data/backup_config/{backup_file_name}")
        response = "Backup file deleted"
    else:
        response = "File not exist"
    return(response)
