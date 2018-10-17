import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from collections import namedtuple

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

def bar_plot2(mean1,coefficientOfVariance1,name1, mean2,coefficientOfVariance2,name2, n_groups, group_names,bar_width, bar_plot2_title):
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
	plt.show()


def bar_plot4(mean1,cv1,name1, mean2,cv2,name2,mean3,cv3,name3, mean4,cv4,name4, n_groups, group_names, bar_width, bar_plot2_title,max_axis=None):
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
	plt.show()


# gRPC vs REST vs SSH vs NETCONF Full Process
bar_plot2_title='Execution Time - Secured'
bar_width = 0.2
n_groups = 3
name1='gRPC'
means1 = ( 1.82265, 0.27954,0.1342)
cv1 = ( 1.07786161724, 0.0165551349664,0.00732826583043)
name2='REST'
means2 = ( 1.11318, 0.3765,0.12653)
cv2 = ( 0.191820307841, 0.00363757481365,0.00932573788992)
name3 = 'NETCONF'
means3 = ( 24.06637, 0.56135,0.3211)
cv3 = ( 1.87328011202e-07, 0.0611907636118,0.0361465510527)
name4 = 'SSH'
means4 = ( 19.73675, 12.19783,0.5776)
cv4 = ( 6.99272111464e-08, 0.0758002010783,0.126988365172)
#group_names = ('Blk', 'PtC','NPC')
group_names = ('NP-Conn-Seq', 'P-Conn','NP-Bulk')
bar_plot4(means1,cv1,name1, means2,cv2,name2,means3,cv3,name3, means4,cv4,name4, n_groups,group_names,bar_width,bar_plot2_title)

# Zoomed (y axis between 0, 3)- gRPC vs REST vs SSH vs NETCONF Full Process
bar_plot2_title='Zoomed (y axis between 0, 3)- Execution Time - Secured'
bar_width = 0.2
n_groups = 3
name1='gRPC'
means1 = ( 1.82265, 0.27954,0.1342)
cv1 = ( 1.07786161724, 0.0165551349664,0.00732826583043)
name2='REST'
means2 = ( 1.11318, 0.3765,0.12653)
cv2 = ( 0.191820307841, 0.00363757481365,0.00932573788992)
name3 = 'NETCONF'
means3 = ( 24.06637, 0.56135,0.3211)
cv3 = ( 1.87328011202e-07, 0.0611907636118,0.0361465510527)
name4 = 'SSH'
means4 = ( 19.73675, 12.19783,0.5776)
cv4 = ( 6.99272111464e-08, 0.0758002010783,0.126988365172)
#group_names = ('Blk', 'PtC','NPC')
group_names = ('NP-Conn-Seq', 'P-Conn','NP-Bulk')
bar_plot4(means1,cv1,name1, means2,cv2,name2,means3,cv3,name3, means4,cv4,name4, n_groups,group_names,bar_width,bar_plot2_title,[0,3])

# gRPC vs REST vs SSH vs NETCONF (just communication)
bar_plot2_title='Communication Time (without local rule enforcment) - Secured'
bar_width = 0.2
n_groups = 3
name1='gRPC'
means1 = ( 1.39552, 0.11602,0.01914)
cv1 = ( 1.07786161724, 0.0165551349664,0.00732826583043)
name2='REST'
means2 = ( 1.11318, 0.3765,0.12653)
cv2 = ( 0.191820307841, 0.00363757481365,0.00932573788992)
name3 = 'NETCONF'
means3 = ( 24.06637, 0.56135,0.3211)
cv3 = ( 1.87328011202e-07, 0.0611907636118,0.0361465510527)
name4 = 'SSH'
means4 = ( 19.73675, 12.19783,0.5776)
cv4 = ( 6.99272111464e-08, 0.0758002010783,0.126988365172)
#group_names = ('NP-Bulk', 'Pt C', 'N Pt C')
#group_names = ('NP-Bulk', 'Persistent Con.','None Persistent Con.')
group_names = ('NP-Conn-Seq', 'P-Conn','NP-Bulk')
bar_plot4(means1,cv1,name1, means2,cv2,name2,means3,cv3,name3, means4,cv4,name4, n_groups,group_names,bar_width,bar_plot2_title)

