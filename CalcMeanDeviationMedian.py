import os
import math
digitToRound = 5

SSH_FullProcess_InputFileName = 'ssh/SSHResults20_FullProcess.txt'
SSH_FullProcess_OutputFileName = 'mean-median/SSH_FullProcess_Mean_Median_Deviation.txt'

#2 percent packet loss and 150ms delay
SSH_PL_DL_InputFileName = 'ssh/SSHResults20_PL_DL.txt'
SSH_PL_DL_OutputFileName = 'mean-median/SSH_PL_DL_Mean_Median_Deviation.txt'

SSH_JustCommunicationPart_InputFileName = 'ssh/SSHResults20_JustCommunication.txt'
SSH_JustCommunicationPart_OutputFileName = 'mean-median/SSH_JustCommunicationPart_Mean_Median_Deviation.txt'

SSH_JustCommunicationPart_PL_DL_InputFileName = 'ssh/SSHResults20_JustCommunication_PL_DL.txt'
SSH_JustCommunicationPart_PL_DL_OutputFileName = 'mean-median/SSH_JustCommunicationPart_PL_DL_Mean_Median_Deviation.txt'

netconf_FullProcess_InputFileName = 'netconf/netconfResults20_FullProcess.txt'
netconf_FullProcess_OutputFileName = 'mean-median/netconf_FullProcess_Mean_Median_Deviation.txt'

#2 percent packet loss and 150ms delay
netconf_PL_DL_InputFileName = 'netconf/netconfResults20_PL_DL.txt'
netconf_PL_DL_OutputFileName = 'mean-median/netconf_PL_DL_Mean_Median_Deviation.txt'

netconf_JustCommunicationPart_InputFileName = 'netconf/netconfResults20_JustCommunication.txt'
netconf_JustCommunicationPart_OutputFileName = 'mean-median/netconf_JustCommunicationPart_Mean_Median_Deviation.txt'

netconf_JustCommunicationPart_PL_DL_InputFileName = 'netconf/netconfResults20_JustCommunication_PL_DL.txt'
netconf_JustCommunicationPart_PL_DL_OutputFileName = 'mean-median/netconf_JustCommunicationPart_PL_DL_Mean_Median_Deviation.txt'

#REST_FullProcess_InputFileName = 'PureResults/RESTResults20.txt'
REST_FullProcess_InputFileName = 'rest/RESTResults20_FullProcess.txt'
REST_FullProcess_OutputFileName = 'mean-median/REST_FullProcess_Mean_Median_Deviation.txt'

#REST_JustCommunicationPart_InputFileName = 'PureResults/RESTResults20.txt'
REST_JustCommunicationPart_InputFileName = 'rest/RESTResults20_JustCommunication.txt'
REST_JustCommunicationPart_OutputFileName = 'mean-median/REST_JustCommunicationPart_Mean_Median_Deviation.txt'

#REST_JustCommunicationPart_InputFileName = 'PureResults/RESTResults20.txt'
REST_JustCommunicationPart_PL_DL_InputFileName = 'rest/RESTResults20_JustCommunication_PL_DL.txt'
REST_JustCommunicationPart_PL_DL_OutputFileName = 'mean-median/REST_JustCommunicationPart_PL_DL_Mean_Median_Deviation.txt'

#2 percent packet loss and 150ms delay
REST_PL_DL_InputFileName = 'rest/RESTResults20_PL_DL.txt'
REST_PL_DL_OutputFileName = 'mean-median/REST_PL_DL_Mean_Median_Deviation.txt'

#gRPC_FullProcess_InputFileName = 'PureResults/gRPCResults20.txt'
gRPC_FullProcess_InputFileName = 'grpc/gRPCResults20_FullProcess.txt'
gRPC_FullProcess_OutputFileName = 'mean-median/gRPC_FullProcess_Mean_Median_Deviation.txt'

#2 percent packet loss and 150ms delay
gRPC_PL_DL_InputFileName = 'grpc/gRPCResutls_PL_DL.txt'
gRPC_PL_DL_OutputFileName = 'mean-median/gRPC_PL_DL_Mean_Median_Deviation.txt'

#gRPC_JustCommunicationPart_InputFileName = 'PureResults/gRPCResults20.txt'
gRPC_JustCommunicationPart_InputFileName = 'grpc/gRPCResults20_JustCommunication.txt'
gRPC_JustCommunicationPart_OutputFileName = 'mean-median/gRPC_JustCommunicationPart_Mean_Median_Deviation.txt'

