import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from collections import namedtuple
import math

# Hatch types
HATCH_TYPES = ['///','...','\\\\\\','---']
# List of colors
COLORS = [
    (0, 0, 1, 0.2),
    (0, 0, 1, 0.4),
    (0, 0, 1, 0.6),
    (0, 0, 1, 1.0)
]

_Font_Size = 19


grpc_full = "mean-CV/gRPC_FullProcess_Mean_Median_Deviation.txt"
grpc_JC = "mean-CV/gRPC_JustCommunicationPart_Mean_Median_Deviation.txt"
grpc_JC_PL = "mean-CV/gRPC_JustCommunicationPart_PL_DL_Mean_Median_Deviation.txt"
gRPC_PL_DL = "mean-CV/gRPC_PL_DL_Mean_Median_Deviation.txt"
LRE = "mean-CV/LocalRuleEnforcement_Mean_Median_Deviation.txt"
netconf_full = "mean-CV/netconf_FullProcess_Mean_Median_Deviation.txt"
netconf_JC = "mean-CV/netconf_JustCommunicationPart_Mean_Median_Deviation.txt"
netconf_JC_PL = "mean-CV/netconf_JustCommunicationPart_PL_DL_Mean_Median_Deviation.txt"
netconf_PL_DL = "mean-CV/netconf_PL_DL_Mean_Median_Deviation.txt"
REST_full = "mean-CV/REST_FullProcess_Mean_Median_Deviation.txt"
REST_JC = "mean-CV/REST_JustCommunicationPart_Mean_Median_Deviation.txt"
REST_JC_PL = "mean-CV/REST_JustCommunicationPart_PL_DL_Mean_Median_Deviation.txt"
REST_PL_DL = "mean-CV/REST_PL_DL_Mean_Median_Deviation.txt"
SSH_full="mean-CV/SSH_FullProcess_Mean_Median_Deviation.txt"
SSH_JC="mean-CV/SSH_JustCommunicationPart_Mean_Median_Deviation.txt"
SSH_JC_PL="mean-CV/SSH_JustCommunicationPart_PL_DL_Mean_Median_Deviation.txt"
SSH_PL_DL="mean-CV/SSH_PL_DL_Mean_Median_Deviation.txt"

grpc_NLD = "mean-CV/grpc_NLD.txt"
rest_NLD = "mean-CV/rest_NLD.txt"
netconf_NLD = "mean-CV/netconf_NLD.txt"
ssh_NLD = "mean-CV/ssh_NLD.txt"

grpc_PL_DL = 'mean-CV/gRPC_'
REST_PL_DL = 'mean-CV/REST_'
netconf_PL_DL = 'mean-CV/NetConf_'
ssh_PL_DL = 'mean-CV/SSH_'

def ReadParameter(pathToFile, lineName, parameterName):
	f1 = open(pathToFile,'r')
	x = f1.read()
	f1.close()

	y = x.split('\n')
	#number of line for each element: add grpc\n cv=... \n \n del grpc
	lN=3
	n = len(y)/lN

	for i in range(0,n):
		if lineName in y[i*lN]:
			if parameterName=="Time miu:":
				miu = float(y[i*lN+1][10:19])
				print lineName, parameterName, miu
				return miu
			elif parameterName=="Coef of Var:":
				cv = (2 * float(y[i*lN+1].split(parameterName)[1])*float(y[i*lN+1][10:19]))/(math.sqrt(20) * 100)
				print lineName, parameterName, cv
				return cv

def bar_plot2(mean1,coefficientOfVariance1,name1, mean2,coefficientOfVariance2,name2, n_groups, group_names,bar_width, bar_plot2_title, bar_plot_name="NoSave"):
	plt.rcParams.update({'font.size': _Font_Size})

	fig, ax = plt.subplots()

	index = np.arange(n_groups)
	#bar_width = 0.35

	opacity = 1
	error_config = {'ecolor': '0.3'}

	rects1 = ax.bar(index, mean1, bar_width,
	                #alpha=opacity, color='b',
	                yerr=coefficientOfVariance1, error_kw=error_config,
	                label=name1,
	                edgecolor='black',hatch=HATCH_TYPES[0],capsize=3,color=COLORS[0])

	rects2 = ax.bar(index + bar_width, mean2, bar_width,
	                #alpha=opacity, color='r',
	                yerr=coefficientOfVariance2, error_kw=error_config,
	                label=name2,
	                edgecolor='black',hatch=HATCH_TYPES[1],capsize=3,color=COLORS[1])

	#ax.set_xlabel('Connection Type')
	ax.set_ylabel('Time (s)')
	#ax.set_title(bar_plot2_title)
	ax.set_xticks(index + bar_width / 2)
	ax.set_xticklabels(group_names)
	ax.legend()

	fig.tight_layout()
	if bar_plot_name != "NoSave":
		plt.savefig(bar_plot_name, bbox_inches='tight', pad_inches=0.0)
	else:
		plt.show()

