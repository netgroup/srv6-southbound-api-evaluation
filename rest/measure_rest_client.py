#!/usr/bin/python
import requests
import json,psutil,time

# Global variables
_Username = 'srv6'
_Password = 'srv6'
_ServerIP = "127.0.0.1"
_Device = 'enp0s25'
_Prefix = ''
_Segments = '2000::1e'
_NumberOfRuleToBeEnforced = 100
_N_Experiment = 20

# Base path for the url
SRV6_BASE_PATH = "srv6-explicit-path"
# HTTP definitions
ACCEPT = "application/json"
CONTENT_TYPE = "application/json"
POST = "POST"
# Define wheter to use HTTP or HTTPS
SECURE = False
# SSL cerificate for server validation
CERTIFICATE = 'cert_client.pem'

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
			 """
		for i in range(2,_NumberOfRuleToBeEnforced+1):
			data += """{
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
			 """
		for i in range(2,_NumberOfRuleToBeEnforced+1):
			data += """{
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