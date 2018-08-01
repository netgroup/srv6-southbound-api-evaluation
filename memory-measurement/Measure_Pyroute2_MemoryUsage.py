import time, sys, os, signal, subprocess

_Address_of_Pyroute2_Codes = "LRE/Pyroute2_LRE.py"
_Number_of_Iteraion = 10

shellCommand = "sudo bash ./monitor.sh &"
child = subprocess.Popen(shellCommand, stdout=subprocess.PIPE, shell=True)
for i in range(1,_Number_of_Iteraion+1):
	print("round %d of %d" %(i,_Number_of_Iteraion))
	time.sleep(3)
	os.system("sudo python "+_Address_of_Pyroute2_Codes)
time.sleep(20)
os.killpg(os.getpgid(child.pid), signal.SIGTERM)