gRPC_JustCommunicationPart_PL_DL_InputFileName = 'grpc/gRPCResults20_JustCommunication_PL_DL.txt'
gRPC_JustCommunicationPart_PL_DL_OutputFileName = 'mean-median/gRPC_JustCommunicationPart_PL_DL_Mean_Median_Deviation.txt'

LREInputFileName = 'LocalRuleEnforcement/Persistant_LocalRuleEnforcement20.txt'
LREOutputFileName = 'mean-median//LocalRuleEnforcement_Mean_Median_Deviation.txt'

"""
FullProcess_gRPC_REST_SSH_OutputName_File = 'FullProcess.txt'
JustCommunicationPart_gRPC_REST_SSH_OutputName_File = 'JustCommunicationPart.txt'
"""
def CalculateMetrics(pathToFile):
	
	f1 = open(pathToFile,'r')
	x = f1.read()
	f1.close()

	y = x.split('\n')

	n = len(y)/3;

	(NumberResults,MeanTime,MeanAppCPU,MeanSysCPU,MeanMem) = (dict(),dict(),dict(),dict(),dict())
	(DeviationTime,DeviationAppCPU,DeviationSysCPU,DeviationMem) = (dict(),dict(),dict(),dict())
	#summation of samples
	for i in range(0,n):
		if (y[i*3]) not in NumberResults.keys():
			NumberResults[y[i*3]] = 1
			MeanTime[y[i*3]] = float(y[i*3+1])
			MeanSysCPU[y[i*3]] = float(y[i*3+2])
		else:
			NumberResults[y[i*3]] += 1
			MeanTime[y[i*3]] += float(y[i*3+1])
			MeanSysCPU[y[i*3]] += float(y[i*3+2])

	#mean of samples
	resultsKeys = NumberResults.keys()
	resultsKeys.sort()
	for i in range(0, len(resultsKeys)):
		nOS = NumberResults[resultsKeys[i]] #number of samples
		MeanTime[resultsKeys[i]]= MeanTime[resultsKeys[i]]/(nOS)
		MeanSysCPU[resultsKeys[i]]= MeanSysCPU[resultsKeys[i]]/(nOS)
	#print(nOS)
	#deviation
	for a in resultsKeys:
		DeviationTime[a] = 0
		DeviationSysCPU[a] = 0
	for i in range(0,n):
		DeviationTime[y[i*3]] += pow(float(y[i*3+1])-MeanTime[y[i*3]],2)
		DeviationSysCPU[y[i*3]] += pow(float(y[i*3+2])-MeanSysCPU[y[i*3]],2)
	for i in range(0, len(resultsKeys)):
		DeviationTime[y[i*3]] /=(nOS-1)
		DeviationSysCPU[y[i*3]] /=(nOS-1)

	return (resultsKeys,DeviationTime,DeviationSysCPU,MeanTime,MeanSysCPU)
	
def PrintResults(f2,i,resultsKeys,DeviationTime,DeviationSysCPU,MeanTime,MeanSysCPU):
	f2.write(resultsKeys[i]+'\n')
	f2.write('Time miu:   '+str(round(MeanTime[resultsKeys[i]],digitToRound))+'\t\t')
	#f2.write('Coef of Var:'+str(int(math.sqrt(DeviationTime[resultsKeys[i]])/MeanTime[resultsKeys[i]]*100))+'\n')
	f2.write('Coef of Var:'+str(DeviationTime[resultsKeys[i]])+'\n')
	f2.write('Sys CPU miu:'+str(round(MeanSysCPU[resultsKeys[i]],digitToRound))+'\t\t')
	#f2.write('Coef of Var:'+str(int(math.sqrt(DeviationSysCPU[resultsKeys[i]])/MeanSysCPU[resultsKeys[i]]*100))+'\n')
	f2.write('Coef of Var:'+str(DeviationSysCPU[resultsKeys[i]])+'\n')
	f2.write('\n')
	
#print result of local rule enforcement
(resultsKeys,DeviationTime,DeviationSysCPU,MeanTime,MeanSysCPU) = CalculateMetrics(LREInputFileName)
f2 = open(LREOutputFileName,'w')
for i in range(0, len(resultsKeys)):
	PrintResults(f2,i,resultsKeys,DeviationTime,DeviationSysCPU,MeanTime,MeanSysCPU)
