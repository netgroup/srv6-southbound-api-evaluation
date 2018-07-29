#!/usr/bin/python

import grpc
import json, psutil,time

import srv6_explicit_path_pb2_grpc
import srv6_explicit_path_pb2

# Define wheter to use SSL or not
SECURE = False
# SSL cerificate for server validation
CERTIFICATE = 'cert_client.pem'

# Global variables
_Username = 'srv6'
_Password = 'srv6'
_ServerIP = "192.168.1.2"#"127.0.0.1"
_Device = "enp5s0"#'enp0s25'
_Prefix = ''
_Segments = '2000::1e'
_NumberOfRuleToBeEnforced = 100ss
_N_Experiment = 20
_Port = 1234


# Build a grpc stub
def get_grpc_session(ip_address, port, secure):
  # If secure we need to establish a channel with the secure endpoint
  if secure:
    # Open the certificate file
    with open(CERTIFICATE) as f:
      certificate = f.read()
    # Then create the SSL credentials and establish the channel
    grpc_client_credentials = grpc.ssl_channel_credentials(certificate)
    channel = grpc.secure_channel("%s:%s" %(ip_address, port), grpc_client_credentials)
  else:
    channel = grpc.insecure_channel("%s:%s" %(ip_address, port))
  return srv6_explicit_path_pb2_grpc.SRv6ExplicitPathStub(channel), channel


def add(communicationType):
    if communicationType == "non persistent sequential":
        for i in range(1,_NumberOfRuleToBeEnforced+1):
            # Get the reference of the stub
            srv6_stub,channel = get_grpc_session(_ServerIP, _Port, SECURE)
            # Create message request
            path_request = srv6_explicit_path_pb2.SRv6EPRequest()
            # Create a new path
            path = path_request.path.add()
            # Set destination, device, encapmode
            path.destination = _Prefix+str(i)+'/128'
            path.device = _Device
            path.encapmode = "inline"
            # Create a new segment
            srv6_segment = path.sr_path.add()
            srv6_segment.segment = _Segments
            # Single add
            srv6_stub.Create(path_request)
            # Let's close the session
            channel.close()

    elif communicationType == "non persistent bulk":
        # Get the reference of the stub
        srv6_stub,channel = get_grpc_session(_ServerIP, _Port, SECURE)
        # Create message request
        path_request = srv6_explicit_path_pb2.SRv6EPRequest()
        for i in range(1,_NumberOfRuleToBeEnforced+1):
            # Create a new path
            path = path_request.path.add()
            # Set destination, device, encapmode
            path.destination = _Prefix+str(i)+'/128'
            path.device = _Device
            path.encapmode = "inline"
            # Create a new segment
            srv6_segment = path.sr_path.add()
            srv6_segment.segment = _Segments
        # Single add
        srv6_stub.Create(path_request)
        # Let's close the session
        channel.close()

    elif communicationType == "persistent Conncection":
        # Get the reference of the stub
        srv6_stub,channel = get_grpc_session(_ServerIP, _Port, SECURE)
        for i in range(1,_NumberOfRuleToBeEnforced+1):
            # Create message request
            path_request = srv6_explicit_path_pb2.SRv6EPRequest()
            # Create a new path
            path = path_request.path.add()
            # Set destination, device, encapmode
            path.destination = _Prefix+str(i)+'/128'
            path.device = _Device
            path.encapmode = "inline"
            # Create a new segment
            srv6_segment = path.sr_path.add()
            srv6_segment.segment = _Segments
            # Single add
            srv6_stub.Create(path_request)
        # Let's close the session
        channel.close()

def delete(communicationType):
    if communicationType == "non persistent sequential":
        for i in range(1,_NumberOfRuleToBeEnforced+1):
            # Get the reference of the stub
            srv6_stub,channel = get_grpc_session(_ServerIP, _Port, SECURE)
            # Create message request
            path_request = srv6_explicit_path_pb2.SRv6EPRequest()
            # Create a new path
            path = path_request.path.add()
            # Set destination, device, encapmode
            path.destination = _Prefix+str(i)+'/128'
            path.device = _Device
            path.encapmode = "inline"
            # Create a new segment
            srv6_segment = path.sr_path.add()
            srv6_segment.segment = _Segments
            # Single delete
            srv6_stub.Remove(path_request)
            # Let's close the session
            channel.close()

    elif communicationType == "non persistent bulk":
        # Get the reference of the stub
        srv6_stub,channel = get_grpc_session(_ServerIP, _Port, SECURE)
        # Create message request
        path_request = srv6_explicit_path_pb2.SRv6EPRequest()
        for i in range(1,_NumberOfRuleToBeEnforced+1):
            # Create a new path
            path = path_request.path.add()
            # Set destination, device, encapmode
            path.destination = _Prefix+str(i)+'/128'
            path.device = _Device
            path.encapmode = "inline"
            # Create a new segment
            srv6_segment = path.sr_path.add()
            srv6_segment.segment = _Segments
        # Single delete
        srv6_stub.Remove(path_request)
        # Let's close the session
        channel.close()

    elif communicationType == "persistent Conncection":
        # Get the reference of the stub
        srv6_stub,channel = get_grpc_session(_ServerIP, _Port, SECURE)
        for i in range(1,_NumberOfRuleToBeEnforced+1):
            # Create message request
            path_request = srv6_explicit_path_pb2.SRv6EPRequest()
            # Create a new path
            path = path_request.path.add()
            # Set destination, device, encapmode
            path.destination = _Prefix+str(i)+'/128'
            path.device = _Device
            path.encapmode = "inline"
            # Create a new segment
            srv6_segment = path.sr_path.add()
            srv6_segment.segment = _Segments
            # Single delete
            srv6_stub.Remove(path_request)
        # Let's close the session
        channel.close()

