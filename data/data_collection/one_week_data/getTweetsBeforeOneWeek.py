import json
import csv
import os
import glob
from nltk.stem.porter import PorterStemmer
from nltk.metrics import edit_distance
from nltk.corpus import stopwords
from nltk.corpus import wordnet
import string
import re


starttime  = "1459460159000"
endtime = "1460151359000"

def convertTocsv(jsonFileName,csv_file,count):
    print jsonFileName
    with open(jsonFileName) as file:
        data = json.load(file)
        for item in data:
            try:
              if(str(item['timestamp_ms']) >= starttime and str(item['timestamp_ms']) <= endtime):
                print "yes"
                csv_file.writerow({'index': count,
                               'id': item['id'],
                               'user_screen_name': item['user_screen_name'],
                               #'name': item['name'],
                               'text': item['text'].encode('ascii', 'ignore'),
                               'created_at': item['created_at'],
                               'userid': item['userid'],
                               'timestamp_ms': item['timestamp_ms'],
                               'followers_count': item['followers_count'],
                               'userid_str': item['userid_str'],
                               'text_1': item['text_1'].decode('utf8')})
                count = count + 1
              else:
                print "no"
            except:
                print "Error in parsing data with ID : %s" % item['id']
        print len(data)

def iterateThroughDirectory(directoryList):
  for directoryname in directoryList:
    currentdirectoryname = os.getcwd();
    fulldirecname =  currentdirectoryname+"/"+directoryname;
    csvFileName = fulldirecname+"/"+directoryname+".csv"
    print csvFileName
    with open(csvFileName, "w") as file:
      output = open(csvFileName,"wb")
      fieldnames = ['index', 'id','user_screen_name','name','text','created_at','userid','timestamp_ms','followers_count','userid_str','text_1']
      csv_file = csv.DictWriter(output, fieldnames=fieldnames)
      csv_file.writeheader()
    
    count = 1
    
    for filename in os.listdir(fulldirecname):
      if filename.endswith(".data"):
        jsonFilename  =fulldirecname + "/"+filename;
        convertTocsv(jsonFilename,csv_file,count)
    
    output.close()

directoryList = ["test2"]
iterateThroughDirectory(directoryList)