########################################################
## CIS 700 Term Project
## Saurabh Patel, Ojas Juneja, Ronak Bhuptani
#######################################################

import httplib2
import os
import sys
import csv
from apiclient.discovery import build_from_document
from apiclient.errors import HttpError
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import argparser, run_flow

VIDEO_ID = "HcgJRQWxKnw"
CSVFILENAME = "JungleBook.csv"
TXTFILENAME = "JungleBook.txt"

CLIENT_SECRETS_FILE = "client_secrets.json"
YOUTUBE_READ_WRITE_SSL_SCOPE = "https://www.googleapis.com/auth/youtube.force-ssl"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
MISSING_CLIENT_SECRETS_MESSAGE = """
WARNING: Please configure OAuth 2.0

To make this sample run you will need to populate the client_secrets.json file
found at:
   %s
with information from the APIs Console
https://developers.google.com/console

For more information about the client_secrets.json file format, please visit:
https://developers.google.com/api-client-library/python/guide/aaa_client_secrets
""" % os.path.abspath(os.path.join(os.path.dirname(__file__),
                                   CLIENT_SECRETS_FILE))


def get_authenticated_service(args):
  flow = flow_from_clientsecrets(CLIENT_SECRETS_FILE, scope=YOUTUBE_READ_WRITE_SSL_SCOPE,
    message=MISSING_CLIENT_SECRETS_MESSAGE)
  storage = Storage("%s-oauth2.json" % sys.argv[0])
  credentials = storage.get()
  args.noauth_local_webserver = True
  if credentials is None or credentials.invalid:
      credentials = run_flow(flow, storage, args)
  with open("youtube-v3-discoverydocument.json", "r") as f:
    doc = f.read()
    return build_from_document(doc, http=credentials.authorize(httplib2.Http()))



def get_all_comment_threads_rec(youtube, video_id,nextToken,csvFileName,currCount):
    output = open(csvFileName,"a")
    fieldnames = ['index', 'id','authorName','comment','likeCount','publishedAt','updatedAt']
    csv_file = csv.DictWriter(output, fieldnames=fieldnames)
    count = currCount
    results = youtube.commentThreads().list( part="snippet",
    maxResults=100,
    videoId=video_id,
    pageToken=nextToken,                                         
    textFormat="plainText"
  ).execute()
    for item in results["items"]:
        _id = item["id"] #comment id , not user id
        comment = item["snippet"]["topLevelComment"]
        author = comment["snippet"]["authorDisplayName"]
        comment_text = comment["snippet"]["textDisplay"]
        likeCount = comment["snippet"]["likeCount"]
        publishedAt = comment["snippet"]["publishedAt"]
        updatedAt = comment["snippet"]["updatedAt"]
        print comment_text
        csv_file.writerow({'index': count,
                               'id': _id,
                               'authorName': author.encode('ascii', 'ignore').decode('ascii'),
                               'comment': comment_text.encode('ascii', 'ignore').decode('ascii'),
                               'likeCount': likeCount,
                               'publishedAt': publishedAt,
                               'updatedAt': updatedAt})
        count = count +1
    if "nextPageToken" in results:
        output.close()
        get_all_comment_threads_rec(youtube, video_id,results["nextPageToken"],csvFileName,count)

def get_all_comment_threads(youtube, video_id,csvFileName,textFileName):
    output = open(csvFileName,"wb")
    fieldnames = ['index', 'id','authorName','comment','likeCount','publishedAt','updatedAt']
    csv_file = csv.DictWriter(output, fieldnames=fieldnames)
    csv_file.writeheader()
    count = 1
    results = youtube.commentThreads().list( part="snippet",
    maxResults=100,
    videoId=video_id,
    textFormat="plainText"
  ).execute()
    for item in results["items"]:
        _id = item["id"] #comment id , not user id
        comment = item["snippet"]["topLevelComment"]
        author = comment["snippet"]["authorDisplayName"]
        comment_text = comment["snippet"]["textDisplay"]
        likeCount = comment["snippet"]["likeCount"]
        publishedAt = comment["snippet"]["publishedAt"]
        updatedAt = comment["snippet"]["updatedAt"]
        print comment_text
        csv_file.writerow({'index': count,
                               'id': _id,
                               'authorName': author.encode('ascii', 'ignore').decode('ascii'),
                               'comment': comment_text.encode('ascii', 'ignore').decode('ascii'),
                               'likeCount': likeCount,
                               'publishedAt': publishedAt,
                               'updatedAt': updatedAt})
        count = count +1
    if "nextPageToken" in results:
        output.close()
        get_all_comment_threads_rec(youtube, video_id,results["nextPageToken"],csvFileName,count)


# Call the API's comments.list method to list the existing comment replies.
def get_comments(youtube, parent_id):
  results = youtube.comments().list(
    part="snippet",
    parentId=parent_id,
    textFormat="plainText"
  ).execute()

  for item in results["items"]:
    author = item["snippet"]["authorDisplayName"]
    text = item["snippet"]["textDisplay"]
    print "Comment by %s: %s" % (author, text)

  return results["items"]



argparser.add_argument("--videoid",help="rked6UjNlk0")
argparser.add_argument("--text", help="Required; text that will be used as comment.")
args = argparser.parse_args() 
youtube = get_authenticated_service(args)

try:
    get_all_comment_threads(youtube, VIDEO_ID,CSVFILENAME,TXTFILENAME)
except HttpError, e:
    print "An HTTP error %d occurred:\n%s" % (e.resp.status, e.content)
