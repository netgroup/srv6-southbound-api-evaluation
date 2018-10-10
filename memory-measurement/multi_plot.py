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


def draw_unreclaim(f,fName,g=0,gName=0,h=0,hName=0,figName=0,pruneMode="Not Prune",max_time=0,syncMemValueF=0,syncMemValueG=0,syncMemValueH=0):
    plt.rcParams.update({'font.size': 19})

    MemFreeF = run_system("grep MemFree %s | awk '{print $2}'" %f)
    MemFreeF = np.asarray(MemFreeF, dtype=int) / 1024 # MB
    if syncMemValueF!=0:
    	MemFreeF-=syncMemValueF
    
    if g!=0:
        MemFreeG = run_system("grep MemFree %s | awk '{print $2}'" %g)
        MemFreeG = np.asarray(MemFreeG, dtype=int) / 1024 # MB
        if syncMemValueG!=0:
        	MemFreeG-=syncMemValueG

    if h!=0:
        MemFreeH = run_system("grep MemFree %s | awk '{print $2}'" %h)
        MemFreeH = np.asarray(MemFreeH, dtype=int) / 1024 # MB
        if syncMemValueH!=0:
        	MemFreeH-=syncMemValueH

    if h!=0:
        minLen=min(len(MemFreeG), len(MemFreeF), len(MemFreeH))
    elif g!=0:
        minLen=min(len(MemFreeG), len(MemFreeF))


    if h!=0 and g==0:
        diffMemFree = abs(MemFreeF[0] - MemFreeG[0])
        if MemFreeG[0] < MemFreeF[0]:
            for i in range(0,minLen):
                MemFreeF[i] = MemFreeF[i] - diffMemFree
        else:
            for i in range(0,minLen):
                MemFreeG[i] = MemFreeG[i] - diffMemFree

    fig,ax1 = plt.subplots()

    if max_time==0:
        xF = np.arange(0,len(MemFreeF)/2.0,0.5)
        if g!=0:
        	xG = np.arange(0,len(MemFreeG)/2.0,0.5)
        if h!=0:
        	xH = np.arange(0,len(MemFreeH)/2.0,0.5)
        ax1.plot(xF, MemFreeF, 'b', label=fName)
        if g!=0:
        	ax1.plot(xG, MemFreeG, 'r', label=gName)
        if h!=0:
        	ax1.plot(xH, MemFreeH, 'g', label=hName)
    else:
        xF = np.arange(0,min(2*max_time,len(MemFreeF))/2.0,0.5)
        if g!=0:
        	xG = np.arange(0,min(2*max_time,len(MemFreeG))/2.0,0.5)
        if h!=0:
        	xH = np.arange(0,min(2*max_time,len(MemFreeH))/2.0,0.5)
        ax1.plot(xF, MemFreeF[0:min(int(2*max_time),len(MemFreeF))], 'b', label=fName)
        if g!=0:
        	ax1.plot(xG, MemFreeG[0:min(int(2*max_time),len(MemFreeG))], 'r', label=gName)
        if h!=0:
        	ax1.plot(xH, MemFreeH[0:min(int(2*max_time),len(MemFreeH))], 'g', label=hName)
    #ax1.plot(x, MemFreeG, 'b', label=gName)
    ax1.set_xlabel('time (s)')
    # Make the y-axis label and tick labels match the line color.
    ax1.set_ylabel('MemFree (MB)')
    #ax1.set_ylabel('MemFree (MB)', color='r')
    #for tl in ax1.get_yticklabels():
    #    tl.set_color('r')

    #plt.legend(loc='upper center')
    plt.legend()
    ax1.grid(True)
    fig.tight_layout()
    if figName!=0:
        plt.savefig(figName, bbox_inches='tight', pad_inches=0.0)
    else:
        plt.show()    


if __name__ == '__main__':
    draw_unreclaim("grpc.dat","gRPC","rest.dat","REST","netconf.dat","NETCONF",figName="memory-pc-grpc-rest-netconf.pdf")
    draw_unreclaim("ssh.dat","SSH",figName="memory-pc-ssh.pdf",syncMemValueF=505)
    #draw_unreclaim("results/add-netconf.dat","NETCONF","results/add-ssh.dat","SSH","Not Prune")
    #draw_unreclaim("results/pyroute-20-mem.dat","Pyroute2","results/shell-20-mem.dat","Shell","Not Prune",5)
