#!/usr/bin/python
import time,psutil
from netconf.client import NetconfSSHSession
try:
    from lxml import etree
except ImportError:
    from xml.etree import ElementTree as etree

_Username = 'srv6'
_Password = 'srv6'
_ServerIP = "192.168.1.2"#"127.0.0.1"
_Device = "enp5s0"#'enp0s25'
_Prefix = ''
_Segments = '2000::1e'
_NumberOfRuleToBeEnforced = 100
_N_Experiment = 20
_Port = 830

# Utility to close Netconf sessions
def close_netconf_session(session):
  # Let's take the reference of the transport
  transport = session.pkt_stream.stream
  # Let's close the Netconf session
  session.close()
  # This is a workaround for RST_ACK
  time.sleep(0.05)
  # Close the transport
  transport.close()
  # Flush the cache
  transport.cache.flush()

def add(communicationType):
  if communicationType == "non persistent sequential":
    for i in range(1,_NumberOfRuleToBeEnforced+1):
      config = """
      <edit-config>
      <target>
        <running/>
      </target>
      <default-operation>none</default-operation>
      <test-option>test-then-set</test-option>
      <error-option>rollback-on-error</error-option>
      <config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
        <srv6-explicit-path operation="create" xmlns="urn:ietf:params:xml:ns:yang:srv6-explicit-path">
            <path>
                <destination>%s</destination>
                <sr-path>
                    <srv6-segment>%s</srv6-segment>
                </sr-path>
                <encapmode>inline</encapmode>
                <device>%s</device>
            </path>
          </srv6-explicit-path>
      </config>
      </edit-config>
      """ %(_Prefix+str(i)+'/128', _Segments, _Device)

      session = NetconfSSHSession(_ServerIP, _Port, _Username, _Password)
      session.send_rpc(config)
      close_netconf_session(session)

  elif communicationType == "non persistent bulk":
    config = """
      <edit-config>
      <target>
        <running/>
      </target>
      <default-operation>none</default-operation>
      <test-option>test-then-set</test-option>
      <error-option>rollback-on-error</error-option>
      <config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
        <srv6-explicit-path operation="create" xmlns="urn:ietf:params:xml:ns:yang:srv6-explicit-path">
            <path>
                <destination>%s</destination>
                <sr-path>
                    <srv6-segment>%s</srv6-segment>
                </sr-path>
                <encapmode>inline</encapmode>
                <device>%s</device>
            </path>
      """ %(_Prefix+str(1)+'/128', _Segments, _Device)
    for i in range(2,_NumberOfRuleToBeEnforced+1):
      config += """
        <path>
            <destination>%s</destination>
            <sr-path>
                <srv6-segment>%s</srv6-segment>
            </sr-path>
            <encapmode>inline</encapmode>
            <device>%s</device>
        </path>
      """ %(_Prefix+str(i)+'/128', _Segments, _Device)
    config += """
        </srv6-explicit-path>
    </config>
    </edit-config>
    """
    session = NetconfSSHSession(_ServerIP, _Port, _Username, _Password)
    session.send_rpc(config)
    close_netconf_session(session)

  elif communicationType == "persistent Conncection":
    session = NetconfSSHSession(_ServerIP, _Port, _Username, _Password)
    for i in range(1,_NumberOfRuleToBeEnforced+1):
      config = """
      <edit-config>
      <target>
        <running/>
      </target>
      <default-operation>none</default-operation>
      <test-option>test-then-set</test-option>
      <error-option>rollback-on-error</error-option>
      <config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
        <srv6-explicit-path operation="create" xmlns="urn:ietf:params:xml:ns:yang:srv6-explicit-path">
            <path>
                <destination>%s</destination>
                <sr-path>
                    <srv6-segment>%s</srv6-segment>
                </sr-path>
                <encapmode>inline</encapmode>
                <device>%s</device>
            </path>
          </srv6-explicit-path>
      </config>
      </edit-config>
      """ %(_Prefix+str(i)+'/128', _Segments, _Device)

      session.send_rpc(config)
    close_netconf_session(session)

def delete(communicationType):
  if communicationType == "non persistent sequential":
    for i in range(1,_NumberOfRuleToBeEnforced+1):
      config ="""
      <edit-config>
      <target>
        <running/>
      </target>
      <default-operation>none</default-operation>
      <test-option>test-then-set</test-option>
      <error-option>rollback-on-error</error-option>
      <config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
        <srv6-explicit-path operation="remove" xmlns="urn:ietf:params:xml:ns:yang:srv6-explicit-path">
            <path>
                <destination>%s</destination>
                <sr-path>
                    <srv6-segment>%s</srv6-segment>
                </sr-path>
                <encapmode>inline</encapmode>
                <device>%s</device>
            </path>
          </srv6-explicit-path>
      </config>
      </edit-config>
      """ %(_Prefix+str(i)+'/128', _Segments, _Device)

      session = NetconfSSHSession(_ServerIP, _Port, _Username, _Password)
      session.send_rpc(config)
      close_netconf_session(session)

  elif communicationType == "non persistent bulk":
    config ="""
      <edit-config>
      <target>
        <running/>
      </target>
      <default-operation>none</default-operation>
      <test-option>test-then-set</test-option>
      <error-option>rollback-on-error</error-option>
      <config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
        <srv6-explicit-path operation="remove" xmlns="urn:ietf:params:xml:ns:yang:srv6-explicit-path">
            <path>
                <destination>%s</destination>
                <sr-path>
                    <srv6-segment>%s</srv6-segment>
                </sr-path>
                <encapmode>inline</encapmode>
                <device>%s</device>
            </path>
      """ %(_Prefix+str(1)+'/128', _Segments, _Device)
    for i in range(2,_NumberOfRuleToBeEnforced+1):
      config += """
        <path>
            <destination>%s</destination>
            <sr-path>
                <srv6-segment>%s</srv6-segment>
            </sr-path>
            <encapmode>inline</encapmode>
            <device>%s</device>
        </path>
      """ %(_Prefix+str(i)+'/128', _Segments, _Device)
    config += """
        </srv6-explicit-path>
    </config>
    </edit-config>
    """
    session = NetconfSSHSession(_ServerIP, _Port, _Username, _Password)
    session.send_rpc(config)
    close_netconf_session(session)

  elif communicationType == "persistent Conncection":
    session = NetconfSSHSession(_ServerIP, _Port, _Username, _Password)
    for i in range(1,_NumberOfRuleToBeEnforced+1):
      config ="""
      <edit-config>
      <target>
        <running/>
      </target>
      <default-operation>none</default-operation>
      <test-option>test-then-set</test-option>
      <error-option>rollback-on-error</error-option>
      <config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
        <srv6-explicit-path operation="remove" xmlns="urn:ietf:params:xml:ns:yang:srv6-explicit-path">
            <path>
                <destination>%s</destination>
                <sr-path>
                    <srv6-segment>%s</srv6-segment>
                </sr-path>
                <encapmode>inline</encapmode>
                <device>%s</device>
            </path>
          </srv6-explicit-path>
      </config>
      </edit-config>
      """ %(_Prefix+str(i)+'/128', _Segments, _Device)
      session.send_rpc(config)
    close_netconf_session(session)


