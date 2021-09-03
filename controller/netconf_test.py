from ncclient import manager
import xml.etree.ElementTree as ET

# Couldnt download the capability from Nexus , but the XR is working
viosdevice = {
    "host": "192.168.200.101",
    "username": "cisco",
    "password": "cisco",
    "port": 22,
    "hostkey_verify": False

}

with manager.connect(**viosdevice) as conn:
    print(conn.connected)

    # Check the capability and find fith specific name
    capabilities = conn.server_capabilities
    for capabile in capabilities:
        if "interface" in capabile:
            print(capabile)

    # Download the capability
    # Need to filter the module name from the capability list
    # http://openconfig.net/yang/interfaces?module=openconfig-interfaces&revision=2018-01-05&deviations=cisco-xe-openconfig-interfaces-deviation
    # IN this example the module=openconfig-interfaces <<< need to filter module= ??
    # data = conn.get_schema()
    # print(data)

    # # inser the data inside to the XML E tree
    # root = ET.fromstring(data.xml)

    # # # Filter acctual yang data from the output <data> </data> is the first child from the root
    # # # That is contains the acctuall yang data
    # YangText = list(root)[0].text
    # with open ("./openconfig-interfaces.yang", 'w') as src:
    #     src.write(YangText)