f2.close()

#########SSH#################
#print result of SSH - Full
(resultsKeys,DeviationTime,DeviationSysCPU,MeanTime,MeanSysCPU)  = CalculateMetrics(SSH_FullProcess_InputFileName)
f2 = open(SSH_FullProcess_OutputFileName,'w')
for i in range(0, len(resultsKeys)):
	PrintResults(f2,i,resultsKeys,DeviationTime,DeviationSysCPU,MeanTime,MeanSysCPU)
f2.close()

#print result of SSH - Just Communication
(resultsKeys,DeviationTime,DeviationSysCPU,MeanTime,MeanSysCPU) = CalculateMetrics(SSH_JustCommunicationPart_InputFileName)
f2 = open(SSH_JustCommunicationPart_OutputFileName,'w')
for i in range(0, len(resultsKeys)):
	PrintResults(f2,i,resultsKeys,DeviationTime,DeviationSysCPU,MeanTime,MeanSysCPU)
f2.close()

#print result of SSH - Full PL DL
(resultsKeys,DeviationTime,DeviationSysCPU,MeanTime,MeanSysCPU)  = CalculateMetrics(SSH_PL_DL_InputFileName)
f2 = open(SSH_PL_DL_OutputFileName,'w')
for i in range(0, len(resultsKeys)):
	PrintResults(f2,i,resultsKeys,DeviationTime,DeviationSysCPU,MeanTime,MeanSysCPU)
f2.close()

#print result of SSH - Just Communication  PL DL
(resultsKeys,DeviationTime,DeviationSysCPU,MeanTime,MeanSysCPU) = CalculateMetrics(SSH_JustCommunicationPart_PL_DL_InputFileName)
f2 = open(SSH_JustCommunicationPart_PL_DL_OutputFileName,'w')
for i in range(0, len(resultsKeys)):
	PrintResults(f2,i,resultsKeys,DeviationTime,DeviationSysCPU,MeanTime,MeanSysCPU)
f2.close()

#########gRPC#################
#print result of gRPC - Full 
(resultsKeys,DeviationTime,DeviationSysCPU,MeanTime,MeanSysCPU) = CalculateMetrics(gRPC_FullProcess_InputFileName)
f2 = open(gRPC_FullProcess_OutputFileName,'w')
for i in range(0, len(resultsKeys)):
	PrintResults(f2,i,resultsKeys,DeviationTime,DeviationSysCPU,MeanTime,MeanSysCPU)
f2.close()

#print result of gRPC - Just Communication
(resultsKeys,DeviationTime,DeviationSysCPU,MeanTime,MeanSysCPU) = CalculateMetrics(gRPC_JustCommunicationPart_InputFileName)
f2 = open(gRPC_JustCommunicationPart_OutputFileName,'w')
for i in range(0, len(resultsKeys)):
	PrintResults(f2,i,resultsKeys,DeviationTime,DeviationSysCPU,MeanTime,MeanSysCPU)
f2.close()

#print result of gRPC - Full _PL_DL
(resultsKeys,DeviationTime,DeviationSysCPU,MeanTime,MeanSysCPU) = CalculateMetrics(gRPC_PL_DL_InputFileName)
f2 = open(gRPC_PL_DL_OutputFileName,'w')
for i in range(0, len(resultsKeys)):
	PrintResults(f2,i,resultsKeys,DeviationTime,DeviationSysCPU,MeanTime,MeanSysCPU)
f2.close()

#print result of gRPC - Just Communication_PL_DL
(resultsKeys,DeviationTime,DeviationSysCPU,MeanTime,MeanSysCPU) = CalculateMetrics(gRPC_JustCommunicationPart_PL_DL_InputFileName)
f2 = open(gRPC_JustCommunicationPart_PL_DL_OutputFileName,'w')
for i in range(0, len(resultsKeys)):
	PrintResults(f2,i,resultsKeys,DeviationTime,DeviationSysCPU,MeanTime,MeanSysCPU)
f2.close()

#########netconf#################
#print result of netConf - Full 
(resultsKeys,DeviationTime,DeviationSysCPU,MeanTime,MeanSysCPU) = CalculateMetrics(netconf_FullProcess_InputFileName)
f2 = open(netconf_FullProcess_OutputFileName,'w')
for i in range(0, len(resultsKeys)):
	PrintResults(f2,i,resultsKeys,DeviationTime,DeviationSysCPU,MeanTime,MeanSysCPU)
