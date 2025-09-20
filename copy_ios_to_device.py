from netmiko import ConnectHandler
from netmiko.exceptions import NetMikoTimeoutException
from netmiko.exceptions import AuthenticationException
from netmiko.exceptions import SSHException
import threading
from getpass import getpass

devices = []

with open( "exp.txt", "r" ) as devices_file:
    for line in devices_file:
        devices.append(line)
             
print ('\n----- devices --------------------------')
print( devices )

passwd = getpass("Enter the password: ")

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
    except (AuthenticationException):
        print ('Authentication failed: ' + ipaddr)
    except (NetMikoTimeoutException):
        print ('Timeout expired: ' + ipaddr)
    except (SSHException):
        print ('SSH error. Check if ssh enabled on device ' + ipaddr)
    except Exception as unknown_error:
        print ('Unknown error: ' + str(unknown_error))
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
