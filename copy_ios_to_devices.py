from netmiko import ConnectHandler
passwd = getpass.getpass("Enter the password: ")
device_list = []
for n in range (20,178):
    device = {
        "device_type": "cisco_ios",
        "host": "10.10.10." + str(n),
        "username": "xxxx",
        "password": passwd,
        "secret": passwd # Enable password
        "read_timeout_override": "300"
    }
    device_list.append(device)
 for device in device_list:
    connection = ConnectHandler(**device)
    list_inventory = ['switch_type_1', 
                      'switch_type_2',
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
    if software_ver == 'switch_type_1':
        print ('Copy ios')
        copy_command = f"copy tftp: flash:"
        output = net_connect.send_command_timing(copy_command)
        if "Address or name of remote host" in output:
            output += net_connect.send_command_timing("10.45.5.10\n")
        if "Source filename" in output:
            output += net_connect.send_command_timing("switch_image\n")
        if "Destination filename" in output:
            output += net_connect.send_command_timing("\n")
        output += net_connect.save_config()
        output += net_connect.send_command('dir')
        print (output)
        net_connect.disconnect()
        print("--------------------")
    else:
        print ('switch_type_2')
