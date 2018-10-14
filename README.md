# SRv6 Southbound API Evaluation

This project provides a collection of modules for the evaluation of the SRv6 SRv6 Southbound API

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

In the Client machine, move in to the gRPC folder

    cd gRPC/

Open the A_gRPC_20Times.py file

    nano A_gRPC_20Times.py

Change the value of "_Device" variable to the selected <interface> in step 7. Now press ctrl+o and then ctrl+x
In the server machine, to gRPC folder and run the gRPC servers.

    sudo python Server_gRPC_Shell.py secure
    sudo python Server_gRPC_Shell.py insecure
    sudo python NullServer_gRPC.py secure
    sudo python NullServer_gRPC.py insecure

In the client machine, run A_gRPC_20Times.py  

    sudo python A_gRPC_20Times.py

After the execution is finished the results of the Full process and Just communication parts (with and without packet loss and delay) will be in the gRPC/PureResults folder

### How to perform the REST experiment ###

In the Client machine, move in to the REST folder

    cd REST/

Open the A_REST_20Times.py file

    nano A_REST_20Times.py

Change the value of "_Device" variable to the selected <interface> in step 7. Now press ctrl+o and then ctrl+x
In the server machine, to REST folder and run the REST servers.

    sudo python Server_REST_Shell.py secure
    sudo python Server_REST_Shell.py insecure
    sudo python NullServer_REST.py secure
    sudo python NullServer_REST.py insecure

In the client machine, run A_REST_20Times.py

    sudo python A_REST_20Times.py

After the execution is finished the results of the Full process and Just communication parts (with and without packet loss and delay) will be in the REST/PureResults folder

### How to perform the SSH experiment ###

In the Client machine, move in to the SSH folder

    cd SSH/

Open the A_SSH_20Times.py file
    

    nano A_SSH_20Times.py

Change the value of "_Device" variable to the selected <interface> in step 7. Now press ctrl+o and then ctrl+x
In the client machine, run A_REST_20Times.py

    sudo python A_SSH_20Times.py

After the execution is finished the results of the Full process and Just communication parts (with and without packet loss and delay) will be in the SSH/PureResults folder

### How to perform the pyroute2 and shell experiments ###

In the server, move in to the LocalRuleEnforcement folder

    cd LocalRuleEnforcement/

Open A_LocalRuleEnforcement_20Times.py

    nano A_LocalRuleEnforcement_20Times.py

Change the value of "_Device" variable to the selected <interface> in step 7. Now press ctrl+o and then ctrl+x
In the server, run A_LocalRuleEnforcement_20Times.py

    sudo python A_LocalRuleEnforcement_20Times.py

After the execution is finished the results of the Full process and Just communication parts (with and without packet loss and delay) will be in the LocalRuleEnforcement folder
