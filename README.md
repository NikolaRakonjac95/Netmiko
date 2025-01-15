*bgp script helped me to push bgp password to over a 200 branch locations in WAN network for certain bgp neighbors, not to all. In this script I used some lines in bgp config in order to export certain piece of configuration and filter ip address of bgp neighbors to which I want to configure bgp password.

*finding_config_lines script helped me to see on which device I need to put new tacacs commands. I want add new tacacs commands at just certain routers model as you can see in the script.

*In copy_ios_to_devices script I provide code that iterates over more than one hundred switches, finding right model and copy ios to them.

* access_to_many_devices simultaneous script shows how to execute multiple threads concurrently in order to finish some job on multiple cisco devices faster than accessing to devices one per one.

* cisco_concurent_sessions is the similar script as a previous one. Only change is in possibility to chose on how many devices we want to log in simultaneous.

* In txt_fsm_iventory script I managed to find on which devices in network certain SFP module is present, using textfsm in order getting more granular output.