def bar_plot4(mean1,cv1,name1, mean2,cv2,name2,mean3,cv3,name3, mean4,cv4,name4, n_groups, group_names, bar_width, bar_plot2_title,bar_plot_name="NoSave", max_axis=None):
	plt.rcParams.update({'font.size': _Font_Size})
	fig, ax = plt.subplots()

	index = np.arange(n_groups)

	opacity = 1
	error_config = {'ecolor': '0.3'}

	xxx = 1

	if max_axis != None:
		plt.ylim(max_axis)


	rects1 = ax.bar(index, mean1, bar_width/xxx,
	                #alpha=opacity, color='b',
	                yerr=cv1, error_kw=error_config,
	                label=name1,
	                edgecolor='black',hatch=HATCH_TYPES[0],capsize=3,color=COLORS[0])

	rects2 = ax.bar(index+bar_width, mean2, bar_width/xxx,
	                #alpha=opacity, color='r',
	                yerr=cv2, error_kw=error_config,
	                label=name2,
	                edgecolor='black',hatch=HATCH_TYPES[1],capsize=3,color=COLORS[1])

	rects3 = ax.bar(index+2*bar_width, mean3, bar_width/xxx,
	                #alpha=opacity, color='tab:brown',
	                yerr=cv3, error_kw=error_config,
	                label=name3,
	                edgecolor='black',hatch=HATCH_TYPES[2],capsize=3,color=COLORS[2])

	rects4 = ax.bar(index+3*bar_width, mean4, bar_width/xxx,
	                #alpha=opacity, color='m',
	                yerr=cv4, error_kw=error_config,
	                label=name4,
	                edgecolor='black',hatch=HATCH_TYPES[3],capsize=3,color=COLORS[3])

	#ax.set_xlabel('Connection Type')
	ax.set_ylabel('Time (s)')
	#ax.set_title(bar_plot2_title)
	ax.set_xticks(index + bar_width/xxx)
	ax.set_xticklabels(group_names)
	ax.legend()

	fig.tight_layout()
	if bar_plot_name != "NoSave":
		plt.savefig(bar_plot_name, bbox_inches='tight', pad_inches=0.0)
	else:
		plt.show()

# gRPC vs REST vs SSH vs NETCONF Full Process
bar_plot_name = "plots/Automatic-plotted/Full-Secure.pdf"
bar_plot2_title='Execution Time - Secured'
bar_width = 0.2
n_groups = 3
name1='gRPC'
means1 = (ReadParameter(grpc_full,"non persistent sequential, gRPC, Secure, add:","Time miu:"), ReadParameter(grpc_full,"persistent Conncection, gRPC, Secure, add:","Time miu:"),ReadParameter(grpc_full,"non persistent bulk, gRPC, Secure, add:","Time miu:"))
cv1 = ( ReadParameter(grpc_full,"non persistent sequential, gRPC, Secure, add:","Coef of Var:"), ReadParameter(grpc_full,"persistent Conncection, gRPC, Secure, add:","Coef of Var:"),ReadParameter(grpc_full,"non persistent bulk, gRPC, Secure, add:","Coef of Var:"))
name2='REST'
means2 = ( ReadParameter(REST_full,"non persistent sequential, rest, Secure, add:","Time miu:"), ReadParameter(REST_full,"persistent Conncection, rest, Secure, add:","Time miu:"),ReadParameter(REST_full,"non persistent bulk, rest, Secure, add:","Time miu:"))
cv2 = ( ReadParameter(REST_full,"non persistent sequential, rest, Secure, add:","Coef of Var:"), ReadParameter(REST_full,"persistent Conncection, rest, Secure, add:","Coef of Var:"),ReadParameter(REST_full,"non persistent bulk, rest, Secure, add:","Coef of Var:"))
name3 = 'NETCONF'
means3 = ( ReadParameter(netconf_full,"non persistent sequential, netconf, add:","Time miu:"), ReadParameter(netconf_full,"persistent Conncection, netconf, add:","Time miu:"),ReadParameter(netconf_full,"non persistent bulk, netconf, add:","Time miu:"))
cv3 = ( ReadParameter(netconf_full,"non persistent sequential, netconf, add:","Coef of Var:"), ReadParameter(netconf_full,"persistent Conncection, netconf, add:","Coef of Var:"),ReadParameter(netconf_full,"non persistent bulk, netconf, add:","Coef of Var:"))
name4 = 'SSH'
means4 = ( ReadParameter(SSH_full,"non persistent sequential, SSH, add:","Time miu:"), ReadParameter(SSH_full,"persistent Conncection, SSH, add:","Time miu:"),ReadParameter(SSH_full,"non persistent bulk, SSH, add:","Time miu:"))
cv4 = ( ReadParameter(SSH_full,"non persistent sequential, SSH, add:","Coef of Var:"), ReadParameter(SSH_full,"persistent Conncection, SSH, add:","Coef of Var:"),ReadParameter(SSH_full,"non persistent bulk, SSH, add:","Coef of Var:"))
#group_names = ('Blk', 'PtC','NPC')
group_names = ('NP-Conn-Seq', 'P-Conn','NP-Bulk')
bar_plot4(means1,cv1,name1, means2,cv2,name2,means3,cv3,name3, means4,cv4,name4, n_groups,group_names,bar_width,bar_plot2_title,bar_plot_name)

