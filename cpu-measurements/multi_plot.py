from __future__ import (unicode_literals, division, print_function, absolute_import)
import matplotlib.pyplot as plt
import time,psutil


def read_file(file_name,min_time,max_time,tune_value, split_value):
    File = open(file_name, 'r')
    data = File.read()
    File.close()
    log = {}
    log['times'] = []
    log['cpu'] = []

    for Line in data.split("\n"):
        if Line is not "":
            Splietted = Line.split(split_value) 
            time_c = float(Splietted[1]) - tune_value
            cpu_c = float(Splietted[2])
            if time_c >= min_time and max_time >= time_c :
                log['times'].append(time_c)
                log['cpu'].append(cpu_c)
    return log

def plot_results(log1, name1, log2=0, name2=0,log3=0, name3=0,fig_name=0):
    plt.rcParams.update({'font.size': 19})
    fig, ax = plt.subplots()
    #ax = plt.subplot(111)
    plt.plot(log1['times'], log1['cpu'],label=name1,color="b")
    if log2 != 0:
        plt.plot(log2['times'], log2['cpu'],label=name2,color="r")
    if log3 != 0:
        plt.plot(log3['times'], log3['cpu'],label=name3,color="g")

    leg = plt.legend(loc='upper center', ncol=2, fancybox=True)
    leg.get_frame().set_alpha(0.5)
    ax.set_ylabel('CPU (%)')
    ax.set_xlabel('time (s)')
    ax.set_ylim(0., max(log1['cpu']) * 1.2)
    fig.tight_layout()
    if fig_name!=0:
        plt.savefig(fig_name, bbox_inches='tight', pad_inches=0.0)
    else:
        plt.show()


#gRPC
log1 = read_file("grpc.txt",1,2.5,0.3,"       ")
#REST
log2 = read_file("rest.txt",1,2.5,0.8,"       ")
#netconf
log3 = read_file("netconf.txt",1,2.5,0,"      ")
#Plot gRPC vs REST
plot_results(log1, "gRPC", log2, "REST",log3, "NETCONF",fig_name="cpu-pc-grpc-rest-netconf.pdf")

#ssh
log1 = read_file("ssh.txt",0,14,0,"      ")
#Plot ssh 
plot_results(log1, "SSH",fig_name="cpu-pc-ssh.pdf")

"""#netconf
log1 = read_file("results/add-ssh.txt",0,100,0,"      ")
#ssh
log2 = read_file("results/add-netconf.txt",1,25,5,"      ")
#Plot ssh vs netconf
plot_results(log1, "SSH", log2, "NETCONF")


#pyroute2
log1 = read_file("results/pyroute-1000-np-add-cpu.txt",0,100,0,"       ")
#shell
log2 = read_file("results/shell-1000-np-add-cpu.txt",0,100,0,"       ")
#Plot ssh vs netconf
plot_results(log1, "Pyroute2", log2, "Shell")

"""
