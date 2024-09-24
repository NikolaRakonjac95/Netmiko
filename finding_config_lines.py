import json
from netmiko import ConnectHandler
from netmiko.exceptions import NetmikoAuthenticationException
from netmiko.exceptions import NetmikoTimeoutException
from netmiko.exceptions import SSHException

range_1 = range(1,6)
range_2 = range(15,20)
IP = list(range_1)+list(range_2)
for n in IP:
    try:
        ip_address = "10.10.10." + str(n)
        net_connect = ConnectHandler(
            device_type ="cisco_ios",
            host = "10.10.10." + str(n),
            username = "xxxx",
            password = "xxxxxx",
            secret = "xxxxx"
            )
    except NetmikoAuthenticationException as authentication:
        print(f"Authentication error {ip_address}: {authentication}")
        continue
    except NetmikoTimeoutException as Timeout:
        print(f"Timeout {ip_address}: {Timeout}")
        continue
    except SSHException as ssh:
        print(f"SSH connection error {ip_address}: {ssh}")
        continue
    except Exception as unknown_error:
        print(f"Error {ip_address}: {unknown_error}")
        continue

    
    output = net_connect.send_command("show inventory")
    lists = ["C1111-4P","C881-K9" ]
    for model in lists:
            inv = 0
            inv += output.find(model)
            if inv > 0:
                print(f"Find {model}")
                break
            else:
                continue
    if model:
            net_connect.enable()
            output_1 = net_connect.send_command("terminal length 0")
            output_2 = net_connect.send_command("show running-config")
            
            with open("raning.txt", "w") as f:
                f.write(output_2)
            with open("raning.txt") as f2:
                konf = f2.readlines()
                x= "ISE"
                y = "hostname"
                res = [i for i in konf if x in i ]
                res_2 = [i for i in konf if y in i]
                if res:
                    print(f"{str(res_2)}")
                    print(f"There is a conf:{str(res)}")
                else:
                    print(f"{str(res_2)}")
                    print(f"Add tacacs command")
    net_connect.disconnect()
    
    
