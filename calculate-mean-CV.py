import os, math
import numpy as np
digitToRound = 5

SSH_FullProcess_InputFileName = 'ssh/SSHResults20_FullProcess.txt'
SSH_FullProcess_OutputFileName = 'mean-CV/SSH_FullProcess_Mean_Median_Deviation.txt'

SSH_PL_DL_InputFileName = 'ssh/SSHResults20_PL_DL.txt'
SSH_PL_DL_OutputFileName = 'mean-CV/SSH_PL_DL_Mean_Median_Deviation.txt'

SSH_JustCommunicationPart_InputFileName = 'ssh/SSHResults20_JustCommunication.txt'
SSH_JustCommunicationPart_OutputFileName = 'mean-CV/SSH_JustCommunicationPart_Mean_Median_Deviation.txt'

SSH_JustCommunicationPart_PL_DL_InputFileName = 'ssh/SSHResults20_JustCommunication_PL_DL.txt'
SSH_JustCommunicationPart_PL_DL_OutputFileName = 'mean-CV/SSH_JustCommunicationPart_PL_DL_Mean_Median_Deviation.txt'

netconf_FullProcess_InputFileName = 'netconf/netconfResults20_FullProcess.txt'
netconf_FullProcess_OutputFileName = 'mean-CV/netconf_FullProcess_Mean_Median_Deviation.txt'

netconf_PL_DL_InputFileName = 'netconf/netconfResults20_PL_DL.txt'
netconf_PL_DL_OutputFileName = 'mean-CV/netconf_PL_DL_Mean_Median_Deviation.txt'

netconf_JustCommunicationPart_InputFileName = 'netconf/netconfResults20_JustCommunication.txt'
netconf_JustCommunicationPart_OutputFileName = 'mean-CV/netconf_JustCommunicationPart_Mean_Median_Deviation.txt'

netconf_JustCommunicationPart_PL_DL_InputFileName = 'netconf/netconfResults20_JustCommunication_PL_DL.txt'
netconf_JustCommunicationPart_PL_DL_OutputFileName = 'mean-CV/netconf_JustCommunicationPart_PL_DL_Mean_Median_Deviation.txt'

REST_FullProcess_InputFileName = 'rest/RESTResults20_FullProcess.txt'
REST_FullProcess_OutputFileName = 'mean-CV/REST_FullProcess_Mean_Median_Deviation.txt'

REST_JustCommunicationPart_InputFileName = 'rest/RESTResults20_JustCommunication.txt'
REST_JustCommunicationPart_OutputFileName = 'mean-CV/REST_JustCommunicationPart_Mean_Median_Deviation.txt'

REST_JustCommunicationPart_PL_DL_InputFileName = 'rest/RESTResults20_JustCommunication_PL_DL.txt'
REST_JustCommunicationPart_PL_DL_OutputFileName = 'mean-CV/REST_JustCommunicationPart_PL_DL_Mean_Median_Deviation.txt'

REST_PL_DL_InputFileName = 'rest/RESTResults20_PL_DL.txt'
REST_PL_DL_OutputFileName = 'mean-CV/REST_PL_DL_Mean_Median_Deviation.txt'

gRPC_FullProcess_InputFileName = 'grpc/gRPCResults20_FullProcess.txt'
gRPC_FullProcess_OutputFileName = 'mean-CV/gRPC_FullProcess_Mean_Median_Deviation.txt'

gRPC_PL_DL_InputFileName = 'grpc/gRPCResults_PL_DL.txt'
gRPC_PL_DL_OutputFileName = 'mean-CV/gRPC_PL_DL_Mean_Median_Deviation.txt'

gRPC_JustCommunicationPart_InputFileName = 'grpc/gRPCResults20_JustCommunication.txt'
gRPC_JustCommunicationPart_OutputFileName = 'mean-CV/gRPC_JustCommunicationPart_Mean_Median_Deviation.txt'

gRPC_JustCommunicationPart_PL_DL_InputFileName = 'grpc/gRPCResults20_JustCommunication_PL_DL.txt'
gRPC_JustCommunicationPart_PL_DL_OutputFileName = 'mean-CV/gRPC_JustCommunicationPart_PL_DL_Mean_Median_Deviation.txt'

LREInputFileName = 'LocalRuleEnforcement/LocalRuleEnforcement20.txt'
LREOutputFileName = 'mean-CV/LocalRuleEnforcement_Mean_Median_Deviation.txt'

grpc_NLDInputFileName = "NLD/results/grpc.txt"
grpc_NLDOutputFileName = "mean-CV/grpc_NLD.txt"
REST_NLDInputFileName = "NLD/results/rest.txt"
REST_NLDOutputFileName = "mean-CV/rest_NLD.txt"
netconf_NLDInputFileName = "NLD/results/netconf.txt"
netconf_NLDOutputFileName = "mean-CV/netconf_NLD.txt"
SSH_NLDInputFileName = "NLD/results/ssh.txt"
SSH_NLDOutputFileName = "mean-CV/ssh_NLD.txt"