# Zoomed (y axis between 0, 3)- gRPC vs REST vs SSH vs NETCONF Full Process
bar_plot_name = "plots/Automatic-plotted/Full-Secure-zoomed.pdf"
bar_plot2_title='Zoomed (y axis between 0, 3)- Execution Time - Secured'
bar_width = 0.2
n_groups = 3
name1='gRPC'
means1 = (ReadParameter(grpc_full,"non persistent sequential, gRPC, Secure, add:","Time miu:"), ReadParameter(grpc_full,"persistent Conncection, gRPC, Secure, add:","Time miu:"),ReadParameter(grpc_full,"non persistent bulk, gRPC, Secure, add:","Time miu:"))
cv1 = ( ReadParameter(grpc_full,"non persistent sequential, gRPC, Secure, add:","Coef of Var:"), ReadParameter(grpc_full,"persistent Conncection, gRPC, Secure, add:","Coef of Var:"),ReadParameter(grpc_full,"non persistent bulk, gRPC, Secure, add:","Coef of Var:"))
name2='REST'
means2 = ( ReadParameter(REST_full,"non persistent sequential, rest, Secure, add:","Time miu:"), ReadParameter(REST_full,"persistent Conncection, rest, Secure, add:","Time miu:"),ReadParameter(REST_full,"non persistent bulk, rest, Secure, add:","Time miu:"))
cv2 = ( ReadParameter(REST_full,"non persistent sequential, rest, Secure, add:","Coef of Var:"), ReadParameter(REST_full,"persistent Conncection, rest, Secure, add:","Coef of Var:"),ReadParameter(REST_full,"non persistent bulk, rest, Secure, add:","Coef of Var:"))
name3 = 'NETCONF'
means3 = ( ReadParameter(netconf_full,"non persistent sequential, netconf, add:","Time miu:"), ReadParameter(netconf_full,"persistent Conncection, netconf, add:","Time miu:"),ReadParameter(netconf_full,"non persistent bulk, netconf, add:","Time miu:"))
cv3 = ( ReadParameter(netconf_full,"non persistent sequential, netconf, add:","Coef of Var:"), ReadParameter(netconf_full,"persistent Conncection, netconf, add:","Coef of Var:"),ReadParameter(netconf_full,"non persistent bulk, netconf, add:","Coef of Var:"))
name4 = 'SSH'
means4 = ( ReadParameter(SSH_full,"non persistent sequential, SSH, add:","Time miu:"), ReadParameter(SSH_full,"persistent Conncection, SSH, add:","Time miu:"),ReadParameter(SSH_full,"non persistent bulk, SSH, add:","Time miu:"))
cv4 = ( ReadParameter(SSH_full,"non persistent sequential, SSH, add:","Coef of Var:"), ReadParameter(SSH_full,"persistent Conncection, SSH, add:","Coef of Var:"),ReadParameter(SSH_full,"non persistent bulk, SSH, add:","Coef of Var:"))
#group_names = ('Blk', 'PtC','NPC')
group_names = ('NP-Conn-Seq', 'P-Conn','NP-Bulk')
bar_plot4(means1,cv1,name1, means2,cv2,name2,means3,cv3,name3, means4,cv4,name4, n_groups,group_names,bar_width,bar_plot2_title,bar_plot_name,[0,2])