if __name__ == '__main__':
    f1 = open('NetConf20.txt','a+')
    #Add Operation
    for i in range(1,_N_Experiment+1):
        _Prefix = str(2000+i) + '::'
        psutil.cpu_percent(interval=None, percpu=False)
        start_time = time.time()

        add("non persistent sequential")

        executionTime=time.time() - start_time
        SystemCPUUsage = psutil.cpu_percent(interval=None, percpu=False)*executionTime

        print("non persistent sequential, netconf, Add "+str(i))
        print("Execution time: " + str(executionTime))
        print("System-wide CPU Usage: " + str(SystemCPUUsage))

        f1.write('non persistent sequential, netconf, add:\n')
        f1.write(str(executionTime) + '\n')
        f1.write(str(SystemCPUUsage) + '\n')

    for i in range(1,_N_Experiment+1):
        _Prefix = str(2000+i) + '::'
        psutil.cpu_percent(interval=None, percpu=False)
        start_time = time.time()

        delete("non persistent sequential")

        executionTime=time.time() - start_time
        SystemCPUUsage = psutil.cpu_percent(interval=None, percpu=False)*executionTime

        print("non persistent sequential, netconf, del "+str(i))
        print("Execution time: " + str(executionTime))
        print("System-wide CPU Usage: " + str(SystemCPUUsage))

        f1.write('non persistent sequential, netconf, del:\n')
        f1.write(str(executionTime) + '\n')
        f1.write(str(SystemCPUUsage) + '\n')

    for i in range(1,_N_Experiment+1):
        _Prefix = str(2000+i) + '::'
        psutil.cpu_percent(interval=None, percpu=False)
        start_time = time.time()

        add("non persistent bulk")

        executionTime=time.time() - start_time
        SystemCPUUsage = psutil.cpu_percent(interval=None, percpu=False)*executionTime

        print("non persistent bulk, netconf, Add "+str(i))
        print("Execution time: " + str(executionTime))
        print("System-wide CPU Usage: " + str(SystemCPUUsage))

        f1.write('non persistent bulk, netconf, add:\n')
        f1.write(str(executionTime) + '\n')
        f1.write(str(SystemCPUUsage) + '\n')

    for i in range(1,_N_Experiment+1):
        _Prefix = str(2000+i) + '::'
        psutil.cpu_percent(interval=None, percpu=False)
        start_time = time.time()

        delete("non persistent bulk")

        executionTime=time.time() - start_time
        SystemCPUUsage = psutil.cpu_percent(interval=None, percpu=False)*executionTime

        print("non persistent bulk, netconf, del "+str(i))
        print("Execution time: " + str(executionTime))
        print("System-wide CPU Usage: " + str(SystemCPUUsage))

        f1.write('non persistent bulk, netconf, del:\n')
        f1.write(str(executionTime) + '\n')
        f1.write(str(SystemCPUUsage) + '\n')

    for i in range(1,_N_Experiment+1):
        _Prefix = str(2000+i) + '::'
        psutil.cpu_percent(interval=None, percpu=False)
        start_time = time.time()

        add("persistent Conncection")

        executionTime=time.time() - start_time
        SystemCPUUsage = psutil.cpu_percent(interval=None, percpu=False)*executionTime

        print("persistent Conncection, netconf, Add "+str(i))
        print("Execution time: " + str(executionTime))
        print("System-wide CPU Usage: " + str(SystemCPUUsage))

        f1.write('persistent Conncection, netconf, add:\n')
        f1.write(str(executionTime) + '\n')
        f1.write(str(SystemCPUUsage) + '\n')

    for i in range(1,_N_Experiment+1):
        _Prefix = str(2000+i) + '::'
        psutil.cpu_percent(interval=None, percpu=False)
        start_time = time.time()

        delete("persistent Conncection")

        executionTime=time.time() - start_time
        SystemCPUUsage = psutil.cpu_percent(interval=None, percpu=False)*executionTime

        print("persistent Conncection, netconf, del "+str(i))
        print("Execution time: " + str(executionTime))
        print("System-wide CPU Usage: " + str(SystemCPUUsage))

        f1.write('persistent Conncection, netconf, del:\n')
        f1.write(str(executionTime) + '\n')
        f1.write(str(SystemCPUUsage) + '\n')