f2.close()

#print result of netconf - Just Communication
(resultsKeys,DeviationTime,DeviationSysCPU,MeanTime,MeanSysCPU) = CalculateMetrics(netconf_JustCommunicationPart_InputFileName)
f2 = open(netconf_JustCommunicationPart_OutputFileName,'w')
for i in range(0, len(resultsKeys)):
	PrintResults(f2,i,resultsKeys,DeviationTime,DeviationSysCPU,MeanTime,MeanSysCPU)
f2.close()

#print result of netconf - Full _PL_DL
(resultsKeys,DeviationTime,DeviationSysCPU,MeanTime,MeanSysCPU) = CalculateMetrics(netconf_PL_DL_InputFileName)
f2 = open(netconf_PL_DL_OutputFileName,'w')
for i in range(0, len(resultsKeys)):
	PrintResults(f2,i,resultsKeys,DeviationTime,DeviationSysCPU,MeanTime,MeanSysCPU)
f2.close()

#print result of netconf - Just Communication_PL_DL
(resultsKeys,DeviationTime,DeviationSysCPU,MeanTime,MeanSysCPU) = CalculateMetrics(netconf_JustCommunicationPart_PL_DL_InputFileName)
f2 = open(netconf_JustCommunicationPart_PL_DL_OutputFileName,'w')
for i in range(0, len(resultsKeys)):
	PrintResults(f2,i,resultsKeys,DeviationTime,DeviationSysCPU,MeanTime,MeanSysCPU)
f2.close()

#########REST#################
#print result of REST - Full 
(resultsKeys,DeviationTime,DeviationSysCPU,MeanTime,MeanSysCPU) = CalculateMetrics(REST_FullProcess_InputFileName)
f2 = open(REST_FullProcess_OutputFileName,'w')
for i in range(0, len(resultsKeys)):
	PrintResults(f2,i,resultsKeys,DeviationTime,DeviationSysCPU,MeanTime,MeanSysCPU)
f2.close()

#print result of REST - Just Communication
(resultsKeys,DeviationTime,DeviationSysCPU,MeanTime,MeanSysCPU) = CalculateMetrics(REST_JustCommunicationPart_InputFileName)
f2 = open(REST_JustCommunicationPart_OutputFileName,'w')
for i in range(0, len(resultsKeys)):
	PrintResults(f2,i,resultsKeys,DeviationTime,DeviationSysCPU,MeanTime,MeanSysCPU)
f2.close()

#print result of REST - Full _PL_DL
(resultsKeys,DeviationTime,DeviationSysCPU,MeanTime,MeanSysCPU) = CalculateMetrics(REST_PL_DL_InputFileName)
f2 = open(REST_PL_DL_OutputFileName,'w')
for i in range(0, len(resultsKeys)):
	PrintResults(f2,i,resultsKeys,DeviationTime,DeviationSysCPU,MeanTime,MeanSysCPU)
f2.close()

#print result of REST - Just Communication_PL_DL
(resultsKeys,DeviationTime,DeviationSysCPU,MeanTime,MeanSysCPU) = CalculateMetrics(REST_JustCommunicationPart_PL_DL_InputFileName)
f2 = open(REST_JustCommunicationPart_PL_DL_OutputFileName,'w')
for i in range(0, len(resultsKeys)):
	PrintResults(f2,i,resultsKeys,DeviationTime,DeviationSysCPU,MeanTime,MeanSysCPU)
f2.close()

