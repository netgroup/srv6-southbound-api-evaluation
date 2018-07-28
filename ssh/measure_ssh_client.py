#!/usr/bin/python
import sshutil,psutil,time
from sshutil.cmd import SSHCommand
import logging
from sshutil.host import Host

_Username = 'srv6'
_Password = 'srv6'
_ServerIP = "192.168.1.2"#"127.0.0.1"
_Device = "enp5s0"#'enp0s25'
_Prefix = ''
_Segments = '2000::1e'
_NumberOfRuleToBeEnforced = 100
_N_Experiment = 20
_port = 220

def SSHCommand_add(communicationType):
    if communicationType == "non persistent sequential":
        for i in range(1,_NumberOfRuleToBeEnforced+1):
            cmd = "ip -6 route add "+_Prefix+str(i)+'/128'+" encap seg6 mode encap segs "+ _Segments+" dev "+_Device
            remoteCmd = SSHCommand(cmd, _ServerIP, _port, _Username, _Password)
            remoteCmd.run()
            # Close the session
            remoteCmd.close()
            # Flush the cache 
            remoteCmd.cache.flush()
    elif communicationType == "non persistent bulk":
        cmd = "ip -6 route add "+_Prefix+'1/128'+" encap seg6 mode encap segs "+ _Segments+" dev "+_Device
        for i in range(2,_NumberOfRuleToBeEnforced+1):
            cmd += ";ip -6 route add "+_Prefix+str(i)+'/128'+" encap seg6 mode encap segs "+ _Segments+" dev "+_Device
        remoteCmd = SSHCommand(cmd, _ServerIP, _port, _Username, _Password)
        remoteCmd.run()
        # Close the session
        remoteCmd.close()
        # Flush the cache 
        remoteCmd.cache.flush()
    elif communicationType == "persistent Conncection":
        for i in range(1,_NumberOfRuleToBeEnforced+1):
            cmd = "ip -6 route add "+_Prefix+str(i)+'/128'+" encap seg6 mode encap segs "+ _Segments+" dev "+_Device
            remoteCmd = SSHCommand(cmd, _ServerIP, _port, _Username, _Password)
            remoteCmd.run()
        # Close the session
        remoteCmd.close()
        # Flush the cache 
        remoteCmd.cache.flush()

def SSHCommand_delete(communicationType):
    if communicationType == "non persistent sequential":
        for i in range(1,_NumberOfRuleToBeEnforced+1):
            cmd = "ip -6 route del "+_Prefix+str(i)+'/128'+" dev "+_Device
            remoteCmd = SSHCommand(cmd, _ServerIP, _port, _Username, _Password)
            remoteCmd.run()
            # Close the session
            remoteCmd.close()
            # Flush the cache 
            remoteCmd.cache.flush()
    elif communicationType == "non persistent bulk":
        cmd = "ip -6 route del "+_Prefix+'1/128'+" dev "+_Device
        for i in range(2,_NumberOfRuleToBeEnforced+1):
            cmd += ";ip -6 route del "+_Prefix+str(i)+'/128'+" dev "+_Device
        remoteCmd = SSHCommand(cmd, _ServerIP, _port, _Username, _Password)
        remoteCmd.run()
        # Close the session
        remoteCmd.close()
        # Flush the cache 
        remoteCmd.cache.flush()
    elif communicationType == "persistent Conncection":
        for i in range(1,_NumberOfRuleToBeEnforced+1):
            cmd = "ip -6 route del "+_Prefix+str(i)+'/128'+" dev "+_Device
            remoteCmd = SSHCommand(cmd, _ServerIP, _port, _Username, _Password)
            remoteCmd.run()
        # Close the session
        remoteCmd.close()
        # Flush the cache 
        remoteCmd.cache.flush()   

