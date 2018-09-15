from __future__ import print_function
from concurrent import futures
import psutil, time, sys, os
from socket import AF_INET
from subprocess import PIPE

_Device = 'enp5s0'#'enp0s25'#'enp5s0'
_NumberOfRuleToBeEnforced = '100'
_N_Experiment = 20
_Prefix = ''
_Segments = '2000::1e'
_Segments_Change = '3000::3'

def Add():
  for i in range(1,int(_NumberOfRuleToBeEnforced)+1):
    shellCommandToAddRouting="ip -6 route add "+_Prefix+str(i)+'/128'+" encap seg6 mode encap"+" segs "+ _Segments+" dev "+_Device
    os.system(shellCommandToAddRouting)
  
def Delete():
  for i in range(1,int(_NumberOfRuleToBeEnforced)+1):
    shellCommandToRemoveRouting="ip -6 route del "+_Prefix+str(i)+'/128'+" dev "+_Device
    os.system(shellCommandToRemoveRouting)

if __name__ == '__main__':

  f1 = open('LocalRuleEnforcement20.txt','a+')
  
  for i in range(1,_N_Experiment+1):
  #Add Operation
    _Prefix = str(2000+i) + '::'
    start_time = time.time()
    Add()
    executionTime=time.time() - start_time
    print("Shell Add "+str(i))
    print("Execution time: " + str(executionTime))
    f1.write('shell add:\n')
    f1.write(str(executionTime) + '\n')
    start_time = time.time()
    Delete()
    executionTime=time.time() - start_time
    print("Shell Delete "+str(i))
    print("Execution time: " + str(executionTime))
    f1.write('shell del:\n')
    f1.write(str(executionTime) + '\n')
    
  f1.close()