# gRPC vs REST vs SSH vs NETCONF (just communication)
bar_plot_name = "plots/Automatic-plotted/Communication-secure.pdf"
bar_plot2_title='Communication Time (without local rule enforcment) - Secured'
bar_width = 0.2
n_groups = 3
name1='gRPC'
means1 = (ReadParameter(grpc_JC,"non persistent sequential, gRPC, Secure,  add:","Time miu:"), ReadParameter(grpc_JC,"persistent Conncection, gRPC, Secure,  add:","Time miu:"),ReadParameter(grpc_JC,"non persistent bulk, gRPC, Secure,  add:","Time miu:"))
cv1 = ( ReadParameter(grpc_JC,"non persistent sequential, gRPC, Secure,  add:","Coef of Var:"), ReadParameter(grpc_JC,"persistent Conncection, gRPC, Secure,  add:","Coef of Var:"),ReadParameter(grpc_JC,"non persistent bulk, gRPC, Secure,  add:","Coef of Var:"))
name2='REST'
means2 = ( ReadParameter(REST_JC,"non persistent sequential, rest, Secure, add:","Time miu:"), ReadParameter(REST_JC,"persistent Conncection, rest, Secure, add:","Time miu:"),ReadParameter(REST_JC,"non persistent bulk, rest, Secure, add:","Time miu:"))
cv2 = ( ReadParameter(REST_JC,"non persistent sequential, rest, Secure, add:","Coef of Var:"), ReadParameter(REST_JC,"persistent Conncection, rest, Secure, add:","Coef of Var:"),ReadParameter(REST_JC,"non persistent bulk, rest, Secure, add:","Coef of Var:"))
name3 = 'NETCONF'
means3 = ( ReadParameter(netconf_JC,"non persistent sequential, netconf, add:","Time miu:"), ReadParameter(netconf_JC,"persistent Conncection, netconf, add:","Time miu:"),ReadParameter(netconf_JC,"non persistent bulk, netconf, add:","Time miu:"))
cv3 = ( ReadParameter(netconf_JC,"non persistent sequential, netconf, add:","Coef of Var:"), ReadParameter(netconf_JC,"persistent Conncection, netconf, add:","Coef of Var:"),ReadParameter(netconf_JC,"non persistent bulk, netconf, add:","Coef of Var:"))
name4 = 'SSH'
means4 = ( ReadParameter(SSH_JC,"non persistent sequential, SSH, add:","Time miu:"), ReadParameter(SSH_JC,"persistent Conncection, SSH, add:","Time miu:"),ReadParameter(SSH_JC,"non persistent bulk, SSH, add:","Time miu:"))
cv4 = ( ReadParameter(SSH_JC,"non persistent sequential, SSH, add:","Coef of Var:"), ReadParameter(SSH_JC,"persistent Conncection, SSH, add:","Coef of Var:"),ReadParameter(SSH_JC,"non persistent bulk, SSH, add:","Coef of Var:"))
#group_names = ('NP-Bulk', 'Pt C', 'N Pt C')
#group_names = ('NP-Bulk', 'Persistent Con.','None Persistent Con.')
group_names = ('NP-Conn-Seq', 'P-Conn','NP-Bulk')
bar_plot4(means1,cv1,name1, means2,cv2,name2,means3,cv3,name3, means4,cv4,name4, n_groups,group_names,bar_width,bar_plot2_title,bar_plot_name)

# Zoomed (y axis between 0, 3)- gRPC vs REST vs SSH vs NETCONF (just communication)
bar_plot_name = "plots/Automatic-plotted/Communication-secure-zoomed.pdf"
bar_plot2_title='Zoomed (y axis between 0, 3)- Communication Time (without local rule enforcment) - Secured'
bar_width = 0.2
n_groups = 3
name1='gRPC'
means1 = (ReadParameter(grpc_JC,"non persistent sequential, gRPC, Secure,  add:","Time miu:"), ReadParameter(grpc_JC,"persistent Conncection, gRPC, Secure,  add:","Time miu:"),ReadParameter(grpc_JC,"non persistent bulk, gRPC, Secure,  add:","Time miu:"))
cv1 = ( ReadParameter(grpc_JC,"non persistent sequential, gRPC, Secure,  add:","Coef of Var:"), ReadParameter(grpc_JC,"persistent Conncection, gRPC, Secure,  add:","Coef of Var:"),ReadParameter(grpc_JC,"non persistent bulk, gRPC, Secure,  add:","Coef of Var:"))
name2='REST'
means2 = ( ReadParameter(REST_JC,"non persistent sequential, rest, Secure, add:","Time miu:"), ReadParameter(REST_JC,"persistent Conncection, rest, Secure, add:","Time miu:"),ReadParameter(REST_JC,"non persistent bulk, rest, Secure, add:","Time miu:"))
cv2 = ( ReadParameter(REST_JC,"non persistent sequential, rest, Secure, add:","Coef of Var:"), ReadParameter(REST_JC,"persistent Conncection, rest, Secure, add:","Coef of Var:"),ReadParameter(REST_JC,"non persistent bulk, rest, Secure, add:","Coef of Var:"))
name3 = 'NETCONF'
means3 = ( ReadParameter(netconf_JC,"non persistent sequential, netconf, add:","Time miu:"), ReadParameter(netconf_JC,"persistent Conncection, netconf, add:","Time miu:"),ReadParameter(netconf_JC,"non persistent bulk, netconf, add:","Time miu:"))
cv3 = ( ReadParameter(netconf_JC,"non persistent sequential, netconf, add:","Coef of Var:"), ReadParameter(netconf_JC,"persistent Conncection, netconf, add:","Coef of Var:"),ReadParameter(netconf_JC,"non persistent bulk, netconf, add:","Coef of Var:"))
name4 = 'SSH'
means4 = ( ReadParameter(SSH_JC,"non persistent sequential, SSH, add:","Time miu:"), ReadParameter(SSH_JC,"persistent Conncection, SSH, add:","Time miu:"),ReadParameter(SSH_JC,"non persistent bulk, SSH, add:","Time miu:"))
cv4 = ( ReadParameter(SSH_JC,"non persistent sequential, SSH, add:","Coef of Var:"), ReadParameter(SSH_JC,"persistent Conncection, SSH, add:","Coef of Var:"),ReadParameter(SSH_JC,"non persistent bulk, SSH, add:","Coef of Var:"))
#group_names = ('NP-Bulk', 'Pt C', 'N Pt C')
#group_names = ('NP-Bulk', 'Persistent Con.','None Persistent Con.')
group_names = ('NP-Conn-Seq', 'P-Conn','NP-Bulk')
bar_plot4(means1,cv1,name1, means2,cv2,name2,means3,cv3,name3, means4,cv4,name4, n_groups,group_names,bar_width,bar_plot2_title,bar_plot_name,[0,1.5])

