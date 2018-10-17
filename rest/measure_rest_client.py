#!/usr/bin/python
import requests
import json,psutil,time

import urllib3

urllib3.disable_warnings()

# Global variables
_Username = 'srv6'
_Password = 'srv6'
_ServerIP = "dell-Inspiron-N5110"#"192.168.1.2"#"127.0.0.1"#"192.168.1.2"
_Device = "enp5s0"#'enp0s25'#"enp5s0"
_Prefix = ''
_Segments = '2000::1e'
_NumberOfRuleToBeEnforced = 100
_N_Experiment = 20
# Define wheter to use HTTP or HTTPS
SECURE = False

_Bulk_Delete_Only = False

# Base path for the url
SRV6_BASE_PATH = "srv6-explicit-path"
# HTTP definitions
ACCEPT = "application/json"
CONTENT_TYPE = "application/json"
POST = "POST"
# SSL cerificate for server validation
CERTIFICATE = 'server.crt'

# Build an http requests object
def get_http_requests(ip_address, port, secure, params, data):
  # Create a request, build the url and headers
  url = '{scheme}://{ip}:{port}/{basePath}'.format(scheme=('https' if secure else 'http'),
                                                  ip=ip_address, port=port, basePath=SRV6_BASE_PATH)
  headers = {'Accept': ACCEPT, 'Content-Type': CONTENT_TYPE}
  request = requests.Request(POST, url, data=data, headers=headers, params=params)
  return request.prepare()


def add(communicationType):
    if communicationType == "non persistent sequential":
        for i in range(1,_NumberOfRuleToBeEnforced+1):
            session = requests.Session()
            data = """
            {
              "paths": [
                {
                  "device": "%s",
                  "destination": "%s",
                  "encapmode": "inline",
                  "segments": [
                    "%s"
                  ]
                }
              ]
            }
            """ %(_Device,_Prefix+str(i)+'/128',_Segments)
            params = {"operation": "create"}
            # Create a POST request with the given data
            request = get_http_requests(_ServerIP, 443 if SECURE else 8080, SECURE, params, data)
            # Single add
            session.send(request, verify=(CERTIFICATE if SECURE else None))
            session.close()

    elif communicationType == "non persistent bulk":
        session = requests.Session()
        params = {"operation": "create"}
        data = """
            {
              "paths": [
                 {
                  "device": "%s",
                  "destination": "%s",
                  "encapmode": "inline",
                  "segments": [
                    "%s"
                  ]
                }
            """ %(_Device,_Prefix+str(1)+'/128',_Segments)
        for i in range(2,_NumberOfRuleToBeEnforced+1):
            data += """,{
                  "device": "%s",
                  "destination": "%s",
                  "encapmode": "inline",
                  "segments": [
                    "%s"
                  ]
                }
            """ %(_Device,_Prefix+str(i)+'/128',_Segments)
        data += """
          ]
            }
        """
        request = get_http_requests(_ServerIP, 443 if SECURE else 8080, SECURE, params, data)
        # Single add
        session.send(request, verify=(CERTIFICATE if SECURE else None))
        session.close()

    elif communicationType == "persistent Conncection":
        session = requests.Session()
        params = {"operation": "create"}
        for i in range(1,_NumberOfRuleToBeEnforced+1):
            data = """
            {
              "paths": [
                {
                  "device": "%s",
                  "destination": "%s",
                  "encapmode": "inline",
                  "segments": [
                    "%s"
                  ]
                }
              ]
            }
            """ %(_Device,_Prefix+str(i)+'/128',_Segments)
            # Create a POST request with the given data
            request = get_http_requests(_ServerIP, 443 if SECURE else 8080, SECURE, params, data)
            # Single add
            session.send(request, verify=(CERTIFICATE if SECURE else None))
        session.close()

def delete(communicationType):
    if communicationType == "non persistent sequential":
        for i in range(1,_NumberOfRuleToBeEnforced+1):
            session = requests.Session()
            data = """
            {
              "paths": [
                {
                  "device": "%s",
                  "destination": "%s",
                  "encapmode": "inline",
                  "segments": [
                    "%s"
                  ]
                }
              ]
            }
            """ %(_Device,_Prefix+str(i)+'/128',_Segments)
            params = {"operation": "remove"}
            # Create a POST request with the given data
            request = get_http_requests(_ServerIP, 443 if SECURE else 8080, SECURE, params, data)
            # Single add
            session.send(request, verify=(CERTIFICATE if SECURE else None))
            session.close()

    elif communicationType == "non persistent bulk":
        session = requests.Session()
        params = {"operation": "remove"}
        data = """
            {
              "paths": [
                 {
                  "device": "%s",
                  "destination": "%s",
                  "encapmode": "inline",
                  "segments": [
                    "%s"
                  ]
                }
            """ %(_Device,_Prefix+str(1)+'/128',_Segments)
        for i in range(2,_NumberOfRuleToBeEnforced+1):
            data += """,{
                  "device": "%s",
                  "destination": "%s",
                  "encapmode": "inline",
                  "segments": [
                    "%s"
                  ]
                }
            """ %(_Device,_Prefix+str(i)+'/128',_Segments)
        data += """
          ]
            }
        """
        request = get_http_requests(_ServerIP, 443 if SECURE else 8080, SECURE, params, data)
        # Single add
        session.send(request, verify=(CERTIFICATE if SECURE else None))
        session.close()

    elif communicationType == "persistent Conncection":
        session = requests.Session()
        params = {"operation": "remove"}
        for i in range(1,_NumberOfRuleToBeEnforced+1):
            # Define body content and query params
            data = """
            {
              "paths": [
                {
                  "device": "%s",
                  "destination": "%s",
                  "encapmode": "inline",
                  "segments": [
                    "%s"
                  ]
                }
              ]
            }
            """ %(_Device,_Prefix+str(i)+'/128',_Segments)
            # Create a POST request with the given data
            request = get_http_requests(_ServerIP, 443 if SECURE else 8080, SECURE, params, data)
            # Single add
            session.send(request, verify=(CERTIFICATE if SECURE else None))
        session.close()