# Zoomed (y axis between 0, 3)- gRPC vs REST vs SSH vs NETCONF (just communication)
bar_plot2_title='Zoomed (y axis between 0, 3)- Communication Time (without local rule enforcment) - Secured'
bar_width = 0.2
n_groups = 3
name1='gRPC'
means1 = ( 1.39552, 0.11602,0.01914)
cv1 = ( 1.07786161724, 0.0165551349664,0.00732826583043)
name2='REST'
means2 = ( 1.11318, 0.3765,0.12653)
cv2 = ( 0.191820307841, 0.00363757481365,0.00932573788992)
name3 = 'NETCONF'
means3 = ( 24.06637, 0.56135,0.3211)
cv3 = ( 1.87328011202e-07, 0.0611907636118,0.0361465510527)
name4 = 'SSH'
means4 = ( 19.73675, 12.19783,0.5776)
cv4 = ( 6.99272111464e-08, 0.0758002010783,0.126988365172)
#group_names = ('NP-Bulk', 'Pt C', 'N Pt C')
#group_names = ('NP-Bulk', 'Persistent Con.','None Persistent Con.')
group_names = ('NP-Conn-Seq', 'P-Conn','NP-Bulk')
bar_plot4(means1,cv1,name1, means2,cv2,name2,means3,cv3,name3, means4,cv4,name4, n_groups,group_names,bar_width,bar_plot2_title,[0,3])

# gRPC vs REST (insecure, Full)
bar_plot2_title='Execution Time - Insecure'
bar_width = 0.35
n_groups = 3
name1='gRPC'
means1 = ( 0.33274, 0.20206,0.08692)
coefficientOfVariance1 = ( 7.68834121255e-18, 0.0320187064025,0.00484677021343)
name2='REST'
means2 = ( 0.42698, 0.33415,0.06938)
coefficientOfVariance2 = ( 9.07152256981e-18, 0.00367518423844,0.00011313622036)
#group_names = ('NP-Bulk', 'Persistent Con.','None Persistent Con.')
group_names = ('NP-Conn-Seq', 'P-Conn','NP-Bulk')
bar_plot2(means1,coefficientOfVariance1,name1, means2,coefficientOfVariance2,name2, n_groups,group_names,bar_width,bar_plot2_title)

# gRPC vs REST (insecure, just communication)
bar_plot2_title='Communication Time (without local rule enforcment) - Insecure'
bar_width = 0.35
n_groups = 3
name1='gRPC'
means1 = ( 0.23556, 0.0985,0.0054)
coefficientOfVariance1 = ( 6.47905686073e-19, 5.38891551346e-05,1.11692776585e-05)
name2='REST'
means2 = (0.40588, 0.275, 0.00843)
coefficientOfVariance2 = (4.08867586157e-19, 0.00011303918589, 1.2800700219e-05)
#group_names = ('NP-Bulk', 'Persistent Con.','None Persistent Con.')
group_names = ('NP-Conn-Seq', 'P-Conn','NP-Bulk')
bar_plot2(means1,coefficientOfVariance1,name1, means2,coefficientOfVariance2,name2, n_groups,group_names,bar_width,bar_plot2_title)

################### 2% packet loss and 150 ms delay ################################
bar_plot2_title='Execution Time - Secured - NLD'
bar_width = 0.2
n_groups = 3
name1='gRPC'
means1 = (68.04323, 17.13084, 0.75429)
cv1 = (0.00534340949219, 6.42335844745, 0.01337183679)
name2='REST'
means2 = (66.25726, 17.22978, 0.90438)
cv2 = (0.0062058574541, 8.33348311276, 0.0212229901978)
name3 = 'NETCONF'
means3 = (225.1517, 18.69058, 2.33876)
cv3 = (0.0170727214349, 5.87182512772, 0.665953672533)
name4 = 'SSH'
means4 = (186.71646, 76.21534, 2.37655)
cv4 = (0.0203346261654, 0.0758002010783, 1.9103400173)
#group_names = ('Blk', 'PtC','NPC')
#group_names = ('NP-Bulk', 'Persistent Con.','None Persistent Con.')
group_names = ('NP-Conn-Seq', 'P-Conn','NP-Bulk')
bar_plot4(means1,cv1,name1, means2,cv2,name2,means3,cv3,name3, means4,cv4,name4, n_groups,group_names,bar_width,bar_plot2_title)


################### 2% packet loss and 150 ms delay ################################
bar_plot2_title='Execution Time - Insecured - NLD'
bar_width = 0.35
n_groups = 3
name1='gRPC'
means1 = ( 34.39994, 16.46343,0.42991)
cv1 = [(34.0434082613, 6.18986550573, 0.314314970048),( 50.0434082613, 6.18986550573,0.314314970048)]
name2='REST'
means2 = (34.27274, 16.80058,0.54377 )
cv2 = ( 33.7783135827, 9.66830517856,0.0494178537469)
#group_names = ('NP-Bulk', 'Persistent Con.','None Persistent Con.')
group_names = ('NP-Conn-Seq', 'P-Conn','NP-Bulk')
bar_plot2(means1,cv1,name1, means2,cv2,name2, n_groups,group_names,bar_width,bar_plot2_title)
