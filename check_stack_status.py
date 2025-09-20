from netmiko import ConnectHandler
import argparse
import sys

def cisco_cli (parameters,commands):
    net_connect = ConnectHandler(**parameters)
    net_connect.enable()
    for cmd in commands:
        output=net_connect.send_command(cmd, use_textfsm=True)
    net_connect.disconnect()
    output_1 = output.split()
    output_2 = output_1[1:]
    if len(output_2) == 12:
        status = [output_2[5], output_2[11]]
    elif len(output_2) == 18:
        status = [output_2[5], output_2[11], output_2[17]]
    elif len(output_2) == 24:
        status = [output_2[5], output_2[11], output_2[17], output_2[23]]
        
    for s in status:
        if s != "Ready":
            print("CRITICAL: Stack status is BAD")
            sys.exit(2)

    print("OK: Stack status is OK")
    sys.exit(0)

commands = ["show switch | begin -------"]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Nagios plugin for Cisco switch stack monitoring")
    parser.add_argument("-H", "--host", required=True, help="Cisco switch IP address")

    args = parser.parse_args()

    parameters = {
        "device_type":"cisco_ios",
        "username":"",
        "password":"",
        "host":args.host,
        "secret":""
}
    cisco_cli(parameters,commands)