if __name__ == '__main__':
    f1 = open('SSH20.txt','a+')
    #Add Operation
    for i in range(1,_N_Experiment+1):
        _Prefix = str(2000+i) + '::'
        psutil.cpu_percent(interval=None, percpu=False)
        start_time = time.time()

        SSHCommand_add("non persistent sequential")

        executionTime=time.time() - start_time
        SystemCPUUsage = psutil.cpu_percent(interval=None, percpu=False)*executionTime

        print("non persistent sequential, SSH, Add "+str(i))
        print("Execution time: " + str(executionTime))
        print("System-wide CPU Usage: " + str(SystemCPUUsage))

        f1.write('non persistent sequential, SSH, add:\n')
        f1.write(str(executionTime) + '\n')
        f1.write(str(SystemCPUUsage) + '\n')

    for i in range(1,_N_Experiment+1):
        _Prefix = str(2000+i) + '::'
        psutil.cpu_percent(interval=None, percpu=False)
        start_time = time.time()

        SSHCommand_delete("non persistent sequential")

        executionTime=time.time() - start_time
        SystemCPUUsage = psutil.cpu_percent(interval=None, percpu=False)*executionTime

        print("non persistent sequential, SSH, del "+str(i))
        print("Execution time: " + str(executionTime))
        print("System-wide CPU Usage: " + str(SystemCPUUsage))

        f1.write('non persistent sequential, SSH, del:\n')
        f1.write(str(executionTime) + '\n')
        f1.write(str(SystemCPUUsage) + '\n')

    for i in range(1,_N_Experiment+1):
        _Prefix = str(2000+i) + '::'
        psutil.cpu_percent(interval=None, percpu=False)
        start_time = time.time()

        SSHCommand_add("non persistent bulk")

        executionTime=time.time() - start_time
        SystemCPUUsage = psutil.cpu_percent(interval=None, percpu=False)*executionTime

        print("non persistent bulk, SSH, Add "+str(i))
        print("Execution time: " + str(executionTime))
        print("System-wide CPU Usage: " + str(SystemCPUUsage))

        f1.write('non persistent bulk, SSH, add:\n')
        f1.write(str(executionTime) + '\n')
        f1.write(str(SystemCPUUsage) + '\n')

    for i in range(1,_N_Experiment+1):
        _Prefix = str(2000+i) + '::'
        psutil.cpu_percent(interval=None, percpu=False)
        start_time = time.time()

        SSHCommand_delete("non persistent bulk")

        executionTime=time.time() - start_time
        SystemCPUUsage = psutil.cpu_percent(interval=None, percpu=False)*executionTime

        print("non persistent bulk, SSH, del "+str(i))
        print("Execution time: " + str(executionTime))
        print("System-wide CPU Usage: " + str(SystemCPUUsage))

        f1.write('non persistent bulk, SSH, del:\n')
        f1.write(str(executionTime) + '\n')
        f1.write(str(SystemCPUUsage) + '\n')

    for i in range(1,_N_Experiment+1):
        _Prefix = str(2000+i) + '::'
        psutil.cpu_percent(interval=None, percpu=False)
        start_time = time.time()

        SSHCommand_add("persistent Conncection")

        executionTime=time.time() - start_time
        SystemCPUUsage = psutil.cpu_percent(interval=None, percpu=False)*executionTime

        print("persistent Conncection, SSH, Add "+str(i))
        print("Execution time: " + str(executionTime))
        print("System-wide CPU Usage: " + str(SystemCPUUsage))

        f1.write('persistent Conncection, SSH, add:\n')
        f1.write(str(executionTime) + '\n')
        f1.write(str(SystemCPUUsage) + '\n')

    for i in range(1,_N_Experiment+1):
        _Prefix = str(2000+i) + '::'
        psutil.cpu_percent(interval=None, percpu=False)
        start_time = time.time()

        SSHCommand_delete("persistent Conncection")

        executionTime=time.time() - start_time
        SystemCPUUsage = psutil.cpu_percent(interval=None, percpu=False)*executionTime

        print("persistent Conncection, SSH, del "+str(i))
        print("Execution time: " + str(executionTime))
        print("System-wide CPU Usage: " + str(SystemCPUUsage))

        f1.write('persistent Conncection, SSH, del:\n')
        f1.write(str(executionTime) + '\n')
        f1.write(str(SystemCPUUsage) + '\n')