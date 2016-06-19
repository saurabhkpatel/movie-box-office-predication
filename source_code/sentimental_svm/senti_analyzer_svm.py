#!/usr/bin/env python
########################################################
## CIS 700 Term Project
## Saurabh Patel, Ojas Juneja, Ronak Bhuptani
#######################################################

import json
import csv
import os
import glob
from nltk.stem.porter import PorterStemmer
from nltk.metrics import edit_distance
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from senti_classifier import senti_classifier
import string
#import regex
import re
from nltk.tokenize import TweetTokenizer
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import wordnet
from nltk.classify.util import accuracy
from nltk.probability import FreqDist
import numpy as np
from sklearn.metrics import classification_report
from sklearn.svm import LinearSVC
from sklearn import svm
import pickle
import os


tknzr = TweetTokenizer()
stoplist = list(set(stopwords.words('english')))
punctuation = list(string.punctuation)
stoplist = stopwords.words('english') + punctuation+ ['RT', 'rt','via','&amp;','htt']
stoplist.append('AT_USER')
stoplist.append('AT')
stoplist.append('USER')
stoplist.append('URL')


def tokenize(tweet):
    #print "making features"
    words_fil = []
    # process the tweets
    #Convert to lower case
    #tweet = tweet.lower()
    #Convert www.* or https?://* to URL
    tweet = re.sub('((www\.[^\s]+)|((http|https|ftp)?://[^\s]+))','URL',tweet)
    tweet = re.sub(r"http\\S+", "", tweet)
    tweet = re.sub(r"http\S+", "", tweet)
    tweet = re.sub(r"https\S+", "", tweet)
    tweet = re.sub(r"https\\S+", "", tweet)
    #Convert @username to AT_USER
    tweet = re.sub('@[^\s]+','AT_USER',tweet)
    #Remove additional white spaces
    tweet = re.sub('[\s]+', ' ', tweet)
    #Replace #word with word
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
     #Remove quotes
    tweet = re.sub(r"&amp;quot;|&amp;amp'", '',tweet)
    #Remove numbers
    #tweet = re.sub(r'[0-9]*','',tweet)
    #Remove everything other than alphabets
    tweet = re.sub("[^a-zA-Z]", " ", tweet)
    #remove special characters
    tweet = re.sub('[!-><|@?]', "", tweet)
    #trim
    tweet = tweet.strip('\'"')

    filtered_line = [w for w in tweet.split() if not w in stoplist]
    tweet =' '.join(filtered_line)
    
    #PORTER STEMMER
    #print 'Apply Porter Stemmer'
    #porter_stemmer = PorterStemmer()
    #print tweet
    words = tknzr.tokenize(tweet)
    #make ill- formed word correct
    '''for word in words:
	    if wordnet.synsets(word) == []:
		    suggestions = spell_dict.suggest(word)
		    if suggestions and edit_distance(word, suggestions[0]) <= max_dist: 
					words_fil.append(suggestions[0]) 
	    else: words_fil.append(word)'''
    #for j,word in enumerate(words):
    #	words[j] = porter_stemmer.stem(word)
    return words

def getTestData(testfile):
	testlist = []
	if "." in testfile:
		fw = open(testfile,"r")
		line = fw.readline()
		while line:
			line = fw.readline()
			testlist.append(line.decode('utf-8').strip())
	else:	
		currentdirectoryname = os.getcwd();
		fulldirecname =  currentdirectoryname+"/"+testfile;
		for filename in os.listdir(fulldirecname):
			if filename.endswith(".txt"):
					fw = open(testfile + '/' + filename,"r")
					line = fw.readline()
					while line:
						line = fw.readline()
						testlist.append(line.decode('utf-8').strip())
	return testlist


def training(trainfile,model,test_features_model,solution_file):
	f_features = open("features.csv","w")
	f_sloution = open(solution_file,"w")
	train_list = []
	sentiment_list = []
	f_data = open(trainfile,"r")
	line = f_data.readline()
	#sprint train_data_df.SentimentText.tolist()
    	while line:
			try:
			   	train_list.append(line.split(",")[3].decode('utf-8').strip())
				sentiment_list.append(line.split(",")[1].strip())
				line = f_data.readline()
			except:
			   	line = f_data.readline()
	f_data.close()
	trainlen = int(0.85 * len(train_list))
	print "file read done..."
	vectorizer = CountVectorizer(
                             analyzer = 'word',
                             tokenizer = tokenize,
                             lowercase = True,
                             max_features = 1000
                             )
	corpus_data_features = vectorizer.fit_transform(train_list)
	corpus_data_features_nd = corpus_data_features.toarray()
	clf = LinearSVC()
	#clf = svm.SVC(kernel='rbf')
	clf.fit(corpus_data_features_nd[:trainlen], sentiment_list[:trainlen])
	#save the model
	fmodel = open(model, 'wb')
	pickle.dump(clf, fmodel)
	fmodel.close()
	#store prediction in one file
	#fw = open("solution.txt","w")
	##see features
	vocab = vectorizer.get_feature_names()
	dist = np.sum(corpus_data_features_nd, axis=0)
	for tag, count in zip(vocab, dist):
    					f_features.write(tag + "," + str(count) + "\n")
	#fw.close()		
	f_features.close()
	print "training done"	
	#save test features
	fmodel = open(test_features_model, 'wb')
	pickle.dump(corpus_data_features_nd[trainlen:], fmodel)
	fmodel.close()
	for result in sentiment_list[trainlen:]:
			f_sloution.write(result + "\n")
	f_sloution.close()


def testing(output,model,test_features_model):
	ftest_features_model = open(test_features_model,'rb')
	corpus_data_features_nd = pickle.load(ftest_features_model)
	fmodel = open(model, 'rb')
	classifier = pickle.load(fmodel)
	fmodel.close()
	y_pred =  classifier.predict(corpus_data_features_nd)
	fw = open(output,"w")
	for prediction in y_pred:
			pred = str(prediction)
			fw.write(pred + '\n')
	fw.close()
	
print "training classifier"
corpus_data_features_nd = training("./train/small_senti_dataset.csv","./model/model.pkl","test_corpus.pkl","solution.txt")
print "testing classfier and output will be in output_svm.txt"
testing("./tweets_result/output_svm.txt","./model/model.pkl","test_corpus.pkl")