#packet loss and delay in each interface
gRPC_0PL_75DL_InputFileName = 'grpc/gRPC20_0PL_75ms.txt'
gRPC_0PL_75DL_OutputFileName = 'mean-CV/gRPC_0PL_75ms.txt'
gRPC_halfPL_75DL_InputFileName = 'grpc/gRPC20_0.5PL_75ms.txt'
gRPC_halfPL_75DL_OutputFileName = 'mean-CV/gRPC_0.5PL_75ms.txt'
gRPC_1PL_75DL_InputFileName = 'grpc/gRPC20_1PL_75ms.txt'
gRPC_1PL_75DL_OutputFileName = 'mean-CV/gRPC_1PL_75ms.txt'
gRPC_2PL_75DL_InputFileName = 'grpc/gRPC20_2PL_75ms.txt'
gRPC_2PL_75DL_OutputFileName = 'mean-CV/gRPC_2PL_75ms.txt'

REST_0PL_75DL_InputFileName = 'rest/REST20_0PL_75ms.txt'
REST_0PL_75DL_OutputFileName = 'mean-CV/REST_0PL_75ms.txt'
REST_halfPL_75DL_InputFileName = 'rest/REST20_0.5PL_75ms.txt'
REST_halfPL_75DL_OutputFileName = 'mean-CV/REST_0.5PL_75ms.txt'
REST_1PL_75DL_InputFileName = 'rest/REST20_1PL_75ms.txt'
REST_1PL_75DL_OutputFileName = 'mean-CV/REST_1PL_75ms.txt'
REST_2PL_75DL_InputFileName = 'rest/REST20_2PL_75ms.txt'
REST_2PL_75DL_OutputFileName = 'mean-CV/REST_2PL_75ms.txt'

NetConf_0PL_75DL_InputFileName = 'netconf/NetConf20_0PL_75ms.txt'
NetConf_0PL_75DL_OutputFileName = 'mean-CV/NetConf_0PL_75ms.txt'
NetConf_halfPL_75DL_InputFileName = 'netconf/NetConf20_0.5PL_75ms.txt'
NetConf_halfPL_75DL_OutputFileName = 'mean-CV/NetConf_0.5PL_75ms.txt'
NetConf_1PL_75DL_InputFileName = 'netconf/NetConf20_1PL_75ms.txt'
NetConf_1PL_75DL_OutputFileName = 'mean-CV/NetConf_1PL_75ms.txt'
NetConf_2PL_75DL_InputFileName = 'netconf/NetConf20_2PL_75ms.txt'
NetConf_2PL_75DL_OutputFileName = 'mean-CV/NetConf_2PL_75ms.txt'

SSH_0PL_75DL_InputFileName = 'ssh/SSH20_0PL_75ms.txt'
SSH_0PL_75DL_OutputFileName = 'mean-CV/SSH_0PL_75ms.txt'
SSH_halfPL_75DL_InputFileName = 'ssh/SSH20_0.5PL_75ms.txt'
SSH_halfPL_75DL_OutputFileName = 'mean-CV/SSH_0.5PL_75ms.txt'
SSH_1PL_75DL_InputFileName = 'ssh/SSH20_1PL_75ms.txt'
SSH_1PL_75DL_OutputFileName = 'mean-CV/SSH_1PL_75ms.txt'
SSH_2PL_75DL_InputFileName = 'ssh/SSH20_2PL_75ms.txt'
SSH_2PL_75DL_OutputFileName = 'mean-CV/SSH_2PL_75ms.txt'

def CalculateMetrics(pathToFile, db=3):
	#db is the number of elements in file (cpu, memory, time ,....)

	f1 = open(pathToFile,'r')
	x = f1.read()
	f1.close()
	y = x.split('\n')
	n = len(y)/db
	(NumberResults,TimeValues,MeanTime,CVTime) = (dict(),dict(),dict(),dict())
	for i in range(0,n):
		if (y[i*db]) not in NumberResults.keys():
			NumberResults[y[i*db]] = 1
			TimeValues[y[i*db]] = np.array([float(y[i*db+1])])
		else:
			NumberResults[y[i*db]] += 1
			TimeValues[y[i*db]] = np.append(TimeValues[y[i*db]],np.array([float(y[i*db+1])]))
			
	resultsKeys = NumberResults.keys()
	resultsKeys.sort()
	for i in range(0, len(resultsKeys)):
		MeanTime[resultsKeys[i]]= np.mean(TimeValues[resultsKeys[i]])
		CVTime[resultsKeys[i]] = np.std(TimeValues[resultsKeys[i]])/MeanTime[resultsKeys[i]]*100
		
	return (resultsKeys,MeanTime,CVTime)
	
def PrintResults(f2,i,resultsKeys,CVTime,MeanTime):
	f2.write(resultsKeys[i]+'\n')
	f2.write('Time miu:   '+str(round(MeanTime[resultsKeys[i]],digitToRound))+'\t\t')
	f2.write('Coef of Var:'+str(round(CVTime[resultsKeys[i]],1))+'\n')
	f2.write('\n')
	
