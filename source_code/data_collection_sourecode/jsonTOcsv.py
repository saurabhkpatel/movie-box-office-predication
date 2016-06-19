import json
import csv
import os

########################################################
## CIS 700 Term Project
## Saurabh Patel, Ojas Juneja, Ronak Bhuptani
#######################################################

def convertTocsv(jsonFileName,csvFileName):
    with open(jsonFileName) as file:
        data = json.load(file)
    with open(csvFileName, "w") as file:
        output = open(csvFileName,"wb")
        fieldnames = ['index', 'id','user_screen_name','name','text','created_at','userid','timestamp_ms','followers_count','userid_str','text_1']
        csv_file = csv.DictWriter(output, fieldnames=fieldnames)
        csv_file.writeheader()
        count = 1
        for item in data:
            try:
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
            except:
                print "Error in parsing data with ID : %s" % item['id'] 
        output.close()
        print len(data)

jsonFileName = "LTB.json" 
csvFileName = "LTB_csv.csv"



for filename in os.listdir(os.getcwd()):
	jsonfilename = 
	convertTocsv(filename,csvFileName)

