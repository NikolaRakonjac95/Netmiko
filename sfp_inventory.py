from netmiko import ConnectHandler
import json

def cisco_cli (parms,commands):
    net_connect = ConnectHandler(**parms)
    net_connect.enable
    for cmd in commands:
        output=net_connect.send_command(cmd, use_textfsm=True)
        output_1=json.dumps(output,indent=10)
    net_connect.disconnect
    print(output_1)
    sfp_module = [n for n in output if n["pid"].startswith("M125")]
    print(f"Device {parms['host']}")
    for n in sfp_module:
        print(n["pid"], n["sn"], "\n")


commands = ["terminal length 0", "show inventory"]
for n in range (x,y):
    parms = {
        "device_type":"cisco_ios",
        "username":"",
        "password":"",
        "host":"10.10.10." + str(n),
        "secret":""
    }
    cisco_cli(parms,commands)

