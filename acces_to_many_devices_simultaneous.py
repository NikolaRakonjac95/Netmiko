import threading
from netmiko.exceptions import NetMikoTimeoutException
from netmiko.exceptions import AuthenticationException
from netmiko.exceptions import SSHException
from netmiko import ConnectHandler
from time import time
#------------------------------------------------------------------------------
devices = []

with open( "exp.txt", "r" ) as devices_file:

    for line in devices_file:
        devices.append(line)
             

print ('\n----- devices --------------------------')
print( devices )
#------------------------------------------------------------------------------
def config_worker( ipaddr ):
    print (f"---- Connect to {ipaddr}")
    try:
        net_connect = ConnectHandler(
        device_type="cisco_ios",
        host=ipaddr,
        username="",
        password="",
        secret=""
        )
        config_data = net_connect.send_command('show interfaces description')
        print("\n", ipaddr)
        print(config_data)
        print("-------")

        net_connect.disconnect()
    except (AuthenticationException):
        print ('Authentication failed: ' + ipaddr)
    except (NetMikoTimeoutException):
        print ('Timeout expired: ' + ipaddr)
    except (SSHException):
        print ('SSH error. Check if ssh enabled on device ' + ipaddr)
    except Exception as unknown_error:
        print ('Unknown error: ' + str(unknown_error))

    return
#==============================================================================
starting_time = time()

config_threads_list = []
for ipaddr in devices:
    config_threads_list.append( threading.Thread( target=config_worker, args=(ipaddr,) ) )

print ('\n---- Start with threading ----\n')
for config_thread in config_threads_list:
    config_thread.start()

for config_thread in config_threads_list:
    config_thread.join()

print ('\n---- DONE! TIME=', time() - starting_time)