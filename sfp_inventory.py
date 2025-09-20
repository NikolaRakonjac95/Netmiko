from netmiko import ConnectHandler
import json

def cisco_cli (parametri,komande):
    net_connect = ConnectHandler(**parametri)
    net_connect.enable
    for cmd in komande:
        output=net_connect.send_command(cmd, use_textfsm=True)
        output_1=json.dumps(output,indent=10)
    net_connect.disconnect
    print(output_1)
    sfp_module = [n for n in output if n["pid"].startswith("M125")]
    print(f"Uredjaj {parametri['host']}")
    for n in sfp_module:
        print(n["pid"], n["sn"], "\n")


komande = ["terminal length 0", "show inventory"]
for n in range (x,y):
    parametri = {
        "device_type":"cisco_ios",
        "username":"",
        "password":"",
        "host":"10.10.10." + str(n),
        "secret":""
    }
    cisco_cli(parametri,komande)