if __name__ == '__main__':
    f1 = open('gRPC20.txt','a+')
    #Add Operation
    for i in range(1,_N_Experiment+1):
        _Prefix = str(2000+i) + '::'
        psutil.cpu_percent(interval=None, percpu=False)
        start_time = time.time()

        add("non persistent sequential")

        executionTime=time.time() - start_time
        SystemCPUUsage = psutil.cpu_percent(interval=None, percpu=False)*executionTime

        print("non persistent sequential, gRPC, Add "+str(i))
        print("Execution time: " + str(executionTime))
        print("System-wide CPU Usage: " + str(SystemCPUUsage))

        f1.write('non persistent sequential, gRPC, add:\n')
        f1.write(str(executionTime) + '\n')
        f1.write(str(SystemCPUUsage) + '\n')

    for i in range(1,_N_Experiment+1):
        _Prefix = str(2000+i) + '::'
        psutil.cpu_percent(interval=None, percpu=False)
        start_time = time.time()

        delete("non persistent sequential")

        executionTime=time.time() - start_time
        SystemCPUUsage = psutil.cpu_percent(interval=None, percpu=False)*executionTime

        print("non persistent sequential, gRPC, del "+str(i))
        print("Execution time: " + str(executionTime))
        print("System-wide CPU Usage: " + str(SystemCPUUsage))

        f1.write('non persistent sequential, gRPC, del:\n')
        f1.write(str(executionTime) + '\n')
        f1.write(str(SystemCPUUsage) + '\n')

    for i in range(1,_N_Experiment+1):
        _Prefix = str(2000+i) + '::'
        psutil.cpu_percent(interval=None, percpu=False)
        start_time = time.time()

        add("non persistent bulk")

        executionTime=time.time() - start_time
        SystemCPUUsage = psutil.cpu_percent(interval=None, percpu=False)*executionTime

        print("non persistent bulk, gRPC, Add "+str(i))
        print("Execution time: " + str(executionTime))
        print("System-wide CPU Usage: " + str(SystemCPUUsage))

        f1.write('non persistent bulk, gRPC, add:\n')
        f1.write(str(executionTime) + '\n')
        f1.write(str(SystemCPUUsage) + '\n')

    for i in range(1,_N_Experiment+1):
        _Prefix = str(2000+i) + '::'
        psutil.cpu_percent(interval=None, percpu=False)
        start_time = time.time()

        delete("non persistent bulk")

        executionTime=time.time() - start_time
        SystemCPUUsage = psutil.cpu_percent(interval=None, percpu=False)*executionTime

        print("non persistent bulk, gRPC, del "+str(i))
        print("Execution time: " + str(executionTime))
        print("System-wide CPU Usage: " + str(SystemCPUUsage))

        f1.write('non persistent bulk, gRPC, del:\n')
        f1.write(str(executionTime) + '\n')
        f1.write(str(SystemCPUUsage) + '\n')

    for i in range(1,_N_Experiment+1):
        _Prefix = str(2000+i) + '::'
        psutil.cpu_percent(interval=None, percpu=False)
        start_time = time.time()

        add("persistent Conncection")

        executionTime=time.time() - start_time
        SystemCPUUsage = psutil.cpu_percent(interval=None, percpu=False)*executionTime

        print("persistent Conncection, gRPC, Add "+str(i))
        print("Execution time: " + str(executionTime))
        print("System-wide CPU Usage: " + str(SystemCPUUsage))

        f1.write('persistent Conncection, gRPC, add:\n')
        f1.write(str(executionTime) + '\n')
        f1.write(str(SystemCPUUsage) + '\n')

    for i in range(1,_N_Experiment+1):
        _Prefix = str(2000+i) + '::'
        psutil.cpu_percent(interval=None, percpu=False)
        start_time = time.time()

        delete("persistent Conncection")

        executionTime=time.time() - start_time
        SystemCPUUsage = psutil.cpu_percent(interval=None, percpu=False)*executionTime

        print("persistent Conncection, gRPC, del "+str(i))
        print("Execution time: " + str(executionTime))
        print("System-wide CPU Usage: " + str(SystemCPUUsage))

        f1.write('persistent Conncection, gRPC, del:\n')
        f1.write(str(executionTime) + '\n')
        f1.write(str(SystemCPUUsage) + '\n')