from __future__ import print_function
from concurrent import futures
import psutil, time, sys, os, grpc
from socket import AF_INET
from pyroute2 import IPRoute

_Device = 'enp5s0'#'enp0s25'#'enp5s0'
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


if __name__ == '__main__':

  f1 = open('LocalRuleEnforcement20.txt','a+')
  

  for i in range(1,_N_Experiment+1):
  #Add Operation
    _Prefix = str(2000+i) + '::'
    start_time = time.time()
    Add()
    executionTime=time.time() - start_time
    print("Pytroute2 Add"+str(i))
    print("Execution time: " + str(executionTime))
    f1.write('pytroute2 add:\n')
    f1.write(str(executionTime) + '\n')
    
  #Delete Operation
    start_time = time.time()
    Delete()
    executionTime=time.time() - start_time
    print("Pytroute2 Delete"+str(i))
    print("Execution time: " + str(executionTime))
    f1.write('pytroute2 del:\n')
    f1.write(str(executionTime) + '\n')
    
  f1.close()
