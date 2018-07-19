from __future__ import print_function
from concurrent import futures
import psutil, time, sys, os
from socket import AF_INET
from subprocess import PIPE

_Device = 'enp0s25'#'enp5s0'
_NumberOfRuleToBeEnforced = '100'
_N_Experiment = 20
_Prefix = ''
_Segments = '2000::1e'
_Segments_Change = '3000::3'

"""
def Measure_Add_Memory_Usage():
  memoryUsage = 0
  for i in range(1,int(_NumberOfRuleToBeEnforced)+1):
    shellCommandToAddRouting="ip -6 route add "+_Prefix+str(i)+'/128'+" encap seg6 mode encap"+" segs "+ _Segments+" dev "+_Device
    child = psutil.Popen([shellCommandToAddRouting], stdout=PIPE, shell=True)
    memoryUsagePerChildern = child.memory_info()[0]/2.**10
    memoryUsage+=memoryUsagePerChildern
    #print("Child %s Memory Usage (KB): %s" %(i, memoryUsagePerChildern))
  print("System-wide usage:%s" %memoryUsage)
  return memoryUsage

def Measure_Delete_Memory_Usage():
  memoryUsage = 0
  for i in range(1,int(_NumberOfRuleToBeEnforced)+1):
    shellCommandToRemoveRouting="ip -6 route del "+_Prefix+str(i)+'/128'+" dev "+_Device
    child = psutil.Popen([shellCommandToRemoveRouting], stdout=PIPE, shell=True)
    memoryUsagePerChildern = child.memory_info()[0]/2.**10
    memoryUsage+=memoryUsagePerChildern
    #print("Child %s Memory Usage (KB): %s" %(i, memoryUsagePerChildern))
  print("System-wide usage:%s" %memoryUsage)
  return memoryUsage
"""

def Add():
  for i in range(1,int(_NumberOfRuleToBeEnforced)+1):
    shellCommandToAddRouting="ip -6 route add "+_Prefix+str(i)+'/128'+" encap seg6 mode encap"+" segs "+ _Segments+" dev "+_Device
    os.system(shellCommandToAddRouting)
  
def Delete():
  for i in range(1,int(_NumberOfRuleToBeEnforced)+1):
    shellCommandToRemoveRouting="ip -6 route del "+_Prefix+str(i)+'/128'+" dev "+_Device
    os.system(shellCommandToRemoveRouting)

"""
def Change():
  for i in range(1,int(_NumberOfRuleToBeEnforced)+1):
      shellCommandToChangeRouting="ip -6 route change "+_Prefix+str(i)+'/128'+" via "+_Segments_Change 
      os.system(shellCommandToChangeRouting)
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

    print("Shell Add "+str(i))
    print("Execution time: " + str(executionTime))
    #print("App CPU Usage: " + str(appCPUUsage))
    print("System-wide CPU Usage: " + str(SystemCPUUsage))
    #print("Memory Usage (KB): " + str(memoryUsage))

    f1.write('shell add:\n')
    f1.write(str(executionTime) + '\n')
   # f1.write(str(appCPUUsage) + '\n')
    f1.write(str(SystemCPUUsage) + '\n')
   # f1.write(str(memoryUsage) + '\n\n')

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

    print("Shell Delete "+str(i))
    print("Execution time: " + str(executionTime))
    #print("App CPU Usage: " + str(appCPUUsage))
    print("System-wide CPU Usage: " + str(SystemCPUUsage))
    #print("Memory Usage (KB): " + str(memoryUsage))

    f1.write('shell del:\n')
    f1.write(str(executionTime) + '\n')
    #f1.write(str(appCPUUsage) + '\n')
    f1.write(str(SystemCPUUsage) + '\n')
    #f1.write(str(memoryUsage) + '\n\n')
  
  f1.close()