from netmiko import ConnectHandler
import argparse

def cisco_cli (parameters,commands):
    net_connect = ConnectHandler(**parameters)
    net_connect.enable()
    for cmd in commands:
        output=net_connect.send_command(cmd, use_textfsm=True)
    net_connect.disconnect()
    output_1 = output.split()
    output_2 = output_1[1:]
    if len(output_2) == 12:
        output_3 = [output_2[0], output_2[5], output_2[6], output_2[11]]
        if output_3[1] != "Ready" or output_3[3] != "Ready":
            print("Stack status is BAD")
        else:
            print("Stack status is OK")
    elif len(output_2) == 18:
        output_3 = [output_2[0], output_2[5], output_2[6], output_2[11], output_2[12], output_2[17]]
        if output_3[1] != "Ready" or output_3[3] != "Ready" or output_3[5] != "Ready":
            print("Stack status is BAD")
        else:
            print("Stack status is OK")
    elif len(output_2) == 24:
        output_3 = [output_2[0], output_2[5], output_2[6], output_2[11], output_2[12], output_2[17], output_2[18], output_2[23]]
        if output_3[1] != "Ready" or output_3[3] != "Ready" or output_3[5] != "Ready" or output_3[7] != "Ready":
            print("Stack status is BAD")
        else:
            print("Stack status is OK")

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