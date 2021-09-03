from easysnmp import snmp_get
session = {"hostname": '192.168.200.101',
           "community": 'pynetwork', "version": 2}


# 1.3.6.1.4.1.9.2.1.3.0 - hostname
hostname = snmp_get('1.3.6.1.6.3.10.2.1.3', **session)

print(hostname)

print(hostname.value)
