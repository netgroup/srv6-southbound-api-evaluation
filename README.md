# SRv6 Southbound API Evaluation

This project provides a collection of modules for the evaluation of the SRv6 Southbound API

### Preliminaries ###

The IP address of the server (routing device) should be 2002::1.

For gRPC experiment, ports 50051, 50052, 50053, and 50054 should not be used by other applications (otherwise, A_gRPC_20Times, NullServer_gRPC.py, Server_gRPC_Pyroute, and Server_gRPC_Shell should be rewritten).

For REST experiment, ports 80, 81, 443, and 444 should be free (otherwise, NullServer_REST.py, Server_REST_Pyroute.py, and Server_REST_Shell.py should be rewritted)

For SSH experiment, SSH service should be active on the Server (routing device)

Rv6 and Pyroute2 should be installed and active on the Server (routing device)

### Before starting the experiment ###

This experiment is designed for a two machine secenario in which the SDN controller is considerd as the client and the routing device is considered as the Server.

At the beginig this repository should be cloned in to the local machines (both client (controller, and Server)

    git clone https://github.com/mohammad59mt/srv6-southbound-api-evaluation.git

The IP address of the server should be 2002::1. To this end, first find the interface name in the server machine:

    ip addr

Then Change the IP address of the selected interface in the Server
    
    sudo ip addr add 2002::1/64 dev <interface name>

### How to perform the gRPC experiment ###

In the server machine, move in to the /srv6-controller/grpc folder.
Open the grpc_server.py file. Change the value of "\_Device" variable to the proper <interface> of the device.
Run the servers in two different terminals:

    sudo python grpc_server.py -s
    sudo python grpc_server.py
    
In the client machine, move in to the /srv6-controller/grpc folder. 
Open measure_grpc_client.py and adjust "ServerIP, \_Device, \_NumberOfRuleToBeEnforced, \_N_Experiment"  parameters. 
Select the connection type by setting "SECURE" parameter in the file. if you choose "True" then the client will make secured connections otherwise insecure connections. 
Then run the file:

    sudo python measure_grpc_client.py

After the execution is finished the results will be in grpc/gRPC20.txt file

### How to perform the REST experiment ###

In the server machine, move in to the /srv6-controller/rest folder. 
Open the rest_server.py file. Change the value of "\_Device" variable to the proper <interface> of the device.
Run the servers in two different terminals:

    sudo python rest_server.py -s
    sudo python rest_server.py
   
In the client machine, move in to the /srv6-controller/rest folder. 
Open measure_rest_client.py and adjust "ServerIP, \_Device, \_NumberOfRuleToBeEnforced, \_N_Experiment"  parameters. 
Select the connection type by setting "SECURE" parameter in the file. if you choose "True" then the client will make secured connections otherwise insecure connections. 
Then run the file:

    sudo python measure_rest_client.py

After the execution is finished the results will be in rest/REST20.txt file

### How to perform the SSH experiment ###

In the server machine, move in to the /srv6-controller/ssh folder. 
Open the ssh_server.py file. Change the value of "\_Device" variable to the proper <interface> of the device.
Run the servers in two different terminals:

    sudo python ssh_server.py
   
In the client machine, move in to the /srv6-controller/ssh folder. 
Open measure_ssh_client.py and adjust "ServerIP, \_Device, \_NumberOfRuleToBeEnforced, \_N_Experiment"  parameters. 
Then run the file:

    sudo python measure_ssh_client.py

After the execution is finished the results will be in ssh/SSH20.txt file

### How to perform the NETCONF experiment ###

In the server machine, move in to the /srv6-controller/netconf folder. 
Open the netconf_server.py file. Change the value of "\_Device" variable to the proper <interface> of the device.
Run the servers in two different terminals:

    sudo python netconf_server.py
   
In the client machine, move in to the /srv6-controller/netconf folder. 
Open measure_netconf_client.py and adjust "ServerIP, \_Device, \_NumberOfRuleToBeEnforced, \_N_Experiment"  parameters. 
Then run the file:

    sudo python measure_netconf_client.py

After the execution is finished the results will be in netconf/netconf20.txt file


### How to perform the pyroute2 and shell experiments ###

In the server, move in to the /srv6-controller/LocalRuleEnforcement folder.
Open the Pyroute2_LRE.py  Shell_LRE.py files. Change the value of "\_Device" variable to the proper <interface> of the device.
Run the codes:

    sudo python Pyroute2_LRE.py
    sudo python Shell_LRE.py

After the execution is finished the results will be in LocalRuleEnforcement/LocalRuleEnforcement20.txt file

### How to Measure the CPU usage ###
Go to /srv6-controller/cpu-measurements folder. 
Run the plot-cpu.py code:

    sudo python plot-cpu.py

By pressing the ctrl+c the measurement will be stopped. Press these keys exactly one time (not more than that)

### How to Measure the Memory usage ###
Go to memory-measurement folder. 
Run the monitor.sh code:

    sudo bash ./monitor.sh

By pressing the ctrl+c the measurement will be stopped. Press these keys exactly one time (not more than that)