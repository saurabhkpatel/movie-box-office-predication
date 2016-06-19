########################################################
## CIS 700 Term Project
## Saurabh Patel, Ojas Juneja, Ronak Bhuptani
#######################################################

import twitter
import json
import csv
import unidecode
import time
import thread
import time


from threading import Thread



# Go to http://dev.twitter.com/apps/new to create an app and get values
# for these credentials, which you'll need to provide in place of these
# empty string values that are defined as placeholders.
# See https://dev.twitter.com/docs/auth/oauth for more information 
# on Twitter's OAuth implementation.

CONSUMER_KEY = '6aAWM1mjauNN2AcioNIiLsEED'
CONSUMER_SECRET = 'xdOhjjQBEmF8Ad3476myGfgHFn5lLgO8sobW0BEAyrnO8vtaLe'
OAUTH_TOKEN = '104543423-z9jPqvi0POicJKcS7UgcmvPh0LPC9vLBGiFvm6uk'
OAUTH_TOKEN_SECRET = 'JSFPzyTgKt5Bz5qZkGlvShO8EOLoCqgd9bLHw28LTxVTp'


def oauth_login():
	auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
	twitter_api = twitter.Twitter(auth=auth)
	return twitter_api

# Returns an instance of twitter.Twitter
twitter_api = oauth_login()
# Reference the self.auth parameter
twitter_stream = twitter.TwitterStream(auth=twitter_api.auth)
##############################################################################################################

timestr = time.strftime("%Y%m%d_%H%M%S")

file_mov1 = "JungleBook_"+timestr + ".data"
file1 = open(file_mov1, "wb")
file1.close()

file_mov2 = "Demolition_"+timestr+ ".data"
file2 = open(file_mov2 ,"wb")
file2.close()

file_mov3 = "HardcoreHenry_"+timestr+ ".data"
file3 = open(file_mov3, "wb")
file3.close()

file_mov4 = "BeforeIWake_"+timestr+ ".data"
file4 = open(file_mov4, "wb")
file4.close()

file_mov5 = "CriminalMovie_"+timestr+ ".data"
file5 = open(file_mov5, "wb")
file5.close()

file_mov6 = "GreenRoomMovie_"+timestr+ ".data"
file6 = open(file_mov6, "wb")
file6.close()

file_mov7 = "TheHuntsman_"+timestr+ ".data"
file7 = open(file_mov7, "wb")
file7.close()

file_mov8 = "AHologramForTheKing_"+timestr+ ".data"
file8 = open(file_mov8, "wb")
file8.close()

file_mov9 = "LouderThanBombs_"+timestr+ ".data"
file9 = open(file_mov9, "wb")
file9.close()

file_mov10 = "FanTheFilm_"+timestr+ ".data"
file10 = open(file_mov10, "wb")
file10.close()

file_mov11 = "TheManWhoKnewInfinity_"+timestr+ ".data"
file11 = open(file_mov11, "wb")
file11.close()

file_mov12 = "ElvisAndNixon_"+timestr+ ".data"
file12 = open(file_mov12, "wb")
file12.close()

file_mov13 = "RatchetAndClank_"+timestr+ ".data"
file13 = open(file_mov13, "wb")
file13.close()


filesList = [
			file_mov1,
			file_mov2,
			file_mov3,
			file_mov4,
			file_mov5,
			file_mov6,
			file_mov7,
			file_mov8,
			file_mov9,
			file_mov10,
			file_mov11,
			file_mov12,
			file_mov13
			]


queryList = ["The Jungle Book,Jungle Book,JungleBook",
			"Demolition,NaomiWatts,DemolitionMovie,jakegyllenhaal",
			"Hardcore Henry,HardcoreHenryFan,HardcoreHenry",
			"Before I Wake,BeforeIWake,BeforeIWakeFilm",
			"Criminal_Movie,CriminalMovie",
			"Green Room,GreenRoom,GreenRoomMovie",
			"TheHuntsman,TheHuntsmanWintersWar,TheHuntsmanMovie",
			"A Hologram for the King,AHologramForTheKing",
			"Louder Than Bombs,LouderThanBombs",
			"FanTheFilm,fan movie,FAN WEEK,WATCH FAN TODAY",
			"TheManWhoKnewInfinity,the man who knew infinity",
			"ElvisNixonMovie,ElvisAndNixon,Elvis and Nixon",
			"Ratchet and Clank,RatchetAndClank"
			]



