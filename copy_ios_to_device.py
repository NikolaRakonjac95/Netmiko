from netmiko import ConnectHandler
from netmiko.exceptions import NetMikoTimeoutException
from netmiko.exceptions import AuthenticationException
from netmiko.exceptions import SSHException
import threading
from getpass import getpass

devices = ["10.10.10.1",
           "10.10.11.1",
           "..."
]

passwd = getpass.getpass("Enter the password: ")
def upgrade (ipaddr):
    try:
        net_connect = ConnectHandler(
        device_type="cisco_ios",
        host=ipaddr,
        username="",
        password=passwd,
        secret="", # Enable password
        read_timeout_override=36000
        )
        net_connect.enable()
        print(f"Copying IOS on {ipaddr}")
        copy_command = f"copy tftp: flash:"
        output = net_connect.send_command_timing(copy_command)
        if "Address or name of remote host" in output:
            output += net_connect.send_command_timing("192.168.10.20\n")
        if "Source filename" in output:
            output += net_connect.send_command_timing("<ios file>\n")
        if "Destination filename" in output:
            output += net_connect.send_command_timing("\n")
        print(output)
        net_connect.disconnect()
        print("------------------------------")
    except AuthenticationException as f:
        print(f"Authentication error: {f}")
    except NetMikoTimeoutException: 
        print("Timeout")
    except EOFError:
        print("EOF error")
    except SSHException:
        print("Problem with ssh connection")
    except Exception as unknown_error:
        print(f"Unexpecet error: {unknown_error}")
    return
#=============================================================================================
config_threads_list = []
for ipaddr in devices:
    config_threads_list.append( threading.Thread( target=upgrade, args=(ipaddr,) ) )

print ('\n---- Start with threading ----\n')
for config_thread in config_threads_list:
    config_thread.start()

for config_thread in config_threads_list:
    config_thread.join()
