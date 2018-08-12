import os

_Packet_Loss = '2%'
_Delay = '150ms'
_Device = 'enp0s25'

os.system('sudo tc qdisc del dev %s root netem loss %s delay %s' %(_Device,_Packet_Loss,_Delay))
