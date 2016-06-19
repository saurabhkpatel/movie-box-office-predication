#!/usr/bin/env python

########################################################
## CIS 700 Term Project
## Saurabh Patel, Ojas Juneja, Ronak Bhuptani
#######################################################



import requests
import json
import facebook
import time
from threading import Thread


ACCESS_TOKEN = 'CAANEx4sBXvcBACYZAPP1J63vr321VKrx3Xx5X6UYZAZCKEuiQowlJuN5weHrUlGKjhKodJYZCR4ET7ZB13bhiAAWN4MSKpuMpbkEE4jZAYTXBUYljGKUsku8qqAltMvHp6T3myVTjZBkVeMgC3EDuZCjf8Ll3AXk0tLCy5JZCqiLzYZBZARsZCVGvKAF'


def jsonObject(o):
	oject = json.dumps(o, indent=1)
	return json.loads(oject)

g = facebook.GraphAPI(ACCESS_TOKEN)

def getPageLikes():
		url = "https://graph.facebook.com/" + jb_id + "?fields=likes&access_token=" + ACCESS_TOKEN
		resp = requests.get(url)
		js_likes = json.loads(resp.text)
		return js_likes["likes"]

#getting the page id of query
def init(thread,query):
	print thread + " is running"
	lists = []
	posts_count = 0
	totalWordPosts = 0
	totalWordComments = 0
	postId = []
	posts = []
	postCreated = []
	count_set = set()
	json_comments = []
	try:
		jsSearchPage = jsonObject(g.request("search", {'q' : query, 'type' : 'page'}))
		jb_id = jsSearchPage["data"][0]["id"] 
		str_posts = ""
		str_posts_time = ""
		str_posts_id = ""
		fileName = 'facebook_' + query + '.txt'
		#getting the posts in dictionary format
		#print jb_id
		jsPosts = jsonObject(g.get_connections(jb_id, 'feed'))
		#print jsPosts
		# open file to write fb data.
		open(fileName, 'w').close()
		file_fb = open(fileName, "a")
		lists.append(jsPosts)
		print "phase 1"
	except Exception as ex:
			template = "An exception of type {0} occured. Arguments:\n{1!r}"
			message = template.format(type(ex).__name__, ex.args)
			print message
	flag_post = True
	while True:
		try:
		    	if "paging" in jsPosts:
				if "next" in jsPosts["paging"]:
					url = json.dumps(jsPosts["paging"]["next"])
					if flag_post == True:
						myurl1 = url.split("&limit=")[0]
						myurl2 = url.split("&limit=")[1]
						myurl2 = "&limit=100" + myurl2[2:]
						myurl = myurl1 + myurl2
						flag_post = False
					else: 	myurl = url
					myurl =  myurl.split("//")[1];
				  	myurl = myurl.split("\"")[0];
					myurl = "https:" + "//" + myurl;
					#print myurl
					#count_set.add(myurl)
					#print len(count_set)
					try:
						resp = requests.get(myurl)
					except Exception as ex:
						template = "An exception of type {0} occured. Arguments:\n{1!r}"
						message = template.format(type(ex).__name__, ex.args)
						print message
					jsPosts = json.loads(resp.text)
					lists.append(jsPosts)
				else: break
			else: break
		except Exception as ex: break
	
	print "phase 2"
	try:
	     for dictionary in lists:
				counter = 0
				length = len(dictionary["data"])
				#print length
				try:
	 				while counter<length:
						if "message" in dictionary["data"][counter]:
							str_posts = json.dumps(dictionary["data"][counter]["message"],indent=1)
						else: str_posts = ""
						posts.append(str_posts)
						if "id" in dictionary["data"][counter]:
							str_posts_id = dictionary["data"][counter]["id"]
						else: str_posts_id = ""
						postId.append(str_posts_id)
						if "created_time" in dictionary["data"][counter]:
								str_posts_time = dictionary["data"][counter]["created_time"]
						else: str_posts_time = ""
						postCreated.append(str_posts_time)
						counter+=1
						posts_count+=1
				except Exception as ex:
					template = "An exception of type {0} occured. Arguments:\n{1!r}"
					message = template.format(type(ex).__name__, ex.args)
					print message
	     counter = 0
	     #test_var = 0
	     print "phase 3"
	     #print postId
	     for ids in postId:
			if ids != "":
				json_dict = {}
				json_dict['postid'] = ids
				json_dict['post'] = posts[counter]
				json_dict['created_time'] = postCreated[counter]
				#print json_dict['postid']
				counter+=1
				time.sleep( 2 )
				#test_var+=1
				#print test_var
				temp = jsonObject(g.get_connections(id = ids, connection_name="comments"))
				#print temp
				json_comments.append(temp)
				list_comments = []
				commentsVar = 0
				flag_comment = True
				while True:
					if "paging" in temp:
						if 'data' in temp:
							for comment in temp['data']:
								comment_dict = {}
								if 'id' in comment['from']:
									comment_dict['personid'] = comment['from']['id']
								else: comment_dict['personid'] = ""
							#count_set.add(comment_id)
							#print len(count_set)
								comment_dict['created_time'] = comment['created_time']
								comment_dict['commentid'] = comment['id']
								comment_dict['message'] =  comment['message']
								comment_dict['messageformat'] =  comment['message'].encode('ascii', errors='ignore')
								commentsVar+=1
								list_comments.append(comment_dict)
						else: break
						if "next" in temp["paging"]:
							url = json.dumps(temp["paging"]["next"])
							if flag_comment == True:
								myurl1 = url.split("&limit=")[0]
								myurl2 = url.split("&limit=")[1]
								myurl2 = "&limit=100" + myurl2[2:]
								myurl = myurl1 + myurl2
								flag_comment = False
							else: 	myurl = url
							#print myurl
							myurl =  myurl.split("//")[1];
						  	myurl = myurl.split("\"")[0];
							myurl = "https:" + "//" + myurl + "&locale=en_EN";
							try:
								resp = requests.get(myurl)
							except Exception as ex:
								template = "An exception of type {0} occured. Arguments:\n{1!r}"
								message = template.format(type(ex).__name__, ex.args)
								print message
							temp = json.loads(resp.text)
						else:break
					else: break
				json_dict['commentscount'] = commentsVar
				json_dict['comments'] = list_comments
				json.dump(json_dict,file_fb,indent=1)
				file_fb.write(',')
	except Exception as ex:
			template = "An exception of type {0} occured. Arguments:\n{1!r}"
			message = template.format(type(ex).__name__, ex.args)
			print message
	file_fb.close()
	var_posts =  "Posts Collected: " + str(posts_count)
	print var_posts


init("","Demolition") 