"""
#print comprative results Full
(resultsKeysREST_F,DeviationTimeREST_F,DeviationAppCPUREST_F,DeviationSysCPUREST_F,DeviationMemREST_F,MeanTimeREST_F,MeanAppCPUREST_F,MeanSysCPUREST_F,MeanMemREST_F) = CalculateMetrics(REST_FullProcess_InputFileName)
(resultsKeysgRPC_F,DeviationTimegRPC_F,DeviationAppCPUgRPC_F,DeviationSysCPUgRPC_F,DeviationMemgRPC_F,MeanTimeRPC,MeanAppCPURPC,MeanSysCPURPC,MeanMemRPC) = CalculateMetrics(gRPC_FullProcess_InputFileName)
(resultsKeysSSH,DeviationTimeSSH,DeviationAppCPUSSH,DeviationSysCPUSSH,DeviationMemSSH,MeanTimeSSH,MeanAppCPUSSH,MeanSysCPUSSH,MeanMemSSH) = CalculateMetrics(SSH_FullProcess_InputFileName)
f2 = open(FullProcess_gRPC_REST_SSH_OutputName_File,'w')
resLen = max(len(resultsKeysREST_F),len(resultsKeysgRPC_F))
#resLen = max(len(resultsKeysREST_F),len(resultsKeysgRPC_F),len(resultsKeysSSH))
for i in range(0, resLen):
#	if len(resultsKeysSSH) > i:
#		f2.write('SSH_F  - ')
#		PrintResults(f2,i,resultsKeysSSH,DeviationTimeSSH,DeviationAppCPUSSH,DeviationSysCPUSSH,DeviationMemSSH,MeanTimeSSH,MeanAppCPUSSH,MeanSysCPUSSH,MeanMemSSH)
	if len(resultsKeysREST_F) > i:
		f2.write('REST_F - ')
		PrintResults(f2,i,resultsKeysREST_F,DeviationTimeREST_F,DeviationAppCPUREST_F,DeviationSysCPUREST_F,DeviationMemREST_F,MeanTimeREST_F,MeanAppCPUREST_F,MeanSysCPUREST_F,MeanMemREST_F)
	if len(resultsKeysgRPC_F) > i:
		f2.write('gRPC_F - ')
		PrintResults(f2,i,resultsKeysgRPC_F,DeviationTimegRPC_F,DeviationAppCPUgRPC_F,DeviationSysCPUgRPC_F,DeviationMemgRPC_F,MeanTimeRPC,MeanAppCPURPC,MeanSysCPURPC,MeanMemRPC)
f2.close()

#print comprative results Just Communication
(resultsKeysREST_JC,DeviationTimeREST_JC,DeviationAppCPUREST_JC,DeviationSysCPUREST_JC,DeviationMemREST_JC,MeanTimeREST_JC,MeanAppCPUREST_JC,MeanSysCPUREST_JC,MeanMemREST_JC) = CalculateMetrics(REST_JustCommunicationPart_InputFileName)
(resultsKeysgRPC_JC,DeviationTimegRPC_JC,DeviationAppCPUgRPC_JC,DeviationSysCPUgRPC_JC,DeviationMemgRPC_JC,MeanTimeRPC,MeanAppCPURPC,MeanSysCPURPC,MeanMemRPC) = CalculateMetrics(gRPC_JustCommunicationPart_InputFileName)
(resultsKeysSSH,DeviationTimeSSH,DeviationAppCPUSSH,DeviationSysCPUSSH,DeviationMemSSH,MeanTimeSSH,MeanAppCPUSSH,MeanSysCPUSSH,MeanMemSSH) = CalculateMetrics(SSH_JustCommunicationPart_InputFileName)
f2 = open(JustCommunicationPart_gRPC_REST_SSH_OutputName_File,'w')
resLen = max(len(resultsKeysREST_JC),len(resultsKeysgRPC_JC))
#resLen = max(len(resultsKeysREST_JC),len(resultsKeysgRPC_JC),len(resultsKeysSSH))
for i in range(0, resLen):
#	if len(resultsKeysSSH) > i:
#		f2.write('SSH_JC  - ')
#		PrintResults(f2,i,resultsKeysSSH,DeviationTimeSSH,DeviationAppCPUSSH,DeviationSysCPUSSH,DeviationMemSSH,MeanTimeSSH,MeanAppCPUSSH,MeanSysCPUSSH,MeanMemSSH)
	if len(resultsKeysREST_JC) > i:
		f2.write('REST_JC - ')
		PrintResults(f2,i,resultsKeysREST_JC,DeviationTimeREST_JC,DeviationAppCPUREST_JC,DeviationSysCPUREST_JC,DeviationMemREST_JC,MeanTimeREST_JC,MeanAppCPUREST_JC,MeanSysCPUREST_JC,MeanMemREST_JC)
	if len(resultsKeysgRPC_JC) > i:
		f2.write('gRPC_JC - ')
		PrintResults(f2,i,resultsKeysgRPC_JC,DeviationTimegRPC_JC,DeviationAppCPUgRPC_JC,DeviationSysCPUgRPC_JC,DeviationMemgRPC_JC,MeanTimeRPC,MeanAppCPURPC,MeanSysCPURPC,MeanMemRPC)
f2.close()

#Making Table
"""