# gRPC vs REST (insecure, Full)
bar_plot_name = "plots/Automatic-plotted/Full-insecure.pdf"
bar_plot2_title='Execution Time - Insecure'
bar_width = 0.35
n_groups = 3
name1='gRPC'
means1 = (ReadParameter(grpc_full,"non persistent sequential, gRPC, Insecure, add:","Time miu:"), ReadParameter(grpc_full,"persistent Conncection, gRPC, Insecure, add:","Time miu:"),ReadParameter(grpc_full,"non persistent bulk, gRPC, Insecure, add:","Time miu:"))
coefficientOfVariance1 = ( ReadParameter(grpc_full,"non persistent sequential, gRPC, Insecure, add:","Coef of Var:"), ReadParameter(grpc_full,"persistent Conncection, gRPC, Insecure, add:","Coef of Var:"),ReadParameter(grpc_full,"non persistent bulk, gRPC, Insecure, add:","Coef of Var:"))
name2='REST'
means2 = ( ReadParameter(REST_full,"non persistent sequential, rest, Insecure, add:","Time miu:"), ReadParameter(REST_full,"persistent Conncection, rest, Insecure, add:","Time miu:"),ReadParameter(REST_full,"non persistent bulk, rest, Insecure, add:","Time miu:"))
coefficientOfVariance2 = ( ReadParameter(REST_full,"non persistent sequential, rest, Insecure, add:","Coef of Var:"), ReadParameter(REST_full,"persistent Conncection, rest, Insecure, add:","Coef of Var:"),ReadParameter(REST_full,"non persistent bulk, rest, Insecure, add:","Coef of Var:"))
#group_names = ('NP-Bulk', 'Persistent Con.','None Persistent Con.')
group_names = ('NP-Conn-Seq', 'P-Conn','NP-Bulk')
bar_plot2(means1,coefficientOfVariance1,name1, means2,coefficientOfVariance2,name2, n_groups,group_names,bar_width,bar_plot2_title,bar_plot_name)

# gRPC vs REST (insecure, just communication)
bar_plot_name = "plots/Automatic-plotted/communication-insecure.pdf"
bar_plot2_title='Communication Time (without local rule enforcment) - Insecure'
bar_width = 0.35
n_groups = 3
name1='gRPC'
means1 = (ReadParameter(grpc_JC,"non persistent sequential, gRPC, Insecure, add:","Time miu:"), ReadParameter(grpc_JC,"persistent Conncection, gRPC, Insecure, add:","Time miu:"),ReadParameter(grpc_JC,"non persistent bulk, gRPC, Insecure, add:","Time miu:"))
coefficientOfVariance1 = ( ReadParameter(grpc_JC,"non persistent sequential, gRPC, Insecure, add:","Coef of Var:"), ReadParameter(grpc_JC,"persistent Conncection, gRPC, Insecure, add:","Coef of Var:"),ReadParameter(grpc_JC,"non persistent bulk, gRPC, Insecure, add:","Coef of Var:"))
name2='REST'
means2 = ( ReadParameter(REST_JC,"non persistent sequential, rest, Insecure, add:","Time miu:"), ReadParameter(REST_JC,"persistent Conncection, rest, Insecure, add:","Time miu:"),ReadParameter(REST_JC,"non persistent bulk, rest, Insecure, add:","Time miu:"))
coefficientOfVariance2 = ( ReadParameter(REST_JC,"non persistent sequential, rest, Insecure, add:","Coef of Var:"), ReadParameter(REST_JC,"persistent Conncection, rest, Insecure, add:","Coef of Var:"),ReadParameter(REST_JC,"non persistent bulk, rest, Insecure, add:","Coef of Var:"))
#group_names = ('NP-Bulk', 'Persistent Con.','None Persistent Con.')
group_names = ('NP-Conn-Seq', 'P-Conn','NP-Bulk')
bar_plot2(means1,coefficientOfVariance1,name1, means2,coefficientOfVariance2,name2, n_groups,group_names,bar_width,bar_plot2_title,bar_plot_name)