def Find_CV_Mean(inputFileName, outputFileName,db=3):
	(resultsKeys,MeanTime,CVTime) = CalculateMetrics(inputFileName,db)
	f2 = open(outputFileName,'w')
	for i in range(0, len(resultsKeys)):
		PrintResults(f2,i,resultsKeys,CVTime,MeanTime)
	f2.close()


Find_CV_Mean(LREInputFileName,LREOutputFileName,2)
Find_CV_Mean(SSH_FullProcess_InputFileName,SSH_FullProcess_OutputFileName)
Find_CV_Mean(SSH_JustCommunicationPart_InputFileName,SSH_JustCommunicationPart_OutputFileName)
Find_CV_Mean(SSH_PL_DL_InputFileName,SSH_PL_DL_OutputFileName)
Find_CV_Mean(SSH_JustCommunicationPart_PL_DL_InputFileName,SSH_JustCommunicationPart_PL_DL_OutputFileName)
Find_CV_Mean(gRPC_FullProcess_InputFileName,gRPC_FullProcess_OutputFileName)
Find_CV_Mean(gRPC_FullProcess_InputFileName,gRPC_FullProcess_OutputFileName)
Find_CV_Mean(gRPC_JustCommunicationPart_InputFileName,gRPC_JustCommunicationPart_OutputFileName)
Find_CV_Mean(gRPC_PL_DL_InputFileName,gRPC_PL_DL_OutputFileName)
Find_CV_Mean(gRPC_JustCommunicationPart_PL_DL_InputFileName,gRPC_JustCommunicationPart_PL_DL_OutputFileName)
Find_CV_Mean(netconf_FullProcess_InputFileName,netconf_FullProcess_OutputFileName)
Find_CV_Mean(netconf_JustCommunicationPart_InputFileName,netconf_JustCommunicationPart_OutputFileName)
Find_CV_Mean(netconf_PL_DL_InputFileName,netconf_PL_DL_OutputFileName)
Find_CV_Mean(netconf_JustCommunicationPart_PL_DL_InputFileName,netconf_JustCommunicationPart_PL_DL_OutputFileName)
Find_CV_Mean(REST_FullProcess_InputFileName,REST_FullProcess_OutputFileName)
Find_CV_Mean(REST_JustCommunicationPart_InputFileName,REST_JustCommunicationPart_OutputFileName)
Find_CV_Mean(REST_PL_DL_InputFileName,REST_PL_DL_OutputFileName)
Find_CV_Mean(REST_JustCommunicationPart_PL_DL_InputFileName,REST_JustCommunicationPart_PL_DL_OutputFileName)

Find_CV_Mean(grpc_NLDInputFileName,grpc_NLDOutputFileName,2)
Find_CV_Mean(REST_NLDInputFileName,REST_NLDOutputFileName,2)
Find_CV_Mean(netconf_NLDInputFileName,netconf_NLDOutputFileName,2)
Find_CV_Mean(SSH_NLDInputFileName,SSH_NLDOutputFileName,2)

Find_CV_Mean(gRPC_0PL_75DL_InputFileName,gRPC_0PL_75DL_OutputFileName)
Find_CV_Mean(gRPC_halfPL_75DL_InputFileName,gRPC_halfPL_75DL_OutputFileName)
Find_CV_Mean(gRPC_1PL_75DL_InputFileName,gRPC_1PL_75DL_OutputFileName)
Find_CV_Mean(gRPC_2PL_75DL_InputFileName,gRPC_2PL_75DL_OutputFileName)

Find_CV_Mean(REST_0PL_75DL_InputFileName,REST_0PL_75DL_OutputFileName)
Find_CV_Mean(REST_halfPL_75DL_InputFileName,REST_halfPL_75DL_OutputFileName)
Find_CV_Mean(REST_1PL_75DL_InputFileName,REST_1PL_75DL_OutputFileName)
Find_CV_Mean(REST_2PL_75DL_InputFileName,REST_2PL_75DL_OutputFileName)

Find_CV_Mean(NetConf_0PL_75DL_InputFileName,NetConf_0PL_75DL_OutputFileName)
Find_CV_Mean(NetConf_halfPL_75DL_InputFileName,NetConf_halfPL_75DL_OutputFileName)
Find_CV_Mean(NetConf_1PL_75DL_InputFileName,NetConf_1PL_75DL_OutputFileName)
Find_CV_Mean(NetConf_2PL_75DL_InputFileName,NetConf_2PL_75DL_OutputFileName)

Find_CV_Mean(SSH_0PL_75DL_InputFileName,SSH_0PL_75DL_OutputFileName)
Find_CV_Mean(SSH_halfPL_75DL_InputFileName,SSH_halfPL_75DL_OutputFileName)
Find_CV_Mean(SSH_1PL_75DL_InputFileName,SSH_1PL_75DL_OutputFileName)
Find_CV_Mean(SSH_2PL_75DL_InputFileName,SSH_2PL_75DL_OutputFileName)