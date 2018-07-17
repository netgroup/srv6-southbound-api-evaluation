from __future__ import print_function
from concurrent import futures
import psutil, time, sys, os, grpc
from socket import AF_INET
from pyroute2 import IPRoute

_Device = 'enp0s25'#'enp5s0'
_NumberOfRuleToBeEnforced = '100'
_N_Experiment = 20
_Prefix = ''
_Segments = '2000::1e'
_Segments_Change = '3000::3'

def Add():
  ip = IPRoute()
  idx = ip.link_lookup(ifname=_Device)[0]
  for i in range(1,int(_NumberOfRuleToBeEnforced)+1):
    ip.route('add',dst=_Prefix+str(i)+'/128',oif=idx,encap={'type': 'seg6','mode': 'encap','segs': _Segments})
  ip.close()
  
def Delete():
  ip = IPRoute()
  idx = ip.link_lookup(ifname=_Device)[0]
  for i in range(1,int(_NumberOfRuleToBeEnforced)+1):
    ip.route('delete',dst=_Prefix+str(i)+'/128',oif=idx)
  ip.close()
"""
def Change():
  ip = IPRoute()
  idx = ip.link_lookup(ifname=_Device)[0]
  for i in range(1,int(_NumberOfRuleToBeEnforced)+1):
      ip.route('change',dst=_Prefix+str(i)+'/128',oif=idx,encap={'via': _Segments_Change})
"""

if __name__ == '__main__':

  f1 = open('LocalRuleEnforcement20.txt','a+')
  
  #Add Operation
  for i in range(1,_N_Experiment+1):
    _Prefix = str(2000+i) + '::'
    #p=psutil.Process(os.getpid())
    #p.cpu_percent()
    psutil.cpu_percent(interval=None, percpu=False)
    start_time = time.time()

    Add()

    executionTime=time.time() - start_time
    #appCPUUsage = p.cpu_percent()*executionTime
    SystemCPUUsage = psutil.cpu_percent(interval=None, percpu=False)*executionTime
    #memoryUsage = p.memory_info()[0]/2.**10

    print("Pytroute2 Add"+str(i))
    print("Execution time: " + str(executionTime))
    #print("App CPU Usage: " + str(appCPUUsage))
    print("Total CPU Usage: " + str(SystemCPUUsage))
    #print("Memory Usage (KB): " + str(memoryUsage))

    f1.write('pytroute2 add:\n')
    f1.write(str(executionTime) + '\n')
    #f1.write(str(appCPUUsage) + '\n')
    f1.write(str(SystemCPUUsage) + '\n')
    #f1.write(str(memoryUsage) + '\n\n')

  #Delete Operation
  for i in range(1,_N_Experiment+1):
    _Prefix = str(2000+i) + '::'
    #p=psutil.Process(os.getpid())
    #p.cpu_percent()
    psutil.cpu_percent(interval=None, percpu=False)
    start_time = time.time()

    Delete()

    executionTime=time.time() - start_time
    #appCPUUsage = p.cpu_percent()*executionTime
    SystemCPUUsage = psutil.cpu_percent(interval=None, percpu=False)*executionTime
    #memoryUsage = p.memory_info()[0]/2.**10

    print("Pytroute2 Delete"+str(i))
    print("Execution time: " + str(executionTime))
    #print("App CPU Usage: " + str(appCPUUsage))
    print("Total CPU Usage: " + str(SystemCPUUsage))
    #print("Memory Usage (KB): " + str(memoryUsage))

    f1.write('pytroute2 del:\n')
    f1.write(str(executionTime) + '\n')
    #f1.write(str(appCPUUsage) + '\n')
    f1.write(str(SystemCPUUsage) + '\n')
    #f1.write(str(memoryUsage) + '\n\n')
  
  f1.close()