################### 2% packet loss and 150 ms delay ################################
bar_plot_name = "plots/Automatic-plotted/NLD_secured.pdf"
bar_plot2_title='Execution Time - Secured - NLD'
bar_width = 0.2
n_groups = 3
name1='gRPC'
means1 = ( ReadParameter(grpc_NLD,"persistent Conncection, gRPC -0, add:","Time miu:"), ReadParameter(grpc_NLD,"persistent Conncection, gRPC-0.5, add:","Time miu:"),ReadParameter(grpc_NLD,"persistent Conncection, gRPC-1, add:","Time miu:"))
cv1 = ( ReadParameter(grpc_NLD,"persistent Conncection, gRPC -0, add:","Coef of Var:"), ReadParameter(grpc_NLD,"persistent Conncection, gRPC-0.5, add:","Coef of Var:"),ReadParameter(grpc_NLD,"persistent Conncection, gRPC-1, add:","Coef of Var:"))
name2='REST'
means2 = ( ReadParameter(rest_NLD,"persistent Conncection, rest-0, add:","Time miu:"), ReadParameter(rest_NLD,"persistent Conncection, rest-0.5, add:","Time miu:"),ReadParameter(rest_NLD,"persistent Conncection, rest-1,  add:","Time miu:"))
cv2 = ( ReadParameter(rest_NLD,"persistent Conncection, rest-0, add:","Coef of Var:"), ReadParameter(rest_NLD,"persistent Conncection, rest-0.5, add:","Coef of Var:"),ReadParameter(rest_NLD,"persistent Conncection, rest-1,  add:","Coef of Var:"))
name3 = 'NETCONF'
means3 = ( ReadParameter(netconf_NLD,"persistent Conncection, netconf-0, add:","Time miu:"), ReadParameter(netconf_NLD,"persistent Conncection, netconf-0.5, add:","Time miu:"),ReadParameter(netconf_NLD,"persistent Conncection, netconf-1, add:","Time miu:"))
cv3 = ( ReadParameter(netconf_NLD,"persistent Conncection, netconf-0, add:","Coef of Var:"), ReadParameter(netconf_NLD,"persistent Conncection, netconf-0.5, add:","Coef of Var:"),ReadParameter(netconf_NLD,"persistent Conncection, netconf-1, add:","Coef of Var:"))
name4 = 'SSH'
means4 = ( ReadParameter(ssh_NLD,"persistent Conncection, SSH-0, add:","Time miu:"), ReadParameter(ssh_NLD,"persistent Conncection, SSH-0.5,add:","Time miu:"),ReadParameter(ssh_NLD,"persistent Conncection, SSH-1,  add:","Time miu:"))
cv4 = ( ReadParameter(ssh_NLD,"persistent Conncection, SSH-0, add:","Coef of Var:"), ReadParameter(ssh_NLD,"persistent Conncection, SSH-0.5,add:","Coef of Var:"),ReadParameter(ssh_NLD,"persistent Conncection, SSH-1,  add:","Coef of Var:"))
#group_names = ('Blk', 'PtC','NPC')
#group_names = ('NP-Bulk', 'Persistent Con.','None Persistent Con.')
group_names = ('0% PL', '0.5% PL','1% PL')
bar_plot4(means1,cv1,name1, means2,cv2,name2,means3,cv3,name3, means4,cv4,name4, n_groups,group_names,bar_width,bar_plot2_title,bar_plot_name)

"""
################### 2% packet loss and 150 ms delay ################################
bar_plot_name = "plots/Automatic-plotted/NLD_Insecure.pdf"
bar_plot2_title='Execution Time - Secured - NLD'
bar_width = 0.2
n_groups = 3
name1='gRPC'
means1 = ( ReadParameter(grpc_NLDgrpc_NLD,"persistent Conncection, gRPC-0.1, add:","Time miu:"), ReadParameter(grpc_NLD,"persistent Conncection, gRPC-0.5, add:","Time miu:"),ReadParameter(grpc_NLD,"persistent Conncection, gRPC-1, add:","Time miu:"))
cv1 = ( ReadParameter(grpc_NLD,"persistent Conncection, gRPC-0.1, add:","Coef of Var:"), ReadParameter(grpc_NLD,"persistent Conncection, gRPC-0.5, add:","Coef of Var:"),ReadParameter(grpc_NLD,"persistent Conncection, gRPC-1, add:","Coef of Var:"))
name2='REST'
means2 = ( ReadParameter(rest_NLD,"persistent Conncection, rest-0.1,  add:","Time miu:"), ReadParameter(rest_NLD,"persistent Conncection, rest-0.5, add:","Time miu:"),ReadParameter(rest_NLD,"persistent Conncection, rest-1,  add:","Time miu:"))
cv2 = ( ReadParameter(rest_NLD,"persistent Conncection, rest-0.1,  add:","Coef of Var:"), ReadParameter(rest_NLD,"persistent Conncection, rest-0.5, add:","Coef of Var:"),ReadParameter(rest_NLD,"persistent Conncection, rest-1,  add:","Coef of Var:"))
name3 = 'NETCONF'
means3 = ( ReadParameter(netconf_NLD,"persistent Conncection, netconf-0.1, add:","Time miu:"), ReadParameter(netconf_NLD,"persistent Conncection, netconf-0.5, add:","Time miu:"),ReadParameter(netconf_NLD,"persistent Conncection, netconf-1, add:","Time miu:"))
cv3 = ( ReadParameter(netconf_NLD,"persistent Conncection, netconf-0.1, add:","Coef of Var:"), ReadParameter(netconf_NLD,"persistent Conncection, netconf-0.5, add:"),ReadParameter(netconf_NLD,"persistent Conncection, netconf-1, add:","Coef of Var:"))
name4 = 'SSH'
means4 = ( ReadParameter(ssh_NLD,"persistent Conncection, SSH-0.1, add:","Time miu:"), ReadParameter(ssh_NLD,"persistent Conncection, SSH-0.5,add:","Time miu:"),ReadParameter(ssh_NLD,"persistent Conncection, SSH-1,  add:","Time miu:"))
cv4 = ( ReadParameter(ssh_NLD,"persistent Conncection, SSH-0.1, add:","Coef of Var:"), ReadParameter(ssh_NLD,"persistent Conncection, SSH-0.5,add:","Coef of Var:"),ReadParameter(ssh_NLD,"persistent Conncection, SSH-1,  add:","Coef of Var:"))
#group_names = ('Blk', 'PtC','NPC')
#group_names = ('NP-Bulk', 'Persistent Con.','None Persistent Con.')
group_names = ('0% PL', '0.5% PL','1% PL')
bar_plot4(means1,cv1,name1, means2,cv2,name2,means3,cv3,name3, means4,cv4,name4, n_groups,group_names,bar_width,bar_plot2_title)
"""

