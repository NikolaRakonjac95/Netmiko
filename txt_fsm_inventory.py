from netmiko import ConnectHandler
import json

def cisco_cli (parameters,commands):
    net_connect = ConnectHandler(**parameters)
    net_connect.enable
    for cmd in commands:
        output=net_connect.send_command(cmd, use_textfsm=True)
        output_1=json.dumps(output,indent=10)
    net_connect.disconnect
    print(output_1)
    sfp_module = [n for n in output if n["pid"].startswith("M125")]
    print(parameters["host"], "\n",sfp_module)


commands = ["terminal length 0", "show inventory"]
for n in range (101,150):
    parameters = {
        "device_type":"cisco_ios",
        "username":"",
        "password":"",
        "host":"10.35.3." + str(n),
        "secret":""
    }
    cisco_cli(parameters,commands)