########################################################
## CIS 700 Term Project
## Saurabh Patel, Ojas Juneja, Ronak Bhuptani
#######################################################
import json
import csv
import os
import glob
import pandas as pd

#3600000
starttime  = 1459491257253#1459987443720#1459987206455#1459491143293#1460645476037#1460592029573#1459571091193#1459987201385
endtime = starttime+3600000
totalHypeCount = 0
totalHype = 0



def calculateHype(dict,count):
  #print dict
  #print count
  global totalHype,totalHypeCount
  totalSigmaCount  =0
  print totalHypeCount
  totalHypeCount = totalHypeCount+1
  if count is not 0:
    	#totalHypeCount = totalHypeCount+1
    	alpha  = len(dict)/float(count)
    	print "Aplha " + str(alpha)
	total = sum(dict.values())
	T = total/float(len(dict))
	sigma = 0
	totalSigma = 0
	for key, value in dict.iteritems():
		partSigma = 0.0
		if value != 0 and value >= T:
			totalSigmaCount = totalSigmaCount + 1
			print "totalSigmaCount "+ str(totalSigmaCount)
			partSigma = (value-T)/(float)(value)
			if partSigma < 0.1:
				partSigma = 0.1
			print "partsigma "+ str(partSigma)
		totalSigma = totalSigma + partSigma
		print "totalSigma "+ str(totalSigma)
	sigma=totalSigma/(float)(totalSigmaCount)
	print "sigma "+ str(sigma)
	hype= (alpha+sigma)/2
	print "hype" + str(hype)
	totalHype = totalHype + hype
	print "totalHype " + str(totalHype)


def convertTocsv(csvFile,outFile):
  global totalHype,totalHypeCount
  print csvFile
  df1 = pd.read_csv(csvFile)
  df1 = df1.sort(['timestamp_ms'], ascending=[True])
  count = 0
  userDict = {}
  
  for idx, row in df1.iterrows():
    global starttime,endtime

    if row['timestamp_ms'] >= starttime and row['timestamp_ms'] <= endtime:
      count = count+1
      if not row['userid'] in userDict:
        userDict[row['userid']] = row['followers_count']
    else:
      print row['timestamp_ms']
      calculateHype(userDict,count)
      count = 0
      userDict = {}
      starttime = endtime
      endtime=starttime+3600000
      print "first time after else " + str(starttime) + " " + str(endtime) + " "+ str(row['timestamp_ms'])
      flag = False
      while True:  
        if row['timestamp_ms'] >= starttime and row['timestamp_ms'] <= endtime:
          print "in side while if " + str(starttime) + " " + str(endtime) + " "+ str(row['timestamp_ms'])
          flag = True
          count = count+1
          if not row['userid'] in userDict:
            userDict[row['userid']] = row['followers_count']
        else :
          print "from here " + str(starttime) + " " + str(endtime) + " "+ str(row['timestamp_ms'])
          calculateHype(userDict,count)
          count = 0
          userDict = {}
          starttime = endtime
          endtime=starttime+3600000
        if flag:
          print "breakkkkkk"
          print "break " + str(starttime) + " " + str(endtime) + " "+ str(row['timestamp_ms'])
          break

  print "****************"
  print csvFile + " done"
  print totalHype
  print totalHype/float(totalHypeCount)
  print "****************"



def iterateThroughDirectory(directoryList):
  for directoryname in directoryList:
    currentdirectoryname = os.getcwd();
    fulldirecname =  currentdirectoryname+"/"+directoryname;
    count = 1
    for filename in os.listdir(fulldirecname):
      if filename.endswith(".csv"):
        csvFile  =fulldirecname + "/"+filename;
        outputFile  =fulldirecname + "/"+filename+".hype";
        convertTocsv(csvFile,outputFile)

directoryList = ["test"]
iterateThroughDirectory(directoryList)