################### different packet loss and 150 ms delay ################################
bar_plot_name = "plots/Automatic-plotted/PL_DL_secured.pdf"
bar_plot2_title='Execution Time - Secured - PL_DL'
bar_width = 0.2
n_groups = 4
name1='gRPC'
(tmp1,tmp2,tmp3) = ("persistent Conncection, gRPC , add:","Time miu:",'PL_75ms.txt')
means1 = ( ReadParameter(grpc_PL_DL+'0'+tmp3,tmp1,tmp2),ReadParameter(grpc_PL_DL+'0.5'+tmp3,tmp1,tmp2),ReadParameter(grpc_PL_DL+'1'+tmp3,tmp1,tmp2),ReadParameter(grpc_PL_DL+'2'+tmp3,tmp1,tmp2))
tmp2 = "Coef of Var:"
cv1 = ( ReadParameter(grpc_PL_DL+'0'+tmp3,tmp1,tmp2),ReadParameter(grpc_PL_DL+'0.5'+tmp3,tmp1,tmp2),ReadParameter(grpc_PL_DL+'1'+tmp3,tmp1,tmp2),ReadParameter(grpc_PL_DL+'2'+tmp3,tmp1,tmp2))

name2='REST'
(tmp1,tmp2,tmp3) = ("persistent Conncection, rest, add:","Time miu:",'PL_75ms.txt')
means2 = ( ReadParameter(REST_PL_DL+'0'+tmp3,tmp1,tmp2),ReadParameter(REST_PL_DL+'0.5'+tmp3,tmp1,tmp2),ReadParameter(REST_PL_DL+'1'+tmp3,tmp1,tmp2),ReadParameter(REST_PL_DL+'2'+tmp3,tmp1,tmp2))
tmp2 = "Coef of Var:"
cv2 = ( ReadParameter(REST_PL_DL+'0'+tmp3,tmp1,tmp2),ReadParameter(REST_PL_DL+'0.5'+tmp3,tmp1,tmp2),ReadParameter(REST_PL_DL+'1'+tmp3,tmp1,tmp2),ReadParameter(REST_PL_DL+'2'+tmp3,tmp1,tmp2))

name3 = 'NETCONF'
(tmp1,tmp2,tmp3) = ("persistent Conncection, netconf, add:","Time miu:",'PL_75ms.txt')
means3 = ( ReadParameter(netconf_PL_DL+'0'+tmp3,tmp1,tmp2),ReadParameter(netconf_PL_DL+'0.5'+tmp3,tmp1,tmp2),ReadParameter(netconf_PL_DL+'1'+tmp3,tmp1,tmp2),ReadParameter(netconf_PL_DL+'2'+tmp3,tmp1,tmp2))
tmp2 = "Coef of Var:"
cv3 = ( ReadParameter(netconf_PL_DL+'0'+tmp3,tmp1,tmp2),ReadParameter(netconf_PL_DL+'0.5'+tmp3,tmp1,tmp2),ReadParameter(netconf_PL_DL+'1'+tmp3,tmp1,tmp2),ReadParameter(netconf_PL_DL+'2'+tmp3,tmp1,tmp2))

name4 = 'SSH'
(tmp1,tmp2,tmp3) = ("persistent Conncection, SSH, add:","Time miu:",'PL_75ms.txt')
means4 = ( ReadParameter(ssh_PL_DL+'0'+tmp3,tmp1,tmp2),ReadParameter(ssh_PL_DL+'0.5'+tmp3,tmp1,tmp2),ReadParameter(ssh_PL_DL+'1'+tmp3,tmp1,tmp2),ReadParameter(ssh_PL_DL+'2'+tmp3,tmp1,tmp2))
tmp2 = "Coef of Var:"
cv4 = ( ReadParameter(ssh_PL_DL+'0'+tmp3,tmp1,tmp2),ReadParameter(ssh_PL_DL+'0.5'+tmp3,tmp1,tmp2),ReadParameter(ssh_PL_DL+'1'+tmp3,tmp1,tmp2),ReadParameter(ssh_PL_DL+'2'+tmp3,tmp1,tmp2))