import re
def checkSubstring(queryCheck, str):
	termsList = queryCheck.split(',')
	for words in termsList:
		if re.search(words,str,re.IGNORECASE):
			return True
	return False

# Define a function for the thread
def gatherTweets( query):
	# See https://dev.twitter.com/docs/streaming-apis
	stream = twitter_stream.statuses.filter(track=query, language="en")
	count = 0
	for tweet in stream:
		try:
			data = {}

			#j= json.dumps(tweet)
			j = tweet
			#j = json.loads(json.dumps(tweet))
			#print j
			#print type(j)
			if 'id' in j:
				data['id'] = j['id']
			else:
				data['id'] = ""	

			if 'created_at' in j:
				data['created_at'] = j['created_at']
			else:
				data['created_at'] = ""

			if 'text' in j:
				data['text'] = j['text']
				data['text_1'] = j['text'].encode('ascii', 'ignore').decode('ascii')
			else:
				data['text'] = ""
				data['text_1'] = ""

			if 'timestamp_ms' in j:
				data['timestamp_ms'] = j['timestamp_ms']
			else:
				data['timestamp_ms'] = ""


			if 'user' in j:
				if 'id' in j['user']:
					data['userid'] = j['user']['id']
				else:
					data['userid'] = ""

				if 'name' in j['user']:
					data['name'] = j['user']['name']
				else:
					data['name'] = ""

				if 'followers_count' in j['user']:
					data['followers_count'] = j['user']['followers_count']
				else:
					data['followers_count'] = ""

				if 'id_str' in j['user']:
					data['userid_str'] = j['user']['id_str']
				else:
					data['userid_str'] = ""

				if 'screen_name' in j['user']:
					data['user_screen_name'] = j['user']['screen_name']
				else:
					data['user_screen_name'] = ""

			else:
				data['userid'] = ""
				data['name'] = ""
				data['followers_count'] = ""
				data['userid_str'] = ""
				data['user_screen_name'] = ""

			filename = "local.txt"
			for subquery in queryList:
				if checkSubstring(subquery,data['text_1']):
					index = queryList.index(subquery)
					filename = filesList[index]

			localFileName = open(filename, 'ab')
			json.dump(data,localFileName, indent=4)
			localFileName.write(",")
			localFileName.close()
			count = count+1
			print str(count) +":" +str(thread.get_ident())
		except Exception as ex:
			template = "An exception of type {0} occured. Arguments:\n{1!r}"
			message = template.format(type(ex).__name__, ex.args)
			print message
	print "program exiit, this thread " +str(thread.get_ident())

'''query = "The Jungle Book,Jungle Book,JungleBook,"\
"Demolition,NaomiWatts,DemolitionMovie,jakegyllenhaal,"\
"Hardcore Henry,HardcoreHenryFan,HardcoreHenry,"\
"Before I Wake,BeforeIWake,BeforeIWakeFilm,"\
"Criminal_Movie,CriminalMovie,"\
"Green Room,GreenRoom,GreenRoomMovie,"\
"TheHuntsman,TheHuntsmanWintersWar,TheHuntsmanMovie,"\
"A Hologram for the King,AHologramForTheKing,"\
"Louder Than Bombs,LouderThanBombs,"\
"FanTheFilm,fan movie,FAN WEEK,WATCH FAN TODAY,"\
"TheManWhoKnewInfinity,the man who knew infinity,"\
"ElvisNixonMovie,ElvisAndNixon,Elvis and Nixon";'''

query = "TheHuntsman,TheHuntsmanWintersWar,TheHuntsmanMovie,"\
"A Hologram for the King,AHologramForTheKing,"\
"TheManWhoKnewInfinity,the man who knew infinity,"\
"Ratchet and Clank,RatchetAndClank,"\
"ElvisNixonMovie,ElvisAndNixon,Elvis and Nixon";

gatherTweets(query)

print "program finished...exiting"
