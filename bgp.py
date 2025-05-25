from netmiko import ConnectHandler
from netmiko.exceptions import NetMikoTimeoutException
from netmiko.exceptions import AuthenticationException
from netmiko.exceptions import SSHException
import contextlib

with open("description.txt", "w") as f:
        with contextlib.redirect_stdout(f):
            for n in range (5,255):
                IP = "x.y." + str(n) + ".1"
                try:
                    net_connect = ConnectHandler(
                    device_type="cisco_ios",
                    host=IP,
                    username="xxxxx",
                    password="xxxxxx",
                    secret="xxxx"
                    )
                except (AuthenticationException):
                    continue
                except (NetMikoTimeoutException):
                    continue
                except (EOFError):
                    continue
                except (SSHException):
                    continue
                except Exception as unknown_error:
                    continue

                net_connect.enable()
                
                print (f"Connect to: {IP}")

                output = net_connect.send_command("show running-config | section bgp", use_textfsm=True)
                output = output.splitlines()
                x,y,z,d= "IBGP_TUN_PRIORITY_3", "IBGP_TUN_PRIORITY_4", "IBGP_TUN_PRIORITY_2", "IBGP_TUN_PRIORITY_1"
                res, res_2, res_3, res_4 = [i for i in output if x in i ], [i for i in output if y in i], [i for i in output if z in i], [i for i in output if d in i]
                result_all = res + res_2 + res_3 + res_4
                result_all_new = []
                for line in result_all:
                     line = line.strip()
                     if "in" in line:
                          result_all_new.append(line)
                start_char = "neighbor"
                end_char = "route-map"
                for line in result_all_new:
                    start_pos = line.find(start_char) + len(start_char)
                    end_pos = line.find(end_char)
                    result = line[start_pos:end_pos].strip()
                    commands = ["router bgp xxxxx",
                                   f"neighbor {result} password 7 xxxxxxxxxxxx"
                                   ]
                    output_bgp = net_connect.send_config_set(commands)
                    output_bgp += net_connect.save_config()
                    print(output_bgp)

                net_connect.disconnect()