if __name__ == '__main__':
    f1 = open('REST20.txt','a+')

    ##################################################################
    #Add Operation - non persistent sequential Connection (NP-Con-Seq)    
    for i in range(1,_N_Experiment+1):
        _Prefix = str(2000+i) + '::'
        psutil.cpu_percent(interval=None, percpu=False)
        start_time = time.time()
        add("non persistent sequential")
        executionTime=time.time() - start_time
        SystemCPUUsage = psutil.cpu_percent(interval=None, percpu=False)*executionTime
        print("non persistent sequential, rest, Add "+str(i))
        print("Execution time: " + str(executionTime))
        print("System-wide CPU Usage: " + str(SystemCPUUsage))
        f1.write('non persistent sequential, rest, add:\n')
        f1.write(str(executionTime) + '\n')
        f1.write(str(SystemCPUUsage) + '\n')
    #Delete Operation - non persistent sequential Connection (NP-Con-Seq)
    if _Bulk_Delete_Only:
        for i in range(1,_N_Experiment+1):
            _Prefix = str(2000+i) + '::'
            psutil.cpu_percent(interval=None, percpu=False)
            start_time = time.time()
            delete("non persistent sequential")
            executionTime=time.time() - start_time
            SystemCPUUsage = psutil.cpu_percent(interval=None, percpu=False)*executionTime
            print("non persistent sequential, rest, del "+str(i))
            print("Execution time: " + str(executionTime))
            print("System-wide CPU Usage: " + str(SystemCPUUsage))
            f1.write('non persistent sequential, rest, del:\n')
            f1.write(str(executionTime) + '\n')
            f1.write(str(SystemCPUUsage) + '\n')
    else:
        for i in range(1,_N_Experiment+1):
            _Prefix = str(2000+i) + '::'
            delete("non persistent bulk")

    ##################################################################
    #Add Operation - non persistent bulk (NP-Bulk)
    for i in range(1,_N_Experiment+1):
        _Prefix = str(2000+i) + '::'
        psutil.cpu_percent(interval=None, percpu=False)
        start_time = time.time()
        add("non persistent bulk")
        executionTime=time.time() - start_time
        SystemCPUUsage = psutil.cpu_percent(interval=None, percpu=False)*executionTime
        print("non persistent bulk, rest, Add "+str(i))
        print("Execution time: " + str(executionTime))
        print("System-wide CPU Usage: " + str(SystemCPUUsage))
        f1.write('non persistent bulk, rest, add:\n')
        f1.write(str(executionTime) + '\n')
        f1.write(str(SystemCPUUsage) + '\n')
    #Delete Operation - non persistent bulk (NP-Bulk)
    if _Bulk_Delete_Only:
        for i in range(1,_N_Experiment+1):
            _Prefix = str(2000+i) + '::'
            psutil.cpu_percent(interval=None, percpu=False)
            start_time = time.time()
            delete("non persistent bulk")
            executionTime=time.time() - start_time
            SystemCPUUsage = psutil.cpu_percent(interval=None, percpu=False)*executionTime
            print("non persistent bulk, rest, del "+str(i))
            print("Execution time: " + str(executionTime))
            print("System-wide CPU Usage: " + str(SystemCPUUsage))
            f1.write('non persistent bulk, rest, del:\n')
            f1.write(str(executionTime) + '\n')
            f1.write(str(SystemCPUUsage) + '\n')
    else:
        for i in range(1,_N_Experiment+1):
            _Prefix = str(2000+i) + '::'
            delete("non persistent bulk")

    ##################################################################
    #Add Operation - persistent Conncection (P-Con_Seq)
    for i in range(1,_N_Experiment+1):
        _Prefix = str(2000+i) + '::'
        psutil.cpu_percent(interval=None, percpu=False)
        start_time = time.time()
        add("persistent Conncection")
        executionTime=time.time() - start_time
        SystemCPUUsage = psutil.cpu_percent(interval=None, percpu=False)*executionTime
        print("persistent Conncection, rest, Add "+str(i))
        print("Execution time: " + str(executionTime))
        print("System-wide CPU Usage: " + str(SystemCPUUsage))
        f1.write('persistent Conncection, rest, add:\n')
        f1.write(str(executionTime) + '\n')
        f1.write(str(SystemCPUUsage) + '\n')
    #Delete Operation - persistent Conncection (P-Con_Seq)    
    if _Bulk_Delete_Only:
        for i in range(1,_N_Experiment+1):
            _Prefix = str(2000+i) + '::'
            psutil.cpu_percent(interval=None, percpu=False)
            start_time = time.time()
            delete("persistent Conncection")
            executionTime=time.time() - start_time
            SystemCPUUsage = psutil.cpu_percent(interval=None, percpu=False)*executionTime
            print("persistent Conncection, rest, del "+str(i))
            print("Execution time: " + str(executionTime))
            print("System-wide CPU Usage: " + str(SystemCPUUsage))
            f1.write('persistent Conncection, rest, del:\n')
            f1.write(str(executionTime) + '\n')
            f1.write(str(SystemCPUUsage) + '\n')
    else:
        for i in range(1,_N_Experiment+1):
            _Prefix = str(2000+i) + '::'
            delete("non persistent bulk")
    f1.close()