#group_names = ('Blk', 'PtC','NPC')
#group_names = ('NP-Bulk', 'Persistent Con.','None Persistent Con.')
group_names = ('0% PL', '0.5% PL','1% PL','2% PL')
bar_plot4(means1,cv1,name1, means2,cv2,name2,means3,cv3,name3, means4,cv4,name4, n_groups,group_names,bar_width,bar_plot2_title,bar_plot_name)

###################  Zoomed (y axis between 15, 20)- different packet loss and 150 ms delay ################################
bar_plot_name = "plots/Automatic-plotted/PL_DL_secured_zoomed.pdf"
bar_plot2_title='Execution Time - Secured - PL_DL'
bar_width = 0.2
n_groups = 4
name1='gRPC'
(tmp1,tmp2,tmp3) = ("persistent Conncection, gRPC , add:","Time miu:",'PL_75ms.txt')
means1 = ( ReadParameter(grpc_PL_DL+'0'+tmp3,tmp1,tmp2),ReadParameter(grpc_PL_DL+'0.5'+tmp3,tmp1,tmp2),ReadParameter(grpc_PL_DL+'1'+tmp3,tmp1,tmp2),ReadParameter(grpc_PL_DL+'2'+tmp3,tmp1,tmp2))
tmp2 = "Coef of Var:"
cv1 = ( ReadParameter(grpc_PL_DL+'0'+tmp3,tmp1,tmp2),ReadParameter(grpc_PL_DL+'0.5'+tmp3,tmp1,tmp2),ReadParameter(grpc_PL_DL+'1'+tmp3,tmp1,tmp2),ReadParameter(grpc_PL_DL+'2'+tmp3,tmp1,tmp2))

name2='REST'
(tmp1,tmp2,tmp3) = ("persistent Conncection, rest, add:","Time miu:",'PL_75ms.txt')
means2 = ( ReadParameter(REST_PL_DL+'0'+tmp3,tmp1,tmp2),ReadParameter(REST_PL_DL+'0.5'+tmp3,tmp1,tmp2),ReadParameter(REST_PL_DL+'1'+tmp3,tmp1,tmp2),ReadParameter(REST_PL_DL+'2'+tmp3,tmp1,tmp2))
tmp2 = "Coef of Var:"
cv2 = ( ReadParameter(REST_PL_DL+'0'+tmp3,tmp1,tmp2),ReadParameter(REST_PL_DL+'0.5'+tmp3,tmp1,tmp2),ReadParameter(REST_PL_DL+'1'+tmp3,tmp1,tmp2),ReadParameter(REST_PL_DL+'2'+tmp3,tmp1,tmp2))

name3 = 'NETCONF'
(tmp1,tmp2,tmp3) = ("persistent Conncection, netconf, add:","Time miu:",'PL_75ms.txt')
means3 = ( ReadParameter(netconf_PL_DL+'0'+tmp3,tmp1,tmp2),ReadParameter(netconf_PL_DL+'0.5'+tmp3,tmp1,tmp2),ReadParameter(netconf_PL_DL+'1'+tmp3,tmp1,tmp2),ReadParameter(netconf_PL_DL+'2'+tmp3,tmp1,tmp2))
tmp2 = "Coef of Var:"
cv3 = ( ReadParameter(netconf_PL_DL+'0'+tmp3,tmp1,tmp2),ReadParameter(netconf_PL_DL+'0.5'+tmp3,tmp1,tmp2),ReadParameter(netconf_PL_DL+'1'+tmp3,tmp1,tmp2),ReadParameter(netconf_PL_DL+'2'+tmp3,tmp1,tmp2))

name4 = 'SSH'
(tmp1,tmp2,tmp3) = ("persistent Conncection, SSH, add:","Time miu:",'PL_75ms.txt')
means4 = ( ReadParameter(ssh_PL_DL+'0'+tmp3,tmp1,tmp2),ReadParameter(ssh_PL_DL+'0.5'+tmp3,tmp1,tmp2),ReadParameter(ssh_PL_DL+'1'+tmp3,tmp1,tmp2),ReadParameter(ssh_PL_DL+'2'+tmp3,tmp1,tmp2))
tmp2 = "Coef of Var:"
cv4 = ( ReadParameter(ssh_PL_DL+'0'+tmp3,tmp1,tmp2),ReadParameter(ssh_PL_DL+'0.5'+tmp3,tmp1,tmp2),ReadParameter(ssh_PL_DL+'1'+tmp3,tmp1,tmp2),ReadParameter(ssh_PL_DL+'2'+tmp3,tmp1,tmp2))

#group_names = ('Blk', 'PtC','NPC')
#group_names = ('NP-Bulk', 'Persistent Con.','None Persistent Con.')
group_names = ('0% PL', '0.5% PL','1% PL','2% PL')
bar_plot4(means1,cv1,name1, means2,cv2,name2,means3,cv3,name3, means4,cv4,name4, n_groups,group_names,bar_width,bar_plot2_title,bar_plot_name,[15,20])