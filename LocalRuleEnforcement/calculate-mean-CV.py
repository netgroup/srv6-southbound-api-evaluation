import os, math
import numpy as np
digitToRound = 5

LREInputFileName = 'LocalRuleEnforcement20.txt'
LREOutputFileName = 'LocalRuleEnforcement_Miu_CV.txt'

def CalculateMetrics(pathToFile):
	
	f1 = open(pathToFile,'r')
	x = f1.read()
	f1.close()

	y = x.split('\n')
	n = len(y)/2;


	(NumberResults,TimeValues,MeanTime,sikmaTime) = (dict(),dict(),dict(),dict())
	for i in range(0,n):
		if (y[i*2]) not in NumberResults.keys():
			NumberResults[y[i*2]] = 1
			TimeValues[y[i*2]] = np.array([float(y[i*2+1])])
		else:
			NumberResults[y[i*2]] += 1
			TimeValues[y[i*2]] = np.append(TimeValues[y[i*2]],np.array([float(y[i*2+1])]))
			
	#mean of samples
	resultsKeys = NumberResults.keys()
	resultsKeys.sort()
	for i in range(0, len(resultsKeys)):
		MeanTime[resultsKeys[i]]= np.mean(TimeValues[resultsKeys[i]])
		sikmaTime[resultsKeys[i]] = np.std(TimeValues[resultsKeys[i]])
		

	return (resultsKeys,MeanTime,sikmaTime)
	
def PrintResults(f2,i,resultsKeys,sikmaTime,MeanTime):
	f2.write(resultsKeys[i]+'\n')
	f2.write('Time miu:   '+str(round(MeanTime[resultsKeys[i]],digitToRound))+'\t\t')
	f2.write('Coef of Var:'+str(round(sikmaTime[resultsKeys[i]]/MeanTime[resultsKeys[i]]*100,1))+'\n')
	f2.write('\n')
	
#print result of local rule enforcement
(resultsKeys,MeanTime,sikmaTime) = CalculateMetrics(LREInputFileName)
f2 = open(LREOutputFileName,'w')
for i in range(0, len(resultsKeys)):
	PrintResults(f2,i,resultsKeys,sikmaTime,MeanTime)
f2.close()