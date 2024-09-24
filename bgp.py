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

                output = net_connect.send_command("show running-config | section bgp")
                with open("bgp_conf.txt", "w") as f:
                    f.write(output)
                with open("bgp_conf.txt") as f2:
                    conf = f2.readlines()
                    x= "IBGP_TUN_PRIORITY_3"
                    y = "IBGP_TUN_PRIORITY_4"
                    z = "IBGP_TUN_PRIORITY_2"
                    d = "IBGP_TUN_PRIORITY_1"
                    res = [i for i in conf if x in i ]
                    res_2 = [i for i in conf if y in i]
                    res_3 = [i for i in conf if z in i]
                    res_4 = [i for i in conf if d in i]
                    result_all = res + res_2 + res_3 + res_4
                    start_char = "neighbor "
                    end_char = " route-map"
                    for line in result_all:
                        start_pos = line.find(start_char) + len(start_char)
                        end_pos = line.find(end_char, start_pos)
                        result = line[start_pos:end_pos]
                        commands = ["router bgp 65533",
                                   f"neighbor {result} password 7 xxxxxxxxxxxx"
                                   ]
                        commands = "\n".join(commands)
                        with open ("commands_for_bgp.txt", "w") as f:
                            f.write(commands)
                        with open ("commands_za_bgp.txt") as f2:
                            commands_output = f2.readlines()
                        output_bgp = net_connect.send_config_set(commands_output)
                        print(output_bgp)

                net_connect.disconnect()
