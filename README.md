*bgp script helped me to push bgp password to over a 200 branch locations in WAN network for certain bgp neighbors, not to all. In this script I used some lines in bgp config in order to export certain piece of configuration and filter ip address of bgp neighbors to which I want to configure bgp password.

*In copying_ios_to_different_type_of_devices.py I provided code that iterates over more than one hundred switches, finding right model and copy ios to them using thread in order to make paralel sessions.

* In sfp_inventory.py I managed to find on which devices in network certain SFP module is present, using textfsm in order getting more granular output.
* Txt_FSM is also usefull for extract some information from "show version" command, for example: hostname, uptime, version, hardware...

* chack_stack_status is made to be used by Nagios server for monitoring stack status. This script covers stack with two, three and four switches.

* copy_ios_to_device.py helped me to copy IOS on more than 200 routers in WAN

* upgrade.py serves to perform md5 checksum check and then boot new ios image to device
