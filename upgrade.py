from netmiko import ConnectHandler
from netmiko.exceptions import NetMikoTimeoutException
from netmiko.exceptions import AuthenticationException
from netmiko.exceptions import SSHException

devices = []

with open ("exp.txt", "r") as devices_file:
    for line in devices_file:
        devices.append(line)

for n in devices:
    print("Connecting to " + n)
    try:
        net_connect = ConnectHandler(
        device_type="cisco_ios",
        host=n,
        username="",
        password="",
        secret="",
        read_timeout_override=300
        )
    except AuthenticationException:
        continue
    except NetMikoTimeoutException:
        continue
    except EOFError:
        continue
    except SSHException:
        continue
    except Exception as unknown_error:
        continue

    net_connect.enable()
    output = net_connect.send_command('verify /md5 flash:xxxx md5_hash')
    check = 0
    provera = output.find("Verified")
    if check > 0:
        print("IOS successfuly verified")
        config_commands = ["no boot system", "boot system flash:xxxx"]
        output_2 = net_connect.send_config_set(config_commands)
        output_2 += net_connect.save_config()
        print(output_2)
    else:
        print("Bad IOS or not copied properly")
        print(output)
    net_connect.disconnect()
    print("------------------------------")
