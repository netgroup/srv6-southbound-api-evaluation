#!/usr/bin/env python

#
# This is a simple script to plot memory usage/allocation trends based on the periodical snapshots of
# /proc/meminfo and /proc/slabinfo.
#


import os
import sys
import os.path
import errno
import re
import glob
import time
import subprocess
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.legend_handler import HandlerLine2D

from getopt import getopt
from getopt import GetoptError

def run_system(cmd):
    """ Run bash commands and return the output """
    p = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
    out,err = p.communicate()
    if len(out) > 0:
        return out.splitlines()
    else:
        return None


def draw_unreclaim(f,fName,g,gName,pruneMode,max_time=0):
    plt.rcParams.update({'font.size': 19})

    MemFreeF = run_system("grep MemFree %s | awk '{print $2}'" %f)
    MemFreeF = np.asarray(MemFreeF, dtype=int) / 1024 # MB
    
    MemFreeG = run_system("grep MemFree %s | awk '{print $2}'" %g)
    MemFreeG = np.asarray(MemFreeG, dtype=int) / 1024 # MB

    minLen=min(len(MemFreeG), len(MemFreeF))


    diffMemFree = abs(MemFreeF[0] - MemFreeG[0])
    if MemFreeG[0] < MemFreeF[0]:
        for i in range(0,minLen):
            MemFreeF[i] = MemFreeF[i] - diffMemFree
    else:
        for i in range(0,minLen):
            MemFreeG[i] = MemFreeG[i] - diffMemFree

    fig,ax1 = plt.subplots()

    if pruneMode == "Not Prune":
    	if max_time==0:
	        xF = np.arange(0,len(MemFreeF)/2.0,0.5)
	        xG = np.arange(0,len(MemFreeG)/2.0,0.5)
	        ax1.plot(xF, MemFreeF, 'r', label=fName)
	        ax1.plot(xG, MemFreeG, 'b', label=gName)
    	else:
	        xF = np.arange(0,min(2*max_time,len(MemFreeF))/2.0,0.5)
	        xG = np.arange(0,min(2*max_time,len(MemFreeG))/2.0,0.5)
	        ax1.plot(xF, MemFreeF[0:min(int(2*max_time),len(MemFreeF))], 'r', label=fName)
	        ax1.plot(xG, MemFreeG[0:min(int(2*max_time),len(MemFreeG))], 'b', label=gName)
    else:
        x = np.arange(0,minLen/2.0,0.5)
        ax1.plot(x, MemFreeF[0:minLen], 'r', label=fName)
        ax1.plot(x, MemFreeG[0:minLen], 'b', label=gName)

    #ax1.plot(x, MemFreeG, 'b', label=gName)
    ax1.set_xlabel('time (s)')
    # Make the y-axis label and tick labels match the line color.
    #ax1.set_ylabel('MemFree (MB)', color='r')
    #for tl in ax1.get_yticklabels():
    #    tl.set_color('r')

    #plt.legend(loc='upper center')
    plt.legend()
    ax1.grid(True)
    fig.tight_layout()
    plt.show()
"""
    ax2 = ax1.twinx() # draw two scales in one plot
    ax2.plot(x, MemFreeG, 'b', label=gName)
    ax2.set_ylabel('MemFree (MB)', color='-*0*/.b')
    for tl in ax2.get_yticklabels():
        tl.set_color('b')

    h1, l1 = ax1.get_legend_handles_labels()
    h2, l2 = ax2.get_legend_handles_labels()
    ax1.legend(h1+h2, l1+l2)
"""
    


if __name__ == '__main__':
    draw_unreclaim("results/add-grpc.dat","gRPC","results/add-rest.dat","REST","Prune")
    draw_unreclaim("results/add-netconf.dat","NETCONF","results/add-ssh.dat","SSH","Not Prune")
    draw_unreclaim("results/pyroute-20-mem.dat","Pyroute2","results/shell-20-mem.dat","Shell","Not Prune",5)
