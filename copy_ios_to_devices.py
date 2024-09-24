from netmiko import ConnectHandler
import logging
logging.basicConfig(filename='test.log', level=logging.DEBUG)
logger = logging.getLogger("netmiko")
for n in range (20,178):
    net_connect = ConnectHandler(
    device_type="cisco_ios",
    host="10.10.10." + str(n),
    username="xxx",
    password="xxxxxx",
    secret="xxxxx",
    read_timeout_override=300
    )
    list_inventory = ['WS-C2960+48TC-L', 
                      'WS-C2960-48PST-L',
                     ]

    for software_ver in list_inventory:
        print ('Check ' + software_ver)
        output_version = net_connect.send_command('show inventory')
        int_version = 0 
        int_version = output_version.find(software_ver)
        if int_version > 0:
            print ('Find: ' + software_ver)
            break
        else:
            print ("Do not find " + software_ver)
    net_connect.enable()
    if software_ver == 'WS-C2960+48TC-L':
        print ('Copy ios')
        copy_command = f"copy tftp: flash:"
        output = net_connect.send_command_timing(copy_command)
        if "Address or name of remote host" in output:
            output += net_connect.send_command_timing("10.45.5.10\n")
        if "Source filename" in output:
            output += net_connect.send_command_timing("c2960-lanbasek9-mz.152-7.E7.bin\n")
        if "Destination filename" in output:
            output += net_connect.send_command_timing("\n")
        output += net_connect.save_config()
        output += net_connect.send_command('dir')
        print (output)
        net_connect.disconnect()
        print("--------------------")
    else:
        print ('Model WS-C2960-48PST-L')
